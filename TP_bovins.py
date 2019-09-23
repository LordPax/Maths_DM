from MatriceXy import *

A = MatZero(7)

A[0][0] = 1
A[0][1] = 1
A[0][2] = 1
A[0][3] = 0
A[0][4] = 0
A[0][5] = 0
A[0][6] = 0

A[1][0] = 1
A[1][1] = 1
A[1][2] = 1
A[1][3] = 1
A[1][4] = 1
A[1][5] = 1
A[1][6] = 1

A[2][0] = -1
A[2][1] = 2
A[2][2] = 0
A[2][3] = 1
A[2][4] = 1
A[2][5] = 1
A[2][6] = 1

A[3][0] = 0
A[3][1] = 1
A[3][2] = 1
A[3][3] = 2
A[3][4] = -1
A[3][5] = 2
A[3][6] = -1

A[4][0] = 1
A[4][1] = 2
A[4][2] = 2
A[4][3] = 2
A[4][4] = 0
A[4][5] = 2
A[4][6] = 0

A[5][0] = 0
A[5][1] = 1
A[5][2] = 1
A[5][3] = 1
A[5][4] = 0
A[5][5] = -1
A[5][6] = 0

A[6][0] = 0
A[6][1] = 1
A[6][2] = 1
A[6][3] = 2
A[6][4] = 0
A[6][5] = 2
A[6][6] = 1

B = MatZero(7, 1)

B[0][0] = -1
B[1][0] = 2
B[2][0] = -4
B[3][0] = 8
B[4][0] = -16
B[5][0] = 32
B[6][0] = -64

X = MatZero(1, 7)
Ainv = MatZero(7)
B2 = MatZero(7, 1)

Ainv = MatInv(A)
X = MatProd(Ainv, B)
B2 = MatProd(A, X)


print("A = \n", MatAff(A))
print("B = \n", MatAff(B))
print("inv(A) = \n", MatAff(Ainv))
print("X = A^1 * B = \n", MatAff(X))
#print("B2 = A * X = \n", MatAff(B2))

pie = 3515820
noire = (pie / 5) / 4
blanc = (noire / 4) / 3
jaune = (blanc / 7) / 6
Pie = (jaune / 6) / 5

pie2 = 3515820
noire2 = FracDiv(FracDiv(pie2, 5), 4)
blanc2 = FracDiv(FracDiv(noire2, 4), 3)
jaune2 = FracDiv(FracDiv(blanc2, 7), 6)
Pie2 = FracDiv(FracDiv(jaune2, 6), 5)

print("pie = ", pie)
print("noire = ", noire)
print("blanc = ", blanc)
print("jaune = ", jaune)
print("Pie2 = ", Pie)

print("\n")

print("pie = ", FracAff(pie2))
print("noire = ", FracAff(noire2))
print("blanc = ", FracAff(blanc2))
print("jaune = ", FracAff(jaune2))
print("Pie2 = ", FracAff(Pie2))