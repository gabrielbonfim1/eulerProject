from helpers import genPrimes

def main(num):
    primes = genPrimes()
    p = next(primes)
    while num != 1:
        if num % p == 0:
            num = num / p
        else:
            p = next(primes)
    print(p)


if __name__ == "__main__":
    num = 600_851_475_143
    main(num)