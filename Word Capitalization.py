def main():
    word = input()
    capital = word[0]
    max = len(word)
    lst = [capital.upper()]
    for letter in word[1:max]:
        lst.append(letter)
    lst = ''.join(lst)
    print(lst)


main()
