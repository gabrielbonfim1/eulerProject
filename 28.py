def main(n):
    sum = 1
    add = 2
    last_num = 1
    for _ in range(3, n+1,2):        
        start = last_num + add
        sum += 4*start + 6* add
        last_num = last_num + (4*add)
        add += 2        

    return sum

if __name__ == "__main__":
    print("sum:", main(1001))