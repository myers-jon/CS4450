// define a grammar called java-python
grammar new_grammar;


/*
  Parser rules
*/

parse : (block)? EOF;

block : (statement NL+)* statement NL*;

statement : operation | print_out;

operation : WS* definition WS* ;  // | WS* arithmetic WS* | assignment WS*;

definition : VARNAME WS* ASSIGN WS* expression;
expression : arithmetic | value;

arithmetic : value WS* op WS* value;
op : PLUS | MINUS | MULT | DIV | MOD;


print_out : PRNT value RPAREN WS*;
value : (VARNAME | INT | FLOAT); 




/*
  Lexer rules
*/

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

VARNAME : ('_'|'A'..'Z'|'a'..'z') ('_'|'A'..'Z'|'0'..'9'|'a'..'z')* ;

WS : ' ';
ASSIGN : '=';
NL : '\n';
PRNT : 'print(';
LPAREN : '(';
RPAREN : ')';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD : '%';



