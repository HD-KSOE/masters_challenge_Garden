def solution(s):
    monja = {}
    answer = []
    for i in range(len(s)):
        if s[i] not in monja:
            answer.append(-1)
        else:
            answer.append(i - monja[s[i]])
        monja[s[i]] = i
            
    return answer