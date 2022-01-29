from possibilities import Possibilities
from random import randint


def main():
    print(
        """
________                                 _____           _______________
___  __ \____  ______________ _______ ______(_)______    ___    |___  _/
__  / / /_  / / /_  __ \  __ `/_  __ `__ \_  /_  ___/    __  /| |__  /  
_  /_/ /_  /_/ /_  / / / /_/ /_  / / / / /  / / /__      _  ___ |_/ /   
/_____/ _\__, / /_/ /_/\__,_/ /_/ /_/ /_//_/  \___/      /_/  |_/___/   
        /____/                                                            
        
        
Play a game vrs a computer that uses a dynamic programming algorithm to choose moves.

Who will win?

Given a list of 10 20 or 50 numbers, take turns choosing from the first number
or the last number to add to your score.

Highest score wins the game!

        """
    )
    choose_list_size()


def choose_list_size():
    print(
        """
-----------------------------------------------------------------------
Enter list size for the game
1. 10
2. 20
3. 30
           
        """
    )
    while True:
        command = input()
        if command == "1":
            choose_turn_order(10)
        elif command == "2":
            choose_turn_order(20)
        elif command == "3":
            choose_turn_order(30)
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def choose_turn_order(list_size):
    game_list = generate_random_game(list_size)
    global possibilities
    possibilities = Possibilities(game_list)
    player_score = 0
    computer_score = 0
    best_move = possibilities.best_turn_order()

    print(
        f"""
-----------------------------------------------------------------------
                           GAME ON!!

Computer: {computer_score}                        Player: {player_score}

{game_list}

The computer would like to go {best_move},
Is that ok? (y/n)
           
        """
    )

    while True:
        command = input()
        if command.lower() == "y":
            if best_move == "first":
                victory_list = possibilities.victory_list("first")
                run_game("computer", victory_list, game_list, player_score, computer_score)
            else:
                victory_list = possibilities.victory_list("second")
                run_game("player", victory_list, game_list, player_score, computer_score)
        elif command.lower() == "n":
            let_player_choose_turn_order(game_list, player_score, computer_score)
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def let_player_choose_turn_order(game_list, player_score, computer_score):
    print(
        f"""
-----------------------------------------------------------------------
Computer: {computer_score}                        Player: {player_score}

{game_list}

Would you like to go first or second? (f/s)
           
        """
    )

    while True:
        command = input()
        if command.lower() == "f":
            victory_list = possibilities.victory_list("second")
            run_game("player", victory_list, game_list, player_score, computer_score)
        elif command.lower() == "s":
            victory_list = possibilities.victory_list("first")
            run_game("computer", victory_list, game_list, player_score, computer_score)
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def run_game(first_player, victory_list, game_list, player_score, computer_score):
    while len(game_list) > 1:
        if first_player == "computer":
            computer_score = take_turn("computer", victory_list, game_list, player_score, computer_score)
            player_score = take_turn("player", victory_list, game_list, player_score, computer_score)
        else:
            player_score = take_turn("player", victory_list, game_list, player_score, computer_score)
            computer_score = take_turn("computer", victory_list, game_list, player_score, computer_score)


def take_turn(player, victory_list, game_list, player_score, computer_score):
    print(
        f"""
-----------------------------------------------------------------------
Computer: {computer_score}                        Player: {player_score}

{game_list}
           
        """
    )

    if player == "computer":
        best_move = possibilities.best_move(victory_list)
        if best_move == "first":
            points = game_list.pop(0)
            victory_list.pop(0)
            print(
                f"""
Computer chooses first number and gets {points} points
 
                  """
            )
            return computer_score + points
        else:
            points = game_list.pop()
            victory_list.pop()
            print(
                f"""
Computer chooses last number and gets {points} points
 
                  """
            )
            return computer_score + points
    else:
        print(
            f"""
Your turn! Would you like to take the first number or the last? (f/l)  
            
              """
        )
        while True:
            command = input()
            if command.lower() == "f":
                points = game_list.pop(0)
                victory_list.pop(0)
                print(
                    f"""
Player chooses first number and gets {points} points
 
                  """
                )
                return player_score + points
            elif command.lower() == "l":
                points = game_list.pop()
                victory_list.pop()
                print(
                    f"""
Player chooses last number and gets {points} points
 
                  """
                )
                return player_score + points
            elif command.lower() == "exit":
                quit()
            else:
                print(f"command {command} not recognized.")


def generate_random_game(list_size):
    game_list = []
    for i in range(list_size):
        game_list.append(randint(1, 10))
    return game_list


main()
