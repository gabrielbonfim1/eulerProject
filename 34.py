from math import factorial
def main():
    result = 0
    for num in range(3,1_000_001):
        sum = 0
        s_num = str(num)
        for digit in s_num:
            sum += factorial(int(digit))
        if sum == num:
            result += sum
    print(result)
    return result


if __name__ == "__main__":
    main()