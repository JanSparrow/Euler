import math

def divisors(n) :
    div = 0
    for x in range(1, int(math.sqrt(n)) + 1) : 
        if n % x == 0 :
            div += 2
    return div

solved = True
i = 1
n = 0

while solved :
    n += i
    div = divisors(n)
    if div >= 500 :
        solved = False
    i += 1

print(n)

print(divisors(10))