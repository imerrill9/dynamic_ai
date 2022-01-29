from statistics import mean


class Possibilities:
    def __init__(self, game_list):
        self.board = self.__calculate_possibilities(game_list)
        self.game_list = game_list

    def victory_list(self, first_or_second):
        victory_list = []
        if first_or_second == "first":
            for i in range(len(self.game_list)):
                victory_list.append(self.board[i][len(self.game_list) - 1 - i])
            return victory_list
        else:
            for i in range(len(self.game_list) + 1):
                victory_list.append(self.board[i][len(self.game_list) - i])
            return victory_list

    def best_turn_order(self):
        first_victory_list = self.victory_list("first")
        second_victory_list = self.victory_list("second")
        average_first = mean(first_victory_list)
        average_second = mean(second_victory_list)
        if average_first > average_second:
            return "first"
        else:
            return "second"

    def best_move(self, victory_list):
        average_score_first = self.average_score(victory_list, "first")
        average_score_last = self.average_score(victory_list, "last")
        if average_score_first > average_score_last:
            return "first"
        else:
            return "last"

    def average_score(self, victory_list, first_or_last):
        copy = victory_list[:]
        print(f"vicotry list {victory_list}")
        if first_or_last == "first":
            copy.pop()
            return mean(copy)
        else:
            copy.pop(0)
            return mean(copy)

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
