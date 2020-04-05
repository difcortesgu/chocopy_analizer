def transition_function (string, line_number, column_number = 0):
    
    if string[column_number] == '#' or string[column_number] == '\n' or string[column_number] == '\r': 
        return # Check for a commented line or end line 
    
    token = check_number(string, column_number)
    if token['lexema']:
        print('< NUMBER, ' + token['lexema'] + ', ' + line_number + ', ' + column_number + ' >')
        return transition_function(string, line_number, token['next'])
    
    token = check_string(string, column_number)
    if token['lexema']:
        print('< STRING, ' + token['lexema'] + ', ' + line_number + ', ' + column_number + ' >')
        return transition_function(string, line_number, token['next'])    
    
    token = check_operator(string, column_number)
    if token['lexema']:
        print('< ' + token['lexema'] + ', ' + line_number + ', ' + column_number + ' >')
        return transition_function(string, line_number, token['next'])

    token = check_special_word(string, column_number)
    if token['lexema']:
        print('< ' + token['lexema'] + ', ' + line_number + ', ' + column_number + ' >')
        return transition_function(string, line_number, token['next'])
    
    token = check_id(string, column_number)
    if token['lexema']:
        print('< ID, ' + token['lexema'] + ', ' + line_number + ', ' + column_number + ' >')
        return transition_function(string, line_number, token['next'])


# All of these functions must receive and return the same
# receives: string, column_number
# returns: <string lexema> found lexema, <int next> position where the next lexema might begin
def check_number(string, column_number):
    return {'token':None, 'next':None}

def check_string(string, column_number):
    return {'token':None, 'next':None}

def check_operator(string, column_number):
    return {'token':None, 'next':None}

def check_special_word(string, column_number):
    return {'token':None, 'next':None}

def check_id(string, column_number):
    return {'token':None, 'next':None}