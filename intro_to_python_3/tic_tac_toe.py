import itertools
import numpy as np

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal winner
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # diagonals
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally upwards - left to right!")
        return True

    diags = []
    for idx in range(len(game)):
        diags.append(game[idx][idx])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally downwards - left to right!")
        return True

    # verticals
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is taken! Choose another!")
            print()
            return game_map, False
        print("   " + "  ".join(str(i) for i in range(len(game_map))))  # column
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):  # enumerate: returns the index and the value
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)
        return game_map, False

    except  Exception as e:
        print("something bad just happened!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    game_size = int(input("what size game of tic_tac_toe will you like to play? Enter value: "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display=True)

    player_choice = itertools.cycle([1, 2])
    while not game_won:
        print()
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            print()
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over! Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("See you later!")
                play = False
            else:
                print("enter y or n next time moron! Bye!!!")
                play = False
