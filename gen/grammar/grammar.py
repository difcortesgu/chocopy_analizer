grammar = {
  "GLOBAL_DECL": [
    [],
    [
      ["tk_global", "tk_id", "tk_newline"]
    ],
    [],
    []
  ],
  "NONLOCAL_DECL": [
    [],
    [
      ["tk_nonlocal", "tk_id", "tk_newline"]
    ],
    [],
    []
  ],
  "LITERAL": [
    [],
    [
      ["tk_None"],
      ["tk_True"],
      ["tk_False"],
      ["tk_number"],
      ["tk_idstring"],
      ["tk_string"]
    ],
    [],
    []
  ],
  "BIN_OP": [
    [],
    [
      ["tk_suma"],
      ["tk_resta"],
      ["tk_mult"],
      ["tk_div_entera"],
      ["tk_modulo"],
      ["tk_igual"],
      ["tk_diferente"],
      ["tk_menor_igual"],
      ["tk_mayor_igual"],
      ["tk_menor_que"],
      ["tk_mayor_que"],
      ["tk_is"]
    ],
    [],
    []
  ],
  "VAR_DEF": [
    [],
    [
      ["TYPED_VAR", "tk_asignacion", "LITERAL", "tk_newline"]
    ],
    [],
    []
  ],
  "TYPED_VAR": [
    [],
    [
      ["tk_id", "tk_dos_puntos", "TYPE"]
    ],
    [],
    []
  ],
  "TYPE": [
    [],
    [
      ["tk_id"],
      ["tk_int"],
      ["tk_str"],
      ["tk_bool"],
      ["tk_object"],
      ["tk_idstring"],
      ["tk_corchete_izq", "TYPE", "tk_corchete_der"]
    ],
    [],
    []
  ],
  "PROGRAM": [
    [],
    [
      ["L_DEF", "L_STMT"]
    ],
    [],
    []
  ],
  "L_DEF": [
    [],
    [
      ["FUNC_DEF", "L_DEF"],
      ["CLASS_DEF", "L_DEF"],
      ["tk_id", "tk_dos_puntos", "TYPE", "tk_asignacion", "LITERAL", "tk_newline", "L_DEF"],
      ["e"]
    ],
    [],
    []
  ],
  "L_STMT": [
    [],
    [
      ["STMT", "L_STMT"],
      ["e"]
    ],
    [],
    []
  ],
  "FUNC_DEF": [
    [],
    [
      ["tk_def", "tk_id", "tk_par_izq", "IL_TYPED_VAR", "tk_par_der", "OPT_TYPE", "tk_dos_puntos", "tk_newline", "tk_indent", "FUNC_BODY", "tk_dedent"]
    ],
    [],
    []
  ],
  "CLASS_DEF": [
    [],
    [
      ["tk_class", "tk_id", "tk_par_izq", "tk_id", "tk_par_der", "tk_dos_puntos", "tk_newline", "tk_indent", "CLASS_BODY", "tk_dedent"]
    ],
    [],
    []
  ],
  "IL_TYPED_VAR": [
    [],
    [
      ["tk_id", "tk_dos_puntos", "TYPE", "L_TYPED_VAR"],
      ["e"]
    ],
    [],
    []
  ],
  "OPT_TYPE": [
    [],
    [
      ["tk_ejecuta", "TYPE"],
      ["e"]
    ],
    [],
    []
  ],
  "FUNC_BODY": [
    [],
    [
      ["L_FUNC_BODY", "L_FUNC_STMT"]
    ],
    [],
    []
  ],
  "CLASS_BODY": [
    [],
    [
      ["tk_pass", "tk_newline"],
      ["L_CLASS_BODY"]
    ],
    [],
    []
  ],
  "L_FUNC_BODY": [
    [],
    [
      ["tk_global", "tk_id", "tk_newline", "L_FUNC_BODY"],
      ["tk_id", "tk_dos_puntos", "TYPE", "tk_asignacion", "LITERAL", "tk_newline", "L_FUNC_BODY"],
      ["tk_def", "tk_id", "tk_par_izq", "IL_TYPED_VAR", "tk_par_der", "OPT_TYPE", "tk_dos_puntos", "tk_newline", "tk_indent", "FUNC_BODY", "tk_dedent", "L_FUNC_BODY"],
      ["tk_nonlocal", "tk_id", "tk_newline", "L_FUNC_BODY"],
      ["e"]
    ],
    [],
    []
  ],
  "L_FUNC_STMT": [
    [],
    [
      ["STMT", "L_FUNC_STMT_"]
    ],
    [],
    []
  ],
  "L_TYPED_VAR": [
    [],
    [
      ["tk_coma", "TYPED_VAR", "L_TYPED_VAR"],
      ["e"]
    ],
    [],
    []
  ],
  "L_CLASS_BODY": [
    [],
    [
      ["tk_id", "tk_dos_puntos", "TYPE", "tk_asignacion", "LITERAL", "tk_newline", "L_CLASS_BODY_"],
      ["tk_def", "tk_id", "tk_par_izq", "IL_TYPED_VAR", "tk_par_der", "OPT_TYPE", "tk_dos_puntos", "tk_newline", "tk_indent", "FUNC_BODY", "tk_dedent", "L_CLASS_BODY_"]
    ],
    [],
    []
  ],
  "STMT": [
    [],
    [
      ["SIMPLE_STMT", "tk_newline"],
      ["tk_if", "tk_id", "tk_dos_puntos", "BLOCK", "L_ELIF", "ELSE"],
      ["tk_while", "tk_id", "tk_dos_puntos", "BLOCK"],
      ["tk_for", "tk_id", "tk_in", "tk_id", "tk_dos_puntos", "BLOCK"]
    ],
    [],
    []
  ],
  "SIMPLE_STMT": [
    [],
    [
      ["tk_pass"],
      ["tk_id"],
      ["tk_return", "OPT_EXPR"],
      ["L_TARGET", "tk_id"]
    ],
    [],
    []
  ],
  "BLOCK": [
    [],
    [
      ["tk_newline", "tk_indent", "L_FUNC_STMT", "tk_dedent"]
    ],
    [],
    []
  ],
  "L_ELIF": [
    [],
    [
      ["tk_elif", "tk_id", "tk_dos_puntos", "BLOCK", "L_ELIF"],
      ["e"]
    ],
    [],
    []
  ],
  "ELSE": [
    [],
    [
      ["tk_else", "tk_dos_puntos", "BLOCK"],
      ["e"]
    ],
    [],
    []
  ],
  "OPT_EXPR": [
    [],
    [
      ["tk_id"],
      ["e"]
    ],
    [],
    []
  ],
  "L_TARGET": [
    [],
    [
      ["TARGET", "tk_asignacion", "L_TARGET_"]
    ],
    [],
    []
  ],
  "TARGET": [
    [],
    [
      ["tk_id"]
    ],
    [],
    []
  ],
  "L_FUNC_STMT_": [
    [],
    [
      ["STMT", "L_FUNC_STMT_"],
      ["e"]
    ],
    [],
    []
  ],
  "L_CLASS_BODY_": [
    [],
    [
      ["VAR_DEF", "L_CLASS_BODY_"],
      ["FUNC_DEF", "L_CLASS_BODY_"],
      ["e"]
    ],
    [],
    []
  ],
  "L_TARGET_": [
    [],
    [
      ["TARGET", "tk_asignacion", "L_TARGET_"],
      ["e"]
    ],
    [],
    []
  ]
}