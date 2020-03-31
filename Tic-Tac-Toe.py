XorO = {
    '1':' ',
    '2':' ',
    '3':' ',
    '4':' ',
    '5':' ',
    '6':' ',
    '7':' ',
    '8':' ',
    '9':' '
}

def printBoard():
    print("     |     |     ")
    print("  " + XorO['7'] + "  " + "|" + "  " + XorO['8'] + "  " + "|" + "  " + XorO['9'] + "  ")
    print("     |     |     ")
    print('-----------------')
    print("     |     |     ")
    print("  " + XorO['4'] + "  " + "|" + "  " + XorO['5'] + "  " + "|" + "  " + XorO['6'] + "  ")
    print("     |     |     ")
    print('-----------------')
    print("     |     |     ")
    print("  " + XorO['1'] + "  " + "|" + "  " + XorO['2'] + "  " + "|" + "  " + XorO['3'] + "  ")
    print("     |     |     ")

printBoard()

print("Welcome to Tic Tac Toe")

player1 = input("Type 'X' or 'O' to choose you fighter: ")
print("Player 1 will go first")
print("Ready Player 1? Enter 'Yes' or 'No': ")
startGame = input()


player2 = input()