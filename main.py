from compileall import compile_file
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
3. 50
           
        """
    )
    while True:
        command = input()
        if command == "1":
            choose_turn_order(10)
        elif command == "2":
            choose_turn_order(20)
        elif command == "3":
            choose_turn_order(50)
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def choose_turn_order(list_size):
    global game_list
    global possibilities
    global player_score
    global computer_score

    game_list = generate_random_game(list_size)
    possibilities = Possibilities(game_list)
    best_move = possibilities.best_turn_order()
    player_score = 0
    computer_score = 0

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
            take_turn("computer")
        elif command.lower() == "n":
            let_player_choose_turn_order()
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def let_player_choose_turn_order():
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
            take_turn("player")
        elif command.lower() == "s":
            take_turn("computer")
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def take_turn(player):
    print(
        f"""
-----------------------------------------------------------------------
Computer: {computer_score}                        Player: {player_score}

{game_list}
           
        """
    )
    if player == "computer":
        take_turn("computer")
    else:
        take_turn("player")


def generate_random_game(list_size):
    game_list = []
    for i in range(list_size):
        game_list.append(randint(1, 10))
    return game_list


main()
