from unittest import TestCase

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Beast")

    def test_pet_shop_init(self):
        self.assertEqual(self.pet_shop.name, "Beast")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_pet_add_food_quantity_for_negative_number(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("CatFood", -20)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_pet_add_food_quantity_is_zero(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("CatFood", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_in_dict(self):
        act = self.pet_shop.add_food("CatFood", 250)
        result = {"CatFood": 250}
        self.assertEqual(result, self.pet_shop.food)
        self.assertEqual(act, f"Successfully added 250.00 grams of CatFood.")

    def test_add_pet_with_same_name(self):
        self.pet_shop.add_pet("Mimi")
        with self.assertRaises(Exception) as error:
            self.pet_shop.add_pet("Mimi")
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_add_pet(self):
        self.pet_shop.add_pet("Kitty")
        result = ["Kitty"]
        self.assertEqual(result, self.pet_shop.pets)
        self.assertEqual(self.pet_shop.add_pet("Doggy"), f"Successfully added Doggy.")

    def test_feed_pet_invalid_pet_name(self):
        self.pet_shop.pets = ["Mimi", "Mindy"]
        with self.assertRaises(Exception) as error:
            self.pet_shop.feed_pet("CatFood", "Lily")
        self.assertEqual(f"Please insert a valid pet name", str(error.exception))

    def test_feed_pet_invalid_food_name(self):
        self.pet_shop.pets = ["Mimi"]
        self.pet_shop.food = {"CatFood": 150, "DogFood": 200}
        self.assertEqual(self.pet_shop.feed_pet("RabitFood", "Mimi"), f'You do not have RabitFood')

    def test_feed_pet_adding_food(self):
        self.pet_shop.pets = ["Mimi"]
        self.pet_shop.food = {"CatFood": 50, "DogFood": 200}
        act = self.pet_shop.feed_pet("CatFood", "Mimi")
        result = "Adding food..."
        self.assertEqual(act, result)
        self.assertEqual({"CatFood": 1050, "DogFood": 200}, self.pet_shop.food)

    def test_feed_pet_successfully_fed(self):
        self.pet_shop.pets = ["Mimi"]
        self.pet_shop.food = {"CatFood": 250, "DogFood": 200}
        act = self.pet_shop.feed_pet("CatFood", "Mimi")
        result = f"Mimi was successfully fed"
        self.assertEqual(act, result)
        self.assertEqual({"CatFood": 150, "DogFood": 200}, self.pet_shop.food)

    def test_pet_shop_repr(self):
        self.pet_shop.pets = ["Mimi", "Lili", "Sandy"]
        result = repr(self.pet_shop)
        expected = f"Shop Beast:\n" + \
                   f"Pets: Mimi, Lili, Sandy"
        self.assertEqual(result, expected)
