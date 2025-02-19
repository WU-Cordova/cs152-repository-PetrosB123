
from datastructures.array import Array

def main():
    
    print("Hello, World!")
    e = Array([1,2,3])
    print(e._Array__items)
    e.append(4)
    print(e._Array__items)
    e.append(5)
    print(e._Array__items)
    e.append_front(0)
    print(e._Array__items)
    e[0] = 4
    print(e._Array__items)
    e.__delitem__(0)
    print(e._Array__items)
    e.pop()
    print(e._Array__items)
    e.pop_front()
    print(e._Array__items)

    
if __name__ == '__main__':
    main()
