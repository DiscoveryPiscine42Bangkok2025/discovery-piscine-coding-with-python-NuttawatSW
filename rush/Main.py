from Checkmate import Checkmate

def main():
    board = """\
            ..P.
            .KPR
            ...B
            .RQ.
            \
            """
    Checkmate(board)

    board = """\
            ......
            .K....
            P..P..
            ......
            ......
            ......
            \
            """
    Checkmate(board)




if __name__ == "__main__":
    main()

