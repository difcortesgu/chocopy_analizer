
grammar = {
    #'PROGRAM':[
    #        [], #conjuntos de prediccion
    #        [['L_DEF','L_STMT']],
    #        [],
    #        []
    #    ],
    
    #'L_STMT': [
    #        [], 
    #        [['STMT','L_STMT'], ['e']] ,
    #        [],
    #        []
    #    ],
    'L_DEF':[
            [], 
            [['VAR_DEF','L_DEF'], ['FUNC_DEF','L_DEF'], ['CLASS_DEF','L_DEF'],['e']],
            [],
            [] 
        ],
    'CLASS_DEF': [
            [], 
            [['tk_class','tk_id','tk_par_izq','tk_id','tk_par_der','tk_dos_puntos','tk_newline','tk_indent','CLASS_BODY','tk_dedent']],
            [],
            [] 
        ],        
    'CLASS_BODY':[
            [], 
            [['tk_pass','tk_newline'], ['L_CLASS_BODY']] ,
            [],
            []
        ],
    'L_CLASS_BODY': [
            [], 
            [['VAR_DEF','_L_CLASS_BODY'], ['FUNC_DEF', '__L_CLASS_BODY']],
            [],
            [] 
        ],
    '_L_CLASS_BODY':[
            [], 
            [['L_CLASS_BODY'], ['e']],
            [],
            [] 
        ],
    '__L_CLASS_BODY':[
            [], 
            [['L_CLASS_BODY'], ['e']],
            [],
            [] 
        ],
    'FUNC_DEF': [
            [], 
            [['tk_def','tk_id','tk_par_izq','IL_TYPED_VAR','tk_par_der','tk_dos_puntos','tk_newline','tk_indent','FUNC_BODY','tk_dedent']],
            [],
            [] 
        ],
    'IL_TYPED_VAR': [
            [], 
            [['TYPED_VAR','L_TYPED_VAR'], ['e']],
            [],
            [] 
        ],
    'L_TYPED_VAR': [
            [], 
            [['tk_coma','TYPED_VAR','L_TYPED_VAR'], ['e']] ,
            [],
            []
        ],
    
    #'FUNC_BODY': [
    #        [], 
    #        [['L_FUNC_BODY','L_FUNC_STMT']],
    #        [],
    #        [] 
    #    ],
    #'L_FUNC_STMT': [
    #        [], 
    #        [['STMT','_L_FUNC_STMT']],
    #        [],
    #        [] 
    #    ],
    #'_L_FUNC_STMT': [
    #        [], 
    #        [['L_FUNC_STMT'], ['e']],
    #        [],
    #        [] 
    #    ],
    
    'L_FUNC_BODY': [
            [], 
            [['VAR_DEF','L_FUNC_BODY'], ['FUNC_DEF','L_FUNC_BODY'], ['GLOBAL_DECL','L_FUNC_BODY'], ['NONLOCAL_DECL','L_FUNC_BODY'], ['e']],
            [],
            [] 
        ],
    'TYPED_VAR': [
            [], 
            [['tk_id','tk_dos_puntos','TYPE']],
            [],
            [] 
        ],
    
    #'TYPE': [
    #        [], 
    #        [['tk_id'], ['ID_STRING'], ['tk_corchete_izq','TYPE','tk_corchete_der']],
    #        [],
    #        [] 
    #    ],
    
    'GLOBAL_DECL': [
            [], 
            [['tk_global','tk_id','tk_newline']],
            [],
            [] 
        ],
        
    'NONLOCAL_DECL': [
            [], 
            [['tk_nonlocal','tk_id','tk_newline']],
            [],
            [] 
        ],
    'VAR_DEF': [
            [], 
            [['TYPED_VAR','tk_asignacion','LITERAL','tk_newline']],
            [],
            [] 
        ],
    #'STMT': [
    #        [], 
    #        [['SIMPLE_STMT','tk_newline'], ['tk_if','EXPR','tk_dos_puntos','BLOCK','L_ELIF','ELSE'],['tk_while','EXPR','tk_dos_puntos','BLOCK'],['tk_for','tk_id','tk_in','EXPR','tk_dos_puntos','BLOCK']],
    #        [],
    #        [] 
    #    ], 
    'L_ELIF': [
            [], 
            [['tk_elif','EXPR','tk_dos_puntos','BLOCK','L_ELIF'], ['e']] ,
            [],
            []
        ],
    #'ELSE': [
    #        [], 
    #        [['tk_else','tk_dos_puntos','BLOCK'], ['e']],
    #        [],
    #        [] 
    #    ],
    #'SIMPLE_STMT': [
    #        [], 
    #        [['tk_pass'], ['EXPR'], ['tk_return','OPT_EXPR'], ['L_TARGET','EXPR']],
    #        [],
    #        [] 
    #    ],
    #'L_TARGET': [
    #        [], 
    #        [['TARGET','tk_asignacion','_L_TARGET']],
    #        [],
    #        [] 
    #    ],
    #'_L_TARGET': [
    #        [], 
    #        [['L_TARGET'], ['e']],
    #        [],
    #        [] 
    #    ],
    #'OPT_EXPR': [
    #        [], 
    #        [['EXPR'], ['e']],
    #        [],
    #        [] 
    #    ],
    'BLOCK': [
            [], 
            [['tk_newline','tk_indent','L_STMT','tk_dedent']],
            [],
            [] 
        ],
    'LITERAL': [
            [], 
            [['tk_None'], ['tk_True'],['tk_False'], ['tk_number'], ['tk_string']],
            [],
            [] 
        ],
    #'EXPR': [
    #        [], 
    #        [['CEXPR','_EXPR'], ['tk_not','EXPR','_EXPR']],
    #        [],
    #        [] 
    #    ],
    '_EXPR': [
            [], 
            [['tk_and','EXPR','_EXPR'], ['tk_or','EXPR','_EXPR'], ['tk_if','EXPR','tk_else','EXPR','_EXPR'], ['e']] ,
            [],
            []
        ],
    #'CEXPR': [
    #        [], 
    #        [['IL_EXPR','_CEXPR'], ['tk_par_izq','EXPR','tk_par_der','_CEXPR'], ['MEMBER_EXPR','__CEXPR'], ['INDEX_EXPR','_CEXPR'], ['tk_id','tk_par_izq','IL_EXPR','tk_par_der','_CEXPR'], ['tk_resta','CEXPR','_CEXPR'], ['_CEXPR']],
    #        [],
    #        [] 
    #    ],
    #'_CEXPR': [
    #        [], 
    #        [['BIN_OP','CEXPR','_CEXPR'], ['tk_id','_CEXPR'],['LITERAL','_CEXPR'], ['e']] ,
    #        [],
    #        []
    #    ],
    #'__CEXPR': [
    #        [], 
    #        [['_CEXPR'], ['tk_par_izq','IL_EXPR','tk_par_der','_CEXPR']],
    #        [],
    #        [] 
    #    ],
    #'IL_EXPR': [
    #        [], 
    #        [['EXPR','L_EXPR']] ,
    #        [],
    #        []
    #    ],
    'L_EXPR': [
            [], 
            [['tk_coma','EXPR','L_EXPR'], ['e']] ,
            [],
            []
        ],
    #'MEMBER_EXPR': [
    #        [], 
    #        [['CEXPR','tk_punto','tk_id']],
    #        [],
    #        [] 
    #    ],
    #'INDEX_EXPR': [
    #        [], 
    #        [['CEXPR','tk_corchete_izq','EXPR','tk_corchete_der']],
    #        [],
    #        [] 
    #    ],
    #'TARGET': [
    #        [], 
    #        [['tk_id'], ['MEMBER_EXPR'], ['INDEX_EXPR']] ,
    #        [],
    #        []
    #    ],
}
def is_alpha_e(no_terminal_rule):
    e = ['e']
    if no_terminal_rule==e:
        return True
    else:
        return False

