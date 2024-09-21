def solve():
    """
    #2247
    실질적 약수

    자연수 N 에 대해서 1 과 자기 자신을 제외한 약수를 실질적 약수라고 함
    그 실질적 약수들의 합을 SOD(Sum Of Divisor) 라고 하겠음
    CSOD(Cumulative SOD) 는 SOD 의 누적
    CSOD(n) 을 구하는 프로그램 작성하기

    1   2   3   4   5   6   7   8   9   10  11  12

        2       2       2       2       2       2
            3           3           3           3
                4               4               4
                    5                   5
                        6                       6
                            7
                                8
                                    9
                                        10
                                            11
                                                12
    """
    n = int(input())
    csod = 0

    i = 2
    while i <= n:
        quotient = n // i

        next_i = min(n // quotient + 1, n + 1)

        count = next_i - i

        csod += quotient * (i * count + (count * (count - 1) // 2))

        i = next_i

    print(csod % 1_000_000)


def solve2():
    # 시간 초과
    n = int(input())
    csod = 0
    for i in range(2, n + 1):
        multiples = (n // i) - 1  # 자기 자신 제외

        csod += i * multiples
    print(csod % 1_000_000)


def solve3():
    # 시간 초과
    n = int(input())
    csod = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            min_divisor = i
            max_divisor = n // i

            csod += sum(j * ((n // j) - 1) for j in range(min_divisor, max_divisor + 1))
            break
    print(csod % 1_000_000)


if __name__ == '__main__':
    # 100 -> 3150
    # 200_000_000 -> 837053

    solve()
