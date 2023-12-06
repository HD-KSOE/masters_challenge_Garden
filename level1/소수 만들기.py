from itertools import combinations

def sosu(n):
    ans = True
    for i in range(2,n//2 + 1):
        if n % i == 0:
            ans = False
            break
    return ans

def solution(nums):
    answer = 0
    for i in combinations(nums,3):
        if(sosu(sum(i))):
            answer += 1

    return answer