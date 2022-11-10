// define a grammar called java-python
grammar new_grammar;


/*
  Parser rules
*/

parse : (block)? EOF;

block : (statement NL+)* statement NL*;

statement : operation | print_out;

operation : WS* definition WS* | WS* assignment WS*;

definition : VARNAME WS* ASSIGN WS* expression;
expression : arithmetic | value;

assignment : VARNAME WS* assop WS* value;
assop : DIVASSIGN | MULTASSIGN | ADDASSIGN | SUBASSIGN;

arithmetic : value WS* op WS* value;
op : ADD | SUB | MULT | DIV | MOD;


print_out : PRNT value RPAREN WS*;
value : (VARNAME | INT | FLOAT); 




/*
  Lexer rules
*/

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

VARNAME : ('_'|'A'..'Z'|'a'..'z') ('_'|'A'..'Z'|'0'..'9'|'a'..'z')* ;

WS : ' ';
DIVASSIGN : '/=';
MULTASSIGN : '*=';
ADDASSIGN : '+=';
SUBASSIGN : '-=';
ASSIGN : '=';
NL : '\n';
PRNT : 'print(';
LPAREN : '(';
RPAREN : ')';
ADD : '+';
SUB : '-';
MULT : '*';
DIV : '/';
MOD : '%';



