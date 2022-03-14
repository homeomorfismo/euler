import math as m

def IsPrime(N):
    isprime = True
    bound = m.ceil(m.sqrt(N))
    while bound > 1:
        if N % bound == 0:
            isprime = False
            break
        bound -= bound
    return isprime

def PrimeFactors(N):
    primes = []
    div = 2
    # bound = m.ceil(m.sqrt(N))
    while True:
        power = 1
        if N % div == 0:
            primes.append(div)
            while N % (div**(power+1)) == 0:
                power += 1
            N = N/(div**power)
        else:
            while True:
                div += 1
                if IsPrime(N) == True:
                    break
        # if div > bound:
        if div > N:
            break
    return primes

def LargestPrimeFactor(N):
    primes = PrimeFactors(N)
    return max(primes)

# print(PrimeFactors(13195))
print(LargestPrimeFactor(600851475143))

print(LargestPrimeFactor(7*2**10))
