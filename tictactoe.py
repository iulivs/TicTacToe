board = [['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]']]


def print_board():
    for row in board:
        print(row[0], row[1], row[2])


def position(player_symbol):
    try:
        row = input("Row: ")
        col = input("Col: ")
        row_int = int(row)
        col_int = int(col)
    except ValueError:
        print("You must only input numbers!")
        position(player_symbol)
    except:
        print('An unknown error occurred.')
        position(player_symbol)

    else:
        try:
            position_selected = board[row_int - 1][col_int - 1]

            if position_selected != '[ ]':
                print("\nSpace already occupied, try again.\n")
                print_board()
                position(player_symbol)
            else:
                print("\nPosition ({}, {}):".format(row_int, col_int))

                board[row_int - 1][col_int - 1] = '[%s]' % player_symbol
                print_board()

        except IndexError:
            num_except = "Number too %s, use one in the range 1 to 3, inclusive."

            if row_int > 3 or col_int > 3:
                print(num_except % "big")
            elif row_int < 1 or col_int < 1:
                print(num_except % "small")
            position(player_symbol)


def start_game():
    while True:

        choice = str(input("Player 1, would you like to use 'X' or 'O': ").upper())

        if choice == 'X' or choice == 'O':
            break
        else:
            print("Please choose either 'X' or 'O'.")
            continue

    empty_spots = 9
    options = ['X', 'O']

    first_player_symbol = choice
    second_player_symbol = [x for x in options if x not in [choice]][0]

    players = dict()
    players[first_player_symbol] = ["Player 1", 0]
    players[second_player_symbol] = ["Player 2", 0]
    move_count = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth'}

    while empty_spots >= 1:
        if empty_spots % 2 != 0:
            current_player_symbol = first_player_symbol
            players[first_player_symbol][1] += 1
        else:
            current_player_symbol = second_player_symbol
            players[second_player_symbol][1] += 1

        checks = [board[0],
                  board[1],
                  board[2],
                  [board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[2][0], board[1][1], board[0][2]]]

        for lst in checks:
            if lst == ['[X]', '[X]', '[X]'] or lst == ['[O]', '[O]', '[O]']:
                options = [first_player_symbol, second_player_symbol]
                print("\n%s has won!" % players[str(list(filter(lambda x: x != current_player_symbol, options)))[2]][0])
                return
            elif lst == ['[O]', '[O]', '[O]']:
                print("\nPlayer using 'O' has won!")
                return
        else:
            full_board = 0

            for lst in board:
                for each in lst:
                    if each != '[ ]':
                        full_board += 1

            if full_board >= 9:
                return

        print("\n%s's %s move (%s's):" %
              (players[current_player_symbol][0], move_count[players[current_player_symbol][1]], current_player_symbol))
        position(current_player_symbol)
        empty_spots -= 1

        if empty_spots == 0:
            return


start_game()