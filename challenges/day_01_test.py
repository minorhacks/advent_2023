import io
import textwrap

from absl.testing import absltest

from challenges import day_01

class TestDay01(absltest.TestCase):

    def test_calibration_number(self):
        self.assertEqual(12, day_01.calibration_number("1abc2"))
        self.assertEqual(38, day_01.calibration_number("pqr3stu8vwx"))
        self.assertEqual(15, day_01.calibration_number("a1b2c3d4e5f"))
        self.assertEqual(77, day_01.calibration_number("treb7uchet"))

    def test_calibration_number_or_word(self):
        self.assertEqual(29, day_01.calibration_number_or_word("two1nine"))
        self.assertEqual(83, day_01.calibration_number_or_word("eightwothree"))
        self.assertEqual(13, day_01.calibration_number_or_word("abcone2threexyz"))
        self.assertEqual(24, day_01.calibration_number_or_word("xtwone3four"))
        self.assertEqual(42, day_01.calibration_number_or_word("4nineeightseven2"))
        self.assertEqual(14, day_01.calibration_number_or_word("zoneight234"))
        self.assertEqual(76, day_01.calibration_number_or_word("7pqrstsixteen"))

    def test_part_1(self):
        sample = textwrap.dedent(
            """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """,
            ).strip()
        self.assertEqual(142, day_01.part_1(io.StringIO(sample)))

    


if __name__ == "__main__":
    absltest.main()