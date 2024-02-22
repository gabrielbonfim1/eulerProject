import math

def main():
    num = str(math.factorial(100))
    sum = 0
    for digit in num:
        sum += int(digit)
    print(sum)



if __name__ == "__main__":
    main()