import sys
import re

CRED = '\033[91m'
CEND = '\033[0m'
MAX_INT = 2147483647
STRING_REGEX = re.compile('[\x20-\x7E\\\n\t\"]')
KEYWORDS = {'a' : ['and','as','assert','async','await'], 
            'b' : ['bool','break'], 
            'c' : ['class','continue'],
            'd' : ['def','del'],
            'e' : ['elif','else','except'],
            'f' : ['finally','for','from'],
            'F' : ['False'],
            'g' : ['global'],
            'i' : ['if','import','in','input','int','is'],
            'l' : ['lambda','len'],
            'n' : ['nonlocal','not'],
            'N' : ['None'],
            'o' : ['object','or'],
            'p' : ['pass','print'],
            'r' : ['raise','return'],
            's' : ['self','str'],
            'T' : ['True'],
            't' : ['try'],
            'w' : ['while','with'],
            'y' : ['yield'],
            '_' : ['__init__']}
KEYWORDS_REGEX = re.compile('[abcdefFgilnNoprsTtwy_]')
                

operators = {'+':"tk_suma", '-':"tk_resta", '*':"tk_mult", '//':"tk_div_entera", '%':"tk_modulo", 
    '<':"tk_menor_que", '>':"tk_mayor_que", '<=':"tk_menor_igual", '>=':"tk_mayor_igual", '==':"tk_igual", 
    '!=':"tk_diferente", '=':"tk_asignacion", '(':"tk_par_izq", ')':"tk_par_der", '[':"tk_corchete_izq", 
    ']':"tk_corchete_der", ',':"tk_coma", ':':"tk_dos_puntos", '.':"tk_punto", '->':"tk_ejecuta"}

def transition_function (string, line_number, column_number = 0):
    
    if column_number >= len(string) or string[column_number] == '#' or string[column_number] == '\n' or string[column_number] == '\r': 
        return # Check for a commented line or end line 
    
    #Read all extra spaces
    while string[column_number] == ' ' or string[column_number] == '\t':
        column_number += 1

    token = check_number(string, line_number, column_number)
    if token['lexema']:
        print('<NUMBER, ' + token['lexema'] + ', ' + str(line_number + 1) + ', ' + str(column_number+1) + '>')
        return transition_function(string, line_number, token['next'])
    
    token = check_string(string, column_number)
    if token['lexema']:
        print('<STRING, ' + token['lexema'] + ', ' + str(line_number +1) + ', ' + str(column_number+1) + '>')
        return transition_function(string, line_number, token['next'])    
    
    token = check_operator(string, column_number)
    if token['lexema']:
        print('<' + token['lexema'] + ', ' + str(line_number +1) + ', ' + str(column_number+1) + '>')
        return transition_function(string, line_number, token['next'])

    token = check_special_word(string, column_number)
    if token['lexema']:
        print('<' + token['lexema'] + ', ' + str(line_number +1) + ', ' + str(column_number+1) + '>')
        return transition_function(string, line_number, token['next'])
    
    token = check_id(string, column_number)
    if token['lexema']:
        print('<ID, ' + token['lexema'] + ', ' + str(line_number +1) + ', ' + str(column_number+1) + '>')
        return transition_function(string, line_number, token['next'])
    sys.exit(CRED + "Error: Unrecognized symbol '"+string[column_number]+"', line: "+str(line_number +1)+", column: "+str(column_number+1) + CEND)


def check_number(string, line_number, column_number):
    if not str.isdigit(string[column_number]):
        return {'lexema':None, 'next':None}
    else:
        final = column_number                
        if int(string[column_number]) == 0:
            if str.isdigit(string[column_number +1]):
                sys.exit(CRED + "Error: A number can't have leading ceros, line: "+str(line_number + 1)+", column: "+str(column_number + 1) + CEND)
            final = column_number + 1
        else:
            for i ,char in enumerate(string[column_number:]):
                if not str.isdigit(char):
                    break
            final = column_number + i
            if str.isdigit(char):
                if int(string[column_number:]) > MAX_INT:
                    sys.exit(CRED + "Error: The maximum value for a number is "+str(MAX_INT)+", line: "+str(line_number + 1)+", column: "+str(column_number + 1) + CEND)
                return {'lexema':string[column_number:], 'next':final+1}
        if int(string[column_number:final]) > MAX_INT:
            sys.exit(CRED + "Error: The maximum value for a number is "+str(MAX_INT)+", line: "+str(line_number + 1)+", column: "+str(column_number + 1) + CEND)
        return {'lexema':string[column_number:final], 'next':final}
           
