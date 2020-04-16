def main():
    n = int(input())
    output = 0
    for x in range(n):
        count = 0
        lst = list(input())
        for number in lst:
            if number == '1':
                count += 1
            else:
                pass
        if count >= 2:
            output += 1
        else:
            pass
    print(output)


main()
