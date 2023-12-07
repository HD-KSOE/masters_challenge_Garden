def solution(participant, completion):
    participant.sort()
    completion.sort()
    tmp = [participant[:len(completion)], completion]
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]