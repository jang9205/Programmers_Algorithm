# 첫 번째 풀이
def solution(order):
    st = str(order)
    count = 0
    for i in st:
        if int(i) == 3 or int(i) == 6 or int(i) == 9:
            count += 1
    return count

# 두 번째 풀이
def solution(order):
    st = str(order)
    return st.count('3') + st.count('6') + st.count('9')