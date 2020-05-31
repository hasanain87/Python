from functools import reduce

def Acronym(phrase): 
    return ''.join([w[0] for w in phrase.split() if w < 'a'])

print(Acronym("the Beauty and Joy of Computing"))

def AcronymSwap(phrase): 
    return ''.join([w for w in [w[0] for w in phrase.split()] if w < 'a'])

print(AcronymSwap("the Beauty and Joy of Computing"))