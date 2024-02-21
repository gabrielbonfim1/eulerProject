def main(below):
    sum = 0
    x0,x1 = 1,1
    while x0+x1 < below:
        x0,x1 = x1, x0+x1
        if x1 %2 == 0:
            sum+=x1
    print(sum)
    return(sum)




if __name__ == "__main__":
    below = 4_000_000
    main(below)