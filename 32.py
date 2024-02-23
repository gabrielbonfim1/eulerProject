from helpers import digits
## Brute Force Try
def main_brute():
    final_set = set()
    for prod in range(4000,99_999//2):
        for i in range(1,9_999):
            if prod % i != 0:
                continue
            str_pand = str(prod)+str(i)+str(int(prod/i))
            if len(str_pand) == 9 and len(set(str_pand)) == 9 and '0' not in str_pand:                           
                print(str(prod),str(i),str(int(prod/i)))
                final_set.add(prod)
        
            
                
    print(sum(final_set))
        

if __name__ == "__main__":
    main_brute()