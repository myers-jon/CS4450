// define a grammar called java-python
grammar new_grammar;


parse : block EOF;

block : statement*;

statement : definition WS* ;  // | arithmetic WS* | assignment WS*;

definition : VAR WS* '=' WS* NUMBER;

WS : '\n' | ' ';

NUMBER : INT | FLOAT;

INT : [0-9]+ ;

FLOAT : [0-9]+ '.' [0-9]* ;

VAR : [a-z]+ ;




