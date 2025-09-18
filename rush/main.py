from checkmate import Checkmate

def main():
    board = """\
            ..
            .K
            \
            """
    Checkmate(board)

    board = """\
            ........
            .K......
            P..P....
            ........
            ........
            ........
            ........
            ........
            \
            """
    Checkmate(board)




if __name__ == "__main__":
        main()

