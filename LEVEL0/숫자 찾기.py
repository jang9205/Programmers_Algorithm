def solution(num, k):
    st = str(num)
    if st.find(str(k)) == -1:
        return -1
    return st.find(str(k)) + 1