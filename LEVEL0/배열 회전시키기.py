def solution(numbers, direction):
    if direction == 'left':
        numbers.append(numbers[0])
        return numbers[1:]
    else:
        numbers.insert(0, numbers[-1])
        return numbers[:-1]