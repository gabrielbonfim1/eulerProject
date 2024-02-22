from helpers import sumOfDivisors
def main():
    abundant = set()
    for i in range(1,28123):
        if sumOfDivisors(i) > i:
            abundant.add(i)

    abundant_list = list(abundant)
    sums_of_abundant = set()

    for num1 in abundant_list:
        if num1 > 28123:
            break
        for num2 in abundant_list:
            if num1 + num2 > 28123:
                break
            sums_of_abundant.add(num1+num2)
    
    all_nums = set(list(range(1,28123)))

    print(sum(list(all_nums - sums_of_abundant)))
        

if __name__ == "__main__":
    main()