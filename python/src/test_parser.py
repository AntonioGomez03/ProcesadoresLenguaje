import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

# Importa tu lexer y parser generados
from lexer.gec_lexer import (
    gec_lexer as Lexer,
)  # Cambia "MyGrammarLexer" por el nombre real
from parser.gec_parserParser import (
    gec_parserParser as Parser,
)  # Cambia "MyGrammarParser" por el nombre real


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        sys.stderr.write(f"Syntax Error: line {line}:{column} {msg}\n")


def main(input_file):
    try:
        # Leer archivo de entrada con codificación UTF-8
        input_stream = FileStream(input_file, encoding="utf-8")

        # Crear lexer y parser
        lexer = Lexer(input_stream)
        tokens = CommonTokenStream(lexer)

        parser = Parser(tokens)

        # Configurar el listener de errores
        error_listener = SyntaxErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Invocar la regla inicial (ajusta el nombre según tu gramática)
        tree = (
            parser.program()
        )  # Cambia "program" por la regla inicial definida en tu gramática.

        # Verificar errores de sintaxis
        if error_listener.has_error:
            print(f"El archivo '{input_file}' contiene errores de sintaxis.")
        else:
            print(f"El archivo '{input_file}' es sintácticamente correcto.")

    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python test_parser.py <archivo_de_entrada>")
        sys.exit(1)

    main(sys.argv[1])
