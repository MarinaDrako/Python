class Matrix:

    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        string = ''
        for i in range(len(self.matrix)):
            string = string + '\t'.join(map(str, self.matrix[i])) + '\n'
        return string

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return self.matrix.__str__()


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[11, 12], [32, 13], [14, 16]])
print(matrix_1)
print(matrix_2)
new_matrix = matrix_1 + matrix_2
print(new_matrix)
