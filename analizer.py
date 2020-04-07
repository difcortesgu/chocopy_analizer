import sys

CRED = '\033[91m'
CEND = '\033[0m'

def transition_function (string, line_number, column_number = 0):
    
    if string[column_number] == '#' or string[column_number] == '\n' or string[column_number] == '\r': 
        return # Check for a commented line or end line 
    
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
    #return transition_function(string, line_number, column_number+1)
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
    return {'lexema':None, 'next':None}

def check_operator(string, column_number):
    return {'lexema':None, 'next':None}

def check_special_word(string, column_number):
    return {'lexema':None, 'next':None}

def check_id(string, column_number):
    return {'lexema':None, 'next':None}