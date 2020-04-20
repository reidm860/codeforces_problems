def main():
    n = int(input())
    s = input()
    remove = remove_stones(n, s)
    print(remove)


def remove_stones(stones, colors):
    if stones == 1:  # Edge Case
        return 0
    elif stones == 2:  # Edge Cases (continued)
        if colors[0] != colors[1]:
            return 0
        else:
            return 1
    lst = []
    for letter in colors:
        lst.append(letter)
    return search_calculate(lst, stones)


def search_calculate(colors_list, length):  # Cases where the number of colors is 2 or 1 are already covered
    last_color = colors_list[0]
    count = 0
    for color in colors_list[1:length]:
        if color == last_color:
            count += 1
            last_color = color
            colors_list.append(color)
        else:
            last_color = color
            colors_list.append(color)
    return count


main()

'''
Notes
Can be done in O(N) time
strategy:
    put letters representing colors into a list
    iterate through the list checking the letter to the
        right and to the left
    Identity theorised:
        if the letter before the term is the same as the letter after, add 1 to the total.
            subtract one if there are more than 2 letters total
                    # could have a case with 2 letters where they are different (edge case)
        Iterate through list and use try/accept blocks to catch errors
            probably ValueError and/or KeyError
        
'''