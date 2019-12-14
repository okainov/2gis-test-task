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

    def input(self, input_symbol: str):
        if self.state == Cat.CatState.HUNGRY and input_symbol == Cat.CatInput.DOG.value:
            self.action_run()
        elif self.state == Cat.CatState.HUNGRY and input_symbol == Cat.CatInput.SALAMI.value:
            self._state = Cat.CatState.FULL
            self.action_eat()
        elif self.state == Cat.CatState.FULL and input_symbol == Cat.CatInput.SALAMI.value:
            self.action_sleep()
            self._state = Cat.CatState.HUNGRY
        elif self.state == Cat.CatState.FULL and input_symbol == Cat.CatInput.DOG.value:
            self.action_run()
            self._state = Cat.CatState.HUNGRY

    def action_run(self):
        print('Run!')

    def action_eat(self):
        print('Eat')

    def action_sleep(self):
        print('sleep')


if __name__ == '__main__':
    cat = Cat()
