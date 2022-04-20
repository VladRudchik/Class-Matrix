from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        MatrixError.matrix1 = matrix1
        MatrixError.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        sumMatrix = []
        if self.size() == other.size():
            for i in range(len(self.matrix)):
                sumMatrixProm = []
                for j in range(len(self.matrix[i])):
                    sumMatrixProm.append(self.matrix[i][j] +
                                         other.matrix[i][j])
                sumMatrix.append(sumMatrixProm)
        else:
            raise MatrixError(self, other)
        return Matrix(sumMatrix)

    def __mul__(self, alfa):
        mulMatrix = []
        if isinstance(alfa, int) or isinstance(alfa, float):
            for i in range(len(self.matrix)):
                mulMatrixProm = []
                for j in range(len(self.matrix[i])):
                    mulMatrixProm.append(self.matrix[i][j] * alfa)
                mulMatrix.append(mulMatrixProm)
        elif len(self.matrix[0]) == len(alfa.matrix):
            for i in range(len(self.matrix)):
                mulMatrixProm = []
                for k in range(len(alfa.matrix[0])):
                    summa = 0
                    for j in range(len(self.matrix[i])):
                        summa += self.matrix[i][j] * alfa.matrix[j][k]
                    mulMatrixProm.append(summa)
                mulMatrix.append(mulMatrixProm)
        else:
            raise MatrixError(self, alfa)
        return Matrix(mulMatrix)

    __rmul__ = __mul__

    def transposed(self):
        tranMatrix = []
        for i in range(len(self.matrix[0])):
            tranMatrix.append([])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                tranMatrix[j].append(self.matrix[i][j])
        return Matrix(tranMatrix)

    def transpose(self):
        tranMatrix = []
        for i in range(len(self.matrix[0])):
            tranMatrix.append([])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                tranMatrix[j].append(self.matrix[i][j])
        self.matrix = tranMatrix
        return self

    def minor(self):
        return self.matrix[0][0] * self.matrix[1][1] - \
               self.matrix[1][0] * self.matrix[0][1]

    def division(self):
        if len(self.matrix[0]) > 2:
            result = 0
            for i in range(len(self.matrix[0])):
                new_arr = []
                for j in range(len(self.matrix[0])):
                    if j != i:
                        for k in range(1, len(self.matrix[0])):
                            new_arr.append(self.matrix[j][k])
                result += Matrix(new_arr).division() *\
                    self.matrix[i][0] * (-1 + 2 * ((i + 1) % 2))
            return result
        else:
            return self.minor()

    def solve(self, array):
        if self.division() == 0 or len(self.matrix) != len(self.matrix[0]):
            raise Exception()
        else:
            div = self.division()
            answer = []
            for i in range(len(array)):
                newMatrix = []
                for j in range(len(array)):
                    newMatrixProm = []
                    for k in range(len(array)):
                        if k != i:
                            newMatrixProm.append(self.matrix[j][k])
                        else:
                            newMatrixProm.append(array[j])
                    newMatrix.append(newMatrixProm)
                answer.append(Matrix(newMatrix).division() / div)
            return answer


class SquareMatrix(Matrix):
    def singleMatrix(self, size):
        single = []
        for i in range(size):
            singleProm = []
            for j in range(size):
                if i != j:
                    singleProm.append(0)
                else:
                    singleProm.append(1)
            single.append(singleProm)
        return Matrix(single)

    def __pow__(self, power):
        if power != 0:
            answer = self
            for i in range(power - 1):
                answer *= self
        else:
            answer = self.singleMatrix(len(self.matrix))
        return answer


exec(stdin.read())
