import math
def permutaciones(n, r):
    p=math.factorial(n) // math.factorial(n - r)
    return p
    
def combinaciones(n, r):
    c=math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    return c
