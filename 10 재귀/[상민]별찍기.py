def emptyCenter(n, start_point):
    x, y = start_point
    for i in range(x, x + n//3):
        for j in range(y, y + n//3):
            grid[i][j] = ' '

def unmarkStars(n, start_point):
    x, y = start_point
    if n == 3:
        grid[x+1][y+1] = ' '

    else:
        for i in range(0, n, n//3):
            for j in range(0, n, n//3):
                start_point = (x + i, y + j)
                if i == n//3 and j == n//3:
                    emptyCenter(n, start_point)
                else:
                    unmarkStars(n//3, start_point)

def printGrid(grid):
    for i in range(len(grid)):
        print(''.join(grid[i]))

n = int(input())
grid = [['*' for _ in range(n)] for _ in range(n)]
unmarkStars(n, (0,0))
printGrid(grid)
