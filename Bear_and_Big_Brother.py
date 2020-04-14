def main():
    limak, bob = list(map(int, input().split()))
    output = get_years(limak,bob)
    print(output)

def get_years(bearA, bearB):
    smaller = True
    count = 0
    if bearA == bearB:
        return '1'
    else:
        pass
    while smaller == True:
        bearA *= 3
        bearB *= 2
        count += 1
        if bearA > bearB:
            return count
        else:
            pass






main()