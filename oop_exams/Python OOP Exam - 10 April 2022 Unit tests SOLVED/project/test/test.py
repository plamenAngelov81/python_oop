from unittest import TestCase
from project.movie import Movie


class TestMovie(TestCase):
    NAME = "Hell Movie"
    YEAR = 1955
    RATING = 10

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_movie_init(self):
        self.assertEqual(self.movie.name, "Hell Movie")
        self.assertEqual(self.movie.year, 1955)
        self.assertEqual(self.movie.rating, 10)

    def test_name_cant_be_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_proper_year(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1887 - 5
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor(self):
        self.movie.add_actor("Tom")
        self.assertEqual(["Tom"], self.movie.actors)

    def test_add_actor_with_same_name(self):
        self.movie.actors = ["John"]
        self.assertEqual(self.movie.add_actor("John"), "John is already added in the list of actors!")

    def test_our_movie_have_better_rating(self):
        other_movie = Movie("AAA", 2000, self.RATING - 1)

        result = self.movie > other_movie
        self.assertEqual(result, f'"{self.movie.name}" is better than "{other_movie.name}"')

    def test_other_movie_have_better_rating(self):
        other_movie = Movie("Rambo 5", 2010, self.RATING + 5)

        result = self.movie > other_movie
        self.assertEqual(f'"{other_movie.name}" is better than "{self.movie.name}"', result)

    def test_repr(self):
        self.movie.actors = ["Tom", "John"]
        result = repr(self.movie)

        expected = f"Name: {self.NAME}\n" \
                   f"Year of Release: {self.YEAR}\n" \
                   f"Rating: {self.RATING:.2f}\n" \
                   f"Cast: {', '.join(self.movie.actors)}"

        self.assertEqual(result, expected)
