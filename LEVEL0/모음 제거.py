def solution(my_string):
    for num in ['a','e','i','o','u']:
        my_string = my_string.replace(num, '')
    return my_string