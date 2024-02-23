import math

from numpy import append

def get_chain_lenght(n):
    if math.log10(n).is_integer():
        return 0
    
    remainders = []
    dividendo = 10**(int(math.log10(n))+1)
    while True:
        rem = dividendo % n
        
        if rem == 0:
            return 0            
        
        if rem not in remainders:
            remainders.append(rem)
            dividendo = rem * 10
        else:
            return len(remainders)- remainders.index(rem)
            

        
        


def main():
    max_length = 0
    max_length_num = 0
    for i in range(2,1_000):
        length = get_chain_lenght(i)
        if length > max_length:
            max_length = length
            max_length_num = i
    
    print(max_length_num)


if __name__ == "__main__":
    main()