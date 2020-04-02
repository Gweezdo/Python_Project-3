# Dictionary to record player inputs
myDict = {
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

# Prints gameboard to console
def printBoard():
    print('\n'*20)
    print("     |     |     ")
    print("  " + myDict['7'] + "  " + "|" + "  " + myDict['8'] + "  " + "|" + "  " + myDict['9'] + "  ")
    print("     |     |     ")
    print('-----------------')
    print("     |     |     ")
    print("  " + myDict['4'] + "  " + "|" + "  " + myDict['5'] + "  " + "|" + "  " + myDict['6'] + "  ")
    print("     |     |     ")
    print('-----------------')
    print("     |     |     ")
    print("  " + myDict['1'] + "  " + "|" + "  " + myDict['2'] + "  " + "|" + "  " + myDict['3'] + "  ")
    print("     |     |     ")
    print('\n'*1)
    
def clearBoard(myDict):
    for key in myDict.keys():
        myDict[key] = " "

def winOrLose(myDict):
    tRow = [myDict['7'], myDict['8'], myDict['9']]
    mRow = [myDict['4'], myDict['5'], myDict['6']]
    bRow = [myDict['1'], myDict['2'], myDict['3']]
    lCol = [myDict['7'], myDict['4'], myDict['1']]
    mCol = [myDict['8'], myDict['5'], myDict['2']]
    rCol = [myDict['9'], myDict['6'], myDict['3']]
    diagDown = [myDict['7'], myDict['5'], myDict['3']]
    diagUp = [myDict['9'], myDict['5'], myDict['1']]
    totalList = tRow + mRow + bRow

    if tRow.count('X') == 3 or tRow.count('O') == 3:
        return True
    elif mRow.count('X') == 3 or mRow.count('O') == 3:
        return True
    elif bRow.count('X') == 3 or bRow.count('O') == 3:
        return True
    elif lCol.count('X') == 3 or lCol.count('O') == 3:
        return True
    elif mCol.count('X') == 3 or mCol.count('O') == 3:
        return True
    elif rCol.count('X') == 3 or rCol.count('O') == 3:
        return True
    elif diagDown.count('X') == 3 or diagDown.count('O') == 3:
        return True
    elif diagUp.count('X') == 3 or diagUp.count('O') == 3:
        return True
    else:
        count = 0
        for item in totalList:
            if item.isalpha():
                count+=1
                if count == 9:
                    print("It's a Draw")



def game_loop():
    print("Welcome to Tic Tac Toe")
    player1 = input("Type 'X' or 'O' to choose you fighter: ")

    if player1.lower() == 'x':
        player2 = 'O'
    else:
        player2 = 'X'    

    print("Player 1 will go first")
    print("Ready Player 1? Enter 'Yes' or 'No': ")
    startGame = input()

    if startGame.lower() == 'yes':
        printBoard()
        while True:
            print("Choose your next position: (1-9)")
            p1 = input()
            while int(p1) >= 10:
                print("Please type in only your next position: (1-9)")
                p1 = input()
            
            myDict[p1] = player1.upper()
            printBoard()
            
            if winOrLose(myDict) == True:
                print("Congratulations! You have won the game!")
                clearBoard(myDict)
                break
            else:
                print("Choose your next position: (1-9)")
                p2 = input()
                while int(p2) >= 10:
                    print("Please type in only your next position: (1-9)")
                    p2 = input()
                
                myDict[p2] = player2
                printBoard()

                if winOrLose(myDict) == True:
                    print("Congratulations! You have won the game!")
                    clearBoard(myDict)
                    break

            

    elif startGame.lower() == 'no':
        print("Goodbye")
        return

    else:
        pass
        return

    replay = input("Do you want to play again? Enter 'Yes' or 'No': ")

    if replay.lower() == 'yes':
        game_loop()
    else:
        print("Goodbye")


# Game Start
game_loop()



    

    