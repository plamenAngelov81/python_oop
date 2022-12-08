from unittest import TestCase

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Mecha", 10)

    def test_paint_factory_init(self):
        self.assertEqual(self.factory.name, "Mecha")
        self.assertEqual(self.factory.capacity, 10)
        self.assertEqual(self.factory.valid_ingredients, ['white', 'yellow', 'blue', 'green', 'red'])
        self.assertEqual(self.factory.ingredients, {})

    def test_product_type_not_in_valid_ingredients(self):
        with self.assertRaises(TypeError) as error:
            self.factory.add_ingredient("purple", 10)
        self.assertEqual(f"Ingredient of type purple not allowed in PaintFactory", str(error.exception))

    def test_add_ingredient_not_enough_space_in_factory(self):
        with self.assertRaises(ValueError) as error:
            self.factory.add_ingredient("red", 11)
        self.assertEqual("Not enough space in factory", str(error.exception))

    def test_add_ingredient_to_factory(self):
        self.factory.add_ingredient("red", 3)
        result_1 = {"red": 3}
        self.assertEqual(result_1, self.factory.ingredients)
        self.factory.add_ingredient("red", 2)
        result_2 = {"red": 5}
        self.assertEqual(result_2, self.factory.ingredients)

    def test_remove_ingredient_not_in_factory(self):
        self.factory.ingredients = {"red": 3, "blue": 5}
        with self.assertRaises(KeyError) as error:
            self.factory.remove_ingredient("green", 4)
        self.assertEqual("'No such ingredient in the factory'", str(error.exception))

    def test_remove_ingredient_quantity_cannot_be_less_than_zero(self):
        self.factory.ingredients = {"red": 3, "blue": 5}
        with self.assertRaises(ValueError) as error:
            self.factory.remove_ingredient("red", 10)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test_remove_ingredient_for_good(self):
        self.factory.ingredients = {"red": 3, "blue": 5}
        self.factory.remove_ingredient("blue", 2)
        expected = {"red": 3, "blue": 3}
        self.assertEqual(expected, self.factory.ingredients)

    def test_products_property_returns_correct_ingredients(self):
        self.factory.add_ingredient("white", 5)
        self.factory.add_ingredient("yellow", 5)
        result = self.factory.products
        expected = {"white": 5, "yellow": 5}
        self.assertEqual(expected, result)

    def test_products(self):
        self.factory.add_ingredient("red", 3)
        self.factory.add_ingredient("blue", 5)

        act = str(self.factory)
        expected = f"Factory name: Mecha with capacity 10.\nred: 3\nblue: 5\n"
        self.assertEqual(act, expected)

    def test_can_add_returns_true_if_quantity(self):
        result = self.factory.can_add(5)
        self.assertEqual(True, result)

        result = self.factory.can_add(10)
        self.assertEqual(True, result)

    def test_can_add_more_than_factory_capacity(self):
        result = self.factory.can_add(15)
        self.assertEqual(False, result)
