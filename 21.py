from helpers import sumOfDivisors

def main():
    amicable = set()
    for i in range(1,10000):
        sum_divs = sumOfDivisors(i)
        if sumOfDivisors(sum_divs) == i and sum_divs != i:
            amicable.add(sum_divs)
            amicable.add(i)
    
    print(sum(amicable))


if __name__ == "__main__":
    main()