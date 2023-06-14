grid = [
    [0,8,0,2,0,0,0,1,0],
    [0,6,0,0,0,3,0,0,0],
    [3,0,1,0,7,0,9,0,0],
    [4,0,2,0,0,8,0,9,0],
    [0,0,0,5,0,0,7,0,0],
    [0,1,0,0,0,0,0,0,0],
    [9,0,3,0,0,4,0,2,0],
    [0,0,0,0,8,0,0,0,4],
    [4,0,0,0,0,0,0,0,0]
]

grid = input()

# print(grid)

def find_empty(cell):
    for i in range(len(cell)):
        for j in range(len(cell[0])):
            if cell[i][j] == 0:
                return (i, j)  # row, col

    return None

def solve(cell):
    find = find_empty(cell)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(cell, i, (row, col)):
            cell[row][col] = i

            if solve(cell):
                return True

            cell[row][col] = 0

    return False


def valid(cell, num, pos):
    # Check row
    for i in range(len(cell[0])):
        if cell[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(cell)):
        if cell[i][pos[1]] == num and pos[0] != i:
            return False

    # Check cells
    cell_x = pos[1] // 3
    cell_y = pos[0] // 3

    for i in range(cell_y*3, cell_y*3 + 3):
        for j in range(cell_x * 3, cell_x*3 + 3):
            if cell[i][j] == num and (i,j) != pos:
                return False

    return True


def print_grid(cell):
    for i in range(len(cell)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(cell[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(cell[i][j])
            else:
                print(str(cell[i][j]) + " ", end="")




print_grid(grid)
solve(grid)
print("___________________")
print_grid(grid)