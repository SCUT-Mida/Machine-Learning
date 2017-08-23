# -*- coding: utf-8 -*-
from myMatrix import Matrix

a1 = [[4, 0, 3], [4, 6, 7]]
a2 = [[1, 3, 3], [24, 6, 7]]
a3 = [[1, 2], [1, 2], [1, 2]]

m1 = Matrix(a1)
m2 = Matrix(a2)
print(m1)
print(m2)

m3 = Matrix(a3)

m4 = m1 + m2
print(m4)

m5 = m1 * m3
print(m5)