def isNonTerminal(simbolo):
    # definir si el simbolo es un terminal o no
    return 95 == ord(simbolo[0]) or (65 <= ord(simbolo[0]) and ord(simbolo[0]) <= 90)

def get_the_first_ones(rule):
    first_ones = []
    if is_alpha_e(rule) and 'e' not in first_ones:
        return ['e']
    if isNonTerminal(rule[0]):
        first_ones.extend(recursive(grammar[rule[0]]))
        if 'e' in first_ones:
            if len(rule)==1:
                pass
            elif len(rule)>1:
                first_ones.remove('e')
                for i in range(1,len(rule)):
                    first_ones.extend(recursive(grammar[rule[i]]))
        return first_ones
    else:
        return rule[0]
    
def recursive(no_terminal):
    first_ones = [0]*len(no_terminal[1])
    for i in range(len(no_terminal[1])):
        first_ones[i] = get_the_first_ones(no_terminal[1][i])
    return first_ones

def get_first_value(arr):
    return arr[0]

def get_grammar():
    for key in grammar:
        no_terminal_def=grammar[key]
        for i in range(len(no_terminal_def[1])):
            result = get_the_first_ones(no_terminal_def[1][i])
            if type(result)==str:
                no_terminal_def[2].append([result])
            else:
                tmp = result[0]
                tmp2= result
                while(type(tmp)!=str):
                    tmp = get_first_value(tmp)
                    tmp2 = get_first_value(tmp2)
                if len(tmp2)>1:
                    no_terminal_def[2].append(tmp2)
                else:
                    no_terminal_def[2].append([tmp])
    for key in grammar:
        grammar[key][3].append(recursive_next(key))
    for key in grammar:
        primeros = grammar[key][2]
        siguientes = grammar[key][3][0]
        for primero in primeros:
            conjunto = []
            if ['e'] == primero:
                conjunto = siguientes            
                grammar[key][0].append(set(conjunto))
            else:
                conjunto=primero
                grammar[key][0].append(set(conjunto))
    return grammar

