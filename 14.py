from helpers import timeit

cache = {}

def collatz_lenght(start):
    length = 1
    n = start
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n +1
        
        if n in cache:
            length = length + cache[n]
            break
        else:
            length += 1
    
    cache[start] = length
    return length

@timeit
def main():    
    max_length = 0
    max_length_num = 1
    for i in range(1,1_000_000):
        length = collatz_lenght(i)
        if length > max_length:
            max_length = max(length, max_length)
            max_length_num = i

    print(max_length_num, max_length)    


if __name__ == "__main__":
    main()