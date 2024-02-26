from helpers import IsPalindrome
def get_binary(n):
    return str(bin(n))[2::]

def main():
    sum = 0
    for num in range(1_000_000):
        if IsPalindrome(num) and IsPalindrome(get_binary(num)):            
            sum += num
    print(sum) 


if __name__ == "__main__":
    main()