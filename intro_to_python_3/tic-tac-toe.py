# create the board
# list of lists to represent game board

game = [[0, 1, 1],
        [0, 0, 0],
        [0, 2, 2]]

# horizontal winner
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row) and row[1] == 0:
            print("Winner")
        else:
            print('Loser')


win(game)

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
# 
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
