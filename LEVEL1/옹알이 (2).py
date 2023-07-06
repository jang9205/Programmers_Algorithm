def solution(babbling):
    count = 0
    a = ''
    for i in babbling:
        a = i
        if 'aya' in a:
            a = a.replace('aya','1')
        if 'ye' in a:
            a = a.replace('ye','2')
        if 'woo' in a:
            a = a.replace('woo','3')
        if 'ma' in a:
            a = a.replace('ma','4')
        if a.isdigit() and not '11' in a and not '22' in a and not '33' in a and not '44' in a:
            count += 1
    return count