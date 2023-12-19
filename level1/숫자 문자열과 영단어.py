def solution(s):
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    tmp = ''
    answer = []
    for i in s:
        if i.isalpha():
            tmp += i
            if tmp in arr:
                idx = arr.index(tmp)
                answer.append(str(idx))
                tmp = ''
        else:
            answer.append(i)
    return int(''.join(answer))