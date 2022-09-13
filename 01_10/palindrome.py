max = 0
temp = 0

def palindrome(n) :
    s = str(n)
    x = len(s)
    for i in range(0, x - 1) :
        if s[i] != s[x - i - 1] :
            return False
    return True


for i in reversed(range(100, 1000)) :
    for j in reversed(range(100, 1000)) :
        temp = i * j
        if temp > max :
            if palindrome(temp) :
                max = temp


print(max)