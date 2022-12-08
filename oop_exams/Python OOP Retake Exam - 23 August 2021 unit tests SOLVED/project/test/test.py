from unittest import TestCase

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Lib")

    def test_library_init(self):
        self.assertEqual(self.library.name, "Lib")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_library_property(self):
        with self.assertRaises(ValueError) as error:
            library = Library("")
        self.assertEqual(f"Name cannot be empty string!", str(error.exception))

    def test_add_book(self):
        self.library.add_book("Lili", "Title_1")
        result = {"Lili": ["Title_1"]}
        self.assertEqual(result, self.library.books_by_authors)

    def test_add_one_more_book_from_same_author(self):
        self.library.books_by_authors = {"Lili": ["Title_1"]}
        self.library.add_book("Lili", "Title_2")
        result = {"Lili": ["Title_1", "Title_2"]}
        self.assertEqual(result, self.library.books_by_authors)

    def test_add_new_reader(self):
        self.library.add_reader("Mindy")
        result = {"Mindy": []}
        self.assertEqual(result, self.library.readers)

    def test_add_reader_with_same_name(self):
        self.library.readers = {"Mindy": []}
        self.assertEqual(self.library.add_reader("Mindy"), f"Mindy is already registered in the Lib library.")

    def test_rent_book_author_not_exists(self):
        self.library.readers = {"John": []}
        self.library.books_by_authors = {"Lili": ["Title_1"]}
        act = self.library.rent_book("John", "Mimi", "title_1")
        self.assertEqual(act, f"Lib Library does not have any Mimi's books.")

    def test_rent_book_reader_not_registered_in_lib(self):
        self.library.readers = {"John": []}
        self.library.books_by_authors = {"Lili": ["Title_1"]}
        act = self.library.rent_book("Tom", "Lili", "title_1")
        self.assertEqual(act, f"Tom is not registered in the Lib Library.")

    def test_rent_book_library_does_not_have_the_book(self):
        self.library.readers = {"John": []}
        self.library.books_by_authors = {"Lili": ["Title_1"]}
        act = self.library.rent_book("John", "Lili", "Title_2")
        self.assertEqual(act, f"""Lib Library does not have Lili's "Title_2".""")

    def test_reader_rent_book(self):
        self.library.readers = {"John": []}
        self.library.books_by_authors = {"Lili": ["Title_1"]}
        self.library.rent_book("John", "Lili", "Title_1")
        result = {"John": [{"Lili": "Title_1"}]}
        self.assertEqual(result, self.library.readers)

    def test_rent_book_remove_rented_book_from_author_list(self):
        self.library.readers = {"John": []}
        self.library.add_book("Lili", "Title_1")
        self.library.rent_book("John", "Lili", "Title_1")
        result = {"Lili": []}
        self.assertEqual(result, self.library.books_by_authors)

