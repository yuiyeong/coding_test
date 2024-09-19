def solve():
    """
    #1816

    암호 키
    """
    # 1_000_000 보다 작은 소수로 나눠지는 수 라면 valid 하지 않다.
    criterion = 1_000_000

    is_prime = [True] * (criterion + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(criterion ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, criterion + 1, i):
                is_prime[j] = False
    prime_numbers = [i for i in range(2, criterion + 1) if is_prime[i]]

    n = int(input())
    for _ in range(n):
        number = int(input())
        is_valid = "YES"
        for prime_number in prime_numbers:
            if number % prime_number == 0:
                is_valid = "NO"
                break
        print(is_valid)

if __name__ == "__main__":
    solve()
