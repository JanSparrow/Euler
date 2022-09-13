from operator import ne


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

prime = [2]
le = 2000000
while (prime[len(prime) - 1] < le) :
    prime = nextprime(prime)

print(prime[len(prime) - 1])

vsota = sum(prime) - prime[len(prime) - 1]
print(vsota)