from grammar import grammar
# from test_grammar import grammar
import copy

def isNonTerminal(simbol):
    return 95 == ord(simbol[0]) or (65 <= ord(simbol[0]) and ord(simbol[0]) <= 90)

def removeDirectLeftRecursion(grammar, A):
    Bs = []
    aes = []
    grammarShouldChange = False
    for rule in grammar[A][1]:
        if rule[0] == A:
            aes.append(rule[1:])
            grammarShouldChange = True
        else:
            Bs.append(rule)
    if not grammarShouldChange: return grammar
    grammar[A][1] = []
    A_ = A+'_'
    for Bi in Bs:
        Bi.append(A_)
        grammar[A][1].append(Bi)
    grammar[A_] = [[],[],[],[]]
    for ai in aes:
        ai.append(A_)
        grammar[A_][1].append(ai)
    grammar[A_][1].append(['e'])
    return grammar

def removeLeftRecursion(grammar):
    parseF = {k:i for i,(k,v) in enumerate(grammar.items())}
    parseB = {i:k for i,(k,v) in enumerate(grammar.items())}
    for i in range(len(grammar)):
        Ai = parseB[i]
        rules = grammar[Ai]
        grammarChanged = True
        while( grammarChanged ):
            grammarChanged = False
            for index, ai in enumerate(rules[1]):
                if isNonTerminal(ai[0]): 
                    Aj = ai[0] 
                    j = parseF[Aj]
                    if j < parseF[Ai]:
                        Bi = ai[1:] 
                        del grammar[Ai][1][index]
                        for aj in grammar[Aj][1]:
                            grammar[Ai][1].append(aj + Bi)
                        grammarChanged = True
        grammar = removeDirectLeftRecursion(grammar, Ai)
    return grammar

def get_n_common_factors(value):
    hasMoreFactors = True
    n_common_factors = 0
    while hasMoreFactors:
        hasMoreFactors = False
        if n_common_factors < len(value[0][1]):
            factor = value[0][1][n_common_factors]
            n_common_factors += 1
            hasMoreFactors = True
            for rule in value:
                if n_common_factors > len(rule[1]) or rule[1][n_common_factors-1] != factor:
                    n_common_factors -= 1
                    hasMoreFactors = False
                    break
    return n_common_factors

def getNextFactors(rules):
    factors = {}
    for i, rule in enumerate(rules):
        if rule[0] not in factors:
            factors[rule[0]] = []
        factors[rule[0]].append((i, rule[1:]))
    factor = max(factors, key = lambda k: len(factors[k]))
    if len(factors[factor]) > 1:
        return factors[factor]
    return None

def removeNCommonFactors(grammar, A, factors, n, A_):
    if not factors: return grammar
    factor = grammar[A][1][factors[0][0]][:n]
    aes = []
    j = 0
    for i,value in factors:
        aes.append(grammar[A][1][i-j][n:])
        del grammar[A][1][i - j]
        j+=1
    factor.append(A_)
    grammar[A][1].append(factor)
    grammar[A_] = [[],[],[],[]]
    for a in aes:
        grammar[A_][1].append(a)
    return grammar

def removeLeftCommonFactors(grammar):
    hasChanges = True
    while hasChanges:
        parseB = {i:k for i,(k,v) in enumerate(grammar.items())}
        hasChanges = False            
        for i in range(len(grammar)):
            Ai = parseB[i]
            rules = grammar[Ai][1]
            factor = getNextFactors(rules)
            fi = 1
            while factor != None:
                hasChanges = True
                n_common_factors = get_n_common_factors(factor) + 1
                grammar = removeNCommonFactors(grammar, Ai, factor,  n_common_factors, Ai+str(fi))
                factor = getNextFactors(rules)
                fi+=1
    return grammar

grammar = removeLeftRecursion(grammar)
grammar = removeLeftCommonFactors(grammar)
print(grammar)

