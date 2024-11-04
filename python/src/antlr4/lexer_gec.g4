lexer grammar lexer_gec;

// Reserved words
DEFINE: 'DEFINE' {print("DEFINE")};
SETUP: 'SETUP' {print("SETUP")};
WORLD: 'WORLD' {print("WORLD")};
ADD: 'ADD' {print("ADD")};
APPEND: 'APPEND' {print("APPEND")};
SCENE: 'SCENE' {print("SCENE")};
FOR: 'FOR' {print("FOR")};
FROM: 'FROM' {print("FROM")};
TO: 'TO' {print("TO")};
IN: 'IN' {print("IN")};

// Data types
DESCRIPTOR: 'GAMEOBJECT' | 'CHUNK' {print("DESCRIPTOR")};
LIST: 'LIST' {print("LIST")};
INT: 'INT' {print("INT")};
FLOAT: 'FLOAT' {print("FLOAT")};
STRING: 'STRING' {print("STRING")};

// Symbols
LPAREN: '(' {print("LPAREN")};
RPAREN: ')' {print("RPAREN")};
LBRACE: '{' {print("LBRACE")};
RBRACE: '}' {print("RBRACE")};
LSQUARE: '[' {print("LSQUARE")};
RSQUARE: ']' {print("RSQUARE")};
COMMA: ',' {print("COMMA")};
LT: '<' {print("LT")};
GT: '>' {print("GT")};

// Operators
ASSIGN: '=' {print("ASSIGN")};
OP_ARIT: '+' | '-' | '*' | '/' {print("OP_ARIT")};

// Identifiers
ID: [a-zA-Z] [a-zA-Z0-9_]* {print("ID")};

// Literals
INT_LITERAL: [0-9]+ {print("INT_LITERAL")};
FLOAT_LITERAL: [0-9]+ '.' [0-9]+ {print("FLOAT_LITERAL")};
STRING_LITERAL: '"' ~["]* '"' {print("STRING_LITERAL")};

// Comments
COMMENT: '//' ~[\r\n]* -> skip;

// Whitespace, tabs and newlines
WS: [ \t\r\n]+ -> skip;