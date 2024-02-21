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

def IsPalindrome(num):
    num_string = str(int(num))
    return num_string == num_string[::-1]
