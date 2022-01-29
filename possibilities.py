class Possibilities:
    def __init__(self, game_list):
        self.board = self.__calculate_possibilities(game_list)

    def __calculate_possibilities(self, game_list):
        board = [[0 for x in range(len(game_list) + 1)] for y in range(len(game_list) + 1)]

        # starting values
        board[0][1] = game_list[len(game_list) - 1]
        board[1][0] = game_list[0]

        return self.__run_scenarios(board, game_list, 0, 2)

    def __run_scenarios(self, board, game_list, x, y):
        # base case
        if y > len(game_list):
            return board

        # restart diagnal traversal one level higher
        if y < 0:
            return self.__run_scenarios(board, game_list, 0, x)
        else:
            # calculate board possition
            if x == 0:
                board[x][y] = game_list[len(game_list) - y] + board[x][y - 2]
            elif y == 0:
                board[x][y] = game_list[x - 1] + board[x - 2][y]
            else:
                board[x][y] = game_list[len(game_list) - y] + board[x - 1][y - 1]

            # recurse
            return self.__run_scenarios(board, game_list, x + 1, y - 1)

    def print_board(self):
        for row in self.board:
            print(str(row))
