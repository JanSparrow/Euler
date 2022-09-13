from operator import ne


def nextprime(prime) :
    nxtp = prime[len(prime) - 1] + 2 
    primo = False
    while not primo :
        primo = True
        for x in prime :
            if nxtp % x == 0 :
                nxtp += 2
                primo = False
                break
    return prime + [nxtp]

def primeornoot(n, prime) :
    while (n > prime[len(prime) - 1]) :
        prime = nextprime(prime)
    if (prorn(n, prime)) :
        return True

    return False

def prorn(n, prime) :
    lp = 0
    rp = len(prime) - 1
    while (lp <= rp) :
        s = int((rp + lp) / 2)
        if (prime[s] == n) :
            return True
        elif (prime[s] < n) :
            lp = s + 1
        else :
            rp = s - 1
    return False

def seque(a, b, candidates) :
    t = b
    i = 1
    while (primeornoot(t, candidates)) :
        t = i * i + i * a + b
        i += 1
    return i - 1

prime = [2, 3]
le = 997
while (prime[len(prime) - 1] < le) :
    prime = nextprime(prime)

candidates = [2, 3]

maxs = 0
maxp = 0
for b in prime :
    for a in prime:
        seq = seque(a - b - 1, b, candidates)
        if (seq > maxs) :
            maxs = seq
            maxp = (a - b - 1) * b
        if (a < b) :
            seq = seque(-a, b, candidates)
            if (seq > maxs) :
                maxs = seq
                maxp = - a * b

print(maxs, maxp)