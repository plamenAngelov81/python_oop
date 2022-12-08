from unittest import TestCase

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Speed", 1)

    def test_train_init(self):
        self.assertEqual(self.train.name, "Speed")
        self.assertEqual(self.train.capacity, 1)
        self.assertEqual(self.train.passengers, [])

    def test_add_passenger_no_capacity(self):
        self.train.passengers = ["Tom"]
        with self.assertRaises(ValueError) as error:
            self.train.add("John")
        self.assertEqual("Train is full", str(error.exception))

    def test_add_passenger_with_same_name(self):
        train = Train("AAA", 5)
        train.passengers = ["Tom"]
        with self.assertRaises(ValueError) as error:
            train.add("Tom")
        self.assertEqual("Passenger Tom Exists", str(error.exception))

    def test_add_passenger_into_passengers_list(self):
        self.assertEqual(self.train.add("Mimi"), "Added passenger Mimi")
        self.assertEqual(["Mimi"], self.train.passengers)

    def test_remove_passenger_not_exist(self):
        self.train.passengers = ["Sindy", "Mindy"]
        with self.assertRaises(ValueError) as error:
            self.train.remove("Mandy")
        self.assertEqual("Passenger Not Found", str(error.exception))

    def test_remove_passenger(self):
        self.train.passengers = ["Sindy", "Mindy"]
        self.assertEqual(self.train.remove("Mindy"), "Removed Mindy")
        self.assertEqual(self.train.passengers, ["Sindy"])

