def solution(numbers):
    li = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range (10):
        numbers = numbers.replace(li[i],str(i))
    return int(numbers)