from helpers import primeSieve

def main():
    mult_num = 1
    mult_den = 1
    
    for den in range(11,100):
        for num in range(11,den):
            if num % 10 == 0 or den % 10 == 0:
                continue
            if num == den:
                continue
            
            digit_to_exclude = set(str(num)).intersection(set(str(den)))               
            if len(digit_to_exclude) > 0:
                a,b = num,den
                result = num / den
                if str(num)[0] == list(digit_to_exclude)[0]:
                    #print(str(num))
                    new_num = int(str(num)[1])
                else:
                    new_num = int(str(num)[0])
                if str(den)[0] == list(digit_to_exclude)[0]:
                    new_den = int(str(den)[1])
                else:
                    new_den = int(str(den)[0])
                if result == new_num/new_den:
                    mult_num *= new_num
                    mult_den *= new_den
    print(lowest_common_term(mult_num, mult_den)) 
                
                

def lowest_common_term(num, den):
    primes = primeSieve(num)
    ind = 0
    while primes[ind] <= num:
        while num % primes[ind] == 0 and den % primes[ind] == 0:
            num = num / primes[ind]
            den = den / primes[ind]
        ind += 1
    return(int(num), int(den))



if __name__ == "__main__":
    main()