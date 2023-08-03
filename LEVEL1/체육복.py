def solution(n, lost, reserve):
    lost1 = set(lost) - set(reserve)
    reserve1 = set(reserve) - set(lost)
    for i in lost1:
        if i - 1 in reserve1:
            reserve1.remove(i - 1)
        elif i + 1 in reserve1:
            reserve1.remove(i + 1)
        else:
            n -= 1
    return n