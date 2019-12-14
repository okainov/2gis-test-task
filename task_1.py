import datetime
import xml.etree.ElementTree as ET
from collections import defaultdict

import dateutil.parser


def get_day_beginning(day: datetime.datetime) -> datetime.datetime:
    """
    Returns datetime object with cleaned up "time" part
    """
    return day.replace(hour=0, minute=0, second=0, microsecond=0)


def count_total_stay(file_path: str = 'task_1_input.xml'):
    # Use iterparse because size of XML can be bigger than memory

    # TODO: NOT assuming the data is sorted, so we need to handle all the document
    #  before we can give any response.

    result_data = defaultdict(datetime.timedelta)
    time_entry = None
    time_exit = None
    one_day = datetime.timedelta(days=1)
    for event, data in ET.iterparse(file_path):
        if data.tag == 'start':
            time_entry = dateutil.parser.parse(data.text)
        if data.tag == 'end':
            time_exit = dateutil.parser.parse(data.text)
        if data.tag == 'person':
            if time_entry.date() == time_exit.date():
                # Both entry and exit happened in one day
                result_data[time_entry.date()] += time_exit - time_entry
            else:
                result_data[time_entry.date()] += get_day_beginning(time_entry) + one_day - time_entry
                result_data[time_exit.date()] += time_exit - get_day_beginning(time_exit)

                delta = time_exit - time_entry
                # Add whole days of stay if any
                for i in range(1, delta.days):
                    result_data[(time_entry + datetime.timedelta(days=i)).date()] += one_day

            # Clean up before switching to the next iteration
            time_entry = None
            time_exit = None

    # TODO: validate malformed XMLs with wrong structure

    return result_data


if __name__ == '__main__':
    result = count_total_stay()

    for day in sorted(result):
        print(f'{day}: {result[day]}')
