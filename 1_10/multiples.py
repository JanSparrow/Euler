def f(x) : 
    n = 0
    for y in range(1, x):
        if y % 3 == 0 or y % 5 == 0 : 
            n = n + y
    return n
    
d = f(1000)
print(d)