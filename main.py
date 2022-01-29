from possibilities import Possibilities


def main():
    print("main")
    pb = Possibilities([4, 2, 5, 7, 8, 4])
    vict = pb.victory_list(False)
    print(f"victory!!  {vict}")

    print(f'probability of victory for right: {pb.probability_of_victory(vict, "left")}')

    pb.print_board()


main()
