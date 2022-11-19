// define a new grammar
grammar new_grammar ;

/*
  Parser rules
*/

parse : (block)? EOF ;

block : (statement WS+)* statement WS* ;

statement : ifelseblock
          | operation
          ;

ifelseblock : IF WS* conditional ':' WS* statement
            | IF WS* conditional ':' WS* statement WS* ELSE ':' WS* statement
            ;

operation : WS* ifelseblock WS*
          | WS* assignment WS* 
          ;

assignment : VARNAME WS* boolop WS* expression
           | VARNAME WS* assop WS* expression 
           ;



conditional :VARNAME WS* booln WS* conditional*
            |VARNAME WS* boolop WS* BOOL WS* conditional*
            |VARNAME WS* boolop WS* value WS* conditional*
            ;

expression : booln
           | arith
           | value 
           ;
    

boolop : LTE
       | GTE
       | LT
       | GT
       | EQUALS
       | NTE
       ;       

assop : DIVASSIGN 
      | MULTASSIGN 
      | ADDASSIGN 
      | SUBASSIGN 
      | ASSIGN
      ;

booln : BOOL WS* AND WS* conditional
	| BOOL WS* OR WS* conditional
	| NOT WS* ( BOOL | value ) WS* conditional*
	| BOOL
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
IF : 'if' ;
ELSE : 'else' ;
BOOL : 'True' |  'False' ;
AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

VARNAME : ('_'|'A'..'Z'|'a'..'z') ('_'|'A'..'Z'|'0'..'9'|'a'..'z')* ;

LTE : '<=' ;
GTE : '>=' ;
LT : '<' ;
GT : '>' ;
EQUALS : '==' ;
NTE : '!=' ;

WS : ' ' | '\t' | '\n' ;
DIVASSIGN : '/=' ;
MULTASSIGN : '*=' ;
ADDASSIGN : '+=' ;
SUBASSIGN : '-=' ;
ASSIGN : '=' ;
ADD : '+' ;
SUB : '-' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
