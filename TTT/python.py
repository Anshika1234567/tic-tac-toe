import math

# Constants for the game
BOARD_EMPTY = 0
BOARD_PLAYER_X = 1
BOARD_PLAYER_O = -1

class TicTacToe:
    def __init__(self):
        self.board = [BOARD_EMPTY] * 9
        self.current_player = BOARD_PLAYER_X

    def print_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[3 * i + j] == BOARD_PLAYER_X:
                    print('X', end=' ')
                elif self.board[3 * i + j] == BOARD_PLAYER_O:
                    print('O', end=' ')
                else:
                    print('_', end=' ')
            print()

    def is_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_full(self):
        return all(cell != BOARD_EMPTY for cell in self.board)

    def minimax(self, depth, is_maximizing):
        if self.is_winner(BOARD_PLAYER_O):
            return 10 - depth
        if self.is_winner(BOARD_PLAYER_X):
            return depth - 10
        if self.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == BOARD_EMPTY:
                    self.board[i] = BOARD_PLAYER_O
                    score = self.minimax(depth + 1, False)
                    self.board[i] = BOARD_EMPTY
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == BOARD_EMPTY:
                    self.board[i] = BOARD_PLAYER_X
                    score = self.minimax(depth + 1, True)
                    self.board[i] = BOARD_EMPTY
                    best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = -1
        for i in range(9):
            if self.board[i] == BOARD_EMPTY:
                self.board[i] = BOARD_PLAYER_O
                score = self.minimax(0, False)
                self.board[i] = BOARD_EMPTY
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def play(self):
        while True:
            self.print_board()
            if self.current_player == BOARD_PLAYER_X:
                move = int(input("Player X, enter your move (0-8): "))
                if self.board[move] == BOARD_EMPTY:
                    self.board[move] = BOARD_PLAYER_X
                    if self.is_winner(BOARD_PLAYER_X):
                        self.print_board()
                        print("Player X wins!")
                        break
                    self.current_player = BOARD_PLAYER_O
            else:
                move = self.best_move()
                self.board[move] = BOARD_PLAYER_O
                if self.is_winner(BOARD_PLAYER_O):
                    self.print_board()
                    print("Player O wins!")
                    break
                self.current_player = BOARD_PLAYER_X

            if self.is_full():
                self.print_board()
                print("It's a tie!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()