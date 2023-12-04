"""
You play several games and record the information from each game
(your puzzle input). Each game is listed with its ID number
(like the 11 in Game 11: ...) followed by a semicolon-separated
list of subsets of cubes that were revealed from the bag
(like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag
(and then put back again). The first set is 3 blue cubes and 4 red cubes;
the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible
if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag
had been loaded with that configuration. However, game 3 would have been
impossible because at one point the Elf showed you 20 red cubes at once;
similarly, game 4 would also have been impossible because the Elf showed you
15 blue cubes at once. If you add up the IDs of the games that would have
been possible, you get 8.

--- Part Two ---

As you continue your walk, the Elf poses a second question: in each game you
played, what is the fewest number of cubes of each color that could have been
in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 green,
and 6 blue cubes. If any color had even one fewer cube, the game would have
been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue
cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green,
and blue cubes multiplied together. The power of the minimum set of cubes in
game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.
"""

from cube_conundrum.cube_conundrum import (
    Game,
    check,
    get_fewest_game,
    calculate_power_set,
    total_power_sets,
)


def test_summation_possible_games_must_equal_8():
    games = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]

    result = sum(check(game_raw) for game_raw in games)

    assert result == 8


def test_summation_impossible_games_must_equal_0():
    games = [
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    ]

    result = sum(check(game_raw) for game_raw in games)

    assert result == 0


def test_fewest_game_for_game1_must_be_6_blues_4_reds_2_greens():
    game_raw = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

    fewest = Game(
        game_id=1,
        red=4,
        green=2,
        blue=6,
    )

    result = get_fewest_game(game_raw)

    assert result == fewest


def test_power_set_game1_must_be_48():
    game_raw = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    power = 48

    result = calculate_power_set(game_raw)

    assert result == power


def test_power_set_game2_must_be_12():
    game_raw = 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'
    power = 12

    result = calculate_power_set(game_raw)

    assert result == power


def test_power_set_game3_must_be_1560():
    game_raw = (
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
    )
    power = 1560

    result = calculate_power_set(game_raw)

    assert result == power


def test_power_set_game4_must_be_630():
    game_raw = (
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
    )
    power = 630

    result = calculate_power_set(game_raw)

    assert result == power


def test_power_set_game5_must_be_36():
    game_raw = 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    power = 36

    result = calculate_power_set(game_raw)

    assert result == power


def test_total_power_set_games_must_be_2286():
    games = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
    ]

    total = 2286

    result = total_power_sets(games)

    assert result == total
