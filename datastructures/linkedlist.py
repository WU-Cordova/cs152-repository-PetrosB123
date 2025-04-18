from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list: LinkedList[T] = LinkedList(data_type=data_type)

        for item in sequence:
            if isinstance(item, data_type):
                linked_list.append(item)
            else:
                raise TypeError(f"{item} not of type {data_type}")
            
        return linked_list

    def append(self, item: T) -> None:
        if isinstance(item, self.data_type):
            new_node: LinkedList.Node = LinkedList.Node(data = item)
            if self.empty:
                self.head = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
            self.tail = new_node
            self.count += 1
        else:
            raise TypeError(f"{item} not of type {self.data_type}")

    def prepend(self, item: T) -> None:
        if isinstance(item, self.data_type):
            new_node: LinkedList.Node = LinkedList.Node(data = item)
            if self.empty:
                self.tail = new_node
            else:
                self.head.previous = new_node
                new_node.next = self.head
            self.head = new_node
            self.count += 1
        else:
            raise TypeError(f"{item} not of type {self.data_type}")

    def insert_before(self, target: T, item: T) -> None:
        if isinstance(item, self.data_type):
            if isinstance(target, self.data_type):
                travel = self.head
                while travel is not None:
                    if travel.data == target:
                        break
                    travel = travel.next
                else:
                    raise ValueError(f"The target item {target} is not in the linked list")
                new_node: LinkedList.Node = LinkedList.Node(data = item)
                if self.head == travel:
                    self.head = new_node
                travel.previous.next = new_node
                new_node.next = travel
                new_node.previous = travel.previous
                travel.previous = new_node
                self.count += 1
            else:
                    raise TypeError(f"{target} not of type {self.data_type}")
        else:
            raise TypeError(f"{item} not of type {self.data_type}")

    def insert_after(self, target: T, item: T) -> None:
        if isinstance(item, self.data_type):
            if isinstance(target, self.data_type):
                travel = self.head
                while travel is not None:
                    if travel.data == target:
                        break
                    travel = travel.next
                else:
                    raise ValueError(f"The target item {target} is not in the linked list")
                new_node: LinkedList.Node = LinkedList.Node(data = item)
                if self.head == travel:
                    self.head = new_node
                travel.next.previous = new_node
                new_node.previous = travel
                new_node.next = travel.next
                travel.next = new_node
                self.count += 1
            else:
                raise TypeError(f"{target} not of type {self.data_type}")
        else:
            raise TypeError(f"{item} not of type {self.data_type}")

    def remove(self, item: T) -> None:
        if isinstance(item, self.data_type):
            if self.count == 1:
                    self.clear()
            elif self.head.data == item:
                self.head = self.head.next
                self.head.previous = None
                self.count -= 1
                return None
            elif self.tail.data == item:
                self.tail = self.tail.previous
                self.tail.next = None
                self.count -= 1
                return None
            else:
                travel = self.head.next
                while travel is not self.tail:
                    if travel.data == item:
                        break
                    travel = travel.next
                else:
                    raise ValueError(f"The target item {item} is not in the linked list")
                travel.previous.next = travel.next
                travel.next.previous = travel.previous
                self.count -= 1
        else:
            raise TypeError(f"Cannot remove item that is not of type {self.data_type}")

    def remove_all(self, item: T) -> None:
        if isinstance(item, self.data_type):
            if item in self:
                while item in self:
                    self.remove(item)
            else:
                raise ValueError(f"The target item {item} is not in the linked list")
        else:
            raise TypeError(f"Cannot remove item that is not of type {self.data_type}")
        
        

    def pop(self) -> T:
        if not self.empty:
            item = self.tail.data
            self.remove(self.tail.data)
            return item
        else:
            raise IndexError("Linked list is empty")


    def pop_front(self) -> T:
        if not self.empty:
            item = self.head.data
            self.remove(self.head.data)
            return item
        else:
            raise IndexError("Linked list is empty")

    @property
    def front(self) -> T:
        if not self.empty:
            return self.head.data
        else:
            raise IndexError("The LinkedList is empty")

    @property
    def back(self) -> T:
        if not self.empty:
            return self.tail.data
        else:
            raise IndexError("The LinkedList is empty")

    @property
    def empty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.__init__(self.data_type)

    def __contains__(self, item: T) -> bool:
        for thing in self:
            if item == thing:
                return True
        return False

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        else:
            data = self.travel_node.data
            self.travel_node = self.travel_node.next
            return data

    
    def __reversed__(self) -> T:
        item = self.tail
        while item is not None:
            data = item.data
            item = item.previous
            yield data

    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, LinkedList):
            if self.count == other.count:
                item = self.head
                item2 = other.head
                for i in range(self.count):
                    if item.data != item2.data:
                        return False
                    item = item.next
                    item2 = item2.next
                return True
            else:
                return False
        else:
            return False

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
