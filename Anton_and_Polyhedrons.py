number = int(input())
total = 0
for x in range(number):
    shape = input()
    if shape == 'Icosahedron':
        total += 20
    elif shape == 'Dodecahedron':
        total += 12
    elif shape == 'Octahedron':
        total += 8
    elif shape == 'Cube':
        total += 6
    elif shape == 'Tetrahedron':
        total += 4
print(total)
