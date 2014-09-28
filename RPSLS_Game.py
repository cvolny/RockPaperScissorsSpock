import random
import sys


__plays = {
    ('Scissors', 'Paper'):  'Scissors cut Paper',
    ('Paper', 'Rock'):      'Paper covers Rock',
    ('Rock', 'Lizard'):     'Rock crushes Lizard',
    ('Lizard', 'Spock'):    'Lizard poisons Spock',
    ('Spock', 'Scissors'):  'Spock smashes Scissors',
    ('Scissors', 'Lizard'): 'Scissors decapitate Lizard',
    ('Lizard', 'Paper'):    'Lizard eats Paper',
    ('Paper', 'Spock'):     'Paper disproves Spock',
    ('Spock', 'Rock'):      'Spock vaporizes Rock',
    ('Rock', 'Scissors'):   'Rock crushes Scissors',
}

__players = ["Alice", "Bobby"]
__game_message = "Game {}:"
__pick_message = "{} choose {}."
__draw_message = "Both {}. Draw game!"
__wins_message = "{} wins! {}."


def play_rpsls(count):
    options = list(set([x for x, y in __plays.keys()]))
    a, b = __players

    for i in range(1, count + 1):
        print(__game_message.format(i))
        x = random.choice(options)
        y = random.choice(options)
        print(__pick_message.format(a, x))
        print(__pick_message.format(b, y))

        if x == y:
            print(__draw_message.format(x))
        elif (x, y) in __plays.keys():
            print(__wins_message.format(a, __plays[(x, y)]))
        else:
            print(__wins_message.format(b, __plays[(y, x)]))
        print()
    sys.exit(0)


if "__main__" == __name__:
    play_rpsls(5)