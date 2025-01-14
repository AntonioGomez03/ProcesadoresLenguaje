grammar gec_parser;

options {
	tokenVocab = gec_lexer;
}

program: define_setup define_world EOF;

define_setup:
	DEFINE SETUP LPAREN RPAREN LBRACE statement* RBRACE;

define_world:
	DEFINE WORLD LPAREN string_expression RPAREN LBRACE define_scene* RBRACE;

define_scene:
	DEFINE SCENE LPAREN string_expression COMMA numeric_expression COMMA numeric_expression RPAREN
		LBRACE statement* RBRACE;

statement:
	assignment
	| define_list
	| append_statement
	| for_loop_number
	| for_loop_list
	| declaration
	| add_statement;

chunk_constructor:
	CHUNK LPAREN numeric_expression* COMMA numeric_expression COMMA numeric_expression COMMA
		numeric_expression COMMA string_expression COMMA ID RPAREN;

gameobject_constructor:
	GAMEOBJECT LPAREN string_expression COMMA numeric_expression COMMA numeric_expression COMMA
		numeric_expression RPAREN
	| GAMEOBJECT LPAREN string_expression COMMA numeric_expression COMMA numeric_expression RPAREN;

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

assignment: (INT | FLOAT |) ID ASSIGN numeric_expression
	| (STRING |) ID ASSIGN string_expression
	| (CHUNK |) ID ASSIGN chunk_constructor
	| (GAMEOBJECT |) ID ASSIGN gameobject_constructor;

numeric_expression:
	numeric_expression_aux (OP_ARIT numeric_expression_aux)*;

numeric_expression_aux:
	INT_LITERAL
	| FLOAT_LITERAL
	| ID
	| LPAREN numeric_expression RPAREN;

string_expression:
	string_expression_aux (OP_ARIT string_expression_aux)*;

string_expression_aux:
	STRING_LITERAL
	| ID
	| LPAREN string_expression RPAREN;

declaration: (
		INT
		| STRING
		| FLOAT
		| CHUNK
		| GAMEOBJECT
		| LIST LT (CHUNK | GAMEOBJECT) GT
	) ID;