import random
import time

#Python 3.0+
#Huy Nguyen hmn8@zips.uakron.edu

def displayBoard(board):

    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print ('-------------')
    print('  ' + board[6] + ' | ' + board[5] + ' | ' + board[4] )
    print ('-------------')
    print('  ' + board[3] + ' | ' + board[2] + ' | ' + board[1] )

#--------------------------------------------------------------------------------------

def firstTurn():
    print('Determining Who Goes First...')
    time.sleep(1.5)

    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Human'

#--------------------------------------------------------------------------------------

def playerSymbol():

    letter = input('Choose "X" or "O" :').upper()

    #assign letter of choice recursively
    if(letter == "X"):
        return ["X","O"]
    elif (letter == "O"):
        return ["O","X"]
    else:
        return playerSymbol()

#--------------------------------------------------------------------------------------

def isCheckEmpty(move,board):
    #check if board is empty

    if(board[move] is not ("X") and board[move] is not ("O") ):
        return True
    else:
        return False

#--------------------------------------------------------------------------------------

def getPlayerMove(board):
    move = input("Choose A Space (1-9): ")

    #check input 1-9 and if space is empty
    if(move in '1 2 3 4 5 6 7 8 9'.split() and isCheckEmpty(int(move),board) ):
        return int(move)
    else:
        #loop function
        return getPlayerMove(board)

#--------------------------------------------------------------------------------------

def assignMove(board,symbol,move):
    board[move] = symbol

#--------------------------------------------------------------------------------------

def checkWin(board,symbol):
    if( (board[1] is symbol and board[2] is symbol and board[3] is symbol) or #bottom row
        (board[4] is symbol and board[5] is symbol and board[6] is symbol) or #middle row
        (board[7] is symbol and board[8] is symbol and board[9] is symbol) or #top row

        (board[7] is symbol and board[6] is symbol and board[3] is symbol) or #left column
        (board[8] is symbol and board[5] is symbol and board[2] is symbol) or #middle column
        (board[9] is symbol and board[4] is symbol and board[1] is symbol) or #right column

        (board[7] is symbol and board[5] is symbol and board[1] is symbol) or #diagonal 1
        (board[3] is symbol and board[5] is symbol and board[9] is symbol) #diagonal 2
        ):

        return True


#--------------------------------------------------------------------------------------

def fullBoard(board):
    for i in range (1,10):
        if(board[i] in "1 2 3 4 5 6 7 8 9 ".split()):
            return False

    return True

#--------------------------------------------------------------------------------------

def playAgain():

    play = input("Play Again? Yes(Y) Exit(N) : ").upper()

    if(play == 'Y'):
        return True
    elif(play == 'N'):
        return False
    else:
        return playAgain()#loop function again

#---------------------------------------------------------------------------------------
def setDificulty():

    dific = input("Choose a Difficulty (1)EASY or (2)HARD : ")

    if(dific in "1 2".split()):
        return dific
    else:
        return setDificulty()#loop function again


#-------------------------------------------------------------------------------------
def computerMove(board, symbol, level, humanSymbol):


    if(int(level) == 1):
        move = randomMove(board)
        if(isinstance( move, int) ):
            assignMove(board, symbol, move)
            print ('Computer Moved')
        else:
            computerMove(board, symbol, level, humanSymbol)

    else:
        AIhard(board, symbol, humanSymbol)

#-------------------------------------------------------------------------------------
def randomMove(board):

    copy = list(board)

    move = random.choice(copy)

    if( move in '1 2 3 4 5 6 7 8 9'.split() and isCheckEmpty( int(move) ,copy ) ):
        #print "Computer's Move is ", move, ' \n'
        return int(move)
    else:
        #print "\nused\n"
        randomMove(board)


