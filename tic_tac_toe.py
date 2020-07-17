class Player(object):

    #Attributes

    def __init__(self, name, game_piece):
        self.game_piece = game_piece #whether player is X or O
        self.name = name #name of player

class Move(object):

    #Attributes

    def __init__(self, player, position):
        self.player = player #who made the move
        self.position = position #where the move is placed on the board

class Board(object):

     #Attributes
    current_board = [["X","X","X"],["-","-","-"],["-","-","-"]]


    #Methods

    def display(self):
        for line in self.current_board:
            print(" ".join(line))

    def add_move(self, move):
        row = move.position[0]
        column = move.position[1]
        self.current_board[row][column] = move.player.game_piece
        

class Game(object):

    def __init__(self, board, player1, player2):
        self.board = []
        self.player1 = player1
        self.player2 = player2

    def check_win(self):
        for row in self.board:
            print(row)
        #     if row[0] == row[1] == row[2] == self.player.game_piece:
        #         winner = self.player
        # print(winner)
        


harry = Player("Harry", "X")
hermione = Player("Hermione", "O")

my_board = Board()

my_game = Game(my_board, harry, hermione)

first_move = Move(harry, [0, 2])

my_board.add_move(first_move)

my_board.display()

my_game.check_win()



