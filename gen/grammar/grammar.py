grammar = {
  'PROGRAM': [
    [],
    [
      ['L_DEF', 'L_STMT']
    ],
    [],
    []
  ],
  'L_DEF': [
    [],
    [
      ['VAR_DEF', 'L_DEF'],
      ['FUNC_DEF', 'L_DEF'],
      ['CLASS_DEF', 'L_DEF'],
      ['e']
    ],
    [],
    []
  ],
  'L_STMT': [
    [],
    [
      ['STMT', 'L_STMT'],
      ['e']
    ],
    [],
    []
  ],
  'VAR_DEF': [
    [],
    [
      ['TYPED_VAR', 'tk_asignacion', 'LITERAL', 'tk_newline']
    ],
    [],
    []
  ],
  'FUNC_DEF': [
    [],
    [
      ['tk_def', 'tk_id', 'tk_par_izq', 'IL_TYPED_VAR', 'tk_par_der', 'OPT_TYPE', 'tk_dos_puntos', 'tk_newline', 'tk_indent', 'FUNC_BODY', 'tk_dedent']
    ],
    [],
    []
  ],
  'CLASS_DEF': [
    [],
    [
      ['tk_class', 'tk_id', 'tk_par_izq', 'tk_id', 'tk_par_der', 'tk_dos_puntos', 'tk_newline', 'tk_indent', 'CLASS_BODY', 'tk_dedent']
    ],
    [],
    []
  ],
  'STMT': [
    [],
    [
      ['SIMPLE_STMT', 'tk_newline'],
      ['tk_if', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_ELIF', 'ELSE'],
      ['tk_while', 'EXPR', 'tk_dos_puntos', 'BLOCK'],
      ['tk_for', 'tk_id', 'tk_in', 'EXPR', 'tk_dos_puntos', 'BLOCK']
    ],
    [],
    []
  ],
  'TYPED_VAR': [
    [],
    [
      ['tk_id', 'tk_dos_puntos', 'TYPE']
    ],
    [],
    []
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
    ],
    [],
    []
  ],
  'IL_TYPED_VAR': [
    [],
    [
      ['e'],
      ['tk_id', 'tk_dos_puntos', 'TYPE', 'L_TYPED_VAR']
    ],
    [],
    []
  ],
  'OPT_TYPE': [
    [],
    [
      ['tk_ejecuta', 'TYPE'],
      ['e']
    ],
    [],
    []
  ],
  'FUNC_BODY': [
    [],
    [
      ['L_FUNC_BODY', 'L_FUNC_STMT']
    ],
    [],
    []
  ],
  'CLASS_BODY': [
    [],
    [
      ['tk_pass', 'tk_newline'],
      ['L_CLASS_BODY']
    ],
    [],
    []
  ],
  'SIMPLE_STMT': [
    [],
    [
      ['tk_pass'],
      ['EXPR'],
      ['tk_return', 'OPT_EXPR'],
      ['L_TARGET', 'EXPR']
    ],
    [],
    []
  ],
  'EXPR': [
    [],
    [
      ['CEXPR', 'EXPR_'],
      ['tk_not', 'EXPR', 'EXPR_']
    ],
    [],
    []
  ],
  'BLOCK': [
    [],
    [
      ['tk_newline', 'tk_indent', 'L_FUNC_STMT', 'tk_dedent']
    ],
    [],
    []
  ],
  'L_ELIF': [
    [],
    [
      ['tk_elif', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_ELIF'],
      ['e']
    ],
    [],
    []
  ],
  'ELSE': [
    [],
    [
      ['tk_else', 'tk_dos_puntos', 'BLOCK'],
      ['e']
    ],
    [],
    []
  ],
  'TYPE': [
    [],
    [
      ['tk_id'],
      ['tk_idstring'],
      ['tk_corchete_izq', 'TYPE', 'tk_corchete_der']
    ],
    [],
    []
  ],
  'L_TYPED_VAR': [
    [],
    [
      ['tk_coma', 'TYPED_VAR', 'L_TYPED_VAR'],
      ['e']
    ],
    [],
    []
  ],
  'L_FUNC_BODY': [
    [],
    [
      ['GLOBAL_DECL', 'L_FUNC_BODY'],
      ['NONLOCAL_DECL', 'L_FUNC_BODY'],
      ['e'],
      ['tk_id', 'tk_dos_puntos', 'TYPE', 'tk_asignacion', 'LITERAL', 'tk_newline', 'L_FUNC_BODY'],
      ['tk_def', 'tk_id', 'tk_par_izq', 'IL_TYPED_VAR', 'tk_par_der', 'OPT_TYPE', 'tk_dos_puntos', 'tk_newline', 'tk_indent', 'FUNC_BODY', 'tk_dedent', 'L_FUNC_BODY']
    ],
    [],
    []
  ],
  'L_FUNC_STMT': [
    [],
    [
      ['tk_if', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_ELIF', 'ELSE', 'L_FUNC_STMT_'],
      ['tk_while', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_FUNC_STMT_'],
      ['tk_for', 'tk_id', 'tk_in', 'EXPR', 'tk_dos_puntos', 'BLOCK', 'L_FUNC_STMT_'],
      ['tk_pass', 'tk_newline', 'L_FUNC_STMT_'],
      ['tk_return', 'OPT_EXPR', 'tk_newline', 'L_FUNC_STMT_'],
      ['L_TARGET', 'EXPR', 'tk_newline', 'L_FUNC_STMT_'],
      ['CEXPR', 'EXPR_', 'tk_newline', 'L_FUNC_STMT_'],
      ['tk_not', 'EXPR', 'EXPR_', 'tk_newline', 'L_FUNC_STMT_']
    ],
    [],
    []
  ],
  'L_CLASS_BODY': [
    [],
    [
      ['tk_id', 'tk_dos_puntos', 'TYPE', 'tk_asignacion', 'LITERAL', 'tk_newline', 'L_CLASS_BODY_'],
      ['tk_def', 'tk_id', 'tk_par_izq', 'IL_TYPED_VAR', 'tk_par_der', 'OPT_TYPE', 'tk_dos_puntos', 'tk_newline', 'tk_indent', 'FUNC_BODY', 'tk_dedent', 'L_CLASS_BODY_']
    ],
    [],
    []
  ],
  'OPT_EXPR': [
    [],
    [
      ['e'],
      ['CEXPR', 'EXPR_'],
      ['tk_not', 'EXPR', 'EXPR_']
    ],
    [],
    []
  ],
  'L_TARGET': [
    [],
    [
      ['TARGET', 'tk_asignacion', 'L_TARGET_']
    ],
    [],
    []
  ],
  'CEXPR': [
    [],
    [
      ['tk_corchete_izq', 'IL_EXPR', 'tk_corchete_der', 'CEXPR_'],
      ['tk_par_izq', 'EXPR', 'tk_par_der', 'CEXPR_'],
      ['INDEX_EXPR', 'CEXPR_'],
      ['tk_resta', 'CEXPR', 'CEXPR_'],
      ['tk_None', 'CEXPR_'],
      ['tk_True', 'CEXPR_'],
      ['tk_False', 'CEXPR_'],
      ['tk_number', 'CEXPR_'],
      ['tk_idstring', 'CEXPR_'],
      ['tk_string', 'CEXPR_'],
      ['tk_id', 'CEXPRA'],
      ['MEMBER_EXPR', 'CEXPRA']
    ],
    [],
    []
  ],
  'GLOBAL_DECL': [
    [],
    [
      ['tk_global', 'tk_id', 'tk_newline']
    ],
    [],
    []
  ],
  'NONLOCAL_DECL': [
    [],
    [
      ['tk_nonlocal', 'tk_id', 'tk_newline']
    ],
    [],
    []
  ],
  'TARGET': [
    [],
    [
      ['tk_id'],
      ['MEMBER_EXPR'],
      ['INDEX_EXPR']
    ],
    [],
    []
  ],
  'IL_EXPR': [
    [],
    [
      ['e'],
      ['tk_not', 'EXPR', 'EXPR_', 'L_EXPR'],
      ['tk_corchete_izq', 'IL_EXPR', 'tk_corchete_der', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_par_izq', 'EXPR', 'tk_par_der', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['INDEX_EXPR', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_resta', 'CEXPR', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_None', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_True', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_False', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_number', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_idstring', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_string', 'CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_id', 'IL_EXPRA'],
      ['MEMBER_EXPR', 'IL_EXPRA']
    ],
    [],
    []
  ],
  'MEMBER_EXPR': [
    [],
    [
      ['tk_corchete_izq', 'IL_EXPR', 'tk_corchete_der', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_par_izq', 'EXPR', 'tk_par_der', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['INDEX_EXPR', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_resta', 'CEXPR', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_None', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_True', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_False', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_number', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_idstring', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_string', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_id', 'MEMBER_EXPRA']
    ],
    [],
    []
  ],
  'INDEX_EXPR': [
      [],
      [
          ['tk_id', 'INDEX_EXPR_1'],
          ['tk_corchete_izq', 'INDEX_EXPR_2'],
          ['tk_par_izq', 'INDEX_EXPR_3'],
          ['tk_resta', 'INDEX_EXPR_4'],
          ['tk_None', 'INDEX_EXPR_5'],
          ['tk_True', 'INDEX_EXPR_5'],
          ['tk_False', 'INDEX_EXPR_5'],
          ['tk_number', 'INDEX_EXPR_5'],
          ['tk_string', 'INDEX_EXPR_5'],
          ['tk_idstring', 'INDEX_EXPR_5']
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
    ],
    [],
    []
  ],
  'L_EXPR': [
    [],
    [
      ['tk_coma', 'EXPR', 'L_EXPR'],
      ['e']
    ],
    [],
    []
  ],
  'EXPR_': [
    [],
    [
      ['tk_and', 'EXPR', 'EXPR_'],
      ['tk_or', 'EXPR', 'EXPR_'],
      ['tk_if', 'EXPR', 'tk_else', 'EXPR', 'EXPR_'],
      ['e']
    ],
    [],
    []
  ],
  'L_FUNC_STMT_': [
    [],
    [
      ['STMT', 'L_FUNC_STMT_'],
      ['e']
    ],
    [],
    []
  ],
  'L_CLASS_BODY_': [
    [],
    [
      ['VAR_DEF', 'L_CLASS_BODY_'],
      ['FUNC_DEF', 'L_CLASS_BODY_'],
      ['e']
    ],
    [],
    []
  ],
  'L_TARGET_': [
    [],
    [
      ['TARGET', 'tk_asignacion', 'L_TARGET_'],
      ['e']
    ],
    [],
    []
  ],
  'CEXPR_': [
    [],
    [
      ['BIN_OP', 'CEXPR', 'CEXPR_'],
      ['e']
    ],
    [],
    []
  ],
  'MEMBER_EXPR_': [
    [],
    [
      ['CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_par_izq', 'IL_EXPR', 'tk_par_der', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['e']
    ],
    [],
    []
  ],
  'INDEX_EXPR_': [
    [],
    [
      ['e'],
      ['CEXPR_', 'INDEX_EXPR_A']
    ],
    [],
    []
  ],
  'CEXPRA': [
    [],
    [
      ['CEXPR_'],
      ['tk_par_izq', 'IL_EXPR', 'tk_par_der', 'CEXPR_']
    ],
    [],
    []
  ],
  'IL_EXPRA': [
    [],
    [
      ['CEXPR_', 'EXPR_', 'L_EXPR'],
      ['tk_par_izq', 'IL_EXPR', 'tk_par_der', 'CEXPR_', 'EXPR_', 'L_EXPR']
    ],
    [],
    []
  ],
  'MEMBER_EXPRA': [
    [],
    [
      ['CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_'],
      ['tk_par_izq', 'IL_EXPR', 'tk_par_der', 'CEXPR_', 'tk_punto', 'tk_id', 'MEMBER_EXPR_']
    ],
    [],
    []
  ],
  'INDEX_EXPR_1': [ #id
      [], 
      [
          ['INDEX_EXPR__6__'],
          ['INDEX_EXPR_5'],
          ['tk_par_izq', 'IL_EXPR', 'tk_par_der', 'INDEX_EXPR5_']
      ],[],[] 
  ],
  'INDEX_EXPR_2': [ #corchete_izq
      [], 
      [
          ['IL_EXPR', 'tk_corchete_der', 'INDEX_EXPR5_']
      ],[],[] 
  ],
  'INDEX_EXPR_3': [ #tk_PAR_IZQ
      [], 
      [
          ['EXPR', 'tk_par_der', 'INDEX_EXPR5_']
      ],[],[] 
  ],
  'INDEX_EXPR_4': [ #tk_resta
      [], 
      [
          ['CEXPR', 'INDEX_EXPR5_']
      ],[],[] 
  ],
  'INDEX_EXPR_5': [ #tk_None, tk_true, tk_false, tk_numer, tk_string, tk_idstring
      [], 
      [
          ['CEXPR_', 'INDEX_EXPR_6_'],
      ],[],[] 
  ],
  'INDEX_EXPR_6_': [
      [], 
      [
          ['tk_corchete_izq', 'EXPR', 'tk_corchete_der', 'INDEX_EXPR_'],
          ['tk_punto', 'tk_id', 'MEMBER_EXPR_', 'INDEX_EXPR__6__']

      ],[],[] 
  ],
  'INDEX_EXPR__6__': [
      [], 
      [
          ['CEXPR_', 'tk_corchete_izq', 'EXPR', 'tk_corchete_der', 'INDEX_EXPR_'],
          ['tk_par_izq', 'IL_EXPR', 'tk_par_der', 'CEXPR_', 'tk_corchete_izq', 'EXPR', 'tk_corchete_der', 'INDEX_EXPR_']

      ],[],[] 
  ],
  'INDEX_EXPR_A': [
    [],
    [
      ['tk_corchete_izq', 'EXPR', 'tk_corchete_der', 'INDEX_EXPR_'],
      ['tk_punto', 'tk_id', 'MEMBER_EXPR_', 'CEXPR_', 'tk_corchete_izq', 'EXPR', 'tk_corchete_der', 'INDEX_EXPR_'],
      ['tk_punto', 'tk_id', 'MEMBER_EXPR_', 'tk_par_izq', 'IL_EXPR', 'tk_par_der', 'CEXPR_', 'tk_corchete_izq', 'EXPR', 'tk_corchete_der', 'INDEX_EXPR_']
    ],
    [],
    []
  ]

}