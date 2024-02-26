def gen_next_digit():
    n = 1
    yield 1
    while True:
        n += 1
        for digit in str(n):
            yield int(digit)

def main():
    digits = gen_next_digit()
    mult = 1
    pos_log = 10
    for ind, digit in enumerate(digits):
        pos = ind + 1        
        if pos % pos_log == 0:
            mult *= digit
            pos_log *= 10
        if pos > 1000000:
            break
    print(mult)

if __name__ == "__main__":
    main()