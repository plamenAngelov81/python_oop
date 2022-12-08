from unittest import TestCase

from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("HellTeam")

    def test_team_init(self):
        self.assertEqual(self.team.name, "HellTeam")
        self.assertEqual(self.team.members, {})

    def test_team_name_setter(self):
        with self.assertRaises(ValueError) as error:
            team = Team("Hell Team")
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member(self):
        self.team.members = {"Mimi": 18}
        self.assertEqual(self.team.add_member(Tom=20, John=21, Mimi=18), "Successfully added: Tom, John")
        self.assertEqual({"Mimi": 18, "Tom": 20, "John": 21}, self.team.members)

    def test_remove_member(self):
        self.team.members = {"Mimi": 18, "Tom": 20, "John": 21}
        self.team.remove_member("Mimi")
        self.assertEqual({"Tom": 20, "John": 21}, self.team.members)
        self.assertEqual(self.team.remove_member("John"), f"Member John removed")

    def test_remove_not_exist_member(self):
        self.team.members = {"Mimi": 18, "Tom": 20, "John": 21}
        self.assertEqual(self.team.remove_member("Mandy"), f"Member with name Mandy does not exist")

    def test_our_team_is_bigger_than_other_team(self):
        self.team.members = {"Mimi": 18, "Tom": 20, "John": 21}
        other_team = Team("Other")
        other_team.members = {"Sandy": 18, "Mandy": 22}
        self.assertEqual(self.team.__gt__(other_team), True)

    def test_our_team_is_smaller_than_other_team(self):
        self.team.members = {"Mimi": 18, "Tom": 20}
        other_team = Team("Other")
        other_team.members = {"Sandy": 18, "Mandy": 22, "John": 21}
        self.assertEqual(self.team.__gt__(other_team), False)

    def test_number_of_players(self):
        self.team.members = {"Mimi": 18, "Tom": 20, "John": 21}
        self.assertEqual(self.team.__len__(), 3)

    def test_create_new_team(self):
        self.team.members = {"Mimi": 18, "Tom": 20, "John": 21}
        other_team = Team("Other")
        other_team.members = {"Sandy": 18, "Mandy": 22}

        result = self.team + other_team
        self.assertEqual(result.name, f"{self.team.name}{other_team.name}")
        expected_members = {"Mimi": 18, "Tom": 20, "John": 21, "Sandy": 18, "Mandy": 22}
        self.assertEqual(expected_members, result.members)

    def test_str_return_members_sorted_by_age(self):
        self.team.members = {"Mimi": 18, "Tom": 20, "John": 21}
        result = str(self.team)
        expected = f"Team name: HellTeam\n" + \
                   f"Member: John - 21-years old\n" + \
                   f"Member: Tom - 20-years old\n" + \
                   f"Member: Mimi - 18-years old"
        self.assertEqual(result, expected)
