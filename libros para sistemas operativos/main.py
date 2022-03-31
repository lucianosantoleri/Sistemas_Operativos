import sys

# Ponemos nuestro código en una función main()
def main() -> object:
    print('Hello there', sys.argv[0])
    # Los argumentos de la líena de comando están en sys.argv[1], sys.argv[2] ...
    # sys.argv[0] es el nombre del propio script como sucede en C

# Código estándar para llamar main() cuando arranca en programa.
if __name__ == '__main__':
    main()
