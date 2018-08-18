def display_board(b):
    print(f"{b[7]} | {b[8]} | {b[9]}")
    print(f"{b[4]} | {b[5]} | {b[6]}")
    print(f"{b[1]} | {b[2]} | {b[3]}")


def victory_check(b, player):
    return b[1] == b[2] == b[3] == player or b[4] == b[5] == b[6] == player or b[7] == b[8] == b[9] == player\
or b[1] == b[4] == b[7] == player or b[2] == b[5] == b[8] == player or b[3] == b[6] == b[9] == player\
or b[7] == b[5] == b[3] == player or b[1] == b[5] == b[9] == player


def starting_menu():
    input("Press Enter to play!")


def player_move(b, player):

    while True:
        move = int(input("Choose pos: "))

        if not(b[move] == ' '):
            print("INVALID MOVE")
            continue
        else:
            b[move] = player
            break

    return b


if __name__ == '__main__':

    gameBoard = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while True:
        starting_menu()

        while True:
            display_board(gameBoard)

            if victory_check(gameBoard, 'O'):
                print("Winner: 'O'")
                break

            gameBoard = player_move(gameBoard, 'X')

            display_board(gameBoard)

            if victory_check(gameBoard, 'X'):
                print("Winner: 'X'")
                break

            gameBoard = player_move(gameBoard, 'O')


