class Possibilities:
    def __init__(self, game_list):
        self.board = self.__calculate_possibilities(game_list)
        self.game_list = game_list

    def best_turn_order(self):
        if self.board[0][len(self.game_list) - 1][0] > self.board[0][len(self.game_list) - 1][1]:
            return "first"
        else:
            return "second"

    def best_move(self, x, y):
        return self.board[x][y][2]

    def __calculate_possibilities(self, game_list):
        # (first, second, best_move)
        board = [[(0, 0, 0) for x in range(len(game_list))] for y in range(len(game_list))]

        # starting values
        for i in range(len(game_list)):
            board[i][i] = (i, 0, "first")

        for i in range(len(game_list)):
            board = self.__run_scenarios(board, game_list, 0, i + 1)

        return board

    def __run_scenarios(self, board, game_list, x, y):
        if y > len(game_list) - 1:
            return board

        consider_first = board[x + 1][y][1] + game_list[x]
        consider_last = board[x][y - 1][1] + game_list[y]
        if consider_first > consider_last:
            board[x][y] = (consider_first, board[x + 1][y][0], "first")
        else:
            board[x][y] = (consider_last, board[x][y - 1][0], "last")

        return self.__run_scenarios(board, game_list, x + 1, y + 1)
