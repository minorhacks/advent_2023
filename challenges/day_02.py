import dataclasses
import functools
import io
import logging as log
import re

_BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
_GAME_SPLITTER = re.compile(r', |; ')

@dataclasses.dataclass
class Game:
    gid: int
    totals: dict[str, int]

    @classmethod
    def FromLine(cls, line: str):
        (game, content) = line.split(":", 1)
        (_, id) = game.split(" ", 1)

        rounds = _GAME_SPLITTER.split(content.strip())
        totals = {}

        for round in rounds:
            num, color = round.split(" ")
            totals[color] = max(totals.get(color, 0), int(num))

        return cls(int(id), totals)

    def is_possible(self, available: dict[str, int]) -> bool:
        for (color, amount) in self.totals.items():
            if color not in available:
                log.debug("Game %s not possible: color %s doesn't exist", self.gid, color)
                return False
            if amount > available[color]:
                log.debug("Game %s not possible: too many %s cubes (%d)", self.gid, color, amount)
                return False
        log.debug("Game %s is possible", self.gid)
        return True

    def power(self):
        return functools.reduce(lambda x, y: x*y, self.totals.values())


def part_1(input: io.TextIOBase) -> str:
    games = []
    while (line := input.readline()) != "":
        games.append(Game.FromLine(line))
    return sum(g.gid for g in games if g.is_possible(_BAG))

def part_2(input: io.TextIOBase) -> str:
    games = []
    while (line := input.readline()) != "":
        games.append(Game.FromLine(line))
    return sum(g.power() for g in games)