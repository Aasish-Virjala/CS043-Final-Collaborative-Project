import random
import sqlite3


player1Score = 0
player2Score = 0
winner=''
player1=''
player2=''

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O, ' + player1 + '?')
        letter = input().upper()


    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayer1Move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print('What is your next move, ' + player1 + '? (1-9)')
        move = input()
    return int(move)

def getPlayer2Move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print('What is your next move, ' + player2 + '? (1-9)')
        move = input()
    return int(move)

def isBoardFull(board):
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True


print('Welcome to Tic Tac Toe!')
print('Enter name, player 1')
player1 = input()
print('Who\'s your opponent, ' + player1)
player2 = input()
print('Welcome, ' + player1 + ' and ' + player2 + '!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player 1's turn.
            drawBoard(theBoard)
            move = getPlayer1Move(theBoard)
            makeMove(theBoard, player1Letter, move)

            if isWinner(theBoard, player1Letter):
                drawBoard(theBoard)
                print('Hooray! ' + player1 + ' has won the game! Sorry, ' + player2)
                gameIsPlaying = False
                player1Score += 1
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    player1Score += 1
                    player2Score += 1
                    break
                else:
                    turn = 'player2'

        else:
            # Player 2's turn.
            drawBoard(theBoard)
            move = getPlayer2Move(theBoard)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print(player2 + ' has won the game! Sorry, ' + player1)
                player2Score += 1
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not playAgain():
            break
