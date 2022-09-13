import math

lexi = [*range(0, 10)]
x = 999999

def correct(tab, n, r) : 
    t = tab[n + r]
    i = n + r
    while i > n :
        tab[i] = tab[i - 1]
        i -= 1
    tab[n] = t
    return

while x > 0 :
    i = 1
    j = 1
    while i <= x / (j + 1) :
        i *= (j + 1)
        j += 1
    print(i, j, lexi)
    level = int(math.floor(x / i))
    correct(lexi, 9 - j, level)
    x -= i * level

print(lexi)
    
    