def main():
    n = int(input())
    winner = get_winner(n)
    print(winner)


def get_winner(value):
    if value == 1:
        return 'Ehab'
    elif value % 2 == 0:
        return 'Mahmoud'
    else:
        return 'Ehab'


main()
