def solution(babbling):
    count = 0
    a = ''
    for i in babbling:
        a = i
        if 'aya' in a:
            a = a.replace('aya',' ')
        if 'ye' in a:
            a = a.replace('ye',' ')
        if 'woo' in a:
            a = a.replace('woo',' ')
        if 'ma' in a:
            a = a.replace('ma',' ')
        a = a.strip()
        if a == '':
            count += 1
    return count