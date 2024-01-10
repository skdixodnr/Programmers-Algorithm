def solution(arr, n):
    
    answer = arr.copy()
    
    for i in range(len(answer)):
        if len(answer) % 2 == 1 and i % 2 == 0 :
            answer[i] += n
        elif len(answer) % 2 == 0 and i % 2 == 1 :
            answer[i] += n
    
    return answer