from math import factorial

def paradoxe(seuil):
    n = 1
    p = 0
    while p < seuil:
        n += 1
        p = 1 - ((factorial(365))/((365**n)*(factorial(365-n))))
    return n
