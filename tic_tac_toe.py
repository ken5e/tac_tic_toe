# tac tic toe game
from sys import exit
import random
import time


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

    def updateboard(self, position, letter):
        self.cells[position] = letter

    def win(self, letter):
        if self.cells[1] == self.cells[2] == self.cells[3] == letter:
            return True
        elif self.cells[4] == self.cells[5] == self.cells[6] == letter:
            return True
        elif self.cells[7] == self.cells[8] == self.cells[9] == letter:
            return True
        elif self.cells[1] == self.cells[4] == self.cells[7] == letter:
            return True
        elif self.cells[2] == self.cells[5] == self.cells[8] == letter:
            return True
        elif self.cells[3] == self.cells[6] == self.cells[9] == letter:
            return True
        elif self.cells[1] == self.cells[5] == self.cells[9] == letter:
            return True
        elif self.cells[3] == self.cells[5] == self.cells[7] == letter:
            return True
        else:
            return False

    def choose(self):
        valid_choice = False

        while not valid_choice:
            choice = input("Make X a 1. human 2. computer (1,2): ")

            if choice == "1":
                valid_choice = True
                p = Human()
                return p
            elif choice == "2":
                valid_choice1 = True
                p = Computer()
                return p
            else:
                print("Invalid input!")

demoboard = Board()
demoboard.cells = list(range(0,10))
board = Board()


class Player():

    def get_move(self, game):
        pass


class Human(Player):

    def get_move(self):
        valid_square = False
        place = None

        while not valid_square:

            print("Here are numbers you can choose.")
            print(board.numlist)
            place = input("Input a valid number: ")

            try:
                position = int(place)

                if position not in board.numlist:
                    raise ValueError

                valid_square = True
                board.numlist.remove(position)
                print(f"You made a move to {position}.")
                return position

            except ValueError:
                print("Invalid input!")


class Computer(Player):

    def get_move(self):
        val = random.choice(board.numlist)
        board.numlist.remove(val)
        print(f"Computer made a move to {val}.")
        time.sleep(0.5)
        return val

def play(xp, op):

    letter = "X"

    while True:
        print(f"This is {letter}'s turn.")

        if letter == "X":
            square = xp.get_move()
        else:
            square = op.get_move()

        board.updateboard(square,letter)
        board.printboard()

        if board.win(letter):
            print(f"\nPlayer {letter} won!")
            break
        elif board.numlist == []:
            print("\nTied.")
            break

        letter = "O" if letter =="X" else "X"

print("Welcome to tic tac toe!")
print("Numbers 1-9 correspond to their positions accordingly.")
demoboard.printboard()
p1 = board.choose()
p2 = board.choose()
play(p1,p2)

input("Press Enter to exit.")
exit(0)
