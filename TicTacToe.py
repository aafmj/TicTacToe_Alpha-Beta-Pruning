class TicTocToe:

    def __init__(self):
        self.x_win = "X_WIN"
        self.o_win = "O_WIN"
        self.tie = "TIE"
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.player_turn = 'X'


    def play(self):
        while True:
            self.print_board()
            self.result = self.get_status()

            if self.result is not None:
                if self.result == self.x_win:
                    print('X is winner.')
                elif self.result == self.o_win:
                    print('O is winner.')
                elif self.result == self.tie:
                    print("Tie.")

                return

            if self.player_turn == 'X':
                while True:
                    x = int(input('No of row (1,2,3) : ')) - 1
                    y = int(input('No of col (1,2,3) : ')) - 1

                    if self.is_valid(x, y):
                        self.board[x][y] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('move not valid. try again')

            else:
                # its look like -infinity & +infinity
                (v, x, y) = self.maximizer(-2, 2)
                self.board[x][y] = 'O'
                self.player_turn = 'X'


    def maximizer(self, alpha, beta):
        max_v = -2
        x = None
        y = None

        result = self.get_status()

        if result == self.x_win:
            return -1, 0, 0
        elif result == self.o_win:
            return 1, 0, 0
        elif result == self.tie:
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '-':
                    self.board[i][j] = 'O'
                    (v, min_i, min_j) = self.minimizer(alpha, beta)
                    if v > max_v:
                        max_v = v
                        x = i
                        y = j
                    self.board[i][j] = '-'

                    if max_v >= beta:
                        return max_v, x, y

                    if max_v > alpha:
                        alpha = max_v

        return max_v, x, y


    def minimizer(self, alpha, beta):
        min_v = 2
        x = None
        y = None

        result = self.get_status()
        if result == self.x_win:
            return -1, 0, 0
        elif result == self.o_win:
            return 1, 0, 0
        elif result == self.tie:
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '-':
                    self.board[i][j] = 'X'
                    (v, max_i, max_j) = self.maximizer(alpha, beta)
                    if v < min_v:
                        min_v = v
                        x = i
                        y = j
                    self.board[i][j] = '-'

                    if min_v <= alpha:
                        return min_v, x, y

                    if min_v < beta:
                        beta = min_v

        return min_v, x, y


    def print_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if j != 2:
                    print('{} | '.format(self.board[i][j]), end="")
                else:
                    print('{}'.format(self.board[i][j]), end="")
            print()
        print()


    def is_valid(self, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2 or self.board[x][y] != '-':
            return False
        return True


    def get_status(self):
        # vertical check
        for i in range(0, 3):
            if (self.board[0][i] != '-' and
                    self.board[0][i] == self.board[1][i] == self.board[2][i]):
                if self.board[0][i] == "X":
                    return self.x_win
                return self.o_win

        # horizontal check
        for i in range(0, 3):
            if self.board[i] == ['X', 'X', 'X']:
                return self.x_win
            elif self.board[i] == ['O', 'O', 'O']:
                return self.o_win

        # main diagonal check
        if (self.board[0][0] != '-' and
                self.board[0][0] == self.board[1][1] == self.board[2][2]):
            if self.board[0][0] == "X":
                return self.x_win
            return self.o_win
                

        # subsidiary diagonal check
        if (self.board[0][2] != '-' and
                self.board[0][2] == self.board[1][1] == self.board[2][0]):
            if self.board[0][2] == "X":
                return self.x_win
            return self.o_win
                

        # full board check
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == '-':
                    return None

        # tie
        return self.tie


if __name__ == "__main__":
    tic_toc_toe = TicTocToe()
    tic_toc_toe.play()
