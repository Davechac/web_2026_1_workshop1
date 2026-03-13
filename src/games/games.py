import random

class Games:
    def piedra_papel_tijera(self, j1, j2):
        j1, j2 = j1.lower(), j2.lower()
        valid = {"piedra", "papel", "tijera"}
        if j1 not in valid:
            return "invalid"
        if j2 not in valid:
            return "invalid"
        if j1 == j2:
            return "empate"
        wins = {("piedra", "tijera"), ("papel", "piedra"), ("tijera", "papel")}
        return "jugador1" if (j1, j2) in wins else "jugador2"

    def adivinar_numero_pista(self, secreto, intento):
        if intento == secreto:
            return "correcto"
        return "muy alto" if intento > secreto else "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        for player in ["X", "O"]:
            # Rows
            for row in tablero:
                if all(c == player for c in row):
                    return player
            # Columns
            for j in range(3):
                if all(tablero[i][j] == player for i in range(3)):
                    return player
            # Diagonals
            if all(tablero[i][i] == player for i in range(3)):
                return player
            if all(tablero[i][2-i] == player for i in range(3)):
                return player
        # Check for draw or continue
        if any(tablero[i][j] == " " for i in range(3) for j in range(3)):
            return "continua"
        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores):
        return [random.choice(colores) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, fila_ini, col_ini, fila_fin, col_fin, tablero):
        # Out of bounds
        for v in [fila_ini, col_ini, fila_fin, col_fin]:
            if v < 0 or v > 7:
                return False
        # Same position
        if fila_ini == fila_fin and col_ini == col_fin:
            return False
        # Must move in straight line
        if fila_ini != fila_fin and col_ini != col_fin:
            return False
        # Check for obstacles
        if fila_ini == fila_fin:
            step = 1 if col_fin > col_ini else -1
            for c in range(col_ini + step, col_fin, step):
                if tablero[fila_ini][c] != " ":
                    return False
        else:
            step = 1 if fila_fin > fila_ini else -1
            for r in range(fila_ini + step, fila_fin, step):
                if tablero[r][col_ini] != " ":
                    return False
        return True
