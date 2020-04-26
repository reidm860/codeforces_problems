def main():
    number = str(input())
    if check_lucky(number) == 'YES':
        print('YES')
    else:
        if int(number) % 4 == 0 or int(number) % 7 == 0 or int(number) % 47 == 0:
            print('YES')
        else:
            print('NO')


def check_lucky(digits):
    # Check if it is lucky
    for number in digits:
        if number == '4' or number == '7':
            pass
        else:
            return 'NO'
    return 'YES'

    # Check if divisible by a lucky number


main()
