import io
import re

_SINGLE_DIGIT = re.compile(r"\d")
_SINGLE_DIGIT_OR_WORD = re.compile(r"zero|one|two|three|four|five|six|seven|eight|nine|\d")
_SINGLE_DIGIT_OR_WORD_REV = re.compile(r"orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d")
_WORD_TO_NUM = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "orez": "0",
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
}

def calibration_number(line: str) -> int:
    return int(_SINGLE_DIGIT.search(line).group() + _SINGLE_DIGIT.search(line[::-1]).group())

def calibration_number_or_word(line: str) -> int:
    first_num = _SINGLE_DIGIT_OR_WORD.search(line).group()
    last_num = _SINGLE_DIGIT_OR_WORD_REV.search(line[::-1]).group()
    return int(_WORD_TO_NUM.get(first_num, first_num) + _WORD_TO_NUM.get(last_num, last_num))

def part_1(input: io.TextIOBase):
    sum = 0
    while (line := input.readline()) != "":
        sum = sum + calibration_number(line)
    return sum

def part_2(input: io.TextIOBase):
    sum = 0
    while (line := input.readline()) != "":
        sum = sum + calibration_number_or_word(line)
    return sum