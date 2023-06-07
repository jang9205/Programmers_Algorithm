def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        if max(i) > w:
            w = max(i)
        if min(i) > h:
            h = min(i)
    return w * h