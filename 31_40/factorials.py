import math
from re import I

def sumf(x) :
    y =  math.factorial(x % 10)
    if (x >= 10) :
        return y + sumf(int(math.floor(x / 10)))
    else :
        return y

vsota = 0

for i in range(10, 42000) :
    if (i == sumf(i)) :
        vsota += i


print(vsota)