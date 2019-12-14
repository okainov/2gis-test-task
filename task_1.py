import datetime
import xml.etree.ElementTree as ET
from collections import defaultdict

import dateutil.parser


def get_day_beginning(day: datetime.datetime) -> datetime.datetime:
    """
    Returns datetime object with cleaned up "time" part
    """
    return day.replace(hour=0, minute=0, second=0, microsecond=0)


def update_count_stay(result_data, time_entry: datetime.datetime, time_exit: datetime.datetime):
    """
    Modifies result_data to update it in accordance with given stay
    :param result_data: data storarage
    :param time_entry: datetime of entrance
    :param time_exit: datetime of exit
    """
    ONE_DAY = datetime.timedelta(days=1)
    if time_entry.date() == time_exit.date():
        # Both entry and exit happened in one day
        result_data[time_entry.date()] += time_exit - time_entry
    else:
        result_data[time_entry.date()] += get_day_beginning(time_entry) + ONE_DAY - time_entry
        result_data[time_exit.date()] += time_exit - get_day_beginning(time_exit)

        delta = time_exit - time_entry
        # Add whole days of stay if any
        for i in range(1, delta.days):
            result_data[(time_entry + datetime.timedelta(days=i)).date()] += ONE_DAY


def count_total_stay(file_path: str = 'task_1_input.xml'):
    """
    Counts total duration of people stay per days
    :param file_path: path to the input XML file
    :return: duration of stays split by days
    """

    # TODO: NOT assuming the data is sorted, so we need to handle all the document
    #  before we can give any response.

    result_data = defaultdict(datetime.timedelta)

    time_entry = None
    time_exit = None
    person = None

    # Use iterparse because size of XML can be bigger than memory
    for event, data in ET.iterparse(file_path, events=('start', 'end')):
        # TODO: validate malformed XMLs with completely wrong structure
        if event == 'start':
            if data.tag == 'person':
                if 'full_name' not in data.attrib:
                    raise Exception('Name of the person is missing for some entries')
                person = data.attrib['full_name']
            continue

        if data.tag == 'start':
            time_entry = dateutil.parser.parse(data.text)
        elif data.tag == 'end':
            time_exit = dateutil.parser.parse(data.text)
        elif data.tag == 'person':
            if time_entry is None or time_exit is None:
                raise Exception(f'Invalid input: some dates for {person} are missing')

            if time_exit < time_entry:
                raise Exception(f'Invalid input: entry date for {person} is after exit date')

            update_count_stay(result_data, time_entry, time_exit)

            # Clean up before switching to the next iteration
            time_entry = None
            time_exit = None

    return result_data


if __name__ == '__main__':
    result = count_total_stay()

    for day in sorted(result):
        print(f'{day}: {result[day]}')
