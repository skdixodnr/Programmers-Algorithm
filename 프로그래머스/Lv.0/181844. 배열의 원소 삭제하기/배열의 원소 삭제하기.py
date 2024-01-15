def solution(arr, delete_list):
    answer = []
    
    arr1 = arr.copy()
    
    for i in arr1 :
        if i not in delete_list:
            answer.append(i)
    
    
    return answer