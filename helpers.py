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
