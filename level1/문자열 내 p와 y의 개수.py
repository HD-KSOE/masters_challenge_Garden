def solution(s):
    answer = True
    cnt_p= 0
    cnt_y = 0
    for i in s.lower():
        if i == "p":
            cnt_p += 1
        elif i == "y":
            cnt_y += 1
    
    if cnt_p == cnt_y:
        answer = True
    elif cnt_p == 0 and cnt_y == 0:
        answer = True
    else:
        answer = False

    return answer