from __future__ import annotations
import os
from typing import Iterator, List, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def map_index(self, row_index: int, column_index) -> int:
            return row_index * self.num_columns + column_index

        def __getitem__(self, column_index: int) -> T:
            # If row and column are out of bounds raise IndexError
            if column_index < self.num_columns:
                index: int = self.map_index(self.row_index, column_index)

                return self.array[index]
            else:
                raise IndexError("Index out of bounds")
        
        def __setitem__(self, column_index: int, value: T) -> None:
            # If row and column are out of bounds raise IndexError
            if column_index < self.num_columns:
                index: int = self.map_index(self.row_index, column_index)

                self.array[index] = value
            else:
                raise IndexError("Index out of bounds")
        
        def __iter__(self) -> Iterator[T]:
            for item in self.array:
                yield item
        
        def __reversed__(self) -> Iterator[T]:
            for item in self.array[-1:0]:
                yield item

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        self.__data_type = data_type

        # Check that starting_sequence is a sequence
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("starting_sequence must be a Sequence")
        
        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0])
        
        # Check that all the lengths are the same as starting_sequence[0]
        for row in starting_sequence:
            if len(row) != self.rows_len:
                raise ValueError("Lengths of starting_sequence not all the same")

        py_list = []
        for row in range(self.rows_len):
            for col in range(self.cols_len):
                py_list.append(starting_sequence[row][col])

        for item in py_list:
            if not isinstance(item, data_type):
                raise ValueError(f"{item} not of type {data_type}")

        self.__elements2d = Array(starting_sequence=py_list, data_type=data_type)


    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        
        py_list2d: List[List[T]] = []
        for row in range(rows):
            py_list2d.append([])
            for col in range(cols):
                py_list2d[row].append(data_type())

        return Array2D(starting_sequence=py_list2d, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index < self.rows_len:
            return Array2D.Row(row_index, self.__elements2d, self.cols_len, self.__data_type)
        else:
            raise IndexError("Index out of bounds")
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row in range(self.rows_len):
            yield [self[row][col] for col in range(self.cols_len)]
    
    def __reversed__(self):
        for row in range(self.rows_len):
            yield [self[-(row+1)][col] for col in range(self.cols_len)]
    
    def __len__(self): 
        return self.rows_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(self[row])}" for row in range(self.rows_len))}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.rows_len} Rows x {self.cols_len} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')