def solution(n, numlist):
    answer = []
    i = 0
    for i in range(len(numlist)):
        if numlist[i] % n == 0 :
            answer.append(numlist[i])
        i += 1
    
    return answer
    
    