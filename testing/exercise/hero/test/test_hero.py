from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Lahn", 30, 500, 5)
        self.enemy = Hero("Maehwa", 30, 500, 5)

    def test_init(self):
        self.assertEqual("Lahn", self.hero.username)
        self.assertEqual(30, self.hero.level)
        self.assertEqual(500, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_fight_yourself_exception_raise(self):
        with self.assertRaises(Exception) as e:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_battle_your_health_less_than_one_exception_raise(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_battle_enemy_health_less_than_one_exception_raise(self):
        self.enemy.health = 0

        with self.assertRaises(Exception) as e:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Maehwa. He needs to rest", str(e.exception))

    def test_battle_draw(self):
        self.hero.health = 150
        self.enemy.health = 150
        res = self.hero.battle(self.enemy)
        self.assertEqual("Draw", res)

    def test_battle_win(self):
        self.enemy.health = 150
        res = self.hero.battle(self.enemy)
        self.assertEqual(31, self.hero.level)
        self.assertEqual(355, self.hero.health)
        self.assertEqual(10, self.hero.damage)
        self.assertEqual("You win", res)

    def test_battle_loss(self):
        self.hero.health = 150
        res = self.hero.battle(self.enemy)
        self.assertEqual(31, self.enemy.level)
        self.assertEqual(355, self.enemy.health)
        self.assertEqual(10, self.enemy.damage)
        self.assertEqual("You lose", res)

    def test_str(self):
        self.assertEqual(f"Hero Lahn: 30 lvl\nHealth: 500\nDamage: 5\n", str(self.hero))


if __name__ == "__main__":
    main()

