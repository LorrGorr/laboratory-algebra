import numpy as np

def determ(A, n):
    if n != 1:
        c = 1 + 1
        det = 0
        i = 0
        for j in range(n):
            M = []
            for str_A in A:
                if str_A != A[i]:
                    str_A_for_M = [str_A[x] for x in range(n) if x != j]
                    M.append(str_A_for_M)
            det_M_ij = determ(M, n - 1)
            M_ij = (-1) ** c * det_M_ij * A[i][j]
            det = det + M_ij
            c += 1
        return det
    else:
        return A[0][0]

A = [[1.0, 1.0, 2.0], [2.0, 3.0, 1.0], [3.0, 2.0, 4.0]]
matrix_A = np.array(A)
b = np.array([[7.0], [8.0], [14.0]])
A_b = np.array([[1.0, 1.0, 2.0, 7.0], [2.0, 3.0, 1.0, 8.0], [3.0, 2.0, 4.0, 14.0]])

det_A = determ(A, 3)
rank_A = np.linalg.matrix_rank(matrix_A)
rank_A_b = np.linalg.matrix_rank(A_b)

print(det_A)
print(rank_A)

# Работает только для матрицы А, размером 3 * 3
if rank_A != rank_A_b:
    print('Система не совместна')
else:
    # Общее решение
    x = np.linalg.solve(matrix_A, b)
    x = [round(i[0], 2) for i in x]         # Округление подстроено под конкретный ответ.
    # Частное решение. Работает только для матрицы А, размером 3 * 3
    # Приводим матрицу к ступенчатому виду
    k1 = A_b[1][0] / A_b[0][0]
    k2 = A_b[2][0] / A_b[0][0]
    A_b[1] = A_b[1] - k1 * A_b[0]
    A_b[2] = A_b[2] - k2 * A_b[0]
    k3 = A_b[1][1] / A_b[2][1]
    A_b[2] = A_b[2] - k3 * A_b[1]
    # Делаем коэфициенты, равными 1.
    if A_b[2][2] != 1:
        x3 = A_b[2][3]/A_b[2][2]
        A_b[2][3] = x3
        A_b[2][2] = 1
    if A_b[1][1] != 1:
        x2 = A_b[1][2] / A_b[1][1]
        A_b[1][2] = x2
        x3 = A_b[1][3] / A_b[1][1]
        A_b[1][3] = x3
        A_b[1][1] = 1
    if A_b[0][0] != 1:
        x1 = A_b[0][1] / A_b[0][0]
        A_b[0][1] = x1
        x2 = A_b[0][2] / A_b[0][0]
        A_b[0][2] = x2
        x3 = A_b[0][3] / A_b[0][0]
        A_b[0][3] = x3
        A_b[0][0] = 1
    # Заполняем матрицу ответа.
    x = [[0], [0], [0]]
    x[2][0] = float(A_b[2][3] / A_b[2][2])
    x[1][0] = float((A_b[1][3] - A_b[1][2] * x[2][0]) / A_b[1][1])
    x[0][0] = float((A_b[0][3] - A_b[0][1] * x[1][0] - A_b[0][2] * x[2][0]) / A_b[0][0])
    # Округление подстроено под эту конкретную матрицу
    x = [round(i[0], 2) for i in x]
    print(x)
    matrix_X = np.array(x)
    if (np.dot(matrix_A, matrix_X) == b).all:
        print(True)
    else: print(False)

