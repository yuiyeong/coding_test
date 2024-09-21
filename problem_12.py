def solve():
    """
    #2559
    수열

    누적합을 모두 구한 뒤 본 문제를 푼다.
    """
    days, num_continuous = map(int, input().split())
    sequences = list(map(int, input().split()))

    cumulative = [0] * (days + 1)
    for i in range(days):
        cumulative[i + 1] = cumulative[i] + sequences[i]

    sum_sub_seqs = []
    for i in range(num_continuous, days + 1):
        sum_sub_seqs.append(cumulative[i] - cumulative[i - num_continuous])

    print(max(sum_sub_seqs))

if __name__ == '__main__':
    solve()
