def main():
    n = input()
    lst = input()
    answer = easy_or_hard(lst)
    print(answer)

def easy_or_hard(lst):
    for item in lst:
        if item == '0':
            pass
        elif item == '1':
            return 'HARD'
    return 'EASY'

main()