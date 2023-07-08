def solution(s):
    answer = 0
    first = ''
    for i in range(len(s)):
        if first == '':
            first = s[i]
            first_count = 1
            other_count = 0
        elif s[i] == first:
            first_count += 1
        elif s[i] != first:
            other_count += 1
        if first_count == other_count:
            answer += 1
            first = ''
        elif first_count != other_count and i == len(s) - 1:
            answer += 1
    return answer