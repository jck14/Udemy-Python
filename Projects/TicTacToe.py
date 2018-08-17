def DisplayBoard(b):
    print(f"{b[7]} | {b[8]} | {b[9]}")
    print(f"{b[4]} | {b[5]} | {b[6]}")
    print(f"{b[1]} | {b[2]} | {b[3]}")


def VictoryCheck(b, player):
    return b[1] == b[2] == b[3] == player or b[4] == b[5] == b[6] == player or b[7] == b[8] == b[9] == player\
or b[1] == b[4] == b[7] == player or b[2] == b[5] == b[8] == player or b[3] == b[6] == b[9] == player\
or b[7] == b[5] == b[3] == player or b[1] == b[5] == b[9] == player


def StartingMenu():
    input("Press Enter to play!")


def PlayerMove(b, player):

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
        StartingMenu()

        while True:
            DisplayBoard(gameBoard)

            if VictoryCheck(gameBoard, 'O'):
                print("Winner: 'O'")
                break

            gameBoard = PlayerMove(gameBoard, 'X')

            DisplayBoard(gameBoard)

            if VictoryCheck(gameBoard, 'X'):
                print("Winner: 'X'")
                break

            gameBoard = PlayerMove(gameBoard, 'O')


