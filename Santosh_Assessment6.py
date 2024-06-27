# Create a simulation for Tic Tac Toe | Assignment 6

class TicTacToe:
    def __init__(self, game_structure: list):
        self.game_structure = game_structure
        self.current_player = 'X'

    def conditions(self):
        for i in range(3):
            if all(self.game_structure[i][j] == self.current_player for j in range(3)):
                return f"Player {self.current_player} wins!"
            if all(self.game_structure[j][i] == self.current_player for j in range(3)):
                return f"Player {self.current_player} wins!"

        if all(self.game_structure[i][i] == self.current_player for i in range(3)):
            return f"Player {self.current_player} wins!"
        if all(self.game_structure[i][2-i] == self.current_player for i in range(3)):
            return f"Player {self.current_player} wins!"

        if all(isinstance(self.game_structure[i][j], str) for i in range(3) for j in range(3)):
            return "The Game is Draw! \nYou have to be more intelligent than your opponent to win so work hard and come next time!!!"

        return None

    def gameOutput(self):
        return "\n".join([" ".join([str(j) for j in i]) for i in self.game_structure])

    def input_from_user(self):
        while True:
            user_input = input(
                f"Player {self.current_player}, enter a number you want to change (type 'stop' to exit): ")
            if user_input.lower() == 'stop':
                return False
            try:
                user_input = int(user_input)
                if user_input not in range(1, 10):
                    raise ValueError
                for i in range(3):
                    for j in range(3):
                        if self.game_structure[i][j] == user_input:
                            self.game_structure[i][j] = self.current_player
                            return True
                print("This spot is already taken. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'


game_struct = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
gamePlay = TicTacToe(game_struct)

print("Initial Game Structure :::")
print(gamePlay.gameOutput())

while True:
    if not gamePlay.input_from_user():
        break
    print("\nCurrent Game Structure :::")
    print(gamePlay.gameOutput())

    result = gamePlay.conditions()
    if result:
        print(result)
        break

    gamePlay.switch_player()

print("Final Game Structure :::")
print(gamePlay.gameOutput())
print("Game Over. Win and lose is just a part of game, never be disappointed 😁 \n... Thank You :)")
