# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type = object) -> None: 
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("'starting_sequence' must be a valid sequence type")
        self.__logical_size: int = len(starting_sequence)
        self.__capacity: int = self.__logical_size
        self.__data_type: type = data_type

        self.__elements = np.empty(self.__logical_size, dtype = self.__data_type)
        
        for item in starting_sequence:
            if not isinstance(item, self.__data_type):
                raise TypeError(f"Item {repr(item)} is not of type {str(data_type)}")

        self.__items: NDArray = np.empty(self.__logical_size, dtype = self.__data_type)

        for index in range(self.__logical_size):
            self.__items[index] = starting_sequence[index]

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
            
        if isinstance(index, slice):

            start, stop, step = index.start, index.stop, index.step

            items_to_return = self.__items[index]

            if start is not None and stop is not None:
                if -len(self) <= start < len(self) and -len(self) <= stop <= len(self):
                    return Array(starting_sequence=items_to_return.tolist(), data_type=self.__data_type)
                else:
                    raise IndexError("Index out of bounds")
            else:
                raise TypeError("Slice cannot be None")



        elif isinstance(index, int):

            if -len(self) <= index < len(self):
                return self.__items[index]
            
            else:
                raise IndexError("Index out of bounds")
        
        else:
            raise TypeError(f"{index} not an integer or slice")
            
    
    def __setitem__(self, index: int, item: T) -> None:
        if isinstance(item, self.__data_type):
            if -len(self) <= index < len(self):
                self.__items[index] = item
            else:
                raise IndexError("Index out of bounds")
        else:
            raise TypeError(f"{item} must be of type {self.__data_type}")

    def append(self, data: T) -> None:
        if isinstance(data, self.__data_type):
            self.__grow(self.__logical_size + 1)
            self.__items[self.__logical_size] = data
            self.__logical_size += 1
        else:
            raise TypeError(f"{data} must be of type {self.__data_type}")

    def append_front(self, data: T) -> None:
        if isinstance(data, self.__data_type):
            self.__grow(self.__logical_size + 1)
            for i in range(self.__logical_size, 0, -1):
                self.__items[i] = self.__items[i-1]
            self.__items[0] = data
            self.__logical_size += 1
        else:
            raise TypeError(f"{data} must be of type {self.__data_type}")
    
    def __grow(self, new_size: int) -> None:
        if new_size > self.__capacity:
            while new_size > self.__capacity:
                if self.__capacity == 0:
                    self.__capacity += 1
                else:
                    self.__capacity *= 2
            new_items = np.empty(self.__capacity, dtype=self.__data_type)
            new_items[:self.__logical_size] = self.__items
            self.__items = new_items


    def pop(self) -> None:
        self.__delitem__(self.__logical_size-1)
    
    def pop_front(self) -> None:
        self.__delitem__(0)

    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Array):
            if len(self) == len(other):
                for i in range(len(self)):
                    if self[i] != other[i]:
                        return False
                return True
            else:
                return False
        else:
            return False
    
    def __iter__(self) -> Iterator[T]:
        for item in self.__items:
            yield item

    def __reversed__(self) -> Iterator[T]:
        for item in self.__items[-1:0]:
            yield item
            
    def __delitem__(self, index: int) -> None:
        if isinstance(index, int):
            if -len(self) <= index < len(self):
                new_items = np.empty(self.__logical_size - 1, dtype=self.__data_type)
                new_items[:index] = self.__items[:index]
                new_items[index:self.__logical_size - 1] = self.__items[index + 1:self.__logical_size]
                self.__items = new_items
                self.__logical_size -= 1


                new_size = self.__logical_size
                if new_size <= self.__capacity//4:
                    self.__capacity //= 4
                    new_items = np.empty(self.__capacity, dtype=self.__data_type)
                    new_items[:self.__logical_size] = self.__items
                    self.__items = new_items
            else:
                raise IndexError("Index out of bounds")
        else:
            raise TypeError(f"{index} is not of type 'int'")
        


    def __contains__(self, item: Any) -> bool:
        return any(thing == item for thing in self.__items)

    def clear(self) -> None:
        self.__init__()

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')