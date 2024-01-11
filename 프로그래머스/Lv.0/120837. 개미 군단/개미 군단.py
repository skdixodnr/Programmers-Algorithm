def solution(hp):
    answer = 0
    
    a = hp // 5
    b = hp % 5
    if b > 3 :
        b = b // 3
        c = b % 3
        answer += (a + b + c)
    elif b == 3 :
        answer += (a + 1)
    elif b < 3 :
        answer += (a + b)
    
    return answer