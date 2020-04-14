x1, x2, x3, x4 = list(map(int, input().split()))

lst = [x1, x2, x3, x4]

lst.sort()

c = lst[3] - lst[0]
b = lst[3] - lst[1]
a = lst[3] - lst[2]

print(a, b, c)
