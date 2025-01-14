/* --------------------------Sección código-usuario ------------------------*/
package gec; 
import java_cup.runtime.Symbol;

class Utility {
  
   public static void error(String cadena, int linea, int columna)
       {
         System.out.println("Error: no se ha encontrado fin del comentario, escribe */ al final." + cadena+" en la linea: "+linea+" columna: "+columna);
       }
}

%%
/* -------------------------Sección de opciones y declaraciones ------------------------- */

/* Posibilitar acceso a la columna y fila actual de análisis */ 

%line
%column

/* Compatibilidad con el interfaz CUP para el generador sintáctico */ 

%standalone
%cup 

/* Declarar los estados */ 

%state COMMENT 

/* Inicio de declaraciones */ 
%{

private int c_line; 
private int c_column; 

/* Objeto java_cup.runtime.Symbol con información del token sin valor */ 

    public Symbol symbol(int type) {

   return new Symbol(type, yyline ,yycolumn, yytext());
 }

 public Symbol symbol(int type, Object value){ 
	return new Symbol(type,yyline,yycolumn,value); 
} 
 

%} 

/* Fin de las declaraciones */

/*---------------------------Macros--------------------------------*/
ID = [a-zA-Z][a-zA-Z0-9_]*
INT_LITERAL = [0-9]+
FLOAT_LITERAL = [0-9]+\.[0-9]+
STRING_LITERAL = \"([^\"\n\r])*\" 
OP_ARIT = "+"|"-"|"*"|"/"
START_COMMENT = "/*" 
END_COMMENT = "*/"
WHITE = " " | \n |\r|\r\n | \t

%%
/* ------------------------Seccion de reglas y acciones ----------------------*/
<YYINITIAL> {

DEFINE   {return symbol(sym.DEFINE);}
SETUP   {return symbol(sym.SETUP);}
WORLD   {return symbol(sym.WORLD);}
ADD     {return symbol(sym.ADD);}
APPEND  {return symbol(sym.APPEND);}
SCENE   {return symbol(sym.SCENE);}
FOR     {return symbol(sym.FOR);}
FROM    {return symbol(sym.FROM);}
TO      {return symbol(sym.TO);}
IN      {return symbol(sym.IN);}
CHUNK   {return symbol(sym.CHUNK);}
GAMEOBJECT  {return symbol(sym.GAMEOBJECT);}
LIST    {return symbol(sym.LIST);}
INT     {return symbol(sym.INT);}
FLOAT   {return symbol(sym.FLOAT);}
STRING  {return symbol(sym.STRING);}

{ID} {return symbol(sym.ID);}
{INT_LITERAL} {return symbol(sym.INT_LITERAL, new Integer(yytext()));}
{FLOAT_LITERAL} {return symbol(sym.FLOAT_LITERAL, new Float(yytext()));}
{STRING_LITERAL} {return symbol(sym.STRING_LITERAL, new String(yytext()));}
{OP_ARIT} {return symbol(sym.OP_ARIT);}
{START_COMMENT}  {yybegin(COMMENT);}
\( {return symbol(sym.LPAREN);}
\) {return symbol(sym.RPAREN);} 
\{ {return symbol(sym.LBRACE);} 
\} {return symbol(sym.RBRACE);}  
\[ {return symbol(sym.LSQUARE);}   
\] {return symbol(sym.RSQUARE);}   
, {return symbol(sym.COMMA);}  
\< {return symbol(sym.LT);}  
\> {return symbol(sym.GT);} 
{WHITE} {/* ignora los espacios blancos */}
"//".*      { } 
= {return symbol(sym.ASSIGN);} 
. {System.out.println("Token No Válido < " +yytext()+ " >linea: " + (yyline+1) + " columna: " + (yycolumn+1));}
}/* fin YYinitial */
 
<COMMENT> {
{WHITE}     {/* ignora los espacios en blanco */ }
{END_COMMENT} {yybegin(YYINITIAL);}
<<EOF>>		{/* Error */ Utility.error("",(yyline+1),(yycolumn+1)); /* System.exit(0);*/ return symbol(sym.EOF);}
. {} 
}
/* Fin del comentario */