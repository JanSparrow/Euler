import math
from unittest import skip


def val(n) :
    o = 0
    o = n + 1
    o = o - 1
    vr = 0
    if n >= 100 :
        vr = 7
        vr += lt10(int(n / 100))
        n = n % 100
        if n > 0 : 
            vr += 3

    if n > 19 :
        vr += tens(n)
        n = n % 10
    
    vr += lt10(n)
    print("n = ", o, ", vr = ", vr)
    return vr

def tens(n):
    m = int(n / 10)
    z = 0
    match m : 
        case 4 | 5 | 6 : z = 5
        case 2 | 3 | 8 | 9 : z = 6
        case 7 : z = 7
        case _ : skip
    return z

def lt10(n):
    x = 0
    match n :
        case 1 | 2 | 6 | 10 : x = 3
        case 4 | 5 | 9 : x = 4
        case 3 | 7 | 8 : x = 5
        case 11 | 12 : x = 6
        case 15 | 16 : x = 7
        case 13 | 14 | 18 | 19: x = 8
        case 17 : x = 9
        case _ : skip
    return x

vsota = 11

for i in range(1, 1000) :
    vsota += val(i)

print(vsota)
