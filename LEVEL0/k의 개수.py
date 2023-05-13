def solution(i, j, k):
    st = ''
    for l in range(i,j+1):
        st += str(l)
    return st.count(str(k))