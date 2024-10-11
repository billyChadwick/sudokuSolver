#Global variables
everSolved = False
matrix = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

#Function for verifying if it is valid to enter a number in a given square
def verifyNumber(rowIn, columnIn, numberIn):
    global matrix
    boxRowInt = rowIn // 3
    boxColumnInt = columnIn // 3

    for rowCheck in range(9):
        if matrix[rowCheck][columnIn] == numberIn:
            return False

    for columnCheck in range(9):
        if matrix[rowIn][columnCheck] == numberIn:
            return False
    
    for boxRow in range(boxRowInt * 3, (boxRowInt + 1) * 3):
        for boxColumn in range(boxColumnInt * 3, (boxColumnInt + 1) * 3):
            if matrix[boxRow][boxColumn] == numberIn:
                return False

    return True

#Recursive function for solving the sudoku
def solve():
    global everSolved
    global matrix
    
    for row in range(9):
        for column in range(9):
            if matrix[row][column] == 0:
                for possibleNumber in range(1,10):
                    if verifyNumber(row, column, possibleNumber):
                        matrix[row][column] = possibleNumber
                        solve()
                        matrix[row][column] = 0
                return

    everSolved = True

    print("\nHere is your solved sudoku:")
    printMatrix()
    input("\nPlease enter to continue searching for solutions:\n")

#Function for getting the user to input a valid matrix
def getMatrix():
    global matrix
    correctInput = ''

    while correctInput != 'y':
        for row in range(9):
            for column in range (9):
                print("What number is in row", row, "and column", column, "?")
                inputtedNumber = input()

                while len(inputtedNumber) != 1 or not (ord("0") <= ord(inputtedNumber) <= ord("9")):
                    print("The character(s) inputted are not a valid input")
                    print("Please enter either 1 to 9 for a filled number or 0 for an empty square:")
                    inputtedNumber = input()
                
                matrix[row][column] = int(inputtedNumber)

        print("\nHere is the sudoku you have entered:")
        printMatrix()

        print("\nIs this correct? (y/n)")
        correctInput = input()

        while correctInput != 'y' and correctInput != 'n':
            print("\nThe input given is not valid, please enter either 'y' or 'n':")
            correctInput = input()

        if correctInput == 'n':
            print("\nPlease enter the sudoku again:\n")
        else:
            print('\nChecking the sudoku entered is valid...')

            validMatrix = verifyMatrix()

            if validMatrix:
                print("\nThe sudoku entered is valid")
            else:
                print("\nThe sudoku entered is not valid, please re-enter the sudoku\n")
                correctInput = 'n'

#Function to verify the inputted matrix is valid
def verifyMatrix():
    global matrix

    for row in range(9):
        for column in range(9):
            if matrix[row][column] != 0:
                numberToCheck = matrix[row][column]
                matrix[row][column] = 0
                
                if not verifyNumber(row,column,numberToCheck):
                    return False
                
                matrix[row][column] = numberToCheck
    
    return True

#Function to print the matrix
def printMatrix():
    global matrix

    print("\n+-------+-------+-------+")
    print("|", matrix[0][0], matrix[0][1], matrix [0][2], "|", matrix[0][3], matrix[0][4], matrix[0][5], "|", matrix[0][6], matrix[0][7], matrix[0][8], "|")
    print("|", matrix[1][0], matrix[1][1], matrix [1][2], "|", matrix[1][3], matrix[1][4], matrix[1][5], "|", matrix[1][6], matrix[1][7], matrix[1][8], "|")
    print("|", matrix[2][0], matrix[2][1], matrix [2][2], "|", matrix[2][3], matrix[2][4], matrix[2][5], "|", matrix[2][6], matrix[2][7], matrix[2][8], "|")
    print("+-------+-------+-------+")
    print("|", matrix[3][0], matrix[3][1], matrix [3][2], "|", matrix[3][3], matrix[3][4], matrix[3][5], "|", matrix[3][6], matrix[3][7], matrix[3][8], "|")
    print("|", matrix[4][0], matrix[4][1], matrix [4][2], "|", matrix[4][3], matrix[4][4], matrix[4][5], "|", matrix[4][6], matrix[4][7], matrix[4][8], "|")
    print("|", matrix[5][0], matrix[5][1], matrix [5][2], "|", matrix[5][3], matrix[5][4], matrix[5][5], "|", matrix[5][6], matrix[5][7], matrix[5][8], "|")
    print("+-------+-------+-------+")
    print("|", matrix[6][0], matrix[6][1], matrix [6][2], "|", matrix[6][3], matrix[6][4], matrix[6][5], "|", matrix[6][6], matrix[6][7], matrix[6][8], "|")
    print("|", matrix[7][0], matrix[7][1], matrix [7][2], "|", matrix[7][3], matrix[7][4], matrix[7][5], "|", matrix[7][6], matrix[7][7], matrix[7][8], "|")
    print("|", matrix[8][0], matrix[8][1], matrix [8][2], "|", matrix[8][3], matrix[8][4], matrix[8][5], "|", matrix[8][6], matrix[8][7], matrix[8][8], "|")
    print("+-------+-------+-------+")

#Main
print("Welcome to this sudoku solver by Billy Chadwick")
print("First we will get you to fill out the sudoku, please enter 0 for a square if it is empty:\n")

getMatrix()

print("\nSolving...")

solve()

if everSolved:
    print("No further solutions were found")
else:
    print("\nNo solutions were found for the given sudoku")
