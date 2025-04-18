
from datastructures.array2d import Array2D
from tests.car import Car
from datastructures.linkedlist import LinkedList

def main():
    
    test = LinkedList(int)
    test.append(2)
    test.append(1)
    test.append(2)
    test.append(2)
    print(test)
    print(test.head)
    test.remove_all(2)
    print(test)
    print(test.head)

if __name__ == '__main__':
    main()
