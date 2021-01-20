# Python code to implement Conway's Game Of Life
# setting up the values for the grid
import random

ON = 255
OFF = 0
vals = [ON, OFF]


def randomGrid(N, M):
    grid = {}
    for i in range(N):
        for j in range(M):
            grid[i, j] = random.choices(vals)[0]
    return grid


def update(grid, N, M):
    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = grid.copy()
    for i in range(N):
        for j in range(M):

            # compute 8-neghbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulaton takes place on a toroidal surface.
            total = int((grid[i, (j - 1) % N] + grid[i, (j + 1) % M] +
                         grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                         grid[(i - 1) % N, (j - 1) % M] + grid[(i - 1) % N, (j + 1) % M] +
                         grid[(i + 1) % N, (j - 1) % M] + grid[(i + 1) % N, (j + 1) % M]) / 255)

            # apply Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    return newGrid


# main() function
def main():
    # set grid size
    N = 64
    M = 128

    # check if "glider" demo flag is specified
    #   addGlider(1, 1, grid)
    #  addGosperGliderGun(10, 10, grid)
    grid = randomGrid(N, M)
    update(grid, N, M, )


# call main
if __name__ == '__main__':
    main()
