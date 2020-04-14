def main():
    feelings = input()
    feelings = int(feelings)
    output = get_feelings(feelings)
    print(output)


def get_feelings(number):
    love = 'I love'
    hate = 'I hate'
    that = 'that'
    ending = 'it'
    lst = []
    for x in range(number):
        if (x + 1) % 2 > 0:
            lst.append(hate)
            lst.append(that)
        else:
            lst.append(love)
            lst.append(that)
    del lst[-1]
    lst.append(ending)
    lst = ' '.join(lst)
    return lst


main()
