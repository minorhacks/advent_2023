import io
import textwrap

from challenges import day_03

from absl.testing import absltest

class TestDay03(absltest.TestCase):

    def test_part_1(self):
        sample = textwrap.dedent(
            """
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..
            """
        ).strip()
        self.assertEqual(4361, day_03.part_1(io.StringIO(sample)))

if __name__ == "__main__":
    absltest.main()