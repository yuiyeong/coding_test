def find_prime_numbers(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i,n, i):
                is_prime[j] = False

    return [num for num in range(n) if is_prime[num]]

def solve():
    """
    #1978

    소수 찾기
    """
    _ = int(input())
    numbers = set(map(int, input().split()))
    prime_numbers = set(find_prime_numbers(1000))
    print(len(numbers.intersection(prime_numbers)))


if __name__ == '__main__':
    solve()