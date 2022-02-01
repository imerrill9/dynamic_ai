from possibilities import Possibilities
from game import Game
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

Given a list of 10 20 or 30 numbers, take turns choosing from the first number
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
1. 10 - easy
2. 20 - medium
3. 30 - difficult
           
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
    global game
    game = Game(game_list)

    print(
        f"""
-----------------------------------------------------------------------

{game.display_list()}

Call the coin toss! (h/t)
    """
    )

    while True:
        command = input()
        if command == "h":
            winner = run_coin_toss(0)
            break
        elif command == "t":
            winner = run_coin_toss(1)
            break
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")

    if winner == "player":
        let_player_choose_turn_order()
    else:
        best_turn_order = possibilities.best_turn_order()
        if best_turn_order == "first":
            run_game("computer")
        else:
            run_game("player")


def run_coin_toss(called):
    coin = randint(0, 1)

    if coin == 0:
        print(
            """
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \\
  /`       .-'~"-.       `\\
 ; L      / `-    \      Y ;
;        />  `.  -.|        ;
|       /_     '-.__)       |
|        |-  _.' \ |        |
;        `~~;     \\         ;
 ;         /      \\)       ;
  \        '.___.-'`"     /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
        """
        )
    else:
        print(
            """
        _.-'~~`~~'-._
     .'`  B   E   R  `'.
    / I               T \\
  /`                     `\\
 ; L          _          Y ;
;        ___-(o) ___        ;
|       ////\_|_/\\\\\\        |
;      ///    |    \\\\       ;
 ;     /     '|`     \     ;
  \                       /
   `\                   /`
     '._   1 9 9 7   _.'
        `'-..,,,..-'`
              """
        )

    if called == coin:
        print("Congrats! You win the coin toss.")
        return "player"
    else:
        print(f"Sorry! it's {'heads' if coin == 0 else 'tails'}")
        return "computer"


def let_player_choose_turn_order():
    print(
        f"""
-----------------------------------------------------------------------

{game.display_list()}

Would you like to go first or second? (f/s)
           
        """
    )

    while True:
        command = input()
        if command.lower() == "f":
            run_game("player")
        elif command.lower() == "s":
            run_game("computer")
        elif command.lower() == "exit":
            quit()
        else:
            print(f"command {command} not recognized.")


def run_game(first_player):
    while not game.is_finished():
        if first_player == "computer":
            take_turn("computer")
            take_turn("player")
        else:
            take_turn("player")
            take_turn("computer")

    if game.player_score > game.computer_score:
        print(
            f"""
-----------------------------------------------------------------------
Computer: {game.computer_score}                        Player: {game.player_score}
      
      
      PLAYER WINS!!!!!!!!! GO HUMANS!! WE GOT THE BRAINS!!
          """
        )
    elif game.player_score == game.computer_score:
        print(
            f"""
-----------------------------------------------------------------------
Computer: {game.computer_score}                        Player: {game.player_score}
      
      
      Tie game. Well played GG
          """
        )
    else:
        print(
            f"""
-----------------------------------------------------------------------
Computer: {game.computer_score}                        Player: {game.player_score}
      
      
      Computer wins with {game.computer_score} points!
          """
        )
    quit()


def take_turn(player):
    print(
        f"""
-----------------------------------------------------------------------
Computer: {game.computer_score}                        Player: {game.player_score}

{game.display_list()}
           
        """
    )
    ## to see what the computer is thinking add this to the print above
    ## computer brain:
    ##x: {game.x} y: {game.y} tuple: {possibilities.board[game.x][game.y]}

    if player == "computer":
        best_move = possibilities.best_move(game.x, game.y)
        if best_move == "first":
            points = game.game_list[game.x]
            game.computer_score += points
            game.x += 1
            print(
                f"""
Computer chooses first number and gets {points} points
 
                  """
            )
        else:
            points = game.game_list[game.y]
            game.computer_score += points
            game.y -= 1
            print(
                f"""
Computer chooses last number and gets {points} points
 
                  """
            )
    else:
        print(
            f"""
Your turn! Would you like to take the first number or the last? (f/l)  
            
              """
        )
        while True:
            command = input()
            if command.lower() == "f":
                points = game.game_list[game.x]
                game.player_score += points
                game.x += 1
                print(
                    f"""
Player chooses first number and gets {points} points
 
                  """
                )
                break
            elif command.lower() == "l":
                points = game.game_list[game.y]
                game.player_score += points
                game.y -= 1
                print(
                    f"""
Player chooses last number and gets {points} points
 
                  """
                )
                break
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
