def solution(lottos, win_nums):
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    max_count, min_count = 0, 0
    for i in lottos:
        if i in win_nums:
            max_count += 1
            min_count += 1
        elif i == 0:
            max_count += 1
    return ranking[max_count], ranking[min_count]