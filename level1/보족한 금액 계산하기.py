def solution(price, money, count):
    m_sum = 0
    for i in range(1, count + 1):
        m_sum += i * price;
    if m_sum - money > 0:
        return m_sum - money
    else:
        return 0