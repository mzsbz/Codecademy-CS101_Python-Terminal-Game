class TicTacToe:
    win_conditions = [
        ['A1', 'B1', 'C1'],
        ['A2', 'B2', 'C2'],
        ['A3', 'B3', 'C3'],
        ['A1', 'A2', 'A3'],
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3'],
        ['A1', 'B2', 'C3'],
        ['A3', 'B2', 'C1']
    ]

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.players = [player_1, player_2]

    def render_table(self):
        table = {
            0: "0 | 1 | 2 | 3 |",
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

        for row in table:
            print(''.join(table[row]))



class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.moves = []

    def move(self, move):
        self.moves.append(move)

player_1 = Player("Alex", "X")
player_2 = Player("Lisa", "O")
game = TicTacToe(player_1, player_2)

player_1.move("A1")
player_2.move("B2")
game.render_table()