grammar PYMJC;	

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: class_decl+ EOF;
class_decl: CLASS ID (EXTENDS ID)? LP member* RP;

member: attribute_decl 
	| 	method_decl
;

// attribute
attribute_decl: mutable | immutable;
immutable: (STATIC? FINAL | FINAL STATIC?) var_decl SEMI; 
mutable: STATIC? var_decl SEMI; 
var_decl: javatype listID;

// method
method_decl: ID LB params RB block_stmt? // constructor
		|	STATIC? javatype ID LB params RB block_stmt?; // class method
params: (var_decl (SEMI var_decl)*)?;

// statement
for_stmt: FOR ID ASSIGN exp (TO|DOWNTO) exp DO stmt;
assign_stmt: (lhs ASSIGN)+ exp;
if_stmt: IF exp THEN stmt (ELSE stmt)?;
method_invocation: exp DOT ID LB list_exp? RB;
list_exp: exp CM list_exp
		| exp;

block_stmt: LP (stmt | var_decl SEMI)* RP;
stmt: 	block_stmt	
	| 	assign_stmt SEMI
	| 	if_stmt 
	| 	for_stmt
	| 	BREAK SEMI
	| 	CONTINUE SEMI
	| 	RETURN exp SEMI
	| 	method_invocation SEMI
;

//EXPRESSION
exp:	LB exp RB 
	|	<assoc=right> NEW ID LB list_exp? RB
	|	exp DOT ID (LB list_exp? RB)?
	|	exp LQB exp RQR
	|	<assoc=right> (ADD|SUB) exp
	| 	<assoc=right> NOT exp
	| 	exp CONCAT exp
	|	exp (MUL | DIV | DEV_INT | MOD) exp
	|	exp (ADD|SUB) exp
	| 	exp (AND | OR) exp
	| 	exp (EQUAL | NOT_EQUAL) exp
	| 	exp (LT | GT | LTE | GTE) exp
	|	ID
	|	literal
	| 	array_lit
	| 	THIS
;

lhs: ID 
	| exp DOT ID
	| exp LQB exp RQR
	;


// PHASE 1: LEXER ========================================================
BLOCK_COMMENT: ('/*' .*? '*/') -> skip ;
LINE_COMMENT : '#' ~[\r\n]* -> skip ;

// Operator
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
DEV_INT: '\\';
MOD: '%';
NOT_EQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
OR: '||';
AND: '&&';
NOT: '!';	
CONCAT: '^';
ASSIGN: '=';


// Separator
LQB: '[';
RQR: ']';
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SEMI: ';' ;
DOT: '.';
CM: ',';

javatype: (INT | VOID | FLOAT | STRING | BOOLEAN | VOID | ID | array_type);
array_type: javatype (LQB exp RQR);

// Literal
literal: INT_LIT | FLOAT_LIT | STR_LIT | BOOL_LIT | array_lit;

fragment DIGIT: [0-9]+;

INT_LIT: '-'? DIGIT;
FLOAT_LIT: '-'? INT_PART (DOT DEC_PART? EXP_PART? | EXP_PART);
fragment INT_PART: DIGIT;
fragment DEC_PART: DIGIT;
fragment EXP_PART: [eE] [+-]? DIGIT;

BOOL_LIT: TRUE | FALSE;

fragment DoubleQ: '"';
STR_LIT : DoubleQ (~["] | DoubleQ)* DoubleQ ;

// Array
array_lit: LP (literal (CM WS? literal)*)? RP; //{self.text = self.text.replace(" ", "")};


// KEY WORD
BOOLEAN: 'boolean';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
VOID: 'void';
TRUE: 'true';
FALSE: 'false';
NIL: 'nil';

CLASS: 'class';
NEW: 'new';
FINAL: 'final';
STATIC: 'static';
EXTENDS: 'extends';
THIS: 'this';

BREAK: 'break';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
IF: 'if';
THEN: 'then';
FOR: 'for';
TO: 'to';
DOWNTO: 'downto';
RETURN: 'return';

listID: ID (ASSIGN exp)? CM listID
	|	ID (ASSIGN exp)?
;

ID: [a-zA-Z_][a-zA-Z0-9_]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
