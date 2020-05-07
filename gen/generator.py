from conjuntos import get_grammar

def isNonTerminal(simbolo):
    # definir si el simbolo es un terminal o no
    return 65 <= ord(simbolo[0]) and ord(simbolo[0]) <= 90

def non_terminal_function(no_terminal, conjuntos, reglas):
    func = "\n\n\tdef {no_terminal}(self):\n".format(no_terminal = no_terminal)
    func += "\t\ttokens_esperados = [\n"
    for conjunto in conjuntos:
        for prediccion in conjunto:
            func += "\t\t\t\'{prediccion}\',\n".format(prediccion = prediccion)
    func += "\t\t]\n"

    for index, (conjunto, regla) in enumerate(zip(conjuntos, reglas)):
        if index == 0:
            if_statement = "\t\tif self.token.id == \'{prediccion}\'".format(prediccion = conjunto.pop())  
        else:
            if_statement = "\t\telif self.token.id == \'{prediccion}\'".format(prediccion = conjunto.pop())
        for prediccion in conjunto:
            if_statement += " or self.token.id == \'{prediccion}\'".format(prediccion = prediccion)
        if_statement += ":\n"  
        if_body = ""
        if regla == 'e':
            if_body = "\t\t\tpass\n"
        else:                
            for simbolo in regla:
                if isNonTerminal(simbolo):
                    if_body += "\t\t\tself.{simbolo}()\n".format(simbolo = simbolo)
                else:
                    if_body += "\t\t\tself.emparejar(\'{simbolo}\')\n".format(simbolo = simbolo)
        func += if_statement + if_body
    func += "\t\telse:\n\t\t\tself.syntaxError(tokens_esperados)"
    return func

with open(file = '../syntax_analizer.py', encoding='latin-1', mode='w') as f:
    f.write('''from lexical_analizer import LexicalAnalizer
from os import path
import sys

class SyntaxAnalizer:
\tdef __init__(self, file):
\t\tself.CRED = '\\033[91m'
\t\tself.CEND = '\\033[0m'
\t\tself.lexical_analizer = LexicalAnalizer(file, {tab_size})
\t\tself.token = self.lexical_analizer.next_token()
\t\tself.emparejar('tk_newline')

\tdef analize(self):
\t\tself.{initial_node}()
\t\tif (self.token.id != 'EOF'):
\t\t\tsys.exit(self.CRED + "Error: Unexpected token '"+self.token.lexema+"' expecting 'EOF', line: "+str(self.token.line_number)+", column: "+str(self.token.column_number) + self.CEND)

\tdef emparejar(self, simbolo):
\t\tif self.token.id == simbolo:
\t\t\tself.token = self.lexical_analizer.next_token()
\t\telse:
\t\t\tself.syntaxError([simbolo])

\tdef syntaxError(self, tokens_esperados):
\t\terror_message = self.CRED + "Error: Unexpected token '"+self.token.lexema+"' expecting "
\t\tfor x in tokens_esperados:
\t\t\terror_message += "'" + x + "' "
\t\terror_message += ", line: "+str(self.token.line_number)+", column: "+str(self.token.column_number) + self.CEND
\t\tsys.exit(error_message)'''.format(tab_size = 4, initial_node = "PROGRAM"))
    
    grammar = get_grammar()
    for key, value in grammar.items():
        func = non_terminal_function(key, value[0], value[1])
        f.write(func)
