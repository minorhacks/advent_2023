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
        for dx in range(x-1, x+len(s)+1):
            for dy in range(y-1, y+2):
                l.add((dx, dy))
        return cls(int(s), l)

    def num(self) -> int:
        return int(self.val)

@dataclasses.dataclass
class Part:
    symbol: str
    x: int
    y: int

    def labeled_by(self, num: Num) -> bool:
        return (self.x, self.y) in num.locations

def parse(input: io.TextIOBase) -> tuple[list[Num], list[Part]]:
    nums = []
    parts = []

    line_num = 0
    while (line := input.readline()) != "":
        for match in _DIGIT_RE.finditer(line):
            log.debug("Found num %s at line %d pos %d", match.group(), line_num, match.start())
            nums.append(Num.from_str(line[match.start():match.end()], match.start(), line_num))
        for match in _PART_RE.finditer(line):
            log.debug("Found part %s at line %d pos %d", match.group(), line_num, match.start())
            parts.append(Part(match.group(), match.start(), line_num))

        line_num +=1
    
    return nums, parts


def part_1(input: io.TextIOBase) -> str:
    nums, parts = parse(input)

    for n in nums:
        if any(p.labeled_by(n) for p in parts):
            log.debug("num %d is a part number", n.num())
        else:
            log.debug("num %d is not a part number", n.num())

    return sum(n.num() for n in nums if any(p.labeled_by(n) for p in parts))


def part_2(input: io.TextIOBase) -> str:
    nums, parts = parse(input)

    total = 0
    gears = list(p for p in parts if p.symbol == "*" and len([n for n in nums if p.labeled_by(n)]) == 2)
    for g in gears:
        n1, n2 = (n for n in nums if g.labeled_by(n))
        total += n1.num() * n2.num()
    return total