# create the board
# list of lists to represent game board

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


# functions use when we want a repetitive result from our program

def game_board(player=0, row=0, column=0, just_display=False):
    # column
    print("   a  b  c")
    if not just_display:
        game[row][column] = player
    # Built-in functions using enumerate: returns the index and the value
    for count, row in enumerate(game):
        print(count, row)
        # count += 1
        # for item in row:
        #     print(item)
game_board(just_display=True)
game_board(player=1, row=2, column=0)

# indexing and slicing
# game[0][1] = 1
#
# game_board()
