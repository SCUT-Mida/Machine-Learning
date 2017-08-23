# -*- coding: utf-8 -*-

import copy
from functools import reduce


class Matrix(object):
    def __init__(self, dyadic_array):
        self.matrix = dyadic_array

    def __str__(self):
        s = ''
        for arr1 in self.matrix:
            length = len(arr1)
            for index2, item in enumerate(arr1):
                if index2 == 0:
                    s += '| \t'
                s += str(item) + '\t'
                if index2 + 1 == length:
                    s += '| \n'
        return s

    def __add__(self, matrix):
        if self.size() != matrix.size():
            print('Size different error')
        clone_matrix = copy.deepcopy(self.matrix)
        for index1, arr1 in enumerate(clone_matrix):
            for index2, item in enumerate(arr1):
                clone_matrix[index1][index2] += matrix.matrix[index1][index2]
        return Matrix(clone_matrix)

    def __mul__(self, matrix):
        m = self.rows()
        n = matrix.cols()
        k = self.cols()
        if k != matrix.rows():
            print('Size error')
        temp_matrix = [([0] * n) for i in range(m)]
        for index1, arr1 in enumerate(temp_matrix):
            row = self.get_row(index1)
            for index2, item in enumerate(arr1):
                col = matrix.get_col(index2)
                temp_matrix[index1][index2] = reduce(
                    lambda x, y=0: x + y, map(lambda i: row[i] * col[i], range(k)))
        return Matrix(temp_matrix)

    def size(self):
        return '%s*%s' % (len(self.matrix), len(self.matrix[0]))

    def rows(self):
        return len(self.matrix)

    def cols(self):
        return len(self.matrix[0])

    def get_row(self, index):
        return self.matrix[index]

    def get_col(self, index):
        return list(map(lambda a: a[index], self.matrix))
