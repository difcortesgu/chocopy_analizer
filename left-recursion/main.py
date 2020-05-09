from grammar import grammar
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

# def removeLeftCommonFactors(grammar):
#     parseF = {k:i for i,(k,v) in enumerate(grammar.items())}
#     parseB = {i:k for i,(k,v) in enumerate(grammar.items())}
#     for i in range(len(grammar)):
#         Ai = parseB[i]
#         rules = grammar[Ai]
#         for index, ai in enumerate(rules[1]):
#             pass
#     return grammar

grammar = removeLeftRecursion(grammar)
print("hola")