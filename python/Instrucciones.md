# Instrucciones para probar el parser

## 1. Generar el lexer
Nos situamos en la carpeta en la que tengamos los ficheros .g4 del lexer y del parser. A continuación, ejecutamos el siguiente código:
```
antlr4 -Dlanguage=Python3 -o lexer gec_lexer.g4
```

## 2. Generar el parser
Ejecutamos el siguiente comando:
```
antlr4 -Dlanguage=Python3 -o parser gec_lexer.g4
antlr4 -Dlanguage=Python3 -o parser gec_parser.g4
```

## 3. Probar el lexer
En el caso de querer mostrar por consola los tokens detectados en un fichero y conocer su ubicación precisa dentro de este, se puede ejecutar el siguiente comando:
```
python3 python/src/test_lexer.py examples/example1.gec     
```
>[!NOTE]
> Se debe estar situado en la raíz del proyecto.

## 4. Probar un parser
Si se quiere probar si el contenido de un fichero determindado cumple con las reglas sintácticas definidas por nuestro lenguaje, se puede ejecutar el siguiente comando:
```
python3 python/src/test_parser.py examples/example1.gec   
```
>[!NOTE]
> Se debe estar situado en la raíz del proyecto.

>[!NOTE]
> Para ejecutar el script del parser se deberá de tener como mínimo la versión 3.10 de python instalada.


## 5. Probar la semántica
Se debe estar situado en la raíz del proyecto y ejecutar los siguientes comandos:
```
cd python/src 
antlr4 -Dlanguage=Python3 -o parser gec_lexer.g4
antlr4 -Dlanguage=Python3 -o parser gec_parser.g4 -visitor
cd ../..
python3 python/src/test_parser_visitor.py examples/example2_correct.gec
```