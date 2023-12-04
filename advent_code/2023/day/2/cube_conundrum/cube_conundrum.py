"""
Advent of Code - 2023

--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just
barely reaches the surface of a large island floating in the sky. You gently
land in a fluffy pile of leaves. It's quite cold, but you don't see much snow.
An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the
lack of snow. He'll be happy to explain the situation, but it's a bit of a
walk, so you have some time. They don't get many visitors up here; would you
like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either
red, green, or blue. Each time you play this game, he will hide a secret
number of cubes of each color in the bag, and your goal is to figure out
information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach
into the bag, grab a handful of random cubes, show them to you, and then put
them back in the bag. He'll do this a few times per game.

Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the
IDs of those games?
"""

from dataclasses import dataclass
from typing import Iterator


@dataclass
class Game:
    game_id: int
    red: int = 0
    green: int = 0
    blue: int = 0


def parse_sets(sets) -> dict[str, int]:
    plays = sets.split(';')

    for play in plays:
        colors = dict()

        for subset in play.split(','):
            number, color = subset.split()
            colors[color] = int(number)

        yield colors


def parse_name(name: str) -> int:
    _, game_id = name.split()

    return int(game_id)


def parse(game_raw: str) -> Iterator[Game]:
    name, sets = game_raw.split(':')

    game_id = parse_name(name)
    subsets = parse_sets(sets)

    for colors in subsets:
        game = Game(
            game_id,
            **colors
        )

        yield game



def possible_subset(subset: Game, red=12, green=13, blue=14) -> Iterator[int]:
    # Possible subset
    if subset.red <= red and subset.green <= green and subset.blue <= blue:
        return subset

    # Impossible subset
    raise ValueError(f'Impossible subset: {subset}')


def possible_game(game_raw, red=12, green=13, blue=14):
    subsets = parse(game_raw)

    for subset in subsets:
        game = possible_subset(subset, red, green, blue)

    return game.game_id


def check(game_raw: str, red=12, green=13, blue=14) -> int:
    """
    Games would have been possible if the bag had been loaded with
    only 12 red cubes, 13 green cubes, and 14 blue cubes.

    Args:
        game_raw (str): Game with amount of red, green and blue cubes.
        red (int, optional): Maximum of red cubes. Defaults to 12.
        green (int, optional): Maximum of green cubes. Defaults to 13.
        blue (int, optional): Maximum of blue cubes. Defaults to 14.

    Returns:
        int: Summation of possible game identifiers.
    """

    try:
        game_id = possible_game(game_raw, red, green, blue)
    except ValueError:
        return 0

    return game_id
