def solution(x):
    sum_tmp = 0
    for i in str(x): sum_tmp += int(i)
    
    if x % sum_tmp != 0:
        return False
    return True