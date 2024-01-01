import random
from pprint import pprint
class TicTac:
    def __init__(self):
        self.board = []

    def create_boards(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def print(self):
        print("   ",1,"  ",2,"  ",3)
        for i in range(3):
            print(i+1,self.board[i])
            print()
    def check_winner(self):
        #checking rows
        counter_x=0
        counter_o=0
        for i in range(3):
            if counter_x==3:
                return "Player 1 Won"
            elif counter_o==3:
                return "Player 2 Won"
            counter_x=0
            counter_o=0
            for j in range(3):
                if self.board[i][j] == "X":
                    counter_x+=1
                elif self.board[i][j] == "O":
                    counter_o+=1
        #checking columns
        counter_x = 0
        counter_o = 0
        for i in range(3):
            if counter_x == 3:
                return "Player 1 Won"
            elif counter_o == 3:
                return "Player 2 Won"
            counter_x = 0
            counter_o = 0
            for j in range(3):
                if self.board[j][i] == "X":
                    counter_x += 1
                elif self.board[j][i] == "O":
                    counter_o += 1
        #diagonal left
        counter_x = 0
        counter_o = 0
        for i in range(3):
            if self.board[i][i]=="X":
                counter_x+=1
            elif self.board[i][i]=="O":
                counter_o+=1
        if counter_x == 3:
            return "Player 1 Won"
        elif counter_o == 3:
            return "Player 2 Won"
        #diagonal right
        counter_x = 0
        counter_o = 0
        for i in range(2, -1, -1):
            if self.board[i][i]=="X":
                counter_x+=1
            elif self.board[i][i]=="O":
                counter_o+=1
        if counter_x == 3:
            return "Player 1 Won"
        elif counter_o == 3:
            return "Player 2 Won"
        #not won
        return False
    def check_board_full(self):
        if not any('-' in x for x in self.board):
            return True
        else:
            return False
    def change_board(self,coordinate,number):
        try:
            if number ==1:
                self.board[int(coordinate[0])-1][int(coordinate[1])-1]='X'
            else:
                self.board[int(coordinate[0]) - 1][int(coordinate[1]) - 1] = 'O'
        except:
            print("You need to Enter Integer")
    def lenght(self):
        print(len(self.board))
def players(player,number):
    coordinates = input(f'{player} coordinates: ').split(' ')
    game.change_board(coordinates,number)
    game.print()
    if game.check_winner() is not False:
        print(game.check_winner())
        return True
    if game.check_board_full():
        print('Draw')
        return True
game = TicTac()
game.create_boards()
game.print()

while not game.check_board_full():
    if players('Player 1',1):
        break
    if players('Player 2',2):
        break

