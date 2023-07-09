def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif not stack or stack.pop() != '(':
                return False
    return len(stack) == 0