def check_string(string, column_number):
    if str.isdigit(string[column_number]):
        return {'lexema':None, 'next':None}
    final = column_number
    if string[column_number] == '\"':
        for i ,char in enumerate(string[column_number+1:]):
            if char == '\"':
                final = column_number + i 
                break        
    if column_number==final:
        return {'lexema':None, 'next':None}
    else:
        if STRING_REGEX.match(string[column_number:final+2]):
            return {'lexema':string[column_number:final+2], 'next':final+2}
        else:
            return {'lexema':None, 'next':None}

def check_operator(string, column_number):
    sig = column_number + 1
    final = column_number + 2
    #double-character cases
    if string[column_number] == "/":
        if string[sig] == "/":
            return {'lexema':"tk_div_entera", 'next':final}
        else:
            return {'lexema':None, 'next':None}
    if string[column_number] == "!":
        if string[sig] == "=":
            return {'lexema':"tk_diferente", 'next':final}
        else:
            return {'lexema':None, 'next':None}
    if string[column_number] == "-":
        if string[sig] == ">":
            return {'lexema':"tk_ejecuta", 'next':final}
    if string[column_number] == "<":
        if string[sig] == "=":
            return {'lexema':"tk_menor_igual", 'next':final}
    if string[column_number] == ">":
        if string[sig] == "=":
            return {'lexema':"tk_mayor_igual", 'next':final}
    if string[column_number] == "=":
        if string[sig] == "=":
            return {'lexema':"tk_igual", 'next':final}
    #one-character cases
    if string[column_number] in operators:
        lex = operators[string[column_number]]
        return {'lexema':lex, 'next':sig}
    else:
        return {'lexema':None, 'next':None}

def check_special_word(string, column_number):
    if str.isdigit(string[column_number]):
        return {'lexema':None, 'next':None}
    final = column_number
    if KEYWORDS_REGEX.match(string[column_number]):
        for i ,char in enumerate(string[column_number:]):            
            if char == '_':                
                if string[column_number:column_number+7]=="__init__":
                    return {'lexema':string[column_number:column_number+7], 'next':column_number+7}
            elif not char.isalpha():
                break
        final = column_number + i
        if str.isalpha(string[final]) or str.isdigit(string[final] or string[final] == '_'):
            if final == len(string) - 1 and string[column_number:] in KEYWORDS[string[column_number]]:
                return {'lexema':string[column_number:], 'next':len(string)} 
            return {'lexema':None, 'next':None} 
        if string[column_number:final] in KEYWORDS[string[column_number]]:
            return {'lexema':string[column_number:final], 'next':final}
        else:
            return {'lexema':None, 'next':None}
    else:
        return {'lexema':None, 'next':None}

def check_id(string, column_number):
    final = column_number
    actual = string[column_number]
    if ((48 <= ord(actual) and ord(actual) <= 57) or (65 <= ord(actual) and ord(actual) <= 90) or (97 <= ord(actual) and ord(actual) <= 122) or (ord(actual) == 95)): #is number or letter
        for i, char in enumerate(string[column_number:]):
            if not ((48 <= ord(char) and ord(char) <= 57) or (65 <= ord(char) and ord(char) <= 90) or (97 <= ord(char) and ord(char) <= 122) or (ord(char) == 95)):
                break
        final = column_number + i
    if final == len(string) - 1 and (str.isalpha(string[final]) or str.isdigit(string[final]) or string[final] == '_'):
        return {'lexema':string[column_number:], 'next':len(string)}
    return {'lexema':string[column_number:final], 'next':final}
