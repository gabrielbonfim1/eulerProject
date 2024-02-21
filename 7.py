from helpers import genPrimes
def main():
    p_gen = genPrimes()
    for _ in range(10001):
        p = next(p_gen)
    print(p)


if __name__ == "__main__":
    main()