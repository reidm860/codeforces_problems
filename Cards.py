def main():
    n = int(input())
    letters = input()

    z_count = 0
    n_count = 0

    for letter in letters:
        if letter == 'z':
            z_count += 1
        elif letter == 'n':
            n_count += 1
        else:
            pass

    lst = '0' * z_count + '1' * n_count

    output = []

    for item in lst:
        output += item

    output.sort(reverse=True)

    output = ' '.join(output)

    print(output)


main()
