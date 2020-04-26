def main():
    k, n, w = list(map(int, input().split()))
    money_total = 0
    for i in range(w):
        money = k * (i+1)
        money_total += money

    if money_total < n:
        print(0)
    else:
        print(money_total - n)


main()
