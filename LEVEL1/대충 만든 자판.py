def solution(keymap, targets):
    answer = []
    for i in targets:
        count = 0
        for j in i:
            index = []
            for k in keymap:
                if j in k:
                    index.append(k.index(j) + 1)
            if not index:
                count = -1
                break
            else:
                count += min(index)
        answer.append(count)
    if len(answer) != len(targets):
        return [-1]
    return answer