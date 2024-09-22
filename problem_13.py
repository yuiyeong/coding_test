def solve():
    """
    #1912
    연속합
    수열에서 연속된 숫자의 합이 제일 클 때의 부분 수열 합

    1 ≤ n ≤ 100,000
    -1_000 < 수 < 1_000
    """
    num_count = int(input())
    sequence = list(map(int, input().split()))

    cumulative = [-1001] * (num_count + 1)
    for i in range(num_count):
        cumulative[i + 1] = max(cumulative[i] + sequence[i], sequence[i])

    print(max(cumulative))


if __name__ == '__main__':
    solve()
