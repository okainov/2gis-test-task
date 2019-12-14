from unittest import TestCase
from unittest.mock import MagicMock

from task_2 import Cat, InvalidInputException, CatState, CatTransition, InvalidCatConfigurationException


class TestCat(TestCase):
    def test_default_state_hungry(self):
        self.assertEqual(Cat().state, CatState.HUNGRY)

    def test_stays_hungry_when_hungry_and_dog(self):
        cat = Cat(initial_state=CatState.HUNGRY)
        cat.input('dog')
        self.assertEqual(cat.state, CatState.HUNGRY)

    def test_goes_to_full_when_hungry_and_salami(self):
        cat = Cat(initial_state=CatState.HUNGRY)
        cat.input('salami')
        self.assertEqual(cat.state, CatState.FULL)

    def test_goes_to_hungry_when_full_and_salami(self):
        cat = Cat(initial_state=CatState.FULL)
        cat.input('salami')
        self.assertEqual(cat.state, CatState.HUNGRY)

    def test_goes_to_hungry_when_full_and_dog(self):
        cat = Cat(initial_state=CatState.FULL)
        cat.input('dog')
        self.assertEqual(cat.state, CatState.HUNGRY)

    def test_used_side_effect_be_called(self):
        side_effect_run = MagicMock()
        side_effect_eat = MagicMock()
        cat = Cat(initial_state=CatState.HUNGRY, transitions=[
            CatTransition(state=CatState.HUNGRY, input_symbol='dog', side_effect=side_effect_run),
            CatTransition(state=CatState.HUNGRY, input_symbol='salami', new_state=CatState.FULL,
                          side_effect=side_effect_eat)])
        cat.input('dog')
        side_effect_run.assert_called_once()

    def test_unused_side_effect_not_called(self):
        side_effect_run = MagicMock()
        side_effect_eat = MagicMock()
        cat = Cat(initial_state=CatState.HUNGRY, transitions=[
            CatTransition(state=CatState.HUNGRY, input_symbol='dog', side_effect=side_effect_run),
            CatTransition(state=CatState.HUNGRY, input_symbol='salami', new_state=CatState.FULL,
                          side_effect=side_effect_eat)])
        cat.input('dog')
        side_effect_eat.assert_not_called()

    def test_invalid_input_exception(self):
        cat = Cat(initial_state=CatState.FULL)
        with self.assertRaises(InvalidInputException):
            cat.input('invalid')

    def test_error_if_initial_state_is_not_in_states(self):
        with self.assertRaises(InvalidCatConfigurationException):
            Cat(states=[CatState.FULL], initial_state=CatState.HUNGRY)

    def test_error_if_initial_transition_state_is_not_in_states(self):
        with self.assertRaises(InvalidCatConfigurationException):
            Cat(states=[CatState.FULL], initial_state=CatState.FULL, transitions=[
                CatTransition(state=CatState.HUNGRY, input_symbol='dog'),
            ]
                )

    def test_error_if_final_transition_state_is_not_in_states(self):
        with self.assertRaises(InvalidCatConfigurationException):
            Cat(states=[CatState.FULL], initial_state=CatState.FULL, transitions=[
                CatTransition(state=CatState.FULL, new_state=CatState.HUNGRY, input_symbol='dog'),
            ]
                )
