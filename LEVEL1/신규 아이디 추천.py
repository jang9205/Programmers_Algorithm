def solution(new_id):
    char = ['-', '_', '.']
    answer = ''
    
    new_id = new_id.lower()
    
    for i in new_id:
        if i.isalpha() or i in char or i.isdigit():
            answer += i
    
    while True:
        if '..' in answer:
            answer = answer.replace('..', '.')
        else:
            break
            
    if answer[0] == '.':
        answer = answer[1:]
    if answer == '':
        answer = 'a'
    if answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
        
    while True:
        if len(answer) <= 2:
            answer += answer[-1]
        else:
            break
    return answer