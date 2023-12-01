import math

def solution(n):
    
    result = math.sqrt(n)
    result2 = round(result)
    if result2*result2 == n:
        return 1
    else:
        return 2