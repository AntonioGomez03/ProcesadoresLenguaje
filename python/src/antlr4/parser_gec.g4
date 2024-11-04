parser grammar parser_gec;

options {
	tokenVocab = lexer_gec;
} // Import lexer

// Rules

program: define_setup define_world EOF;

define_setup:
	DEFINE SETUP LPAREN RPAREN LBRACE setup_statement* RBRACE;

define_world:
	DEFINE WORLD LPAREN expression RPAREN LBRACE define_scene+ RBRACE;

define_scene:
	DEFINE SCENE LPAREN parameters RPAREN LBRACE statement* RBRACE;

parameters: expression (COMMA expression)*;

expression: expression_aux (OP_ARIT expression_aux)*;

expression_aux:
	STRING_LITERAL
	| INT_LITERAL
	| FLOAT_LITERAL
	| ID
	| LPAREN expression RPAREN
	| LSQUARE expression (COMMA expression)* RSQUARE
	| descriptor_constructor;

descriptor_constructor: DESCRIPTOR LPAREN parameters RPAREN;

setup_statement:
	assignment
	| declaration
	| append_statement
	| for_loop_setup;

statement: setup_statement | add_statement | for_loop_world;

assignment:
	data_type ID ASSIGN expression
	| ID ASSIGN expression;

declaration: data_type ID;

data_type: INT | FLOAT | STRING | DESCRIPTOR | list_type;

list_type: LIST LT DESCRIPTOR GT;

append_statement:
	APPEND ID ID
	| APPEND ID descriptor_constructor;

for_loop_setup:
	FOR ID FROM expression TO expression LBRACE setup_statement* RBRACE
	| FOR ID IN ID LBRACE setup_statement* RBRACE;

for_loop_world:
	FOR ID FROM expression TO expression LBRACE statement* RBRACE
	| FOR ID IN ID LBRACE statement* RBRACE;

add_statement: ADD ID;