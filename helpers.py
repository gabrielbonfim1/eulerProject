def genPrimes():
    primes = [2]
    x = 2
    while True:        
        if x == 2:
            yield 2
            x += 1
        
        for prime in primes:
            if x % prime == 0:
                x += 1
                break
        else:
            primes.append(prime)
            yield x
            x += 1
