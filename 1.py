def main(below):
    sum = 0
    for x in range (3,below):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    print(sum)
    return sum

if __name__ == "__main__":
    below = 1_000
    main(below)