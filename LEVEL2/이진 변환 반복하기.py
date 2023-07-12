def solution(s):
    count, remove_0 = 0, 0
    
    while s != '1':
        remove_0 += s.count('0')
        s = str(format(s.count('1'), 'b'))
        count += 1
    return count, remove_0