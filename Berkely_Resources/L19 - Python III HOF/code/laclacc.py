def reverse(S):
	return S[::-1]

def stutter(S):
	return S[0]+S

def double(S):
	return S+S

"""
print(reverse("cal"))
print(stutter("cal"))
print(double("cal"))
"""

def compose(f,g):
	return lambda x: f(g(x))

from functools import reduce

frankenstein = reduce(compose, [reverse, stutter, double])

print(frankenstein("cal"))