def solution(array):
    answer1, answer2 = 0, 0
    count1, count2 = 0, 0
    set_array = set(array)
    set_array = list(set_array)
    for i in set_array:
        if array.count(i) > count1:
            answer1 = i
            count1 = array.count(i)
    set_array.remove(answer1)
    for j in set_array:
        if array.count(j) > count2:
            answer2 = j
            count2 = array.count(j)
    if count1 == count2 and answer1 != answer2:
        return -1
    return answer1