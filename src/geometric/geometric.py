import math

class Geometria:
    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return base * altura

    def perimetro_rectangulo(self, base, altura):
        return 2 * (base + altura)

    def area_circulo(self, radio):
        if radio < 0:
            return 0
        return math.pi * radio ** 2

    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio

    def area_triangulo(self, base, altura):
        return base * altura / 2

    def perimetro_triangulo(self, a, b, c):
        return a + b + c

    def es_triangulo_valido(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return a + b > c and a + c > b and b + c > a

    def area_trapecio(self, base_mayor, base_menor, altura):
        return (base_mayor + base_menor) * altura / 2

    def area_rombo(self, d1, d2):
        return d1 * d2 / 2

    def area_pentagono_regular(self, lado, apotema):
        return 5 * lado * apotema / 2

    def perimetro_pentagono_regular(self, lado):
        return 5 * lado

    def area_hexagono_regular(self, lado, apotema):
        return 6 * lado * apotema / 2

    def perimetro_hexagono_regular(self, lado):
        return 6 * lado

    def volumen_cubo(self, lado):
        if lado < 0:
            return 0
        return lado ** 3

    def area_superficie_cubo(self, lado):
        return 6 * lado ** 2

    def volumen_esfera(self, radio):
        return (4/3) * math.pi * radio ** 3

    def area_superficie_esfera(self, radio):
        return 4 * math.pi * radio ** 2

    def volumen_cilindro(self, radio, altura):
        return math.pi * radio ** 2 * altura

    def area_superficie_cilindro(self, radio, altura):
        return 2 * math.pi * radio * (radio + altura)

    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            raise ZeroDivisionError("La recta es vertical")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        # Returns (A, B, C) for Ax + By + C = 0
        A = y2 - y1
        B = -(x2 - x1)
        C = (x2 - x1) * y1 - (y2 - y1) * x1
        # Normalize horizontal lines so B = 1
        if A == 0 and B != 0:
            C = int(C / B) if C % B == 0 else C / B
            B = 1
        return (A, B, C)

    def area_poligono_regular(self, n, lado, apotema):
        return n * lado * apotema / 2

    def perimetro_poligono_regular(self, n, lado):
        return n * lado
