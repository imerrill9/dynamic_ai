from possibilities import Possibilities


def main():
    print("main")
    pb = Possibilities([4, 2, 5, 7, 8, 4])
    vict = pb.victory_list(False)
    print(f"victory!!  {vict}")
    pb.print_board()


main()
