def solution(n):
    m = n
    bin_n = str(format(n, 'b'))
    while True:
        m += 1
        bin_m = str(format(m, 'b'))
        if bin_n.count('1') == bin_m.count('1'):
            return m