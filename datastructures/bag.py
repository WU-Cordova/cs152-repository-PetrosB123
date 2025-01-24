from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag: dict[T, int]= {}

        if items is not None:
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
        if item is None:
            raise TypeError("cannot add 'None' to a Bag")
        else:
            if item in self.__bag:
                self.__bag[item] += 1
            else:
                self.__bag[item] = 1

    def remove(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] -= 1
            if self.__bag[item] == 0:
                del self.__bag[item]
        else:
            raise ValueError(f"'{item}' not found in Bag")

    def count(self, item: T) -> int:
        if item in self.__bag:
            return self.__bag[item]
        else:
            return 0

    def __len__(self) -> int:
        count = 0
        for item in self.__bag:
            count += self.__bag[item]
        return count

    def distinct_items(self) -> Iterable[T]:
        list = []
        for item in self.__bag:
            for i in range(self.count(item)):
                list.append(item)
        return list

    def __contains__(self, item) -> bool:
        if item in self.__bag:
            return True
        else:
            return False

    def clear(self) -> None:
        self.__bag: dict[T, int]= {}