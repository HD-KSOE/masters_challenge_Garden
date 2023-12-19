def yaksu(n):
    cnt = 1
    for i in range(1, n//2+1):
        if n % i == 0:
            cnt+=1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if(yaksu(i) % 2 == 0):
            answer += i
        else:
            answer -= i
    return answer