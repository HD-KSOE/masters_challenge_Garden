def solution(arr):
    answer = []
    tmp = arr[0]
    for i in range(1,len(arr)):
        if arr[i] == tmp:
            continue
        else:
            answer.append(tmp)
            tmp = arr[i]
    answer.append(arr[-1])
    return answer