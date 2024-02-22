def main():
    letterDict = {letter:value+1 for value,letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

    with open('./files/0022_names.txt', 'r') as f:
        names = f.read()
        names = names.replace('"','').split(',')
    
    names.sort()
    sum = 0
    for ind,name in enumerate(names):
        position = ind +1
        name_sum = 0
        for letter in name:
            name_sum += letterDict[letter]
        sum += name_sum * position
    
    print(sum)


if __name__ == "__main__":
    main()