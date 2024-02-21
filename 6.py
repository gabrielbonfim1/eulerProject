def main():
    x = sum([x**2 for x in range(1,101)])
    y = sum(range(1,101))**2

    print(y-x)

if __name__ == "__main__":
    main()