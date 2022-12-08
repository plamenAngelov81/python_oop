from unittest import TestCase

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard("Tom", 10)

    def test_student_report_Card_init(self):
        self.assertEqual("Tom", self.card.student_name)
        self.assertEqual(10, self.card.school_year)
        self.assertEqual(self.card.grades_by_subject, {})

    def test_property_student_name_cant_be_empty_string(self):
        with self.assertRaises(ValueError) as error:
            card = StudentReportCard("", 10)
        self.assertEqual(str(error.exception), "Student Name cannot be an empty string!")

    def test_property_school_year_lower_than_one(self):
        with self.assertRaises(ValueError) as error:
            card = StudentReportCard("Tom", 0)
        self.assertEqual(str(error.exception), "School Year must be between 1 and 12!")

    def test_property_school_year_bigger_than_max_year(self):
        with self.assertRaises(ValueError) as error:
            card = StudentReportCard("Tom", 13)
        self.assertEqual(str(error.exception), "School Year must be between 1 and 12!")

    def test_school_year_set_up_with_valid_number(self):
        for grade in range(1, 13):
            self.card.school_year = grade
            self.assertEqual(grade, self.card.school_year)

    def test_add_grade_add_subject_to_dictionary(self):
        self.card.add_grade("Math", 5)
        self.assertEqual({"Math": [5]}, self.card.grades_by_subject)

    def test_add_grade_to_subject(self):
        self.card.add_grade("Math", 5)
        self.card.add_grade("Math", 4)
        self.assertEqual({"Math": [5, 4]}, self.card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.card.grades_by_subject = {"math": [4, 5, 6], "JS": [6, 6]}
        expected = "math: 5.00\nJS: 6.00"
        self.assertEqual(self.card.average_grade_by_subject(), expected)

    def test_average_grade_for_all_subjects(self):
        self.card.grades_by_subject = {"math": [4, 5, 6], "JS": [6, 6]}
        expected = "Average Grade: 5.40"
        self.assertEqual(expected, self.card.average_grade_for_all_subjects())

    def test_repr_method(self):
        self.card.grades_by_subject = {"math": [4, 5, 6], "JS": [6, 6]}
        result = f"Name: {self.card.student_name}\n" \
                 f"Year: {self.card.school_year}\n" \
                 f"----------\n" \
                 f"{self.card.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.card.average_grade_for_all_subjects()}"
        self.assertEqual(result, self.card.__repr__())
