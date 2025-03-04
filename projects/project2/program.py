

from random import randint
from projects.project2.cell import Cell
from projects.project2.gamecontroller import GameController
from projects.project2.grid import Grid


def main():
    """
    Input or generate row and col values and then creates a Grid out of them with randomly dead or alive cells
    """
    if input("Welcome to the Game of Life! Do you want to randomly seed the game?").strip().lower() not in ['yes', 'y']:
        rows = int(input("How many rows should the simulation have?"))
        cols = int(input("How many columns should the simulation have?"))
    else:
        rows = randint(5, 20)
        cols = randint(5, 20)

    grid_list = []
    for row in range(rows):
        grid_list.append([])
        for col in range(cols):
            grid_list[-1].append(Cell(bool(randint(0,1))))

    
    game = GameController()
    grid = Grid(grid_list, Cell)
    game.run(grid)



if __name__ == '__main__':
    main()
