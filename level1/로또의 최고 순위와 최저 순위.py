def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    answer = []    
    z_cnt = lottos.count(0)
    s_cnt = 0
    for i in set(lottos):
        for j in set(win_nums):
            if i == j:
                s_cnt += 1
                
    high = z_cnt + s_cnt
    low = s_cnt
    
    
    answer.append(rank[high])
    answer.append(rank[low])
    return answer