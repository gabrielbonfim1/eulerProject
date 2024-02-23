from timeit import default_timer as timer
import math
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

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
    markers = list([True for i in range(num)])
    markers[0],markers[1],markers[2] = True,True,True
    
    x = 2
    while x**2 <= num:
        if markers[x] == True:        
            for ind in range(x**2,num,x):
                markers[ind] = False
        x += 1
    return(list([ind for ind,_ in enumerate(markers) if _ == True and ind > 1]))
    

def IsPalindrome(num):
    num_string = str(int(num))
    return num_string == num_string[::-1]

def countDivisors(n):
    divs = 0
    for t in range(1,int(math.sqrt(n))+1):
        if n % t == 0:
            if t == n//t:
                divs+=1
            else:
                divs+=2
    return divs

def sumOfDivisors(n):
    divs = set()
    for t in range(1,int(math.sqrt(n))+1):
        if n % t == 0:
            divs.add(t)
            divs.add(n //t)
    return sum(divs) - n

def digits(n):
    return int(math.log10(n)) + 1