#A.I. Thinking Functions
#--------------------------------------------------------------------------------------
def AIhard(board, symbol, humanSymbol):
    copy = list(board)

    #win if possible
    move = winMove(board, symbol)
    if move != None:
        assignMove(board,symbol,move)
        return None

    #block opponent
    move = blockOpponent(copy, humanSymbol)
    if move != None:
        assignMove(board,symbol,move)
        return None

     # block 2 pincer strategy
    if (blockStrat(copy, humanSymbol)):
        if (isCheckEmpty(5, copy)):
            assignMove(board, symbol, 5)
            return None

    #take sides
    if(not isCheckEmpty(5,copy)):
        move = takeSides(copy,[2, 4, 6, 8])
        if(move != None):
            assignMove(board,symbol,move)
            return None

    move = takeCorner(copy, [1, 3, 7, 9])
    if move != None:
        assignMove(board,symbol,move)


#--------------------------------------------------------------------------------------
def takeCorner(board, cornerList):

    openSpace = []

    for i in range(len(cornerList)):
        if ( isinstance(cornerList[i], int) ):
            if( isCheckEmpty(cornerList[i], board) ):
                openSpace.extend([cornerList[i]])

    if(len(openSpace) != 0):
        return random.choice(openSpace)
    else:
        return None
#----------------------------------------------------------------------------------------
def blockOpponent(board, humanSymbol):

    copy = list(board)

    for i in range( 1, len(copy) ):

        if(isCheckEmpty(i, copy)):
            assignMove(copy,humanSymbol,i)
            if(not checkWin(copy,humanSymbol)):
                #refresh board
                copy = list(board)

        if checkWin(copy,humanSymbol) :
            return i

    return None

#----------------------------------------------------------------------------------------
def winMove(board, symbol):

    copy = list(board)

    for i in range( 1, len(copy) ):

        if(isCheckEmpty(i, copy)):
            assignMove(copy,symbol,i)
            if(checkWin(copy,symbol)):
                return i
            else:
                #refresh list
                copy = list(board)

    return None

#----------------------------------------------------------------------------------------
def blockStrat(board, humanSymbol):


    cornerList = [1,3,7,9]
    x = 0

    for i in range(len(cornerList)):

        if( board[cornerList[i]] == humanSymbol  ):
            x += 1
            if (x >= 1):
                return True

    return False


#----------------------------------------------------------------------------------------
def takeSides(board, cornerList):

    openSpace = []

    for i in range(len(cornerList)):
        if ( isinstance(cornerList[i], int) ):
            if( isCheckEmpty(cornerList[i], board) ):
                openSpace.extend([cornerList[i]])

    if(len(openSpace) != 0):
        return int(random.choice(openSpace))
    else:
        return None

#----------------------------------------------------------------------------------------



#start game intialization
while True:
    #create tic tac toe board size
    #theBoard = [' '] * 10
    theBoard = ["0","1","2","3","4","5","6","7","8","9"]
    diffic = setDificulty()
    gameInSession = True
    humanChar, computerChar = playerSymbol()
    Turn = firstTurn()

    print( Turn +  " Goes First." )


    while gameInSession == True:

        #if Human turn is first
        if (Turn is "Human"):
            displayBoard(theBoard)
            move = getPlayerMove(theBoard)
            assignMove(theBoard,humanChar,move)

            if checkWin(theBoard,humanChar):
                print("Winner")
                displayBoard(theBoard)
                gameInSession = False

            elif fullBoard(theBoard):
                print("TIE!")
                displayBoard(theBoard)
                gameInSession = False

            else:
                print("\nComputer's Turn \n")
                Turn = "Computer"

        else:#Computer's Turn
            computerMove(theBoard, computerChar, diffic, humanChar)

            if(checkWin(theBoard,computerChar)):
                print("Winner")
                displayBoard(theBoard)
                gameInSession = False

            elif fullBoard(theBoard):
                print("TIE!")
                gameInSession = False
            else:
                print("\n Human's Turn \n")
                Turn = "Human"

    if not playAgain():
        #exit loop
        print("EXITING")
        break

