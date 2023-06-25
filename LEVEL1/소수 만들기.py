def solution(nums):
    answer, add = 0, 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                add = nums[i] + nums[j] + nums[k]
                count = 0
                for l in range(2, add):
                    if add % l == 0:
                        count += 1
                if count == 0:
                    answer += 1
    return answer