grammar = {
#---ESTO YA SIRVE--------------------------------------------------
#------PRIMERA ITERACION-------------------------------------------

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
            ['tk_number'],
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
            ['tk_int'],
            ['tk_str'],
            ['tk_bool'],
            ['tk_object'],
            ['tk_idstring'],
            ['tk_corchete_izq', 'TYPE', 'tk_corchete_der']
        ],[],[]
    ],
#------------------------------------------------------------------
#-----HASTA AQUI SIRVE---------------------------------------------
#------SEGUNDA ITERACION-------------------------------------------
    'PROGRAM': [
        [],
        [
            ['L_DEF', 'L_STMT']
        ],[],[]
    ],
    'L_DEF': [
        [],
        [
            ['VAR_DEF', 'L_DEF'],
            ['FUNC_DEF', 'L_DEF'],
            ['CLASS_DEF', 'L_DEF'],
            ['e']
        ],[],[]
    ],
    'L_STMT': [
        [],
        [
            ['tk_id', 'L_STMT'],#el id es stmt
            # ['STMT', 'L_STMT'],
            ['e']
        ],[],[]
    ],
    'FUNC_DEF': [
        [],
        [
            ['tk_def', 'tk_id', 'tk_par_izq', 'IL_TYPED_VAR', 'tk_par_der', 'OPT_TYPE','tk_dos_puntos', 'tk_newline', 'tk_indent', 'FUNC_BODY', 'tk_dedent']
        ],[],[]
    ],
    'CLASS_DEF': [
        [],
        [
            ['tk_class', 'tk_id', 'tk_par_izq', 'tk_id', 'tk_par_der', 'tk_dos_puntos', 'tk_newline', 'tk_indent', 'CLASS_BODY', 'tk_dedent']
        ],[],[]
    ],
    'IL_TYPED_VAR': [
        [],
        [
            ['TYPED_VAR', 'L_TYPED_VAR'],
            ['e']
        ],[],[]
    ],
    'OPT_TYPE': [
        [],
        [
            ['tk_ejecuta', 'TYPE'],
            ['e']
        ],[],[]
    ],
    'FUNC_BODY': [
        [],
        [
            ['L_FUNC_BODY', 'L_FUNC_STMT']
        ],[],[]
    ],
    'CLASS_BODY': [
        [],
        [
            ['tk_pass', 'tk_newline'],
            ['L_CLASS_BODY']
        ],[],[]
    ],
    'L_FUNC_BODY': [
        [],
        [
            ['VAR_DEF', 'L_FUNC_BODY'],
            ['FUNC_DEF', 'L_FUNC_BODY'],
            ['GLOBAL_DECL', 'L_FUNC_BODY'],
            ['NONLOCAL_DECL', 'L_FUNC_BODY'],
            ['e']
        ],[],[]
    ],
    'L_FUNC_STMT': [
        [],
        [
            ['L_FUNC_STMT', 'tk_id'],#el id es stmt
            ['tk_id'] #el id es stmt
            # ['L_FUNC_STMT', 'STMT'],
            # ['STMT']
        ],[],[]
    ],
    'L_TYPED_VAR': [
        [],
        [
            ['tk_coma', 'TYPED_VAR', 'L_TYPED_VAR'],
            ['e']
        ],[],[]
    ],
    'L_CLASS_BODY': [
        [],
        [
            ['L_CLASS_BODY', 'VAR_DEF'],
            ['L_CLASS_BODY', 'FUNC_DEF'],
            ['VAR_DEF'],
            ['FUNC_DEF']
        ],[],[]
    ],
#------------------------------------------------------------------
#------TERCERA ITERACION-------------------------------------------

    # 'STMT': [
    #     [],
    #     [
    #         ['SIMPLE_STMT', 'tk_newline'],
    #         ['tk_if', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_ELIF', 'ELSE'],
    #         ['tk_while', 'EXPR', 'tk_dos_puntos', 'BLOCK'],
    #         ['tk_for', 'tk_id', 'tk_in', 'EXPR', 'tk_dos_puntos', 'BLOCK']
    #     ],[],[]
    # ],
    # 'SIMPLE_STMT': [
    #     [],
    #     [
    #         ['tk_pass'],
    #         ['EXPR'],
    #         ['tk_return', 'OPT_EXPR'],
    #         ['L_TARGET', 'EXPR']
    #     ],[],[]
    # ],
    # 'BLOCK': [
    #     [],
    #     [
    #         ['tk_newline', 'tk_indent', 'L_FUNC_STMT', 'tk_dedent']
    #     ],[],[]
    # ],
    # 'L_ELIF': [
    #     [],
    #     [
    #         ['tk_elif', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_ELIF'],
    #         ['e']
    #     ],[],[]
    # ],
    # 'ELSE': [ 
    #     [],
    #     [
    #         ['tk_else', 'tk_dos_puntos', 'BLOCK'],
    #         ['e']
    #     ],[],[]
    # ],
    # 'EXPR': [
    #     [],
    #     [
    #         ['CEXPR'],
    #         ['tk_not', 'EXPR'],
    #         ['EXPR', 'tk_and', 'EXPR'],#
    #         ['EXPR', 'tk_or', 'EXPR'],#
    #         ['EXPR', 'tk_if', 'EXPR', 'tk_else', 'EXPR']#
    #     ],[],[]
    # ],
    # 'OPT_EXPR': [
    #     [],
    #     [
    #         ['EXPR'],
    #         ['e']
    #     ],[],[]
    # ],
    # 'L_TARGET': [
    #     [],
    #     [
    #         ['L_TARGET', 'TARGET', 'tk_asignacion'],
    #         ['TARGET', 'tk_asignacion']
    #     ],[],[]
    # ],
    # 'TARGET': [
    #     [],
    #     [
    #         ['tk_id'],
    #         ['MEMBER_EXPR'],
    #         ['INDEX_EXPR']
    #     ],[],[]
    # ],
#------------------------------------------------------------------
#------CUARTA ITERACION--------------------------------------------
    # 'CEXPR': [
    #     [],
    #     [
    #         ['tk_id'],
    #         ['LITERAL'],
    #         ['tk_corchete_izq', 'IL_EXPR', 'tk_corchete_der'],
    #         ['tk_par_izq', 'EXPR', 'tk_par_der'],
    #         ['MEMBER_EXPR'],
    #         ['INDEX_EXPR'],
    #         ['MEMBER_EXPR', 'tk_par_izq', 'IL_EXPR', 'tk_par_der'],
    #         ['tk_id', 'tk_par_izq', 'IL_EXPR', 'tk_par_der'],
    #         ['CEXPR', 'BIN_OP', 'CEXPR'],
    #         ['tk_resta', 'CEXPR']
    #     ],[],[]
    # ],

    # 'IL_EXPR': [
    #     [], 
    #     [
    #         ['EXPR', 'L_EXPR'],
    #         ['e']
    #     ],[],[] 
    # ],
    # 'MEMBER_EXPR': [
    #     [],
    #     [
    #         ['CEXPR', 'tk_punto', 'tk_id']
    #     ],[],[]
    # ],
    # 'INDEX_EXPR': [
    #     [],
    #     [
    #         ['CEXPR', 'tk_corchete_izq', 'EXPR', 'tk_corchete_der']
    #     ],[],[]
    # ],
    # 'L_EXPR': [
    #     [], 
    #     [
    #         ['tk_coma','EXPR','L_EXPR'],
    #         ['e']
    #     ],[],[] 
    # ],
#------------------------------------------------------------------
}