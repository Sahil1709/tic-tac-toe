import random

board = [' ' for x in range(10)]

def boardIsFree(pos):
    return board[pos] == ' '

def boardIsFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def drawBoard(board):
    print(" " + board[1] + " |" + " " + board[2] + " |" + " " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " |" + " " + board[5] + " |" + " " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " |" + " " + board[8] + " |" + " " + board[9] + " ")

def userInput(letter,pos):
    board[pos] = letter

def getWinner(board,l):
    return (board[1] == board[2] == board[3] == l 
        or board[4] == board[5] == board[6] == l
        or board[7] == board[8] == board[9] == l
        or board[1] == board[4] == board[7] == l
        or board[2] == board[5] == board[8] == l
        or board[3] == board[6] == board[9] == l
        or board[1] == board[5] == board[9] == l
        or board[3] == board[5] == board[7] == l)

def playerMove():
    run = True
    while run:
        move = input("Select position (1-9) to place X :")
        try:
            move = int(move)
            if move > 0 and move <10:
                if boardIsFree(move):
                    run = False
                    userInput('x',move)
                else:
                    print("Space is occupied .")
            else:
                print("Enter a number between (1-9)")
        except:
            print("Enter an integer.")

def compMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['x','o']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if getWinner(boardCopy,let):
                move = i 
                return move

    cornerMoves = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerMoves.append(i)
    if len(cornerMoves) > 0:
        move = random.choice(cornerMoves)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    
    edgeMoves = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgeMoves.append(i)
    if len(cornerMoves) > 0:
        move = random.choice(cornerMoves)
        return move

def main():
    drawBoard(board)
    while not(boardIsFull(board)):
        if not(getWinner(board,'o')):
            playerMove()
            drawBoard(board)
        else:
            print("You lose to computer")
            break

        if not(getWinner(board,'x')):
            move = compMove()
            if move == 0:
                print("no moves left")
            else:
                userInput('o',move)
                print(f" Computer placed O on {move} position.")
                drawBoard(board)
        else:
            print("Wohoo ! you WIN")
            break
    
    if boardIsFull(board):
        print("Game tied")

while True:
    x = input("Do u want to play again (y or n)!").lower()
    if x == 'y':
        board = [' ' for x in range(10)]
        main()
    else:
        break
