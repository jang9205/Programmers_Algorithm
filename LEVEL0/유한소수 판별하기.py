from fractions import Fraction

def solution(a, b):
    fr = Fraction(a, b)
    b = fr.denominator
    for i in range (2, b+1):
        count = 0
        if b % i == 0:
            for j in range (2, i):
                if i % j == 0:
                    count += 1
            if count == 0 and not (i == 2 or i == 5):
                return 2
    return 1