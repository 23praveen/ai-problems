import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize the board with empty spaces
        self.current_winner = None

    def print_board(self):
        # Print the current board state
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Print the numbers for each position on the board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Return a list of available moves (empty squares)
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        # Place the letter on the board at the given square
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check if the most recent move resulted in a win
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def is_board_full(self):
        # Check if the board is full
        return ' ' not in self.board


def minimax(board, maximizing_player, alpha, beta):
    if board.current_winner is not None:
        if board.current_winner == 'X':
            return -1
        else:
            return 1
    elif board.is_board_full():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, False, alpha, beta)
            board.board[move] = ' '  # undo move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, True, alpha, beta)
            board.board[move] = ' '  # undo move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(board):
    best_move = None
    best_eval = -math.inf
    for move in board.available_moves():
        board.make_move(move, 'O')
        eval = minimax(board, False, -math.inf, math.inf)
        board.board[move] = ' '  # undo move
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def play_game():
    # Function to play the Tic Tac Toe game against the computer using Minimax algorithm
    game = TicTacToe()
    print("Welcome to Tic Tac Toe!")

    player1 = 'X'
    player2 = 'O'
    current_player = player1

    while not game.is_board_full():
        game.print_board_nums()
        game.print_board()

        if current_player == player1:
            move = None
            while move not in game.available_moves():
                try:
                    move = int(input(f"{current_player}'s turn. Choose a position from 0-8: "))
                except ValueError:
                    print("Invalid input. Please enter a number from 0 to 8.")
            game.make_move(move, current_player)
        else:
            move = get_best_move(game)
            game.make_move(move, current_player)
            print(f"Computer placed an 'O' in position {move}")

        if game.current_winner:
            print(f"{game.current_winner} wins!")
            break
        else:
            current_player = player2 if current_player == player1 else player1

    if not game.current_winner:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()
