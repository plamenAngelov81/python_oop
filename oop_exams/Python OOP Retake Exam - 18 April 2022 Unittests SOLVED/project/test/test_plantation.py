from unittest import TestCase

from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_plantation_init(self):
        self.assertEqual(self.plantation.size, 5)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_plantation_negative_size(self):
        with self.assertRaises(ValueError) as error:
            Plantation(-5)
        self.assertEqual(str(error.exception), "Size must be positive number!")

    def test_plantation_hire_worker(self):
        self.plantation.hire_worker("John")
        result = ["John"]
        self.assertEqual(result, self.plantation.workers)
        self.assertEqual(self.plantation.hire_worker("Tom"), f"Tom successfully hired.")

    def test_plantation_hire_worker_with_same_name(self):
        self.plantation.workers = ["John"]
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker("John"),
        self.assertEqual(str(error.exception), "Worker already hired!")

    def test_plantation_len(self):
        self.plantation.plants = {"John": ["onion", "garlic"], "Lili": ["carrot"]}
        self.assertEqual(self.plantation.__len__(), 3)

    def test_plantation_len_zero(self):
        self.plantation.plants = {"John": [], "Lili": []}
        self.assertEqual(self.plantation.__len__(), 0)

    def test_planting_worker_not_in_worker_list(self):
        self.plantation.workers = ["John"]
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("Tom", "corn")
        self.assertEqual(str(error.exception), f"Worker with name Tom is not hired!")

    def test_lent_planting_len_error(self):
        self.plantation.hire_worker("John")
        self.plantation.plants = {"John": ["onion", "garlic", "tomato"], "Lili": ["carrot", "cucumber"]}
        with self.assertRaises(ValueError) as error:
            self.plantation.planting("John", "corn")
        self.assertEqual(str(error.exception), "The plantation is full!")

    def test_planting_worker_first_plant(self):
        self.plantation.workers = ["John"]
        act = self.plantation.planting("John", "corn")
        self.assertEqual(act, f"John planted it's first corn.")
        self.assertEqual({'John': ['corn']}, self.plantation.plants)

    def test_planting_worker_plant_his_next_plant(self):
        self.plantation.workers = ["John"]
        self.plantation.plants = {'John': ['corn']}
        act = self.plantation.planting("John", "tomato")
        self.assertEqual(act, f"John planted tomato.")
        self.assertEqual({'John': ['corn', "tomato"]}, self.plantation.plants)

    def test_repr_method(self):
        self.plantation.workers = ["John", "Lili"]
        result = f'Size: 5\nWorkers: John, Lili'
        self.assertEqual(result, self.plantation.__repr__())

    def test_plantation_str_method(self):
        self.plantation.hire_worker("John")
        self.plantation.hire_worker("Lily")
        self.plantation.planting("John", "corn")
        self.plantation.planting("John", "onion")
        self.plantation.planting("Lily", "roses")
        result = str(self.plantation)
        expected = "Plantation size: 5\n" \
                   "John, Lily\n" \
                   "John planted: corn, onion\n" \
                   "Lily planted: roses"
        self.assertEqual(expected, result)


