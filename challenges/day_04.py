import dataclasses
import io
import re

_NUMS_AND_PIPE_RE = re.compile(r"\d+|\|")


@dataclasses.dataclass
class Card:
    score: int
    matching_count: int
    copies: int

    @classmethod
    def from_str(cls, s: str):
        matches = _NUMS_AND_PIPE_RE.finditer(s)
        card_num = int(next(matches).group())
        winning_nums = set()
        selected_nums = set()
        while (m := next(matches).group()) != "|":
            winning_nums.add(int(m))
        for m in matches:
            selected_nums.add(int(m.group()))

        score = 0
        if (matching_count := len(selected_nums.intersection(winning_nums))) > 0:
            score = 2 ** (matching_count - 1)

        return cls(score, matching_count, 1)


def part_1(input: io.TextIOBase) -> str:
    cards = []
    while (line := input.readline()) != "":
        cards.append(Card.from_str(line))
    return sum(c.score for c in cards)


def part_2(input: io.TextIOBase) -> str:
    pass
