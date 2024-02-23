def main():
    coins = [2,5,10,20,50,100,200]
    ways = list([1 for i in range(201)])

    for coin in coins:
        for x in range(coin,201):
            ways[x] = ways[x] + ways[x-coin]

    print(ways[-1]) 


if __name__ == "__main__":
    main()