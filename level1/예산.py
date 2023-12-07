def solution(d, budget):
    d.sort()
    d_sum = 0
    answer = 0
    
    for i in d:
        if d_sum + i <= budget:
            d_sum += i
            answer += 1
        else:
            break
    
    return answer