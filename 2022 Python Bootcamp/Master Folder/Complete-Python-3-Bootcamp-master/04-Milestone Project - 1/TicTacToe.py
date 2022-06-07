import random
from turtle import pos, position

def xOCalculator():
    return random.randint(1,2)

def first_Go():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def ticTacBoard(board):

    print('   |   |   ')
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

def xOrOPlacement(board, marker, position):
    board[position] = marker

def space_check(board, position):
    return board[position] == ' '

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def full_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def playChoice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def playAgain():
    return input('Do you want to play again? (Yes or No): ').lower().startswith('y')



print("This is Tic-Tac-Toe, I will first flip a coin to decide who gets X and who gets O, and another to decide who moves first.")

while True:
    ticBoard = [' '] * 10

    xOCalculator()
    if xOCalculator() == 1:
        print("Player 1 you are X's.")
        strXOrO = 'X'
        strXOrO2 = 'O'
    else:
        print("Player 1 you are O's.")
        strXOrO = 'O'
        strXOrO2 = 'X'
    
    turn = first_Go()
    print(turn + " gets the first move!")
    
    play = input('Are you ready to get this show on the road? (Yes or No): ')
    if play.lower()[0] == 'y':
        game = True
    else:
        game = False
    
    while game:
        if turn == 'Player 1':
            ticTacBoard(ticBoard)
            position = playChoice(ticBoard)
            xOrOPlacement(ticBoard, strXOrO, position)

            if win_check(ticBoard, strXOrO):
                ticTacBoard(ticBoard)
                print("Player 1 WINS!!!!!")
                game = False
            else:
                if full_check(ticBoard):
                    ticTacBoard(ticBoard)
                    print("This game is an absolute deadlock...You've gotta play again now! WE NEED A CHAMPION!!!!")
                    break
                else:
                    turn = 'Player 2'
        else:
            print("Player 2's Turn: \n")
            ticTacBoard(ticBoard)
            position = playChoice(ticBoard)
            xOrOPlacement(ticBoard, strXOrO2, position)

            if win_check(ticBoard, strXOrO2):
                ticTacBoard(ticBoard)
                print("Player 2 WINS!!!!!")
                game = False
            else:
                if full_check(ticBoard):
                    ticTacBoard(ticBoard)
                    print("This game is an absolute deadlock...You've gotta play again now! WE NEED A CHAMPION!!!!")
                    break
                else:
                    turn = 'Player 1'                
    if not playAgain():
        break
