import sys
from antlr4 import FileStream, CommonTokenStream
from gec_lexer import gec_lexer  # Importa tu lexer generado


def main():
    # Ruta al archivo de entrada pasado como parametro
    input_file = sys.argv[1]

    # Leer el archivo y crear un FileStream
    input_stream = FileStream(input_file, encoding="utf-8")

    # Crear una instancia del lexer
    lexer = gec_lexer(input_stream)

    # Obtener todos los tokens del lexer
    tokens = lexer.getAllTokens()

    # Mostrar los tokens
    for token in tokens:
        print(
            f"Token <{lexer.symbolicNames[token.type]}> encontrado en línea {token.line} columna {token.column}"
        )


if __name__ == "__main__":
    main()
