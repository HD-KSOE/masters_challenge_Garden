def solution(strings, n):
    answer = []
    arr = []
    for i in strings:
        a = i[n] + i
        arr.append(a)
    
    arr.sort()
    
    for i in arr:
        answer.append(i[1:])
    return answer