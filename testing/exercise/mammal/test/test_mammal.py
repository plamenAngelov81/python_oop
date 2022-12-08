from unittest import TestCase

from project.mammal import Mammal


class TestingMammal(TestCase):
    def setUp(self) -> None:
        self.name = "Kunio"
        self.type = "Cat"
        self.sound = "pur"
        self.__kingdom = "animals"
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_mammal_init(self):
        self.assertEqual(self.name, "Kunio")
        self.assertEqual(self.type, "Cat")
        self.assertEqual(self.sound, "pur")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected = f"{self.name} makes {self.sound}"
        self.assertEqual(result, expected)

    def test_info(self):
        result = self.mammal.info()
        expected = f"{self.name} is of type {self.type}"
        self.assertEqual(result, expected)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected = "animals"
        self.assertEqual(result, expected)
