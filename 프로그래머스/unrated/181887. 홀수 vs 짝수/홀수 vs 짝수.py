def solution(num_list):
    odd_list = num_list[::2]
    even_list = num_list[1::2]
    if sum(odd_list) >= sum(even_list):
        return sum(odd_list)
    else:
        return sum(even_list)