
from unittest import TestCase

from project.person import Person


class TestPerson(TestCase):
    def setUp(self) -> None:
        self.first_name = "Plamen"
        self.last_name = "Angelov"
        self.age = 41
        self.person = Person(self.first_name, self.last_name, self.age)

    def testing_init_method(self):
        self.assertEqual(self.person.first_name, "Plamen")
        self.assertEqual(self.person.last_name, "Angelov")
        self.assertEqual(self.person.age, 41)
        self.assertEqual(self.person.cars, ["M5", "Gemera"])

    def testing_get_person_full_name(self):
        result = self.person.get_full_name()
        expected = "Plamen Angelov"
        self.assertEqual(result, expected)

    def testing_get_person_info(self):
        result = self.person.get_person_info()
        expected = "Plamen Angelov is 41 years old."
        self.assertEqual(result, expected)

    def testing_person_car_like(self):
        result = self.person.car_like("M5")
        expected = "This M5 is the best"
        self.assertIn(result, expected)


