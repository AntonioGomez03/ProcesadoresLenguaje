grammar gec_parser;

options {
	tokenVocab = gec_lexer;
}

program: define_setup define_world EOF;

define_setup:
	DEFINE SETUP LPAREN RPAREN LBRACE statement* RBRACE;

define_world:
	DEFINE WORLD LPAREN (STRING_LITERAL | ID) RPAREN LBRACE define_scene* RBRACE;

define_scene:
	DEFINE SCENE LPAREN (STRING_LITERAL | ID) COMMA (
		INT_LITERAL
		| ID
	) COMMA (INT_LITERAL | ID) RPAREN LBRACE statement* RBRACE;

statement:
	assignment
	| define_list
	| append_statement
	| for_loop_number
	| for_loop_list
	| declaration
	| add_statement;

chunk_constructor:
	CHUNK LPAREN expression COMMA expression COMMA expression COMMA expression COMMA expression
		COMMA ID RPAREN;

gameobject_constructor:
	GAMEOBJECT LPAREN expression COMMA expression COMMA expression COMMA expression RPAREN
	| GAMEOBJECT LPAREN expression COMMA expression COMMA expression RPAREN;

define_list: (LIST LT (CHUNK | GAMEOBJECT) GT) ID ASSIGN array;

array:
	LSQUARE (ID | chunk_constructor | gameobject_constructor) (
		COMMA (ID | chunk_constructor | gameobject_constructor)
	)* RSQUARE
	| LSQUARE RSQUARE;

append_statement:
	APPEND ID (ID | gameobject_constructor | chunk_constructor);

add_statement: ADD ID | ADD chunk_constructor;

for_loop_number:
	FOR ID FROM INT_LITERAL TO INT_LITERAL LBRACE statement* RBRACE;

for_loop_list: FOR ID IN ID LBRACE statement* RBRACE;

assignment: (INT | STRING | FLOAT |) ID ASSIGN expression
	| (CHUNK |) ID ASSIGN chunk_constructor
	| (GAMEOBJECT |) ID ASSIGN gameobject_constructor;

expression: expression_aux (OP_ARIT expression_aux)*;

expression_aux:
	numeric_expression
	| string_expression
	| LPAREN expression RPAREN;

numeric_expression: INT_LITERAL | FLOAT_LITERAL | ID;

string_expression: STRING_LITERAL | ID;

declaration: (
		INT
		| STRING
		| FLOAT
		| CHUNK
		| GAMEOBJECT
		| LIST LT (CHUNK | GAMEOBJECT) GT
	) ID;