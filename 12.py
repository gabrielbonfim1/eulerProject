from helpers import countDivisors

def gen_triangle():
    x = 2
    sum = 1
    while True:
        if sum == 1:
            yield 1
        sum += x
        x+=1
        yield sum

def main():
    gen = gen_triangle()
    while True:
        num = next(gen)
        if countDivisors(num) > 500:
            print(num, countDivisors(num))
            break


if __name__ == "__main__":
    main()

