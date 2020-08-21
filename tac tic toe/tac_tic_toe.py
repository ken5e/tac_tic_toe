# tac tic toe game
from sys import exit


class Board():

    def __init__(self):
        self.cells = [" "] * 10
        self.numlist = list(range(1,10))

    def printboard(self):
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print("-" * 11)
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print("-" * 11)
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")

    def updateboard(self, position, player):
        self.cells[position] = player

    def win(self, player):
        if self.cells[1] == self.cells[2] == self.cells[3] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[4] == self.cells[5] == self.cells[6] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[7] == self.cells[8] == self.cells[9] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[1] == self.cells[4] == self.cells[7] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[2] == self.cells[5] == self.cells[8] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[3] == self.cells[6] == self.cells[9] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[1] == self.cells[5] == self.cells[9] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.cells[3] == self.cells[5] == self.cells[7] == player:
            print(f"\nPlayer {player} won!")
            return True
        elif self.numlist == []:
            print("\nTied.")
            return True

demoboard = Board()
demoboard.cells = list(range(0,10))
board = Board()

print("Welcome to tic tac toe!")
print("Numbers 1-9 correspond to their positions accordingly.")
demoboard.printboard()


current_player = "X"
next_player = "O"

while True:

    print(" ")
    print(f"This is player {current_player} turn.")
    print("Here are numbers you can input.")
    print(board.numlist)
    place = input("Input a valid number: ")

    try:
        position = int(place)

        if  position in board.numlist:
            board.updateboard(position, current_player)
            board.numlist.remove(position)
            board.printboard()

            if board.win(current_player):
                break

            current_player, next_player = next_player, current_player


        else:
            print("Invalid input!\n")

    except ValueError:
        print("Invalid input!\n")

input("Press Enter to exit.")
exit(0)
