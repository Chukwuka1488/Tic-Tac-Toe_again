# create the board
# list of lists to represent game board

game = [[2, 0, 2],
        [0, 2, 1],
        [2, 0, 1]]


def win(current_game):
    # horizontal winner
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[1] == 0:
            print(f"Player {row[0]} is the winner horizontally!")

    # diagonals
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        print(col, row)
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[1] == 0:
        print(f"Player {diags[0]} is the winner diagonally upwards - left to right!")

    diags = []
    for idx in range(len(game)):
        diags.append(game[idx][idx])
    if diags.count(diags[0]) == len(diags) and diags[1] == 0:
        print(f"Player {diags[0]} is the winner diagonally downwards - left to right!")

    # verticals
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically!")


win(game)

# if game[0][0] == game[1][1] == game[2][2]:
#     print("Winner")
# if game[2][0] == game[1][1] == game[0][2]:
#     print("Winner")


# functions use when we want a repetitive result from our program

# def game_board(game_map, player=0, row=0, column=0, just_display=False):
#     try:
#         print("   a  b  c")  # column
#         if not just_display:
#             game_map[row][column] = player
#         for count, row in enumerate(game_map):  # Built-in functions using enumerate: returns the index and the value
#             print(count, row)
#         return game_map
#     except IndexError as e:
#         print("Error: make sure you input row/column as 0, 1 or 2?", e)
#     except  Exception as e:
#         print("something bad just happened!", e)
# 
# 
# game = game_board(game, just_display=True)
# game = game_board(game_board, player=1, row=2, column=0)
# 
# # indexing and slicing
# # game[0][1] = 1
# #
# # game_board()
