from itertools import product
from helpers import IsPalindrome
def main():
    mx = 0
    for pair in product(range(100,1000),range(100,1000)):
        if IsPalindrome(pair[0]*pair[1]):
            mx = max(mx, pair[0]*pair[1])
    print(mx)


if __name__ == "__main__":
    main()