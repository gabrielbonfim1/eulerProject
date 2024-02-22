def main():
    n1 = 1
    n2 = 1
    x = 2
    while len(str(n2)) < 1000:
        n1, n2 = n2, n1+n2
        x+=1
    print(x)

if __name__ == "__main__":
    main()