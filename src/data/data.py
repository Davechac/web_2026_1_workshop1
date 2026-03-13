class Data:
    def invertir_lista(self, lista):
        return lista[::-1]

    def buscar_elemento(self, lista, elemento):
        try:
            return lista.index(elemento)
        except ValueError:
            return -1

    def eliminar_duplicados(self, lista):
        seen = []
        result = []
        for item in lista:
            if not any(x == item and type(x) == type(item) for x in seen):
                seen.append(item)
                result.append(item)
        return result

    def merge_ordenado(self, a, b):
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i]); i += 1
            else:
                result.append(b[j]); j += 1
        return result + a[i:] + b[j:]

    def rotar_lista(self, lista, k):
        if not lista:
            return []
        k = k % len(lista)
        return lista[-k:] + lista[:-k] if k else lista[:]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        return n * (n + 1) // 2 - sum(lista)

    def es_subconjunto(self, a, b):
        return all(x in b for x in a)

    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop(),
            "peek": lambda: pila[-1],
            "is_empty": lambda: len(pila) == 0,
        }

    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0),
            "peek": lambda: cola[0],
            "is_empty": lambda: len(cola) == 0,
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]
