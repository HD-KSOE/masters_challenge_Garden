def solution(dartResult):
    answer = []
    tmp = ["","S","D","T","*","#"]
    cnt = 0
    num = ""
    for i in range(len(dartResult)):
        if dartResult[i].isnumeric():
            num += dartResult[i]
        else:
            if dartResult[i] in ["S","D","T"]:
                num = pow(int(num), tmp.index(dartResult[i]))
                answer.append(num)
                print(num)
                num = ""
                cnt += 1
            elif dartResult[i] == "#":
                answer[cnt-1] *= -1
            else:
                if len(answer) >= 2:
                    answer[cnt-1] *= 2
                    answer[cnt-2] *= 2
                else:
                    answer[cnt-1] *= 2
    return sum(answer)