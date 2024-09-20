def solve():
    """
    #14232
    보석 도둑

    보석 무게는 2 이상

    총 들고 올 수 있는 보석 무게 = 모든 보석의 곱

    보석의 개수를 최대로 많이 가져오고 싶다면?

    """
    k = int(input())
    jewels = []
    divisor = 2
    while divisor * divisor <= k:
        if k % divisor == 0:
            jewels.append(divisor)
            k //= divisor
        else:
            divisor += 1

    if k > 1:
        jewels.append(k)
    print(len(jewels))
    print(" ".join(map(str, jewels)))


if __name__ == '__main__':
    solve()
