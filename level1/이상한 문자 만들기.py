def solution(s):
    answer = ""
    string = s.split(" ")
    
    for s in string:
        for i in range(len(s)):
            if i % 2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
        answer += ' '
    return answer[:-1]