grammar = {
    'PROGRAM': [
        [],
        [
            ['GLOBAL_DECL', 'PROGRAM'],
            ['NONLOCAL_DECL', 'PROGRAM'],
            ['LITERAL', 'PROGRAM'],
            ['BIN_OP', 'PROGRAM'],
            ['VAR_DEF', 'PROGRAM']
        ],[],[]
    ],
    'GLOBAL_DECL': [
        [],
        [
            ['tk_global', 'tk_id', 'tk_newline']
        ],[],[]
    ],
    'NONLOCAL_DECL': [
        [],
        [
            ['tk_nonlocal', 'tk_id', 'tk_newline']
        ],[],[]
    ],
    'LITERAL': [
        [],
        [
            ['tk_None'],
            ['tk_True'],
            ['tk_False'],
            ['tk_integer'],
            ['tk_idstring'],
            ['tk_string']
        ],[],[]
    ],
    'BIN_OP': [
        [],
        [
            ['tk_suma'],
            ['tk_resta'],
            ['tk_mult'],
            ['tk_div_entera'],
            ['tk_modulo'],
            ['tk_igual'],
            ['tk_diferente'],
            ['tk_menor_igual'],
            ['tk_mayor_igual'],
            ['tk_menor_que'],
            ['tk_mayor_que'],
            ['tk_is']
        ],[],[]
    ],
    'VAR_DEF': [
        [],
        [
            ['TYPED_VAR', 'tk_asignacion', 'LITERAL', 'tk_newline']
        ],[],[]
    ],
    'TYPED_VAR': [
        [],
        [
            ['tk_id', 'tk_dos_puntos', 'TYPE']
        ],[],[]
    ],
    'TYPE': [
        [],
        [
            ['tk_id'],
            ['tk_idstring'],
            ['tk_corchete_izq', 'TYPE', 'tk_corchete_der']
        ],[],[]
    ]
}
'''
    gramatic = {
        'PROGRAM': [
            [[],['STMT','PROGRAM']]
        ],
        'STMT': [
            [['SIMPLE_STMT', 'newline']]
        ],
        'SIMPLE_STMT': [
            [['pass'],['EXPR']]
        ],
        'EXPR':[
            [['CEXPR'],['not', 'EXPR']]
        ],
        'CEXPR':[
            [['ID'],['LITERAL'],['(', 'EXPR', ')'], ['MEMBER_EXPR'], ['-', 'CEXPR']]
        ],
        'BIN-OP':[
            [[''],['not', 'EXPR']]
        ]
    } 

    # REVISAR TK_ EN TODOS LOS TOKENS

    PROGRAM -> L_DEF L_STMT

    L_STMT -> STMT L_STMT
    L_DEF -> VAR_DEF L_DEF
    L_DEF -> FUNC_DEF L_DEF
    L_DEF -> CLASS_DEF L_DEF
    L_STMT -> e
    L_DEF -> e

    CLASS_DEF -> tk_class tk_id tk_par_izq tk_id tk_par_der tk_dos_puntos tk_newline tk_indent CLASS_BODY tk_dedent

    CLASS_BODY -> tk_pass tk_newline
    CLASS_BODY -> L_CLASS_BODY

    L_CLASS_BODY -> VAR_DEF _L_CLASS_BODY
    L_CLASS_BODY -> FUNC_DEF __L_CLASS_BODY

    _L_CLASS_BODY -> L_CLASS_BODY
    _L_CLASS_BODY -> e

    __L_CLASS_BODY -> L_CLASS_BODY
    __L_CLASS_BODY -> e

    FUNC_DEF -> tk_def tk_id tk_par_izq IL_TYPED_VAR tk_par_der tk_dos_puntos tk_newline tk_indent FUNC_BODY tk_dedent

    IL_TYPED_VAR -> TYPED_VAR L_TYPED_VAR
    IL_TYPED_VAR -> e

    L_TYPED_VAR -> tk_coma TYPED_VAR L_TYPED_VAR
    L_TYPED_VAR -> e

    FUNC_BODY -> L_FUNC_BODY L_FUNC_STMT

    L_FUNC_STMT -> STMT _L_FUNC_STMT

    _L_FUNC_STMT -> L_FUNC_STMT
    _L_FUNC_STMT -> e

    L_FUNC_BODY -> VAR_DEF L_FUNC_BODY
    L_FUNC_BODY -> FUNC_DEF L_FUNC_BODY
    L_FUNC_BODY -> GLOBAL_DECL L_FUNC_BODY
    L_FUNC_BODY -> NONLOCAL_DECL L_FUNC_BODY
    L_FUNC_BODY -> e

    TYPED_VAR -> tk_id tk_dos_puntos TYPE

    TYPE -> tk_id
    TYPE -> ID_STRING
    TYPE -> tk_corchete_izq TYPE tk_corchete_der

    GLOBAL_DECL -> tk_global tk_id tk_newline
    NONLOCAL_DECL -> tk_nonlocal tk_id tk_newline

    VAR_DEF -> TYPED_VAR tk_asignacion LITERAL tk_newline

    STMT -> SIMPLE_STMT tk_newline
    STMT -> tk_if EXPR tk_dos_puntos BLOCK L_ELIF ELSE
    STMT -> tk_while EXPR tk_dos_puntos BLOCK
    STMT -> tk_for tk_id tk_in EXPR tk_dos_puntos BLOCK

    L_ELIF -> tk_elif EXPR tk_dos_puntos BLOCK L_ELIF
    L_ELIF -> e

    ELSE -> tk_else tk_dos_puntos BLOCK
    ELSE -> e

    SIMPLE_STMT -> tk_pass
    SIMPLE_STMT -> EXPR
    SIMPLE_STMT -> tk_return OPT_EXPR
    SIMPLE_STMT -> L_TARGET EXPR

    L_TARGET -> TARGET tk_asignacion _L_TARGET

    _L_TARGET -> L_TARGET
    _L_TARGET -> e

    OPT_EXPR -> EXPR
    OPT_EXPR -> e

    BLOCK -> tk_newline tk_indent L_STMT tk_dedent

    LITERAL -> tk_None
    LITERAL -> tk_True
    LITERAL -> tk_False
    LITERAL -> tk_number
    LITERAL -> tk_string

    EXPR -> CEXPR _EXPR
    EXPR -> tk_not EXPR _EXPR

    _EXPR -> tk_and EXPR _EXPR
    _EXPR -> tk_or EXPR _EXPR
    _EXPR -> tk_if EXPR tk_else EXPR _EXPR
    _EXPR -> e

    CEXPR -> IL_EXPR _CEXPR
    CEXPR -> tk_par_izq EXPR tk_par_der _CEXPR
    CEXPR -> MEMBER_EXPR __CEXPR
    CEXPR -> INDEX_EXPR _CEXPR
    CEXPR -> tk_id tk_par_izq IL_EXPR tk_par_der _CEXPR
    CEXPR -> tk_resta CEXPR _CEXPR
    CEXPR -> _CEXPR

    _CEXPR -> BIN_OP CEXPR _CEXPR
    _CEXPR -> tk_id _CEXPR
    _CEXPR -> LITERAL _CEXPR
    _CEXPR -> e

    __CEXPR -> _CEXPR
    __CEXPR -> tk_par_izq IL_EXPR tk_par_der _CEXPR

    IL_EXPR -> EXPR L_EXPR

    L_EXPR -> tk_coma EXPR L_EXPR
    L_EXPR -> e

    MEMBER_EXPR -> CEXPR tk_punto tk_id 

    INDEX_EXPR -> CEXPR tk_corchete_izq EXPR tk_corchete_der

    TARGET -> tk_id
    TARGET -> MEMBER_EXPR
    TARGET -> INDEX_EXPR
    CEXPR -> ID
    CEXPR -> LITERAL
    CEXPR -> IL_EXPR
    IL_EXPR -> EXPR L_EXPR
    L_EXPR -> tk_coma EXPR L_EXPR
    L_EXPR -> e
    CEXPR -> e
    CEXPR -> tk_par_izq EXPR tk_par_der
    CEXPR -> MEMBER_EXPR
    CEXPR -> INDEX_EXPR
    CEXPR -> MEMBER_EXPR tk_par_izq IL_EXPR tk_par_der 
    CEXPR -> ID tk_par_izq IL_EXPR tk_par_der
    CEXPR -> CEXPR BIN_OP CEXPR
    CEXPR -> tk_resta CEXPR
'''