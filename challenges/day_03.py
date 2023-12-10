import dataclasses
import io
import logging as log
import re

_DIGIT_RE = re.compile(r"\d+")
_PART_RE = re.compile(r"[^\d\.\s]")

@dataclasses.dataclass
class Num:
    val: int
    locations: set[tuple[int, int]]

    @classmethod
    def from_str(cls, s: str, x: int, y: int):
        l = set()
        for i in range(len(s)):
            l.add((x+i, y))
        return cls(int(s), l)

    def num(self) -> int:
        return int(self.val)

@dataclasses.dataclass
class Parts:
    adjacent: set[tuple[int, int]]

    def add(self, x: int, y: int):
        for dx in range(max(0, x-1), x+2):
            for dy in range(max(0, y-1), y+2):
                self.adjacent.add((dx, dy))

    def labeled_by(self, num: Num) -> bool:
        return len(self.adjacent.intersection(num.locations)) > 0

def part_1(input: io.TextIOBase) -> str:
    nums = []
    parts = Parts(set())

    line_num = 0
    while (line := input.readline()) != "":
        for match in _DIGIT_RE.finditer(line):
            log.debug("Found num %s at line %d pos %d", match.group(), line_num, match.start())
            nums.append(Num.from_str(line[match.start():match.end()], match.start(), line_num))
        for match in _PART_RE.finditer(line):
            log.debug("Found part %s at line %d pos %d", match.group(), line_num, match.start())
            parts.add(match.start(), line_num)

        line_num +=1

    for n in nums:
        if parts.labeled_by(n):
            log.debug("num %d is a part number", n.num())
        else:
            log.debug("num %d is not a part number", n.num())

    return sum(n.num() for n in nums if parts.labeled_by(n))


def part_2(input: io.TextIOBase) -> str:
    pass