def f(x):
    n = 0
    m = 1
    temp = 0
    for i in range(0, x):
        temp = n + m
        n = m
        m = temp
    return n

x = 0
vsota = 0
while f(x) < 4000000 :
    if f(x) % 2 == 0 :
        vsota += f(x)
    x += 1

print(vsota)

for i in range(0, 10): 
    print(f(i))

