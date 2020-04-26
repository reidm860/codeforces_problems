def main():
    username = input()
    unique_chars = get_unique(username)
    if unique_chars % 2 != 0:
        print('IGNORE HIM!')
    else:
        print('CHAT WITH HER!')


def get_unique(name):
    lst = []
    for letter in name:
        if letter not in lst:
            lst.append(letter)
    return len(lst)


main()
