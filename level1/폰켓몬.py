def solution(nums):
    answer = 0
    n = len(nums)//2
    nums_set = len(set(nums))
    
    if n > nums_set:
        answer = nums_set
    else:
        answer = n
    return answer