# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"|{i}:{j}|")
#         print(" ---")

cell = [
    [f'1', f'2', f'3'],
    [f'4', f'5', f'6'],
    [f'7', f'8', f'9'],
]

j = 0
for i in range(len(cell[j])):
    for j in range(len(cell)):
        print(cell[i][j],end = ' ')
    print()
    if i != len(cell) - 1:
        print('-' * 9)
print()

points = {
    '1': [0, 0], '2': [0, 1], '3': [0, 2],
    '4': [1, 0], '5': [1, 1], '6': [1, 2],
    '7': [2, 0], '8': [2, 1], '9': [2, 2],
}


a = '1'
cell[points[a][0]][points[a][1]] = 'x'


j = 0
for i in range(len(cell[j])):
    for j in range(len(cell)):
        print(cell[i][j],end = ' ')
    print()
    if i != len(cell) - 1:
        print('-' * 5)

print()

a = '3'
cell[points[a][0]][points[a][1]] = 'o'


j = 0
for i in range(len(cell[j])):
    for j in range(len(cell)):
        if j == 0:
            print(cell[i][j],end = ' |')
        elif j == 2:
            print(f'| {cell[i][j]}', end='  ')
        else:
            print(f' {cell[i][j]}',end = ' ')
    print()
    if i != len(cell) - 1:
        print('-' * 10)
print()


