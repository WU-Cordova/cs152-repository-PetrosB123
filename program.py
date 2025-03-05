
from datastructures.array2d import Array2D
from tests.car import Car

def main():
    
    data_type = Car
    rows_len = 5
    cols_len = 5

    sequence2d = [[data_type() for _ in range(cols_len)] for _ in range(rows_len)]
    print(sequence2d)
    return Array2D(starting_sequence=sequence2d, data_type=data_type)

    sequence2d_2 = []
    for row_index in range(rows_len):
        sequence2d_2.append([])
        for col_index in range(cols_len):
            sequence2d_2[row_index].append(data_type())


if __name__ == '__main__':
    main()
