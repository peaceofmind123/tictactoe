from Player import Player
import Helper
from Board import Board
MAXSIGN = 0 # by default
if __name__ == '__main__':
    sign: int = None

    user: Player = Player()
    computer: Player = Player()
    board: Board = Board()

    while True:
        print("Choose your sign:")
        print("1. O")
        print("2. X")
        response: str = input()
        try:
            sign = int(response) - 1  # 0 based response
            user.sign = sign
            computer.sign = Helper.getOppositeSign(user.sign)
            break
        except ValueError:
            print("Please enter a valid response")
            continue
    while True:

        gofirst: str = input("Would you like to go first?(y/n)")

        if str.upper(gofirst) == 'Y':
            user.isMax = True
            computer.isMax = False
            break
        elif str.upper(gofirst) == 'N':
            user.isMax = False
            computer.isMax = True
            break
        else:
            print("Please enter a valid value (y/n)")
            continue

    board.turn = 0  # max's turn in the beginning
    if user.isMax:
        board.turnStr = 'user'
        board.currentSign = user.sign
        MAXSIGN = user.sign

    else:
        board.turnStr = 'computer'
        board.currentSign = computer.sign
        MAXSIGN = computer.sign

    while board.isLeaf() is False:
        if board.turnStr=='user':
            print("Current state")
            board.displayState()
            while True:

                try:

                    row, col = map(int, input("Please enter your move (row col): ").split())
                    if row > 0 <= 3 and col > 0 <= 3:
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    print("Wrong values entered")

            board = board.move(row, col, user.sign)  # no computation required here
            board.displayState()
        else:

            board = board.findMoveAndMoveIt(MAXSIGN)
            board.displayState()
