def solve():
    """
    #19532
    수학은 비대면강의입니다.
    """
    a, b, c, d, e, f = map(int, input().split())

    min_number = -999
    max_number = 999
    for x in range(min_number, max_number + 1):
        for y in range(min_number, max_number + 1):
            if (a*x + b*y) == c and (d*x + e*y) == f:
                return x, y

if __name__ == '__main__':
    print(*solve())