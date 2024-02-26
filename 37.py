from helpers import primeSieve
from itertools import chain

def gen_left_truncates(num):
    arr = []
    string = str(num)
    while len(string) > 1:
        string = string [1::]
        arr.append(string)
    return arr

def gen_right_truncates(num):
    arr = []
    string = str(num)
    while len(string) > 1:
        string = string [0:-1]
        arr.append(string)
    return arr

def main():
    primes = primeSieve(1_000_000)
    prime_set = set(primes)
    sum = 0
    for prime in primes:
        for p in chain(gen_left_truncates(prime), gen_right_truncates(prime)):
            if int(p) not in prime_set:
                break
        else:
            sum += prime            
    sum -= 17
    print(f"{sum=}")

if __name__ == "__main__":
    main()