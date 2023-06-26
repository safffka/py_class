
matrix = [
    [1, 2, 3],
    [2, 4, 5]
]

def quadruple_matrix(matrix):
    result = [row + row[::-1] for row in matrix]
    return result + result[::-1]


result = quadruple_matrix(matrix)

for row in result:
    print(row)
