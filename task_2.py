from enum import Enum


class Cat:
    class CatInput(Enum):
        SALAMI = 'salami'
        DOG = 'dog'

    @property
    def state(self):
        return self._state

    class CatState(Enum):
        HUNGRY = 1
        FULL = 2

        def handle(self, input_symbol: str, cat: 'Cat') -> 'Cat.CatState':
            new_state = self
            if self == Cat.CatState.HUNGRY and input_symbol == Cat.CatInput.DOG.value:
                cat.action_run()
            elif self == Cat.CatState.HUNGRY and input_symbol == Cat.CatInput.SALAMI.value:
                cat.action_eat()
                new_state = Cat.CatState.FULL
            elif self == Cat.CatState.FULL and input_symbol == Cat.CatInput.SALAMI.value:
                cat.action_sleep()
                new_state = Cat.CatState.HUNGRY
            elif self == Cat.CatState.FULL and input_symbol == Cat.CatInput.DOG.value:
                cat.action_run()
                new_state = Cat.CatState.HUNGRY
            return new_state

    def __init__(self, initial_state: CatState = CatState.HUNGRY):
        self._state = initial_state

    def input(self, input_symbol: str):
        self._state = self.state.handle(input_symbol, self)

    def action_run(self):
        print('Run!')

    def action_eat(self):
        print('Eat')

    def action_sleep(self):
        print('sleep')


if __name__ == '__main__':
    cat = Cat()
