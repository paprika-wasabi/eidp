number_field = []
t = int(input())
for i in range(t):
    x, y = input().split(" ")
    x = int(x)
    field = []
    for i in range(x):
        line_in_field = []
        line = input()
        for sym in line:
            line_in_field.append(sym)
        field.append(line_in_field)
    number_field.append(field)

for field in range(len(number_field)):
    for y in range(len(number_field[field])):
        for x in range(len(number_field[field][y])):
            count_mines = 0
            spot = number_field[field]
            if spot[y][x] == '*':
                print(spot[y][x], end='')
            elif spot[y][x] == '.':
                #check up
                if y > 0 and spot[y - 1][x] == '*':
                    count_mines = count_mines + 1
                #check down
                if y < len(number_field[field]) - 1 and spot[y + 1][x] == '*':
                    count_mines = count_mines + 1
                #check left
                if x > 0 and spot[y][x - 1] == '*':
                    count_mines = count_mines + 1
                #check right
                if x < len(number_field[field][y]) - 1 and spot[y][x + 1] == '*':
                    count_mines = count_mines + 1
                #check up right
                if y > 0 and x < len(number_field[field][y]) - 1 and spot[y - 1][x + 1] == '*':
                    count_mines = count_mines + 1
                #check down right
                if y < len(number_field[field]) - 1 and x < len(number_field[field][y]) - 1 and spot[y + 1][x + 1] == '*':
                    count_mines = count_mines + 1
                #check down left
                if y < len(number_field[field]) - 1 and x > 0 and spot[y + 1][x - 1] == '*':
                    count_mines = count_mines + 1
                #check up left
                if y > 0 and x > 0 and spot[y - 1][x - 1] == '*':
                    count_mines = count_mines + 1
                print(count_mines, end='')
        print()
    if field + 1 != len(number_field):
        print()