class Conversion:
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }
    MORSE_REVERSE = {v: k for k, v in MORSE_CODE.items()}

    ROMAN_VALUES = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]

    def celsius_a_fahrenheit(self, c):
        return round(c * 9/5 + 32, 10)

    def fahrenheit_a_celsius(self, f):
        return round((f - 32) * 5/9, 10)

    def metros_a_pies(self, m):
        return m * 3.28084

    def pies_a_metros(self, p):
        return p * 0.3048

    def decimal_a_binario(self, n):
        return bin(n)[2:]

    def binario_a_decimal(self, b):
        return int(b, 2)

    def decimal_a_romano(self, n):
        result = ''
        for valor, simbolo in self.ROMAN_VALUES:
            while n >= valor:
                result += simbolo
                n -= valor
        return result

    def romano_a_decimal(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and roman[c] < roman[s[i+1]]:
                result -= roman[c]
            else:
                result += roman[c]
        return result

    def texto_a_morse(self, texto):
        if not texto:
            return ""
        return ' '.join(self.MORSE_CODE[c] for c in texto.upper() if c in self.MORSE_CODE)

    def morse_a_texto(self, morse):
        if not morse:
            return ""
        tokens = morse.split()
        return ''.join(self.MORSE_REVERSE.get(t, '') for t in tokens if t)
