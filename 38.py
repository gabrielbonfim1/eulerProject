from helpers import isPandigital1To9
def concat_product(n):
    string = ''
    mult = 1
    while len(string) < 9:
        string += str(n*mult)
        mult += 1
    if len(string) > 9:
        return None
    if "0" in string:
        return None
    return string

def main():
    nums = []
    for num in range(50_000):
        conc = concat_product(num)
        if conc is not None and isPandigital1To9(conc):
            nums.append(conc)
    print(sorted(nums)[-1])


if __name__ == "__main__":
    main()