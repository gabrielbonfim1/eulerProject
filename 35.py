from helpers import primeSieve
from itertools import permutations

def rotations(string):
    rotations = []
    arr = list(string)
    while "".join(arr) not in rotations:
        rotations.append("".join(arr))
        arr.append(arr.pop(0))
    return rotations

def main():
    count = 0
    primes_below_milion = primeSieve(10_000_000)
    prime_set = set(primes_below_milion)
    for p in primes_below_milion:
        if p > 1_000_000:
            break
        permuts = rotations(str(p))
        for num in permuts:
            if int("".join(num)) not in prime_set:
                break
        else:
            count += 1
            print(p)
        
    print(count)
    return count


if __name__ == "__main__":
    main()