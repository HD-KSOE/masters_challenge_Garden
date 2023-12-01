def solution(n, m):
    a = 0
    b = 0
    for i in range(1, min(n,m)+1):
        if n % i == 0 and m % i == 0:
            a = i
            
    for j in range(max(n, m),n*m+1):
        if j % n == 0 and j % m == 0:
            b = j
            break
    result = list()
    result.append(a)
    result.append(b)
    return result