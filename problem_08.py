def find_prime_numbers(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return [num for num in range(n) if is_prime[num]]


def solve():
    """
    #11653

    소인수분해
    """
    num = int(input())

    if num < 2:
        return

    prime_numbers = find_prime_numbers(10_000_000)
    idx = 0
    while num != 1:
        prime_number = prime_numbers[idx]
        if num % prime_number == 0:
            print(prime_number)
            num //= prime_number
        else:
            idx += 1

def solve2():
    num = int(input())

    if num > 1:
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                print(divisor)
                num //= divisor
            else:
                divisor += 1

        if num > 1:
            print(num)



if __name__ == '__main__':
    solve()
