grammar gec;

//////////////////////////////////////////////
// PARSER RULES // ////////////////////////////////////////////

program: define_setup define_world EOF;

define_setup:
	DEFINE SETUP LPAREN RPAREN LBRACE statement* RBRACE;

define_world:
	DEFINE WORLD LPAREN (STRING_LITERAL | ID) RPAREN LBRACE define_scene* RBRACE;

define_scene:
	DEFINE SCENE LPAREN (STRING_LITERAL | ID) COMMA (INT | ID) COMMA (INT | ID) RPAREN LBRACE statement* RBRACE;

statement:
	assignment
	| define list
	| append_statement
	| for_loop_number
	| for_loop_list
	| declaration
	| add_statement;

chunk_constructor: CHUNK LPAREN (ID | INT_LITERAL) COMMA (ID | INT_LITERAL) COMMA (ID | FLOAT_LITERAL) COMMA (ID | FLOAT_LITERAL) COMMA (ID | STRING_LITERAL) COMMA (ID | array) RPAREN;

gameobject_constructor: GAMEOBJECT LPAREN (ID | STRING_LITERAL) COMMA (ID | INT_LITERAL) COMMA (ID | FLOAT_LITERAL) COMMA (ID | FLOAT_LITERAL) RPAREN;
						| GAMEOBJECT LPAREN (ID | STRING_LITERAL) COMMA (ID | INT_LITERAL) COMMA (ID | FLOAT_LITERAL) RPAREN;

define_list: (LIST LT (CHUNK | GAMEOBJECT) GT | ) ID ASSIGN array;

array: LSQUARE (ID | chunk_constructor | gameobject_constructor)* RSQUARE;


append_statement: APPEND ID (ID | gameobject_constructor | chunk_constructor);

add_statement:	ADD ID
				| ADD chunk_constructor;

for_loop_number: FOR ID FROM INT_LITERAL TO INT_LITERAL LBRACE statement* RBRACE;

for_loop_list: FOR ID IN ID LBRACE statement* RBRACE;

assignment:
	(INT | STRING | FLOAT | ) ID ASSIGN expression
	| (CHUNK | ) ID ASSIGN chunk_constructor
	| (GAMEOBJECT | ) ID ASSIGN gameobject_constructor;

expression: expression_aux (OP_ARIT expression_aux)*;

expression_aux:
	STRING_LITERAL
	| INT_LITERAL
	| FLOAT_LITERAL
	| ID
	| LPAREN expression RPAREN;

declaration: (INT | STRING | FLOAT | CHUNK | GAMEOBJECT | LIST LT (CHUNK | GAMEOBJECT) GT) ID;





//////////////////////////////////////////////
// LEXER RULES // ////////////////////////////////////////////

// Palabras reservadas
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

// Tipos de datos
CHUNK: 'CHUNK' {print("CHUNK")};
GAMEOBJECT: 'GAMEOBJECT' {print("GAMEOBJECT")};
LIST: 'LIST' {print("LIST")};
INT: 'INT' {print("INT")};
FLOAT: 'FLOAT' {print("FLOAT")};
STRING: 'STRING' {print("STRING")};

// Simbolos
LPAREN: '(' {print("LPAREN")};
RPAREN: ')' {print("RPAREN")};
LBRACE: '{' {print("LBRACE")};
RBRACE: '}' {print("RBRACE")};
LSQUARE: '[' {print("LSQUARE")};
RSQUARE: ']' {print("RSQUARE")};
COMMA: ',' {print("COMMA")};
LT: '<' {print("LT")};
GT: '>' {print("GT")};

// Operadores
ASSIGN: '=' {print("ASSIGN")};
OP_ARIT: '+' | '-' | '*' | '/' {print("OP_ARIT")};

// Identificadores
ID: [a-zA-Z] [a-zA-Z0-9_]* {print("ID")};

// Literales
INT_LITERAL: [0-9]+ {print("INT_LITERAL")};
FLOAT_LITERAL: [0-9]+ '.' [0-9]+ {print("FLOAT_LITERAL")};
STRING_LITERAL: '"' ~["]* '"' {print("STRING_LITERAL")};

// Comentarios
COMMENT: '//' ~[\r\n]* | '/*' ~('*/')* '*/' -> skip;

// Espacios en blanco
WS: [ \t\r\n]+ -> skip;