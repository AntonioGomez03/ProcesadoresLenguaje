import sys
from antlr4 import *
# Importa tu lexer y parser generados
from lexer.gec_lexer import (
    gec_lexer as Lexer,
)  # Cambia "Lexer" por el nombre real
from parser.gec_parserParser import (
    gec_parserParser as Parser,
)  # Cambia "Parser" por el nombre real
from semantic.gec_visitor import GecVisitor


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python prueba_grammar.py <archivo_entrada>")
    else:
        input_stream = FileStream(sys.argv[1], encoding="utf-8")
    lexer = Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Parser(token_stream)
    tree = parser.program()

    visitor = GecVisitor()
    visitor.visit(tree)
