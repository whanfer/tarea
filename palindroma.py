import sys

# Verificar si se proporcionó una palabra
if len(sys.argv) != 2:
    print("Uso: python palindroma.py <palabra>")
    sys.exit(1)

word = sys.argv[1]  # Toma la palabra desde la terminal

# Verificar si es palíndroma
if word == word[::-1]:  # Compara la palabra con su versión invertida
    print("es palindroma")
else:
    print("no es palindroma")
