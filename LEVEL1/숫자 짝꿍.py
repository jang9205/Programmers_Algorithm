def solution(X, Y):
    partner = ''
    for i in range(0,10):
        partner += str(i) * min(X.count(str(i)), Y.count(str(i)))
    if partner == '':
        return '-1'
    elif partner[-1] == '0':
        return '0'
    else:
        return ''.join(sorted(partner, reverse = True))