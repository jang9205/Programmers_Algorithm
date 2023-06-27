def solution(cards1, cards2, goal):
    index1, index2 = [], []
    for i in goal:
        if i in cards1:
            index1.append(cards1.index(i))
        else:
            index2.append(cards2.index(i))
    if index1 != sorted(index1) or index2 != sorted(index2):
        return 'No'
    for j in range(len(index1)):
        if j not in index1:
            return 'No'
    return 'Yes'