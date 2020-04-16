def main():
    n = int(input())
    for x in range(n):
        word = input()
        print(get_output(word))

def get_output(string):
    if len(string) <= 10:
        return string
    else:
        first_letter = string[0]
        last_letter = str(string[len(string) - 1])
        number = str((len(string) - 2))
        lst = [first_letter, number, last_letter]
        lst = ''.join(lst)
        return lst


main()