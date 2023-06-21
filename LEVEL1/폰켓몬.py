def solution(nums):
    pick = len(nums) / 2
    count = len(set(nums))
    if count >= pick:
        return pick
    else:
        return count