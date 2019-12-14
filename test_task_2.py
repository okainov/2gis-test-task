from unittest import TestCase

from task_2 import Cat


class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat()

    def test_default_state_hungry(self):
        self.assertEqual(self.cat.state, Cat.CatState.HUNGRY)
