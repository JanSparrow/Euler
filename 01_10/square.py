sum = 0
square = 0

for x in range(1, 101):
    sum += x
    square += x * x

sum = sum * sum

dif = sum - square


print(square)
print(sum)
print(dif)