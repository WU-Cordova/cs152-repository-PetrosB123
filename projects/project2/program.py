

from random import randint
from projects.project2.cell import Cell
from projects.project2.gamecontroller import GameController
from projects.project2.grid import Grid


def main():
    """
    Input or generate row and col values and then creates a Grid out of them with randomly dead or alive cells
    """
    if input("Do you have a file to import?").strip().lower() not in ['yes', 'y']:
        if input("Welcome to the Game of Life! Do you want to randomly seed the game?").strip().lower() not in ['yes', 'y']:
            rows = int(input("How many rows should the simulation have?"))
            cols = int(input("How many columns should the simulation have?"))
        else:
            rows = randint(5, 20)
            cols = randint(5, 20)
        
        grid_list = []
        percent = int(input("What percent of the cells should be alive?"))
        for row in range(rows):
            grid_list.append([])
            for col in range(cols):
                grid_list[-1].append(Cell(bool(True if randint(0,100) <= percent else False)))


    else:
        file = input("What is the name of the file? (include file extension)")
        with open(fr"projects\project2\{file}", "r") as f:
            while True:
                line = f.readline()
                while line[0] == "#":
                    break
                else:
                    break
            rows = int(line)
            cols = int(f.readline())
            grid_list = []
            for row in range(rows):
                grid_list.append([])
                line = f.readline()
                for col in range(cols):
                    if line[col] == "X":
                        grid_list[-1].append(Cell(True))
                    else:
                        grid_list[-1].append(Cell(False))




    
    game = GameController()
    grid = Grid(grid_list, Cell)
    game.run(grid)



if __name__ == '__main__':
    main()
