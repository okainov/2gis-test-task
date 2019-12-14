from unittest import TestCase
from unittest.mock import MagicMock

from task_2 import Cat


class TestCat(TestCase):
    def test_default_state_hungry(self):
        self.assertEqual(Cat().state, Cat.CatState.HUNGRY)

    def test_run_when_hungry_and_dog(self):
        cat = Cat(Cat.CatState.HUNGRY)
        cat.action_run = MagicMock()
        cat.input('dog')
        cat.action_run.assert_called_once()

    def test_stays_hungry_when_hungry_and_dog(self):
        cat = Cat(Cat.CatState.HUNGRY)
        cat.input('dog')
        self.assertEqual(cat.state, cat.CatState.HUNGRY)

    def test_eat_when_hungry_and_salami(self):
        cat = Cat(Cat.CatState.HUNGRY)
        cat.action_eat = MagicMock()
        cat.input('salami')
        cat.action_eat.assert_called_once()

    def test_goes_to_full_when_hungry_and_salami(self):
        cat = Cat(Cat.CatState.HUNGRY)
        cat.input('salami')
        self.assertEqual(cat.state, cat.CatState.FULL)

    def test_sleep_when_full_and_salami(self):
        cat = Cat(Cat.CatState.FULL)
        cat.action_sleep = MagicMock()
        cat.input('salami')
        cat.action_sleep.assert_called_once()

    def test_goes_to_hungry_when_full_and_salami(self):
        cat = Cat(Cat.CatState.FULL)
        cat.input('salami')
        self.assertEqual(cat.state, cat.CatState.HUNGRY)

    def test_goes_to_hungry_when_full_and_dog(self):
        cat = Cat(Cat.CatState.FULL)
        cat.input('dog')
        self.assertEqual(cat.state, cat.CatState.HUNGRY)

    def test_run_when_full_and_dog(self):
        cat = Cat(Cat.CatState.FULL)
        cat.action_run = MagicMock()
        cat.input('dog')
        cat.action_run.assert_called_once()
