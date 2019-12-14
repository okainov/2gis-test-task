from enum import Enum
from typing import List


class InvalidInputException(Exception):
    """
    Error raised if provided input does not correspond to any of acceptable transition's input
    """
    pass


class InvalidCatConfigurationException(Exception):
    """
    Error raised if some of the configuration parameters for Cat are wrong
    """
    pass


# TODO: In order to fulfil OCP, it would be better to define some general CatState type/interface,
#  so users could create new types on their side and keep the original code closed
class CatState(Enum):
    HUNGRY = 1
    FULL = 2


class CatTransition:
    """
    Description of a single Finite Automata transition. If Cat is in the `state` and the input given is `input_symbol`
    then Cat will move to `new_state` executing `side_effect`.
    If `new_state` is None, no state will be changed.
    """

    def __init__(self, state: CatState, input_symbol: str, new_state: CatState = None, side_effect: callable = None):
        self.state = state
        self.input = input_symbol
        self.new_state = new_state
        self.side_effect = side_effect


# TODO: it's not really known what kind of side effects are here, thus assuming they're just normal functions
#  without arguments. If needed, it can be extended either to some CatSideEffect interface or just modify arguments
#  i.e. to include Cat instance itself.
def side_effect_run():
    """
    Default side effect, called when cat is running
    """
    print('Run')


def side_effect_eat():
    """
    Default side effect, called when cat is eating
    """
    print('Eat')


def side_effect_sleep():
    """
    Default side effect, called when cat is sleeping
    """
    print('Sleep')


class Cat:
    @property
    def state(self):
        """
        Returns current state of the Cat
        :return: current state of the Cat
        """
        return self._state

    def __init__(self, states: List[CatState] = None, initial_state: CatState = CatState.HUNGRY,
                 transitions: List[CatTransition] = None):
        """
        Creates Cat finite automata from the given list of states and transitions.
        By default behavior is the same as described in the task description, but it can be customized.
        :param states: list of possible Cat states
        :param initial_state: initial state of the Cat
        :param transitions: list of possible transitions
        """

        if states is None:
            self.states = [CatState.FULL, CatState.HUNGRY]
        else:
            self.states = states

        if initial_state is None:
            self._state = CatState.HUNGRY
        else:
            if initial_state not in self.states:
                raise InvalidCatConfigurationException('Initial state is not present in available states')
            self._state = initial_state

        if transitions is None:
            self.transitions = [
                CatTransition(state=CatState.HUNGRY, input_symbol='dog', side_effect=side_effect_run),
                CatTransition(state=CatState.HUNGRY, input_symbol='salami', new_state=CatState.FULL,
                              side_effect=side_effect_eat),
                CatTransition(state=CatState.FULL, input_symbol='dog', new_state=CatState.HUNGRY,
                              side_effect=side_effect_run),
                CatTransition(state=CatState.FULL, input_symbol='salami', new_state=CatState.HUNGRY,
                              side_effect=side_effect_sleep),
            ]
        else:
            self.transitions = transitions

        # Validate states in transitions
        for transition in self.transitions:
            if transition.state is not None and transition.state not in self.states:
                raise InvalidCatConfigurationException('Initial transition state is not present in available states')
            if transition.new_state is not None and transition.new_state not in self.states:
                raise InvalidCatConfigurationException('New transition state is not present in available states')

    def input(self, input_symbol: str):
        """
        Handles input and performs transition according to the current state and input.
        :param input_symbol: input string
        """
        executed = False
        for transition in self.transitions:
            if transition.state == self.state and transition.input == input_symbol:
                if transition.side_effect is not None:
                    transition.side_effect()
                if transition.new_state is not None:
                    self._state = transition.new_state
                executed = True
                break
        if not executed:
            raise InvalidInputException


if __name__ == '__main__':
    cat = Cat()
