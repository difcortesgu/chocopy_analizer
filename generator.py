from gramatica import get_grammar

def isNonTerminal(simbolo):
    # definir si el simbolo es un terminal o no
    return 65 <= ord(simbolo[0]) and ord(simbolo[0]) <= 90

def non_terminal_function(no_terminal, conjuntos, reglas):
    func = "\n\ndef {no_terminal}(token):\n".format(no_terminal = no_terminal)
    func += "\ttokens_esperados = [\n"
    for conjunto in conjuntos:
        for prediccion in conjunto:
            func += "\t\t\'{prediccion}\'\n".format(prediccion = prediccion)
    func += "\t]\n"

    for index, (conjunto, regla) in enumerate(zip(conjuntos, reglas)):
        if index == 0:
            if_statement = "\tif token.id == \'{prediccion}\'".format(prediccion = conjunto.pop())  
        else:
            if_statement = "\telif token.id == \'{prediccion}\'".format(prediccion = conjunto.pop())
        for prediccion in conjunto:
            if_statement += " or token.id == \'{prediccion}\'".format(prediccion = prediccion)
        if_statement += ":\n"  
        if_body = ""
        if not regla:
            if_body = "\t\tpass\n"
        else:                
            for simbolo in regla:
                if isNonTerminal(simbolo):
                    if_body += "\t\t{simbolo}(token)\n".format(simbolo = simbolo)
                else:
                    if_body += "\t\ttoken = emparejar(\'{simbolo}\', token)\n".format(simbolo = simbolo)
        func += if_statement + if_body
    func += "\telse:\n\t\tsyntaxisError(token, tokens_esperados)"
    return func

with open(file = 'syntaxis_analizer.py', encoding='latin-1', mode='w') as f:
    main = '''from analizer import SyntaxAnalizer
from os import path
import sys

CRED = '\\033[91m'
CEND = '\\033[0m'

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
    sys.exit(error_message)'''

    f.write(main)
    grammar = get_grammar()
    for key, value in grammar.items():
        func = non_terminal_function(key, value[0], value[1])
        f.write(func)
