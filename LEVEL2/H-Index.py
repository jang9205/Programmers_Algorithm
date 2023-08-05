def solution(citations):
    h = 1
    answer = 0
    while True:
        count = 0
        for i in citations:
            if i >= h:
                count += 1
        if count >= h and len(citations) - count <= h:
            answer = h
        else:
            return answer
        h += 1