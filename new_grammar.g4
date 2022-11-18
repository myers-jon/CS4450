// define a new grammar
grammar new_grammar ;

/*
  Parser rules
*/

parse : (block)? EOF ;

block : (statement NL+)* statement NL* ;

statement : operation ;

operation : assignment WS* ;

assignment : VARNAME WS* assop WS* expression ;

expression : boolean
           | value 
           | arith
           ;

assop : DIVASSIGN 
      | MULTASSIGN 
      | ADDASSIGN 
      | SUBASSIGN 
      | ASSIGN
      ;

boolean : BOOL
        | NOT boolean 
        | BOOL AND boolean
        | BOOL OR boolean
        | expression boolop expression
        ;

boolop : 
       | 
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


value : VARNAME 
      | INT 
      | FLOAT
      ; 


/*
  Lexer rules
*/

BOOL : 'True' |  'False' ;
AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

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
ADD : '+' ;
SUB : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
