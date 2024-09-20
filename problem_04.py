def is_possible(possible_answer, hint_number, count_strike, count_ball):
    str_answer_num, str_guessing_num = str(possible_answer), str(hint_number)

    if len(set(str_answer_num)) != 3:  # 서로 다른 세 숫자가 아님
        return False

    if "0" in str_answer_num:  # 1 ~ 9 까지 숫자만 허용
        return False

    how_many_strike = sum(a == g for a, g in zip(str_answer_num, str_guessing_num))
    how_many_ball = sum(a in str_guessing_num for a in str_answer_num) - how_many_strike

    return count_strike == how_many_strike and count_ball == how_many_ball


def solve():
    """
    #2503

    숫자 야구
    """
num_of_hints = int(input())
hints = [list(map(int, input().split())) for _ in range(num_of_hints)]

min_number = 100
max_number = 999
how_many_possible = 0
for possible_number in range(min_number, max_number + 1):
    if all(is_possible(possible_number, hint[0], hint[1], hint[2]) for hint in hints):
        how_many_possible += 1
print(how_many_possible)


if __name__ == '__main__':
    solve()
