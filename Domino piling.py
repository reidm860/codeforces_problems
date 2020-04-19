def main():
    m, n = list(map(int, input().split()))
    domino = int(2)
    board_size = m * n
    board_size = int(board_size)
    if board_size % 2 == 0:
        print(int(board_size / domino))
    else:
        board_size -= 1
        if board_size == 0:
            print(0)
        else:
            print(int(board_size / domino))


main()
