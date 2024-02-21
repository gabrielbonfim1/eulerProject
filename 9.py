from itertools import product
def main():
    for (a,b) in product(range(1,1000),range(1,1000)):
        if (a**2 + b**2)**0.5 // 1 == (a**2 + b**2)**0.5:
            c = (a**2 + b**2)**0.5
            if a + b + c == 1000:
                print(int(a*b*c))
                break


if __name__ == "__main__":
    main()