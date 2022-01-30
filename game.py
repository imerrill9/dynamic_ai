class Game:
    def __init__(self, game_list):
        self.game_list = game_list
        self.x = 0
        self.y = len(game_list) - 1
        self.player_score = 0
        self.computer_score = 0

    def print_list(self):
        return self.game_list[self.x : (self.y + 1)]

    def is_finished(self):
        if self.x > self.y:
            return True
        else:
            return False
