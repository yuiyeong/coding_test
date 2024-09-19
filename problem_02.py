def solve():
    """
    #14568

    2017 연세대학교 프로그래밍 경시대회 - 사탕 나누기
    """
    total_candy = int(input())

    count = 0

    for a in range(1, total_candy + 1):
        for b in range(1, total_candy + 1):
            for c in range(1, total_candy + 1):
                if a + b + c != total_candy:
                    continue

                if c >= b + 2 and a % 2 == 0:
                    count += 1
    print(count)

if __name__ == '__main__':
    solve()
