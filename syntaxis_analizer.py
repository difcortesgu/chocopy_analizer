from analizer import SyntaxAnalizer
from os import path
import sys

CRED = '\033[91m'
CEND = '\033[0m'

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        f = sys.argv[1]
    else:
        sys.exit(CRED +"Error: Debe pasar el nombre del archivo como argumento"+ CEND)
    if not path.isfile(f):
        sys.exit(CRED +'Error: El archivo especificado no existe'+ CEND)

    syntax_analizer = SyntaxAnalizer(f, 4)
    token = syntax_analizer.next_token()
    token = A(token)
    if (token.id != 'EOF'):
        sys.exit(CRED + "Error: Unexpected token '"+token.lexema+"' expecting 'EOF', line: "+str(token.line_number)+", column: "+str(token.column_number) + CEND)

def emparejar(simbolo, token):
    if token.id == simbolo:
        return syntax_analizer.next_token()
    else:
        syntaxisError(token, [simbolo])

def syntaxisError(token, tokens_esperados):
    error_message = CRED + "Error: Unexpected token '"+token.lexema+"' expecting "
    for x in tokens_esperados:
        error_message += "'" + x + "' "
    error_message = ", line: "+str(token.line_number)+", column: "+str(token.column_number) + CEND
    sys.exit(error_message)

def L_DEF(token):
	tokens_esperados = [
		'tk_id'
		'tk_class'
		'tk_def'
	]
	if token.id == 'tk_id':
		VAR_DEF(token)
		L_DEF(token)
	elif token.id == 'tk_class':
		FUNC_DEF(token)
		L_DEF(token)
	elif token.id == 'tk_def':
		CLASS_DEF(token)
		L_DEF(token)
	else:
		syntaxisError(token, tokens_esperados)

def CLASS_DEF(token):
	tokens_esperados = [
		'tk_class'
	]
	if token.id == 'tk_class':
		token = emparejar('tk_class', token)
		token = emparejar('tk_id', token)
		token = emparejar('tk_par_izq', token)
		token = emparejar('tk_id', token)
		token = emparejar('tk_par_der', token)
		token = emparejar('tk_dos_puntos', token)
		token = emparejar('tk_newline', token)
		token = emparejar('tk_indent', token)
		CLASS_BODY(token)
		token = emparejar('tk_dedent', token)
	else:
		syntaxisError(token, tokens_esperados)

def CLASS_BODY(token):
	tokens_esperados = [
		'tk_id'
		'tk_pass'
	]
	if token.id == 'tk_id':
		token = emparejar('tk_pass', token)
		token = emparejar('tk_newline', token)
	elif token.id == 'tk_pass':
		L_CLASS_BODY(token)
	else:
		syntaxisError(token, tokens_esperados)

def L_CLASS_BODY(token):
	tokens_esperados = [
		'tk_id'
		'tk_def'
	]
	if token.id == 'tk_id':
		VAR_DEF(token)
		token = emparejar('_L_CLASS_BODY', token)
	elif token.id == 'tk_def':
		FUNC_DEF(token)
		token = emparejar('__L_CLASS_BODY', token)
	else:
		syntaxisError(token, tokens_esperados)

def _L_CLASS_BODY(token):
	tokens_esperados = [
		'tk_id'
	]
	if token.id == 'tk_id':
		L_CLASS_BODY(token)
	else:
		syntaxisError(token, tokens_esperados)

def __L_CLASS_BODY(token):
	tokens_esperados = [
		'tk_id'
	]
	if token.id == 'tk_id':
		L_CLASS_BODY(token)
	else:
		syntaxisError(token, tokens_esperados)

def FUNC_DEF(token):
	tokens_esperados = [
		'tk_def'
	]
	if token.id == 'tk_def':
		token = emparejar('tk_def', token)
		token = emparejar('tk_id', token)
		token = emparejar('tk_par_izq', token)
		IL_TYPED_VAR(token)
		token = emparejar('tk_par_der', token)
		token = emparejar('tk_dos_puntos', token)
		token = emparejar('tk_newline', token)
		token = emparejar('tk_indent', token)
		FUNC_BODY(token)
		token = emparejar('tk_dedent', token)
	else:
		syntaxisError(token, tokens_esperados)

def IL_TYPED_VAR(token):
	tokens_esperados = [
		'tk_id'
	]
	if token.id == 'tk_id':
		TYPED_VAR(token)
		L_TYPED_VAR(token)
	else:
		syntaxisError(token, tokens_esperados)

