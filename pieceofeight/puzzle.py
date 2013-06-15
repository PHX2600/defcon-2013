import sys
import copy

#Puzzle node
class Puzzle:
    def __init__(self, startPuzzle = [[1,2,3],[4,0,6],[7,5,8]]):
        self.startPuzzle = startPuzzle #Current problem state
        self.goalPuzzle = [[1,2,3],[4,5,6],[7,8,0]] #Goal state
        self.puzzleWidth = len(self.startPuzzle[0]) #Width of puzzle
        self.puzzleLength = len(self.startPuzzle) #Length of puzzle
        self.puzzleSize = self.puzzleWidth*self.puzzleLength #Total size of puzzle (n)
        self.heuristicCost = 0 #h(n)
        self.depth = 0 #g(n)
        self.blankColor = None #Color of board underneath blank tile (Unsolvability test)
        self.moveString = ""

    #Overload <= operator, so this way we can use a priority queue/min-heap
    def __le__(self,other):
        return self.heuristicCost + self.depth <= other.heuristicCost + other.depth

    #Print the state of a puzzle
    def printPuzzle(self):
        self.puzzleRow = ''
        print ''
        for i in range( 0 , self.puzzleLength ):
            for j in range( 0 , self.puzzleWidth ):
                self.puzzleRow += str(self.startPuzzle[i][j])
            print self.puzzleRow
            self.puzzleRow = ''

    #Checks if the current state is the goal state
    def checkIfFinished(self):
        for i in range(0, self.puzzleLength):
            for j in range(0, self.puzzleWidth):
                if int(self.startPuzzle[i][j]) != self.goalPuzzle[i][j]:
                    return False
        return True

    #Returns the location of the blank tile in puzzle state
    def getBlankLocation(self):
        for i in range(0,self.puzzleLength):
            for j in range(0,self.puzzleWidth):
                if int(self.startPuzzle[i][j]) == 0:
                    return i,j

    #Returns the location of any tile with value in puzzle state
    def getPuzzleSquareLocation(self,value):
        for i in range(0, self.puzzleLength):
            for j in range(0, self.puzzleWidth):
                if int(self.startPuzzle[i][j]) == value:
                    return i,j

    #Returns the location of any tile with value in goal state
    def getGoalSquareLocation(self,value):
        for i in range(0, self.puzzleLength):
            for j in range(0, self.puzzleWidth):
                if self.goalPuzzle[i][j] == value:
                    return i,j

    #Generates a new puzzle with the blank moved left if possible
    def MoveLeft(self):
        blank_row, blank_col = self.getBlankLocation()
        #If the blank tile is not currently at the left-most column
        if blank_col != 0:
            #Make a deep copy of a new puzzle
            temp = copy.deepcopy(self)
            #Swap places with the blank Tile and the tile to the left
            value = temp.startPuzzle[blank_row][blank_col-1]
            temp.startPuzzle[blank_row][blank_col] = value
            temp.startPuzzle[blank_row][blank_col-1] = '0'
            temp.moveString = self.moveString + "r"
            #Return the new puzzle
            return temp

    #Generates a new puzzle with the blank moved left if possible
    def MoveRight(self):
        blank_row, blank_col = self.getBlankLocation()
        #If the blank tile is not currently at the right-most column
        if blank_col != self.puzzleWidth - 1:
            #Make a deep copy of a new puzzle
            temp = copy.deepcopy(self)
            #Swap places with the blank tile and the tile to #Generates a new puzzle with the blank moved left if possiblethe right
            value = temp.startPuzzle[blank_row][blank_col+1]
            temp.startPuzzle[blank_row][blank_col] = value
            temp.startPuzzle[blank_row][blank_col+1] = '0'
            temp.moveString = self.moveString + "l"
            #Return the new puzzle
            return temp

    #Generates a new puzzle with the blank moved left if possible
    def MoveUp(self):
        blank_row, blank_col = self.getBlankLocation()
        #If the blank tile is not at the top-most row
        if blank_row != 0:
            #Make a deep copy of the puzzle
            temp = copy.deepcopy(self)
            #Swap places with the blank tile and the tile above it
            value = temp.startPuzzle[blank_row-1][blank_col]
            temp.startPuzzle[blank_row][blank_col] = value
            temp.startPuzzle[blank_row-1][blank_col] = '0'
            temp.moveString = self.moveString + "d"
            #Return the new puzzle
            return temp

    #Generates a new puzzle with the blank moved left if possible
    def MoveDown(self):
        blank_row, blank_col = self.getBlankLocation()
        #If the blank tile is not in the last row
        if blank_row != self.puzzleLength - 1:
            #Make a copy of the puzzle
            temp = copy.deepcopy(self)
            #Swap places with the blank tile and the tile below it
            value = temp.startPuzzle[blank_row+1][blank_col]
            temp.startPuzzle[blank_row][blank_col] = value
            temp.startPuzzle[blank_row+1][blank_col] = '0'
            temp.moveString = self.moveString + "u"
            #Return the new puzzle
            return temp

    #Appends all possible moves to a list
    #explicitly deletes None-types from list in case
    #any of the moves were invalid and returned None
    def GenerateMoves(self):
        MoveList = []
        newMoveList = []
        MoveList.append(self.MoveLeft())
        MoveList.append(self.MoveRight())
        MoveList.append(self.MoveUp())
        MoveList.append(self.MoveDown())
        for move in MoveList:
            if move:
                newMoveList.append(move)
        return newMoveList

#Boiler-plate
if __name__ == '__main__':
    #Test cases to test functions and initialization
    fred = Puzzle([[1,2,3],[4,8,0],[7,6,5]])
    fred.printPuzzle()
    fred.GenerateMoves()

    print "================"

    bob = Puzzle()
    bob.printPuzzle()
    bob.GenerateMoves()
