from queue import LifoQueue, Queue
from lexical_token import Token
import sys
import re

class SyntaxAnalizer:
    
    def __init__(self, filename, tab_size):
        self.tab_size = tab_size
        with open(file = filename, encoding='latin-1') as f:
            self.file = f.readlines()
        self.line_number = 0
        self.nextTokens = Queue()
        self.indentation_stack = LifoQueue()
        self.indentation_stack.put(0)
        self.CRED = '\033[91m'
        self.CEND = '\033[0m'
        self.MAX_INT = 2147483647
        self.STRING_REGEX = re.compile('[\x20-\x7E\n\t]')
        self.KEYWORDS = {'a' : ['and','as','assert','async','await'], 
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
        self.KEYWORDS_REGEX = re.compile('[abcdefFgilnNoprsTtwy_]')
        self.OPERATORS = {'+':"tk_suma", '-':"tk_resta", '*':"tk_mult", '//':"tk_div_entera", '%':"tk_modulo", 
            '<':"tk_menor_que", '>':"tk_mayor_que", '<=':"tk_menor_igual", '>=':"tk_mayor_igual", '==':"tk_igual", 
            '!=':"tk_diferente", '=':"tk_asignacion", '(':"tk_par_izq", ')':"tk_par_der", '[':"tk_corchete_izq", 
            ']':"tk_corchete_der", ',':"tk_coma", ':':"tk_dos_puntos", '.':"tk_punto", '->':"tk_ejecuta"}

    def next_token(self):
        while self.nextTokens.empty() and self.line_number < len(self.file):
            self.next_line_tokens()
        if self.line_number >= len(self.file):
            return Token('EOF')
        return self.nextTokens.get()

    def next_line_tokens(self):
        indentation_level = 0
        column_number = 0
        while column_number < len(self.file[self.line_number]): 
            char = self.file[self.line_number][column_number]
         
            if char == '\n' or char == '#':
                break
            elif char == ' ':
                indentation_level += 1
                column_number += 1
            elif char == '\t':
                indentation_level += self.tab_size
                column_number += self.tab_size
            else:
                self.nextTokens.put(Token('NEWLINE'))
                #Logic to check the indentation level
                #The indentation must be a multiple of TAB_SIZE
                if indentation_level % self.tab_size != 0:
                    sys.exit(self.CRED +"Error: Indentation error, line: "+str(self.line_number)+", column: "+str(column_number)+ self.CEND)
                indentation_last_level = self.indentation_stack.get()       
                if indentation_level > indentation_last_level: 
                    #add a new indentation level
                    self.nextTokens.put(Token('INDENT'))
                    self.indentation_stack.put(indentation_last_level)
                    self.indentation_stack.put(indentation_level)
                elif indentation_level == indentation_last_level: 
                    #leave indentation level the same
                    self.indentation_stack.put(indentation_last_level)
                else:
                    #remove from the indentation stack until the desired level is reached
                    while indentation_level < indentation_last_level:
                        indentation_last_level = self.indentation_stack.get()
                        self.nextTokens.put(Token('DEDENT'))
                    self.indentation_stack.put(indentation_level)
                column_number = self.transition_function(column_number)
        self.line_number += 1

    def transition_function (self, column_number):
        char = self.file[self.line_number][column_number]
        #Read all extra spaces
        while column_number < len(self.file[self.line_number]) and (char== ' ' or char == '\t'):
            column_number += 1
            char = self.file[self.line_number][column_number]

        
        if column_number >= len(self.file[self.line_number]) or char == '#' or char == '\n' or char == '\r': 
            return column_number# Check for a commented line or end line or end of file

        token = self.check_number(column_number)
        if token['lexema']:
            self.nextTokens.put(Token('NUMBER', token['lexema'], self.line_number+1, column_number+1))
            return self.transition_function(token['next'])
        
        token = self.check_string(column_number)
        if token['lexema']:
            self.nextTokens.put(Token('STRING', token['lexema'], self.line_number+1, column_number+1))
            return self.transition_function(token['next'])    
        
        token = self.check_operator(column_number)
        if token['lexema']:
            self.nextTokens.put(Token(token['lexema'], token['lexema'], self.line_number+1, column_number+1))
            return self.transition_function(token['next'])

        token = self.check_special_word(column_number)
        if token['lexema']:
            self.nextTokens.put(Token(token['lexema'], token['lexema'], self.line_number+1, column_number+1))
            return self.transition_function(token['next'])
        
        token = self.check_id(column_number)
        if token['lexema']:
            self.nextTokens.put(Token('ID', token['lexema'], self.line_number+1, column_number+1))
            return self.transition_function(token['next'])

        sys.exit(self.CRED + "Error: Unrecognized symbol '"+char+"', line: "+str(self.line_number +1)+", column: "+str(column_number+1) + self.CEND)

    def check_number(self, column_number):
        string = self.file[self.line_number]
        if not str.isdigit(string[column_number]):
            return {'lexema':None, 'next':None}
        else:
            final = column_number                
            if int(string[column_number]) == 0:
                if str.isdigit(string[column_number +1]):
                    sys.exit(self.CRED + "Error: A number can't have leading ceros, line: "+str(self.line_number + 1)+", column: "+str(column_number + 1) + self.CEND)
                final = column_number + 1
            else:
                for i ,char in enumerate(string[column_number:]):
                    if not str.isdigit(char):
                        break
                final = column_number + i
                if str.isdigit(char):
                    if int(string[column_number:]) > self.MAX_INT:
                        sys.exit(self.CRED + "Error: The maximum value for a number is "+str(self.MAX_INT)+", line: "+str(self.line_number + 1)+", column: "+str(column_number + 1) + self.CEND)
                    return {'lexema':string[column_number:], 'next':final+1}
            if int(string[column_number:final]) > self.MAX_INT:
                sys.exit(self.CRED + "Error: The maximum value for a number is "+str(self.MAX_INT)+", line: "+str(self.line_number + 1)+", column: "+str(column_number + 1) + self.CEND)
            return {'lexema':string[column_number:final], 'next':final}
           
    def check_string(self, column_number):
        string = self.file[self.line_number]
        if str.isdigit(string[column_number]):
            return {'lexema':None, 'next':None}
        final = column_number
        if string[column_number] == '\"':
            for i ,char in enumerate(string[column_number+1:]):
                if char == '\"':
                    if string[column_number+i]=='\x5c':
                        continue
                    else:
                        final = column_number + i 
                        break        
            if column_number==final:
                #return {'lexema':None, 'next':None}
                sys.exit(self.CRED + "Error: A \" symbol must close the ' "+string[column_number]+" ' symbol of the line: "+str(self.line_number +1)+" and column: "+str(column_number+1) + self.CEND)
            else:
                i = 0
                is_string = True
                actual_string=string[column_number+1:final+1]
                while i < len(actual_string):
                    if actual_string[i] == '\x5c':
                        if actual_string[i+1] =='\x5c':
                            counter = 0
                            for char in actual_string[i+1:]:
                                if char == '\x5c':
                                    counter += 1
                                else:
                                    break
                            if counter<3 or counter%2==0:
                                is_string = False
                                sys.exit(self.CRED + "Error: Unrecognized symbol '"+string[column_number+i+counter]+"', line: "+str(self.line_number +1)+", column: "+str(column_number+i+counter) + self.CEND)
                            else:
                                i += counter
                        elif actual_string[i+1] =='\x22':
                            i += 1
                        else:
                            sys.exit(self.CRED + "Error: Unrecognized symbol '"+string[column_number+i+1]+"', line: "+str(self.line_number +1)+", column: "+str(column_number+i+2) + self.CEND)
                    elif not self.STRING_REGEX.match(actual_string[i]):
                        is_string = False
                        sys.exit(self.CRED + "Error: Unrecognized symbol '"+string[column_number+i+1]+"', line: "+str(self.line_number +1)+", column: "+str(column_number+2+i) + self.CEND)
                    i += 1
                if is_string:
                    return {'lexema':string[column_number:final+2], 'next':final+2}
                else:
                    return {'lexema':None, 'next':None}
        else:
            return {'lexema':None, 'next':None}

    def check_operator(self, column_number):
        string = self.file[self.line_number]
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
        if string[column_number] in self.OPERATORS:
            lex = self.OPERATORS[string[column_number]]
            return {'lexema':lex, 'next':sig}
        else:
            return {'lexema':None, 'next':None}

    def check_special_word(self, column_number):
        string = self.file[self.line_number]
        if str.isdigit(string[column_number]):
            return {'lexema':None, 'next':None}
        final = column_number
        if self.KEYWORDS_REGEX.match(string[column_number]):
            for i ,char in enumerate(string[column_number:]):            
                if char == '_':                
                    if string[column_number:column_number+7]=="__init__":
                        return {'lexema':string[column_number:column_number+7], 'next':column_number+7}
                elif not char.isalpha():
                    break
            final = column_number + i
            if str.isalpha(string[final]) or str.isdigit(string[final] or string[final] == '_'):
                if final == len(string) - 1 and string[column_number:] in self.KEYWORDS[string[column_number]]:
                    return {'lexema':string[column_number:], 'next':len(string)} 
                return {'lexema':None, 'next':None} 
            if string[column_number:final] in self.KEYWORDS[string[column_number]]:
                return {'lexema':string[column_number:final], 'next':final}
            else:
                return {'lexema':None, 'next':None}
        else:
            return {'lexema':None, 'next':None}

    def check_id(self, column_number):
        string = self.file[self.line_number]
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

        