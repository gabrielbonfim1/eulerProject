def main():
    x = 20
    nums = [11,12,13,14,15,16,17,18,19,20]
    while True:
        for fac in nums:
            if x % fac != 0:
                x += 20
                break
        else:
            return x
        

if __name__ == "__main__":
    print(main())