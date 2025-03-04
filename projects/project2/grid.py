

from datastructures.array2d import Array2D
from projects.project2.cell import Cell


class Grid(Array2D):

    def __init__(self, starting_sequence, data_type) -> None:
        """
        Initializes the grid using Array2D
        """
        Array2D.__init__(self, starting_sequence, data_type)
        self.__data_type = data_type


    def check3x3(self, row_index: int, col_index: int) -> list:
        """
        returns a 2D array of a 3x3 area around the inputted indices (not including).
        """
        if (row_index < self.rows_len) and (col_index < self.cols_len):
                area = []
                for i in range(-1, 2):
                    if 0 <= row_index + i < self.rows_len:
                        area.append([])
                        for e in range(-1, 2):
                            if (i != 0) or (e != 0):
                                if 0 <= col_index + e < self.cols_len:
                                    area[-1].append(self[row_index + i][col_index + e])
                return area
        else:
            raise IndexError("Index out of bounds")
    
    def copy(self):
        """
        Creates and returns a deep copy of the Grid
        """
        grid_list = []
        for row in range(len(self)):
            grid_list.append([])
            for col in range(len(self[0])):
                grid_list[-1].append(Cell(self[row][col].isAlive()))
        grid = Grid(grid_list, Cell)
        return grid
    
    
    def __eq__(self, object) -> bool:
        """
        Checks if an object is equal to a Grid.
        Must be a Grid with same dimensions and each item inside must be the same.
        """
        if isinstance(object, Grid):
            if (self.rows_len == object.rows_len) and (self.cols_len == object.cols_len):
                for row in range(len(self)):
                    for col in range(len(self[0])):
                        if self[row][col] != object[row][col]:
                            return False
                return True
            else:
                return False
        else:
            return False