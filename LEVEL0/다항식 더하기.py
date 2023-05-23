def solution(polynomial):
    a, b = 0, 0
    poly = polynomial.split()
    for i in poly:
        if i == '+':
            continue
        elif i == 'x':
            a += 1
        elif 'x' in i:
            a += int(i[:-1])
        else:
            b += int(i)
    if a == 1:
        a = 'x'
    else:
        a = str(a) + 'x'
    if a == '0x':
        return str(b)
    elif b == 0:
        return str(a)
    else:
        return str(a) + ' + ' + str(b)