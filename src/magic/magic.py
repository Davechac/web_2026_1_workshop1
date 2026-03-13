import math

class Magic:
    def fibonacci(self, n):
        if n < 0:
            return None
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def secuencia_fibonacci(self, n):
        if n == 0:
            return []
        seq = [0]
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
            seq.append(a)
        return seq

    def es_primo(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n

    def triangulo_pascal(self, n):
        triangle = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

    def factorial(self, n):
        if n < 0:
            return None
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digits = str(n)
        power = len(digits)
        return sum(int(d) ** power for d in digits) == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 0:
            return False
        target = sum(matriz[0])
        for row in matriz:
            if sum(row) != target:
                return False
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != target:
                return False
        if sum(matriz[i][i] for i in range(n)) != target:
            return False
        if sum(matriz[i][n-1-i] for i in range(n)) != target:
            return False
        return True
