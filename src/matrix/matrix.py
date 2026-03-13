class Matrix:
    def suma_matrices(self, A, B):
        if len(A) != len(B) or (A and len(A[0]) != len(B[0])):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or (A and len(A[0]) != len(B[0])):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        if not A or not B or len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles")
        rows, cols, inner = len(A), len(B[0]), len(B)
        return [[sum(A[i][k] * B[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]

    def multiplicar_escalar(self, M, escalar):
        return [[M[i][j] * escalar for j in range(len(M[0]))] for i in range(len(M))]

    def transpuesta(self, M):
        if not M:
            return []
        return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]

    def es_cuadrada(self, M):
        if not M:
            return False
        return len(M) == len(M[0])

    def es_simetrica(self, M):
        return M == self.transpuesta(M)

    def traza(self, M):
        if not M or len(M) != len(M[0]):
            raise ValueError("La matriz debe ser cuadrada")
        return sum(M[i][i] for i in range(len(M)))

    def determinante_2x2(self, M):
        if len(M) != 2 or len(M[0]) != 2:
            raise ValueError("La matriz debe ser 2x2")
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]

    def determinante_3x3(self, M):
        if len(M) != 3 or len(M[0]) != 3:
            raise ValueError("La matriz debe ser 3x3")
        a = M[0]
        return (a[0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
               -a[1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
               +a[2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))

    def identidad(self, n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, M):
        if not M or len(M) != len(M[0]):
            raise ValueError("La matriz debe ser cuadrada")
        return [M[i][i] for i in range(len(M))]

    def es_diagonal(self, M):
        n = len(M)
        for i in range(n):
            for j in range(len(M[0])):
                if i != j and M[i][j] != 0:
                    return False
        return True

    def rotar_90(self, M):
        if not M:
            return []
        return [[M[len(M)-1-j][i] for j in range(len(M))] for i in range(len(M[0]))]

    def buscar_en_matriz(self, M, valor):
        result = []
        for i, fila in enumerate(M):
            for j, v in enumerate(fila):
                if v == valor:
                    result.append((i, j))
        return result
