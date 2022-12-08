
from unittest import TestCase

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(50, 100)

    def test_init_constructor(self):
        self.assertEqual(50, self.car.fuel)
        self.assertEqual(50, self.car.capacity)
        self.assertEqual(100, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as e:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_drive(self):
        self.car.drive(10)
        self.assertEqual(37.5, self.car.fuel)

    def test_refuel(self):
        self.car.fuel -= 20
        self.car.refuel(10)
        self.assertEqual(40, self.car.fuel)

    def test_refuel_exception_raise(self):
        with self.assertRaises(Exception) as e:
            self.car.refuel(5)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        self.assertEqual("The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption",
                         str(self.car))
