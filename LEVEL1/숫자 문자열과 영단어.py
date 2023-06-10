# 풀이 1(replace를 생각못함)
def solution(s):
    dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    answer = ''
    st = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            st += i
        if st in dic:
            answer += dic[st]
            st = ''
    return int(answer)

# 풀이 2
def solution(s):
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(words)):
        s = s.replace(words[i], str(i))
    return int(s)