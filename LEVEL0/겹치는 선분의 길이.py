def solution(lines):
    l1, l2, l3 = [], [], []
    count = 0
    for i in range(lines[0][0],lines[0][1]):
        l1.append(i)
    for j in range(lines[1][0],lines[1][1]):
        l2.append(j)
    for k in range(lines[2][0],lines[2][1]):
        l3.append(k)
    for l in l1:
        if l in l2:
            count += 1
        elif l in l3:
            count += 1
    for m in l2:
        if m in l3 and not m in l1:
            count += 1
    return count