# create the board
# list of lists to represent game board

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


# functions use when we want a repetitive result from our program

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")  # column
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):  # Built-in functions using enumerate: returns the index and the value
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2?", e)


game = game_board(game, just_display=True)
game = game_board(game, player=1, row=3, column=0)

# indexing and slicing
# game[0][1] = 1
#
# game_board()
