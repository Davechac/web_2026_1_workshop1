import re

class Strings:
    def es_palindromo(self, s):
        s = s.replace(" ", "").lower()
        return s == s[::-1]

    def invertir_cadena(self, s):
        return s[::-1]

    def contar_vocales(self, s):
        return sum(1 for c in s.lower() if c in "aeiou")

    def contar_consonantes(self, s):
        return sum(1 for c in s.lower() if c.isalpha() and c not in "aeiou")

    def es_anagrama(self, a, b):
        a = a.replace(" ", "").lower()
        b = b.replace(" ", "").lower()
        return sorted(a) == sorted(b)

    def contar_palabras(self, s):
        return len(s.split())

    def palabras_mayus(self, s):
        # Capitalize first letter of each word, preserving spaces
        result = []
        capitalize_next = True
        for i, c in enumerate(s):
            if c == ' ':
                result.append(c)
                capitalize_next = True
            elif capitalize_next and c.isalpha():
                result.append(c.upper())
                capitalize_next = False
            else:
                result.append(c)
        return ''.join(result)

    def eliminar_espacios_duplicados(self, s):
        return re.sub(r' {2,}', ' ', s)

    def es_numero_entero(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def cifrar_cesar(self, texto, desplazamiento):
        result = []
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                result.append(chr((ord(c) - base + desplazamiento) % 26 + base))
            else:
                result.append(c)
        return ''.join(result)

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, sub):
        if not sub:
            return []
        indices = []
        start = 0
        while True:
            idx = texto.find(sub, start)
            if idx == -1:
                break
            indices.append(idx)
            start = idx + 1
        return indices
