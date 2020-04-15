n = int(input())
count = 0
for x in range(n-1):
    if n % (x+1) == 0:
        count += 1
    else:
        pass
print(count)