//////////////////////////////////////////////
lexer grammar gec_lexer;

// LEXER RULES // ////////////////////////////////////////////

// Palabras reservadas
DEFINE: 'DEFINE';
SETUP: 'SETUP';
WORLD: 'WORLD';
ADD: 'ADD';
APPEND: 'APPEND';
SCENE: 'SCENE';
FOR: 'FOR';
FROM: 'FROM';
TO: 'TO';
IN: 'IN';

// Tipos de datos
CHUNK: 'CHUNK';
GAMEOBJECT: 'GAMEOBJECT';
LIST: 'LIST';
INT: 'INT';
FLOAT: 'FLOAT';
STRING: 'STRING';

// Simbolos
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LSQUARE: '[';
RSQUARE: ']';
COMMA: ',';
LT: '<';
GT: '>';

// Operadores
ASSIGN: '=';
OP_ARIT: '+' | '-' | '*' | '/';

// Identificadores
ID: [a-zA-Z] [a-zA-Z0-9_]*;

// Literales
INT_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+ '.' [0-9]+;
STRING_LITERAL: '"' ~["]* '"';

// Comentarios
COMMENT: '//' ~[\r\n]* -> skip;

BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip;

// Para generar el lexer: antlr4 -Dlanguage=Python3 antlr4/lexer.gec