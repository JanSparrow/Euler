x = pow(10, 999)

n = 0 
m = 1
i = 1
t = 0 

while m < x :
    t = m
    m = n + m
    n = t
    i = i + 1

print(i)