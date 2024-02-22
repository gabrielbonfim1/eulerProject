from itertools import permutations

def main():
    all_perms = permutations('0123456789')
    millionth = list(all_perms)[1_000_000 - 1]
    print("".join(millionth))


if __name__ == "__main__":
    main()