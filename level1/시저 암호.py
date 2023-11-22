def solution(s, n):
    answer = ''
    s = list(s)
    for i in s:
        if i.isalpha():
            tmp = ord(i) + n
            if tmp > ord('z'):
                tmp -= 26
            elif ord('A') <= ord(i) <= ord('Z') and tmp > ord('Z'):
                tmp -= 26
            answer += chr(tmp)
        else:
            answer += i
    return answer