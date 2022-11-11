// define a new grammar
grammar new_grammar ;

/*
  Parser rules
*/

parse : (block)? EOF ;

block : (statement NL+)* statement NL* ;

statement : operation 
          | print_out 
          ;

operation : WS* definition WS* 
          | WS* assignment WS* 
          ;

definition : VARNAME WS* ASSIGN WS* expression ;

expression : arith 
           | value 
           ;

assignment : VARNAME WS* assop WS* value ;

assop : DIVASSIGN 
      | MULTASSIGN 
      | ADDASSIGN 
      | SUBASSIGN 
      ;

arith : arith WS* MOD WS* arith
      | arith1
      ;

arith1 : arith1 WS* SUB WS* arith1
       | arith1 WS* ADD WS* arith1
       | arith2
       ;

arith2 : arith2 WS* MULT WS* arith2
       | arith2 WS* DIV WS* arith2
       | value
       ;


print_out : PRNT value RPAREN WS* ;

value : VARNAME 
      | INT 
      | FLOAT 
      ; 


/*
  Lexer rules
*/

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

VARNAME : ('_'|'A'..'Z'|'a'..'z') ('_'|'A'..'Z'|'0'..'9'|'a'..'z')* ;

WS : ' ' ;
DIVASSIGN : '/=' ;
MULTASSIGN : '*=' ;
ADDASSIGN : '+=' ;
SUBASSIGN : '-=' ;
ASSIGN : '=' ;
NL : '\n' ;
PRNT : 'print(' ;
LPAREN : '(' ;
RPAREN : ')' ;
ADD : '+' ;
SUB : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;



