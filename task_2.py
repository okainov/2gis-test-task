from enum import Enum


class Cat:
    class CatState(Enum):
        HUNGRY = 1
        FULL = 2

    class CatInput(Enum):
        SALAMI = 'salami'
        DOG = 'dog'

    @property
    def state(self):
        return self._state

    def __init__(self, initial_state: CatState = CatState.HUNGRY):
        self._state = initial_state

    def input(self, input_symbol: CatInput):
        pass

    def action_run(self):
        print('Run!')

    def action_eat(self):
        print('Eat')

    def action_sleep(self):
        print('sleep')


if __name__ == '__main__':
    cat = Cat()
