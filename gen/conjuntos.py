from grammar.grammar import grammar

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
