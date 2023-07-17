import os

class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.moves = []

class TicTacToe:
    win_conditions = [
        {'A1', 'B1', 'C1'},
        {'A2', 'B2', 'C2'},
        {'A3', 'B3', 'C3'},
        {'A1', 'A2', 'A3'},
        {'B1', 'B2', 'B3'},
        {'C1', 'C2', 'C3'},
        {'A1', 'B2', 'C3'},
        {'A3', 'B2', 'C1'}
    ]

    valid_moves = [
        'A1', 'A2', 'A3',
        'B1', 'B2', 'B3',
        'C1', 'C2', 'C3'
    ]


    def __init__(self):
        self.all_moves = []
        self.game_over = False
        self.turn = 0


    def advance_turn(self):
        self.turn ^= 1
        self.message_turn = f"{self.players[self.turn].name}'s turn."


    def check_valid(self, input):
        self.message_valid = ""
        if input not in TicTacToe.valid_moves or input in self.all_moves:
            self.message_valid = "Invalid Move!"
            return False
        return True

    def check_win(self, player):
        
        '''
        Converts player_moves list into a set.
        Converts win_conditions list into a set
        If win_condition is subset of player_moves
        Player wins
        '''

        player_moves_set = set(self.players[player].moves)
        win_conditions = TicTacToe.win_conditions

        for win_condition in win_conditions:
            if win_condition <= player_moves_set:
                self.message_winner = f"{self.players[player].name} has won!"
                self.game_over = True
                break


    def move(self, input):

        all_moves = self.all_moves
        player_moves = self.players[self.turn].moves
        
        if self.check_valid(input):
            all_moves.append(input)
            player_moves.append(input)
            self.check_win(self.turn)
            self.advance_turn()


    def render_table(self):
        table = {
            0: "  | 1 | 2 | 3 |",
            1: "---------------",
            "A": ["A |", "   |", "   |", "   |"],
            3: "---------------",
            "B": ["B |", "   |", "   |", "   |"],
            5: "---------------",
            "C": ["C |", "   |", "   |", "   |"],
        }      

        for player in self.players:
            for move in player.moves:
                move_row = move[:1]
                move_col = int(move[1:])

                table[move_row][move_col] = f" {player.token} |"

        os.system('cls' if os.name == 'nt' else 'clear')
        print("Tic Tac Toe!")
        print("\n")

        for row in table:
            print(''.join(table[row]))

        print("\n")

    
    def render_messages(self):
        if self.message_valid:
            print(self.message_valid)
        if not self.game_over:
            print(self.message_turn)
        else:
            print(self.message_winner)


    def start(self):
        message = "Welcome to Tic Tac Toe! \n"
        print(message)

        self.player_1 = Player(input("Enter Player 1 Name: "), "O")
        self.player_2 = Player(input("Enter Player 2 Name: "), "X")
        self.players = [self.player_1, self.player_2]

        self.render_table()
        print(f"{self.players[self.turn].name}'s turn.")

        while not self.game_over:
            user_input = input("Select Cell: ").upper()
            self.move(user_input)
            self.render_table()
            self.render_messages()



game = TicTacToe()
game.start()