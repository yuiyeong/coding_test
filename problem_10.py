def f(num):
    total = num
    last_divisor = 1
    divisor = 2

    while divisor <= num:
        total += (divisor - last_divisor) * (num // divisor)
        last_divisor = divisor
        divisor *= 2

    return total

def solve():
    """
    #1407

    2 로 몇 번 나누어질까

    f(x) 는 x 의 모든 약수 중 2의 거듭제곱 꼴이면서 가장 큰 약수를 반환
    두 자연수 A, B(1 <= A <= B <= 10^15)
    f(A) + f(A + 1) +... + f(B - 1) + f(B) 를 구하시오.

    1   2   3   4   5   6   7   8   9   10
    1   1   1   1   1   1   1   1   1   1
        1       1       1       1       1
                2               2
                                4

    1 * 10
    + (2 - 1) * (10 // 2)
    + (4 - 2) * (10 // 4)
    + (8 - 4) * (10 // 8)
    """
    a, b = map(int, input().split())
    print(f(b) - f(a - 1))


def solve2():
    a, b = map(int, input().split())
    total = 0
    for n in range(a, b + 1):
        total += (n & -n)
    print(total)


if __name__ == '__main__':
    solve()