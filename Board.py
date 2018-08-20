import copy


class Board:
    turnStr = 'user'  # user's turn by default
    state = [[2, 2, 2],  # default empty state
             [2, 2, 2],
             [2, 2, 2]]
    currentSign = 0

    def getCopy(self):
        board:Board = Board()
        board.turnStr = self.turnStr
        board.state =[[2,2,2],[2,2,2],[2,2,2]]
        for i in range(3):
            for j in range(3):
                board.state[i][j] = self.state[i][j]
        board.currentSign = self.currentSign
        return board
    def move(self, row: int, col: int, sign: int):

        if row > 0 <= 3 and col > 0 <= 3:
            board: Board = self.getCopy()
            board.state[row - 1][col - 1] = sign
            if self.turnStr == 'user':
                board.turnStr = 'computer'
            else:
                board.turnStr = 'user'

            if self.currentSign == 0:
                board.currentSign = 1
            else:
                board.currentSign = 0

            return board
        else:
            raise ValueError("Invalid row or column parameter")


    def displayState(self):
        displayString: str = ""
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    displayString += 'O'
                elif self.state[i][j] == 1:
                    displayString += 'X'
                else:
                    displayString += '-'
                displayString += " "
            displayString += '\n'
        print(displayString)

    def findChildren(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 2: # empty state
                    child = self.move(i+1,j+1,self.currentSign)
                    children.append(child)
        return children

    def isLeaf(self):

        for i in range(3):
            for j in range(3):
                if self.state[i][j]==2:
                    return False

        return True

    def getMinMaxUtility(self,maxSign:int):
        b = self.getCopy()
        if self.isLeaf():
            return self.getLeafUtility(maxSign)
        else:
            utilities = []
            for i in range(3):
                for j in range(3):
                    if self.state[i][j] == 2:
                        child = self.move(i+1, j+1, self.currentSign)
                        utilities.append(child.getMinMaxUtility(maxSign))
                        pass
            if self.currentSign == maxSign:
                return max(utilities)
            else:
                return min(utilities)

    def getLeafUtility(self, maxSign:int):
        for i in range(3):
            if self.state[0][i] == self.state[1][i] == self.state[2][i]:
                if self.state[0][i] == maxSign:
                    return 1
                else:
                    return -1
            elif self.state[i][0] == self.state[i][1] == self.state[i][2]:
                if self.state[i][0] == maxSign:
                    return 1
                else:
                    return -1

        if self.state[0][0] == self.state[1][1] == self.state[2][2]:
            if self.state[0][0] == maxSign:
                return 1
            else:
                return -1
        elif self.state[0][2] == self.state[1][1] == self.state[2][0]:
            if self.state[0][2] == maxSign:
                return 1
            else:
                return -1
        else:
            return 0
    def findMoveAndMoveIt(self,maxSign:int):
        utils = []
        children = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j]==2:
                    child = self.move(i+1,j+1,self.currentSign)
                    children.append(child)
                    utils.append(child.getMinMaxUtility(maxSign))

        ind = utils.index(max(utils))
        return children[ind]
