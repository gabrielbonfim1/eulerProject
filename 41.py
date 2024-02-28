from helpers import primeSieve
from helpers import isPandigital1Ton

def main():
    primes = primeSieve(9999999)
    print("-- Imprimiu Primos ---")
    max_p = 0
    for p in primes:
        if isPandigital1Ton(p):            
            max_p = p

    print(f"{max_p=}")
if __name__ == "__main__":
    main()