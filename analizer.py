import sys
import re

CRED = '\033[91m'
CEND = '\033[0m'
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
                

def transition_function (string, line_number, column_number = 0):
    
    if string[column_number] == '#' or string[column_number] == '\n' or string[column_number] == '\r': 
        return # Check for a commented line or end line 
    #print(string[column_number])
    token = check_number(string, line_number, column_number)
    if token['lexema']:
        print('<NUMBER, ' + token['lexema'] + ', ' + str(line_number) + ', ' + str(column_number) + '>')
        return transition_function(string, line_number, token['next'])
    
    token = check_string(string, column_number)
    if token['lexema']:
        print('<STRING, ' + token['lexema'] + ', ' + str(line_number) + ', ' + str(column_number) + '>')
        return transition_function(string, line_number, token['next'])    
    
    token = check_operator(string, column_number)
    if token['lexema']:
        print('<' + token['lexema'] + ', ' + str(line_number) + ', ' + str(column_number) + '>')
        return transition_function(string, line_number, token['next'])

    token = check_special_word(string, column_number)
    if token['lexema']:
        print('<' + token['lexema'] + ', ' + str(line_number) + ', ' + str(column_number) + '>')
        return transition_function(string, line_number, token['next'])
    
    token = check_id(string, column_number)
    if token['lexema']:
        print('<ID, ' + token['lexema'] + ', ' + str(line_number) + ', ' + str(column_number) + '>')
        return transition_function(string, line_number, token['next'])
    #This is just to test the functionality while is not complete
    return transition_function(string, line_number, column_number+1)
    sys.exit(CRED + "Error: Unrecognized symbol '"+string[column_number]+"', line: "+str(line_number)+", column: "+str(column_number) + CEND)


# All of these functions must receive and return the same
# receives: string, column_number
# returns: <string lexema> found lexema, <int next> position where the next lexema might begin
def check_number(string, line_number, column_number):
    if not str.isdigit(string[column_number]):
        return {'lexema':None, 'next':None}
    else:
        final = column_number                
        if int(string[column_number]) == 0:
            if str.isdigit(string[column_number +1]):
                sys.exit(CRED + "Error: A number can't have leading ceros, line: "+str(line_number)+", column: "+str(column_number + 1) + CEND)
            final = column_number + 1
        if 1 <= int(string[column_number]) and int(string[column_number]) <= 10:
            for i ,char in enumerate(string[column_number:]):
                if not str.isdigit(char):
                    final = column_number + i
                    break
        for i ,char in enumerate(string[final:]):
            if char != ' ' or char != '\t':
                return {'lexema':string[column_number:final], 'next':final + i}
    
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
                final = column_number + i 
                break
            
        if string[column_number:final] in KEYWORDS[string[column_number]]:
            return {'lexema':string[column_number:final], 'next':final}
        else:
            return {'lexema':None, 'next':None}
    else:
        return {'lexema':None, 'next':None}

    

def check_id(string, column_number):
    return {'lexema':None, 'next':None}