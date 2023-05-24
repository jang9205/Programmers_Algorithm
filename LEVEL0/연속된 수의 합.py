def solution(num, total):
    answer = []
    hap = 0
    count = 0
    for i in range (1, num + 1):
        hap += i
    while hap != total:
        if hap < total:
            hap += num
            count += 1
        elif hap > total:
            hap -= num
            count -= 1
    for i in range (1, num + 1):
        answer.append(i + count)
    return answer