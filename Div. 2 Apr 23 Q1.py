def main():
    n = int(input())

    for x in range(n):
        n, a, b, c, d, = list(map(int, input().split()))
        print(yes_no(n, a, b, c, d))


def yes_no(n, a, b, c, d):
    mini = (a - b) * n
    maxi = (a + b) * n

    c_min = c - d
    c_max = c + d

    for weight in range(mini, maxi + 1):
        if c_min <= weight <= c_max:
            return 'Yes'

    return 'No'


main()
