// define a new grammar
grammar new_grammar ;

/*
  Parser rules
*/

parse : (block)? EOF ;

block : (statement WS*)* statement WS* ;

statement : operation
          | ifelseblock
          | whileblock
          | forblock
          | comment
          | funcdef
          | funccall
          ;

whileblock : WHILE WS* booln WS* COLON (WS* statement)+ ;

forblock : FOR WS* VARNAME WS* IN WS* sequence WS* COLON (WS* statement)+
         | FOR WS* VARNAME WS* IN WS* ('range('INT')'|'range('INT','INT')'|'range('INT','INT','INT')') WS* COLON (WS* statement)+ 
         | FOR WS* VARNAME WS* IN WS* VARNAME WS* COLON (WS* statement)+
         ;

sequence : '[' WS* (INT|FLOAT|VARNAME) WS* ']'
         | '[' WS* (WS* (INT|FLOAT|VARNAME) WS* ',' WS*)* WS* (INT|FLOAT|VARNAME) WS* ']'
         ;

ifelseblock : IF WS* booln COLON (WS* statement)+
            | IF WS* booln COLON (WS* statement)+ WS* ELSE COLON (WS* statement)+
            ;


funcdef : DEF WS* VARNAME WS* '(' WS* (VARNAME WS* (',' WS* VARNAME WS*)*)? ')' WS* COLON (WS* statement | return_stmt)+ ;

funccall : VARNAME WS* '(' WS* (expression WS* (',' WS* expression WS*)*)? ')' ;

return_stmt : RETURN WS* expression ;

operation : assignment WS* ;

assignment : VARNAME WS* assop WS* (expression | booln) ;

booln : booln WS* AND WS* booln
      | booln WS* OR WS* booln
      | NOT WS* booln
      | expression WS* boolop WS* expression
      | booln WS* boolop WS* expression
      | expression WS* boolop WS* booln
      | booln WS* boolop WS* booln
      | BOOL
      | VARNAME
      ;

expression : value
	   | arith
           | funccall
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

value : VARNAME 
      | INT 
      | FLOAT
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

comment : '#' WS* ((INT|FLOAT|VARNAME) WS*)* (WS* statement)*;

/*
  Lexer rules
*/

DEF : 'def' ;
IN : 'in' ;
FOR : 'for' ;
WHILE : 'while' ;
IF : 'if' ;
ELSE : 'else' ;
BOOL : 'True' |  'False' ;
AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
RETURN : 'return' ;

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

VARNAME : ('_'|'A'..'Z'|'a'..'z') ('_'|'A'..'Z'|'0'..'9'|'a'..'z')* ;

COLON : ':' ;

LTE : '<=' ;
GTE : '>=' ;
LT : '<' ;
GT : '>' ;
EQUALS : '==' ;
NTE : '!=' ;

WS : ' ' | '\t' | '\n';
NL : '\n';
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
