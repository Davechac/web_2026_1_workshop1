import math
from collections import Counter

class Stats:
    def promedio(self, lista):
        if not lista:
            return 0
        return sum(lista) / len(lista)

    def mediana(self, lista):
        if not lista:
            return 0
        s = sorted(lista)
        n = len(s)
        mid = n // 2
        if n % 2 == 0:
            return (s[mid - 1] + s[mid]) / 2
        return float(s[mid])

    def moda(self, lista):
        if not lista:
            return None
        c = Counter(lista)
        max_freq = max(c.values())
        for item in lista:
            if c[item] == max_freq:
                return item

    def desviacion_estandar(self, lista):
        if len(lista) < 2:
            return 0.0
        avg = self.promedio(lista)
        variance = sum((x - avg) ** 2 for x in lista) / len(lista)
        return math.sqrt(variance)

    def varianza(self, lista):
        if len(lista) < 2:
            return 0.0
        avg = self.promedio(lista)
        return sum((x - avg) ** 2 for x in lista) / len(lista)

    def rango(self, lista):
        if not lista:
            return 0
        return max(lista) - min(lista)
