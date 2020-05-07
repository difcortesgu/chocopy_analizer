program --> [var_def | func_def | class_def ]∗ stmt∗

class_def --> class ID ( ID ) : NEWLINE INDENT class_body DEDENT

class_body --> pass NEWLINE | [var_def | func_def ]+

func_def --> def ID ( [typed_var [, typed_var]∗]? ) [-> type]? : NEWLINE INDENT func_body DEDENT

func_body --> [global_decl | nonlocal_decl | var_def | func_def ]∗ stmt+

typed_var --> ID : type

type --> ID
type --> IDSTRING
type --> [ type ]

global_decl --> global ID NEWLINE

nonlocal_decl --> nonlocal ID NEWLINE

var_def --> typed_var = literal NEWLINE

stmt --> simple_stmt NEWLINE
stmt --> if expr : block [elif expr : block ]∗ [else : block]?
stmt --> while expr : block
stmt --> for ID in expr : block

simple_stmt --> pass
simple_stmt --> expr
simple_stmt --> return [expr]?
simple_stmt --> [ target = ]+ expr

block --> NEWLINE INDENT stmt+ DEDENT

literal --> None
literal --> True
literal --> False
literal --> INTEGER
literal --> IDSTRING
literal --> STRING

expr --> cexpr
expr --> not expr
expr --> expr [and | or] expr
expr --> expr if expr else expr

cexpr --> ID
cexpr --> literal
cexpr --> [ [expr [, expr]∗]?]
cexpr --> ( expr )
cexpr --> member_expr
cexpr --> index_expr
cexpr --> member_expr ( [expr [, expr]∗]? )
cexpr --> ID ( [expr [, expr]∗]? )
cexpr --> cexpr bin_op cexpr
cexpr --> - cexpr

bin_op --> +
bin_op --> -
bin_op --> *
bin_op --> //
bin_op --> %
bin_op --> ==
bin_op --> !=
bin_op --> <=
bin_op --> >=
bin_op --> <
bin_op --> >
bin_op --> is

member_expr --> cexpr . ID

index_expr --> cexpr [ expr ]

target --> ID
target --> member_expr
target --> index_expr