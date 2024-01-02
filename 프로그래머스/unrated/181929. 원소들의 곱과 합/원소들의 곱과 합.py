def solution(num_list):
    product = 1
    sum_of_elements = 0
    
    for num in num_list:
        product *= num
        sum_of_elements += num
    
    if product < sum_of_elements**2:
        return 1
    else:
        return 0