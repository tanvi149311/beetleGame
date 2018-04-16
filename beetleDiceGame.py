import random
import sys
#global variables for checking previous correct roll
class generator:

    def __init__(self):
        self.sequence = {1: "   #######\n   #  |  #\n   #  |  #\n   #  |  #\n   #######",
        2: "    ##### \n    #   # \n   #######\n   #  |  #\n   #  |  #\n   #  |  #\n   #######",
        31: "    ##### \n    #   # \n   #######\n/^\\#  |  #\n/^\\#  |  #\n/^\\#  |  #\n   #######",
        32: "    ##### \n    #   # \n   #######\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n   #######",
        41: "     \\\n    ##### \n    #   # \n   #######\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n   #######",
        42: "     \\ /\n    ##### \n    #   # \n   #######\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n   #######",
        51: "     \\ /\n    ##### \n    #0  # \n   #######\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n   #######",
        52: "     \\ /\n    ##### \n    #0 0# \n   #######\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n   #######",
        6: "     \\ /\n    ##### \n    #0 0# \n   #######\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n/^\\#  |  #/^\\\n   #######\n     ###\n      #"
        }

    def beetleGenerator(self, dice, previousMove):
        self.dice = dice;
        self.previousMove= previousMove;
        if(self.previousMove == 0 and self.dice ==1):
            self.previousMove = self.previousMove+1
            print(self.sequence[1])
            return self.previousMove
        elif(self.previousMove == 1 and self.dice ==2):
            self.previousMove = self.previousMove+1
            print(self.sequence[2])
            return self.previousMove
        elif(self.previousMove == 2 and self.dice ==3):
            self.previousMove = self.previousMove+1
            print(self.sequence[31])
            return self.previousMove
        elif(self.previousMove == 3 and self.dice ==3):
            self.previousMove = self.previousMove+1
            print(self.sequence[32])
            return self.previousMove
        elif(self.previousMove == 4 and self.dice ==4):
            self.previousMove = self.previousMove+1
            print(self.sequence[41])
            return self.previousMove
        elif(self.previousMove == 5 and self.dice ==4):
            self.previousMove = self.previousMove+1
            print(self.sequence[42])
            return self.previousMove
        elif(self.previousMove == 6 and self.dice ==5):
            self.previousMove = self.previousMove+1
            print(self.sequence[51])
            return self.previousMove
        elif(self.previousMove == 7 and self.dice ==5):
            self.previousMove = self.previousMove+1
            print(self.sequence[52])
            return self.previousMove
        elif(self.previousMove == 8 and self.dice ==6):
            self.previousMove = self.previousMove+1
            print(self.sequence[6])
            return self.previousMove
        else:
            return self.previousMove

### Player Class
class player:

    def __init__(self, name, isPlayer):
        self.name = name
        self.isPlayer = isPlayer
        self.lastMove = 0

    def getPlayer(self):
        return [self.name, self.isPlayer, self.lastMove]



### Game Class:
class game:
    ## roll dice method is returning random int in range 1 to 6
    def rollDice(self):
        dice = random.randint(1, 6)
        return dice

    #returns rollDice value if user entered r
    #else keeps checking for right input from user
    def getInput(self, name):
        self.name = name
        print(self.name + "'s turn")
        while(True and self.name != "Computer"):
            self.choice = input("Enter 'r' to role the dice\n")
            if (self.choice == 'r' or self.choice=='R'):
                break
            elif(self.choice =='q' or self.choice=='Q'):
                return sys.exit()
            else:
                print("Invalid Input, Try Again !")
                continue
        return self.rollDice()

    #starts the game
    def startGame(self, isSinglePlayer):
        self.isSinglePlayer = isSinglePlayer

        #creates an object of player for player1
        p1= player("Player1", True)
        if(isSinglePlayer):
            #creates an object of player for player2
            p2 = player("Computer", False)
        else:
            p2 = player("Player2", False)

        # play is list of player objects
        play = []
        play.append(p1)
        play.append(p2)

        #dice stores value of current roll
        dice = 0
        #flag to change from one player to other and vice versa
        switch = 0
        while(True):

            if(play[switch].isPlayer):
                dice = self.getInput(play[switch].name)
                print(play[switch].name+ " rolled "+str(dice))
                play[switch].lastMove = generator().beetleGenerator(dice, play[switch].lastMove)
                if(play[switch].lastMove == 9):
                    print(play[switch].name + " wins!!")
                    break;
                switch = 1
            else:
                dice = self.getInput(play[switch].name)
                print(play[switch].name+ " rolled "+str(dice))
                play[switch].lastMove =generator().beetleGenerator(dice, play[switch].lastMove)
                if(play[switch].lastMove == 9):
                    print(play[switch].name + " wins!!")
                    break;
                switch = 0


####### main menu logic
def mainMenu():
    while (True):
        print("Welcome to Beetle dice Game")
        print("Choose number of players below:")
        choice = input("Enter '1' for single player \nEnter '2' for two players \nEnter 'q' to quit\n")

        if (choice == '1'):
            print("Lets begin the Game ")
            g1 = game()
            g1.startGame(True)
        elif (choice == '2'):
            print("Lets begin the Game ")
            g2 = game()
            g2.startGame(False)
        elif (choice == 'q'):
            break
        else:
            print("Invalid Input, Try Again !")
            continue


mainMenu()
