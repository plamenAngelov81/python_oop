from unittest import TestCase

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shop = ShoppingCart("Shop", 10)

    def test_shopping_catd_init(self):
        self.assertEqual(self.shop.shop_name, "Shop")
        self.assertEqual(self.shop.budget, 10)

    def test_shopping_card_setter_upper(self):
        with self.assertRaises(ValueError) as error:
            shop = ShoppingCart("shop", 10)
        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")

    def test_shop_card_setter_value_is_alpha(self):
        with self.assertRaises(ValueError) as error:
            shop = ShoppingCart("Shop2", 10)
        self.assertEqual(str(error.exception), "Shop must contain only letters and must start with capital letter!")

    def test_add_to_card_cost_to_mush_100(self):
        product_name = "Name"
        product_price = 100
        with self.assertRaises(ValueError) as error:
            self.shop.add_to_cart(product_name, product_price)
        self.assertEqual(str(error.exception), f"Product {product_name} cost too much!")

    def test_add_to_card_more_than_100(self):
        product_name = "Name"
        product_price = 101
        with self.assertRaises(ValueError) as error:
            self.shop.add_to_cart(product_name, product_price)
        self.assertEqual(str(error.exception), f"Product {product_name} cost too much!")

    def test_add_to_card_item_with_price(self):
        product_name = "Name"
        product_price = 50
        result = self.shop.add_to_cart(product_name, product_price)
        expect = f"{product_name} product was successfully added to the cart!"
        self.assertEqual(result, expect)

    def test_remove_from_card_if_product_name_not_in_the_dict(self):
        self.shop.products = {"item1": 20, "item2": 30}
        product_name = "item3"
        with self.assertRaises(ValueError) as error:
            self.shop.remove_from_cart(product_name)
        self.assertEqual(str(error.exception), f"No product with name {product_name} in the cart!")

    def test_remove_from_card_product_name_in_in_dict(self):
        self.shop.products = {"item1": 20, "item2": 30}
        product_name = "item2"
        act = self.shop.remove_from_cart(product_name)
        expect = f"Product {product_name} was successfully removed from the cart!"
        self.assertEqual(act, expect)
        self.assertEqual(self.shop.products, {"item1": 20})

    def test_add_new_shop_name(self):
        shop2 = ShoppingCart("Hell", 20)
        act = self.shop + shop2

        self.assertEqual(act.shop_name, "ShopHell")

    def test_add_new_shop_budged(self):
        shop2 = ShoppingCart("Hell", 20)
        act = self.shop + shop2

        self.assertEqual(act.budget, 30)

    def test_add_new_shop_shopping_cart(self):
        shop2 = ShoppingCart("Hell", 20)
        shop2.add_to_cart("bla", 2)
        shop2.add_to_cart("blabla", 3)
        act = self.shop + shop2

        self.assertEqual(act.products, {"bla": 2, "blabla": 3})

    def test_buy_product_value_error(self):
        self.shop.products = {"item1": 7, "item2": 5}
        total_sum = 12
        with self.assertRaises(ValueError) as error:
            self.shop.buy_products()
        self.assertEqual(str(error.exception), f"Not enough money to buy the products! Over budget with "
                                               f"{total_sum - self.shop.budget:.2f}lv!")

    def test_buy_product_possible(self):
        self.shop.products = {"item1": 3, "item2": 5}
        total_sum = 8
        act = self.shop.buy_products()
        result = f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'
        self.assertEqual(act, result)
