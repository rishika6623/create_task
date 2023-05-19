class Game():

    def __init__(self, player_1 = "Player 1", player_2 = "Player 2"):

        #creates all the formatting set up for the user at the start of a new game
        self.player_1 = player_1
        self.player_2 = player_2

        #makes new board of users desired size at the start of each game
        self.coordinates = []
        self.p1 = [] #what player 1 has played
        self.p2 = [] #what player 2 has played
        self.board = [["-"] * 3 for i in range(3)]

        for x in range(3):
            for y in range(3):
                self.coordinates.append([x,y])

        self.end_game = False
        self.games_won = [0,0] #number of games player 1 won, number of games player 2 won

    def reset_game(self):
        self.coordinates = []
        self.p1 = []
        self.p2 = []
        self.board = [["-"] * 3 for i in range(3)]

        for x in range(3):
            for y in range(3):
                self.coordinates.append([x,y])

        self.end_game = False

    #after any changes made to the board, it is displayed to the user
    def print_board(self):
        print()
        for row in self.board:
            for element in row:
                print("    " + element, end = "")
            print()
            print()

    #if someone has a connection print "[their name]",
    #if there is no result print nothing and continue
    #if there is a tie print "tie"
    #if continue, then variable end_game = False, if there is a winner or a tie, end_game = True
    def check(self):
        #tie
        if len(self.coordinates) == 0:
            print("There is a tie")
            self.end_game = True
            print(self.player_1 + "'s games won: " + str(self.games_won[0]))
            print(self.player_2 + "'s games won: " + str(self.games_won[1]))
            return

        #player 1 win?
        for i in range(3):
            row_check = [[i,0], [i,1], [i,2]]
            column_check = [[0,i], [1,i], [2,i]]
            # check if any row or column are full for player 1 (a win!)
            if all(coordinate in self.p1 for coordinate in row_check) or all(coordinate in self.p1 for \
                                                                             coordinate in column_check):
                print(self.player_1 + " Wins!!")
                print()
                self.games_won[0] +=1
                print(self.player_1 + "'s games won: " + str(self.games_won[0]))
                print(self.player_2 + "'s games won: " + str(self.games_won[1]))
                self.end_game = True
        # check if either diagnol is full for player 1 since only 2 personalities exist (a win!)
        diagnol_right = [[0,0], [1,1], [2,2]]
        diagnol_left = [[2,0], [1,1], [0,2]]
        if all(coordinate in self.p1 for coordinate in diagnol_right) or all(coordinate in self.p1 for \
                                                                             coordinate in  diagnol_left):
            print(self.player_1 + " Wins!!")
            print()
            self.games_won[0] +=1
            print(self.player_1 + "'s games won: " + str(self.games_won[0]))
            print(self.player_2 + "'s games won: " + str(self.games_won[1]))
            self.end_game = True

        #player 2 win?
        for i in range(3):
            row_check = [[i,0], [i,1], [i,2]]
            column_check = [[0,i], [1,i], [2,i]]
            # check if any row or column are full for player 1 (a win!)
            if all(coordinate in self.p2 for coordinate in row_check) or all(coordinate in self.p2 for \
                                                                             coordinate in column_check):
                print(self.player_2 + " Wins!!")
                print()
                self.games_won[1] +=1
                print(self.player_1 + "'s games won: " + str(self.games_won[0]))
                print(self.player_2 + "'s games won: " + str(self.games_won[1]))
                self.end_game = True
        # check if either diagnol is full for player 1 since only 2 personalities exist (a win!)
        diagnol_right = [[0,0], [1,1], [2,2]]
        diagnol_left = [[2,0], [1,1], [0,2]]
        if all(coordinate in self.p2 for coordinate in diagnol_right) or all(coordinate in self.p2 for \
                                                                             coordinate in  diagnol_left):
            print(self.player_2 + " Wins!!")
            print()
            self.games_won[1] +=1
            print(self.player_1 + "'s games won: " + str(self.games_won[0]))
            print(self.player_2 + "'s games won: " + str(self.games_won[1]))
            self.end_game = True



    def play(self, player, coordinate):

        #if the given coordinate has not been played yet
        if [int(coordinate[0]), int(coordinate[2])] in self.coordinates:
            if player ==1:
                #add coordinate to player 1 list by removing from coordinates list
                self.p1.append(self.coordinates.pop(self.coordinates.index \
                                                    ([int(coordinate[0]), int(coordinate[2])])))
                self.board[int(coordinate[0])][int(coordinate[2])] = "x"
                self.print_board()
                self.check()
                return True
            else:
                #add coordinate to player 2 list by removing from coordinates list
                self.p2.append(self.coordinates.pop(self.coordinates.index \
                                                    ([int(coordinate[0]), int(coordinate[2])])))
                self.board[int(coordinate[0])][int(coordinate[2])] = "o"
                self.print_board()
                self.check()
                return True

        #if coordinate is played, return true
        #if coordiante doesn't exist return false
        else:
            return False


def main():

    new_game = "y"
    player_1 = input("What is player 1's name: ")
    player_2 = input("What is player 2's name: ")
    running_game = Game(player_1, player_2)

    while new_game == "y":
        running_game.print_board()

        while not running_game.end_game:

            p1_coordinate = input(running_game.player_1 + " pick a spot (row, column, 0-2):  ")
            while running_game.play(1, p1_coordinate) == False:
                p1_coordinate = input(running_game.player_1 + " pick a spot (row, column, 0-2):  ")

            if running_game.end_game == True:
                break

            p2_coordinate = input(running_game.player_2 + " pick a spot (row, column, 0-2):  ")
            while running_game.play(2, p2_coordinate) == False:
                p2_coordinate = input(running_game.player_2 + " pick a spot (row, column, 0-2):  ")

        print()
        new_game = input("Would you like to play another game? (y/n):  ")
        running_game.reset_game()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()