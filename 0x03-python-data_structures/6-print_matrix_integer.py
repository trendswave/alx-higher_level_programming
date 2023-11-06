!#/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in range (len(row)):
            end_char = ' ' if cell + 1 != len(row) else ''
            print('{:d}' .format(row[cell]), end=end_char)
        print()
