def main():
    table_card = input()

    table_split = []

    for letter in table_card:
        table_split.append(letter)

    hand_cards = list(input())

    hand_cards = ''.join(hand_cards)

    output = check(hand_cards, table_split)

    print(output)


def check(hand, table):
    for letter in hand:
        if letter in table:
            return 'YES'
        else:
            pass
    return 'NO'


main()
