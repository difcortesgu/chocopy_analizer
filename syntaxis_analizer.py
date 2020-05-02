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

def A(token):
	tokens_esperados = [
		'cuatro'
		'tres'
		'dos'
	]
	if token.id == 'cuatro' or token.id == 'tres':
		B(token)
		token = emparejar('uno', token)
	elif token.id == 'dos':
		token = emparejar('dos', token)
	else:
		syntaxisError(token, tokens_esperados)

def B(token):
	tokens_esperados = [
		'tres'
		'cuatro'
	]
	if token.id == 'tres':
		token = emparejar('tres', token)
	elif token.id == 'cuatro':
		token = emparejar('cuatro', token)
		A(token)
	else:
		syntaxisError(token, tokens_esperados)