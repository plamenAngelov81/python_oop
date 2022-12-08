from unittest import TestCase

from project.bookstore import Bookstore


class TestBookStore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(10)

    def test_store_init(self):
        self.assertEqual(self.store.books_limit, 10)
        self.assertEqual(self.store.availability_in_store_by_book_titles, {})
        #self.assertEqual(store.__total_sold_books, 0)

    def test_total_sold_books(self):
        self.assertEqual(self.store.total_sold_books, 0)

    def test_book_limit(self):
        self.assertEqual(self.store.books_limit, 10)

    def test_book_limit_is_negative(self):

        with self.assertRaises(ValueError) as error:
            store = Bookstore(-1)
        self.assertEqual(str(error.exception), f"Books limit of -1 is not valid")

    def test_for_zero_book_limit(self):
        with self.assertRaises(ValueError) as error:
            store = Bookstore(0)
        self.assertEqual(str(error.exception), f"Books limit of 0 is not valid")

    def test_book_count(self):
        self.store.availability_in_store_by_book_titles = {"Book_1": 5}
        self.assertEqual(self.store.__len__(), 5)

    def test_more_limit(self):
        self.store.availability_in_store_by_book_titles = {"Book_1": 5}
        number_of_books = 8
        with self.assertRaises(Exception) as error:
            self.store.receive_book("Book_1", number_of_books)
        self.assertEqual(str(error.exception), "Books limit is reached. Cannot receive more books!")

    def test_add_book_for_first_time(self):
        self.store.availability_in_store_by_book_titles = {}
        self.store.receive_book("Book_1", 5)
        self.assertEqual({"Book_1": 5}, self.store.availability_in_store_by_book_titles)

        self.store.receive_book("Book_1", 3)
        self.assertEqual({"Book_1": 8}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(self.store.receive_book("Book_1", 1), f"9 copies of Book_1 are available in the bookstore.")

    def test_sell_books_not_exists(self):
        self.store.availability_in_store_by_book_titles = {"Book_1": 5}
        with self.assertRaises(Exception) as error:
            self.store.sell_book("Book_2", 2)
        self.assertEqual(str(error.exception), "Book Book_2 doesn't exist!")

    def test_sell_more_books_than_we_have(self):
        self.store.availability_in_store_by_book_titles = {"Book_1": 5}
        with self.assertRaises(Exception) as error:
            self.store.sell_book("Book_1", 7)
        self.assertEqual(str(error.exception), f"Book_1 has not enough copies to sell. Left: 5")

    def test_sell_book_ok(self):
        self.store.availability_in_store_by_book_titles = {"Book_1": 5}
        self.store.sell_book("Book_1", 1)
        self.assertEqual({"Book_1": 4}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(self.store.total_sold_books, 1)

    def test_sell_book_ok_message(self):
        self.store.availability_in_store_by_book_titles = {"Book_1": 5}
        self.assertEqual(self.store.sell_book("Book_1", 1), "Sold 1 copies of Book_1")

    def test_str_method(self):
        self.store.receive_book("Book_1", 5)
        self.store.receive_book("Book_2", 4)
        self.store.sell_book("Book_1", 1)
        result = self.store.__str__()
        self.assertEqual(result, self.store.__str__())