def recursive_next(no_terminal):
    next_ones = []  
    if no_terminal == 'PROGRAM':
        next_ones.append('$')
    for key in grammar:
        for i in range(len(grammar[key][1])):
            alpha = grammar[key][1][i]
            for j in range(len(alpha)):
                A = alpha[j]       
                if A == no_terminal:
                    tmp = 0
                    if j+1<len(alpha):
                        tmp = j+1
                    elif j+1==len(alpha):
                        tmp = j
                    if isNonTerminal(alpha[tmp]):            
                        next_ones_tmp=transform_to_list(grammar[alpha[tmp]][2])
                        for k in range(len(next_ones_tmp)):
                            if next_ones_tmp[k] not in next_ones and next_ones_tmp[k] != 'e':
                                next_ones.append(next_ones_tmp[k])
                        if 'e' in next_ones:
                            next_ones.remove('e')
                            if key==alpha[tmp]:
                                continue
                            next_ones_tmp2=recursive_next(key)
                            for k in range(len(next_ones_tmp2)):
                                if next_ones_tmp[k] not in next_ones and next_ones_tmp2[k] != 'e':
                                    next_ones.append(next_ones_tmp2[k])              
                    else:
                        next_ones.append(alpha[tmp])        
    return next_ones
    
def transform_to_list(list_of_list):
    list_trans = []
    if len(list_of_list)>1:
        for ind_list in list_of_list:
            list_trans.extend(ind_list) 
    else:
        list_trans=list_of_list
    return list_trans

""" gramatic = {
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
"""
# CEXPR -> ID
# CEXPR -> LITERAL
# CEXPR -> IL_EXPR
# IL_EXPR -> EXPR L_EXPR
# L_EXPR -> tk_coma EXPR L_EXPR
# L_EXPR -> e
# CEXPR -> e
# CEXPR -> tk_par_izq EXPR tk_par_der
# CEXPR -> MEMBER_EXPR
# CEXPR -> INDEX_EXPR
# CEXPR -> MEMBER_EXPR tk_par_izq IL_EXPR tk_par_der 
# CEXPR -> ID tk_par_izq IL_EXPR tk_par_der
# CEXPR -> CEXPR BIN_OP CEXPR
# CEXPR -> tk_resta CEXPR
