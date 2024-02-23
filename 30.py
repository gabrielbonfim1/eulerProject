def main():
    sum_num = 0
    for n in range(2,300_000):
        n_str = str(n)
        p_sum = 0
        for digit in n_str:
            p_sum += int(digit)**5
        if p_sum == n:
            sum_num += n
    print(sum_num)
        

if __name__ == "__main__":
    main()