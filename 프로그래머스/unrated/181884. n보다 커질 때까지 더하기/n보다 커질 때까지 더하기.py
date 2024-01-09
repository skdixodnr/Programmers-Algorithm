def solution(numbers, n):
    
    i = 0
    sum = 0
    
    while sum <= n :
        sum += numbers[i]
        i += 1
    
    return sum