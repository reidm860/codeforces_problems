def main():
    t = int(input())

    for _ in range(t):
        n, s = input().split()
        n = int(n)
        s = int(s)
        players_input = list(input())
        defender_attacker = list(input())

        defenders = []
        forwards = []
        defenders_or_attackers = []
        players = []  # make integers

        for player in players_input:
            if player == ' ':
                pass
            else:
                players.append(int(player))

        for player in defender_attacker:
            if player == ' ':
                pass
            else:
                defenders_or_attackers.append(player)

        # split into defenders and forwards
        for x in range(n):
            if defenders_or_attackers[x] == ' ':
                pass
            if defenders_or_attackers[x] == '1':
                forwards.append(players[x])
            elif defenders_or_attackers[x] == '0':
                defenders.append(players[x])

        forwards.sort()
        defenders.sort()

        print(possible(forwards[0], defenders[0], s))


def possible(forw, defe, money):
    if forw + defe + money <= 100:
        return 'yes'
    else:
        return 'no'


main()