def L_TYPED_VAR(token):
	tokens_esperados = [
		'tk_coma'
	]
	if token.id == 'tk_coma':
		token = emparejar('tk_coma', token)
		TYPED_VAR(token)
		L_TYPED_VAR(token)
	else:
		syntaxisError(token, tokens_esperados)

def L_FUNC_BODY(token):
	tokens_esperados = [
		'tk_id'
		'tk_global'
		'tk_nonlocal'
		'tk_def'
	]
	if token.id == 'tk_id':
		VAR_DEF(token)
		L_FUNC_BODY(token)
	elif token.id == 'tk_global':
		FUNC_DEF(token)
		L_FUNC_BODY(token)
	elif token.id == 'tk_nonlocal':
		GLOBAL_DECL(token)
		L_FUNC_BODY(token)
	elif token.id == 'tk_def':
		NONLOCAL_DECL(token)
		L_FUNC_BODY(token)
	else:
		syntaxisError(token, tokens_esperados)

def TYPED_VAR(token):
	tokens_esperados = [
		'tk_id'
	]
	if token.id == 'tk_id':
		token = emparejar('tk_id', token)
		token = emparejar('tk_dos_puntos', token)
		TYPE(token)
	else:
		syntaxisError(token, tokens_esperados)

def GLOBAL_DECL(token):
	tokens_esperados = [
		'tk_global'
	]
	if token.id == 'tk_global':
		token = emparejar('tk_global', token)
		token = emparejar('tk_id', token)
		token = emparejar('tk_newline', token)
	else:
		syntaxisError(token, tokens_esperados)

def NONLOCAL_DECL(token):
	tokens_esperados = [
		'tk_nonlocal'
	]
	if token.id == 'tk_nonlocal':
		token = emparejar('tk_nonlocal', token)
		token = emparejar('tk_id', token)
		token = emparejar('tk_newline', token)
	else:
		syntaxisError(token, tokens_esperados)

def VAR_DEF(token):
	tokens_esperados = [
		'tk_id'
	]
	if token.id == 'tk_id':
		TYPED_VAR(token)
		token = emparejar('tk_asignacion', token)
		LITERAL(token)
		token = emparejar('tk_newline', token)
	else:
		syntaxisError(token, tokens_esperados)

def L_ELIF(token):
	tokens_esperados = [
		'tk_elif'
	]
	if token.id == 'tk_elif':
		token = emparejar('tk_elif', token)
		EXPR(token)
		token = emparejar('tk_dos_puntos', token)
		BLOCK(token)
		L_ELIF(token)
	else:
		syntaxisError(token, tokens_esperados)

def ELSE(token):
	tokens_esperados = [
		'tk_else'
	]
	if token.id == 'tk_else':
		token = emparejar('tk_else', token)
		token = emparejar('tk_dos_puntos', token)
		BLOCK(token)
	else:
		syntaxisError(token, tokens_esperados)

def BLOCK(token):
	tokens_esperados = [
		'tk_newline'
	]
	if token.id == 'tk_newline':
		token = emparejar('tk_newline', token)
		token = emparejar('tk_indent', token)
		L_STMT(token)
		token = emparejar('tk_dedent', token)
	else:
		syntaxisError(token, tokens_esperados)

def LITERAL(token):
	tokens_esperados = [
		'tk_number'
		'tk_string'
		'tk_False'
		'tk_True'
		'tk_None'
	]
	if token.id == 'tk_number':
		token = emparejar('tk_None', token)
	elif token.id == 'tk_string':
		token = emparejar('tk_True', token)
	elif token.id == 'tk_False':
		token = emparejar('tk_False', token)
	elif token.id == 'tk_True':
		token = emparejar('tk_number', token)
	elif token.id == 'tk_None':
		token = emparejar('tk_string', token)
	else:
		syntaxisError(token, tokens_esperados)

def _EXPR(token):
	tokens_esperados = [
		'tk_and'
		'tk_or'
		'tk_if'
	]
	if token.id == 'tk_and':
		token = emparejar('tk_and', token)
		EXPR(token)
		token = emparejar('_EXPR', token)
	elif token.id == 'tk_or':
		token = emparejar('tk_or', token)
		EXPR(token)
		token = emparejar('_EXPR', token)
	elif token.id == 'tk_if':
		token = emparejar('tk_if', token)
		EXPR(token)
		token = emparejar('tk_else', token)
		EXPR(token)
		token = emparejar('_EXPR', token)
	else:
		syntaxisError(token, tokens_esperados)

def L_EXPR(token):
	tokens_esperados = [
		'tk_coma'
	]
	if token.id == 'tk_coma':
		token = emparejar('tk_coma', token)
		EXPR(token)
		L_EXPR(token)
	else:
		syntaxisError(token, tokens_esperados)