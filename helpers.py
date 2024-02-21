from timeit import default_timer as timer
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
            primes.append(x)
            yield x
            x += 1

    
def primeSieve(num):
    prime = [True for i in range(num)]
    p = 2
    while (p * p <= num): 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True): 
            # Updating all multiples of p
            for i in range(p * p, num, p):
                prime[i] = False
        p += 1
 
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            return [ind for ind,p in enumerate(prime) if p and ind > 1]
    

def IsPalindrome(num):
    num_string = str(int(num))
    return num_string == num_string[::-1]
