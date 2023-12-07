import io
import textwrap

from absl.testing import absltest

from challenges import day_02

class TestDay02(absltest.TestCase):

    sample = textwrap.dedent("""\
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        """).strip()

    def test_game_parse(self):
        self.assertEqual(
            (g := day_02.Game(1, {"blue": 6, "red": 4, "green": 2})),
            day_02.Game.FromLine("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
        )
        self.assertEqual(48, g.power())

    def test_part_1(self):
        self.assertEqual(8, day_02.part_1(io.StringIO(self.sample)))

    def test_part_2(self):
        self.assertEqual(2286, day_02.part_2(io.StringIO(self.sample)))

if __name__ == "__main__":
    absltest.main()