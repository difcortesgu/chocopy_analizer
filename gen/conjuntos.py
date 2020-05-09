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

def get_the_first_ones(rule,id):
    first_ones = []
    if is_alpha_e(rule) and 'e' not in first_ones:
        return ['e',id]
    if isNonTerminal(rule[0]):
        first_ones.extend(recursive(grammar[rule[0]],id))
        if not has_1D(first_ones):
            first_ones = flatten(first_ones)
        
        if 'e' in first_ones:
            if len(rule)==1:
                pass
            elif len(rule)>1:
                index_of_e = int(first_ones.index('e'))
                del first_ones[index_of_e+1]
                first_ones.remove('e')                
                for i in range(1,len(rule)):
                    first_ones.extend(recursive(grammar[rule[i]],id))
                    if not has_1D(first_ones):
                        first_ones = flatten(first_ones)
                    if 'e' in first_ones:
                        index_of_e = int(first_ones.index('e'))
                        del first_ones[index_of_e+1]
                        first_ones.remove('e')
                    else:
                        break
        return first_ones
    else:
        return [rule[0],id]

def recursive(no_terminal,id):
    first_ones = [0]*len(no_terminal[1])
    for i in range(len(no_terminal[1])):
        first_ones[i] = get_the_first_ones(no_terminal[1][i],id)
    return first_ones

def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l

def has_1D(list_):
    has = True
    for element in list_:
        if type(element)==list:
            has = False
            break
    return has

def get_grammar():
    for key in grammar:
        no_terminal_def=grammar[key]
        for i in range(len(no_terminal_def[1])):
            result = get_the_first_ones(no_terminal_def[1][i],i)
            tmp=list(filter((i).__ne__, result))
            no_terminal_def[2].insert(i,tmp)
    for key in grammar:
        grammar[key][3].append(recursive_next(key))
    for key in grammar:
        primeros = grammar[key][2]
        siguientes = grammar[key][3][0]
        for primero in primeros:
            conjunto = []
            if has_1D(primero):
                conjunto = primero
            else:
                conjunto = flatten(primero)
            if 'e' in conjunto:
                conjunto = flatten(siguientes)
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
                        if isNonTerminal(alpha[tmp]):   
                            first = get_the_first_ones(alpha[tmp:],0)      
                            next_ones_tmp=[ele for ele in first if type(ele)==str]
                            for k in range(len(next_ones_tmp)):
                                if next_ones_tmp[k] not in next_ones and next_ones_tmp[k] != 'e':
                                    next_ones.append(next_ones_tmp[k])
                            if 'e' in next_ones:
                                next_ones.remove('e')
                                if key==alpha[tmp]:
                                    continue
                                next_ones_tmp2=recursive_next(key)
                                for k in range(len(next_ones_tmp2)):
                                    if next_ones_tmp2[k] not in next_ones and next_ones_tmp2[k] != 'e':
                                        next_ones.append(next_ones_tmp2[k])              
                        else:
                            next_ones.append(alpha[tmp])  
                    elif j+1==len(alpha):
                        tmp = j
                        if isNonTerminal(alpha[tmp]): 
                            if key==alpha[tmp]:
                                continue
                            next_ones_tmp2=recursive_next(key)
                            for k in range(len(next_ones_tmp2)):
                                if next_ones_tmp2[k] not in next_ones and next_ones_tmp2[k] != 'e':
                                    next_ones.append(next_ones_tmp2[k])
                        else:
                            next_ones.append(alpha[tmp])     
    return next_ones
