def nextprime(prime) :
    nxtp = prime[len(prime) - 1] + 1 
    primo = False
    while not primo :
        primo = True
        for x in prime :
            if nxtp % x == 0 :
                nxtp += 1
                primo = False
                break
    return prime + [nxtp]


def lrgpr(n) :
    prime = [2]
    d = prime[len(prime) - 1]
    while n > 1 : 
        d = prime[len(prime) - 1]
        if n % d == 0 :
            while n % d == 0 :
                n = n / d
        prime = nextprime(prime)
    return d


print(lrgpr(600851475143))
