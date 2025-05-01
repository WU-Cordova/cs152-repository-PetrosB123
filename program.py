
from datastructures.array2d import Array2D
from datastructures.hashmap import HashMap
from tests.car import Car
from datastructures.linkedlist import LinkedList

def main():
    
    test = HashMap(number_of_buckets=3, load_factor=0.1)
    for number in range(50):
        test[number] = f"{number}"
        print(test._bucket_count)

if __name__ == '__main__':
    main()
