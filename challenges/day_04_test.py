import io
import textwrap

from absl.testing import absltest

from challenges import day_04

class TestDay04(absltest.TestCase):

    def test_part_1(self):
        sample = textwrap.dedent(
            """
            """
        ).strip()
        self.assertEqual(13, day_04.part_1(io.StringIO(sample)))

if __name__ == "__main__":
    absltest.main()