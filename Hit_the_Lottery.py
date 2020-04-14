def main():
    n = int(input())
    bills = 0
    while n != 0:
        if n % 100 == 0:
            n -= 100
            bills += 1
        elif n % 20 == 0:
            n -= 20
            bills += 1
        elif n % 10 == 0:
            n -= 10
            bills += 1
        elif n % 5 == 0:
            n -= 5
            bills += 1
        else:
            n -= 1
            bills += 1
    print(bills)


main()
