def solution(num_list):
    list1 = []
    list2 = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            list1.append(str(num_list[i]))
        else :
            list2.append(str(num_list[i]))
    return int(''.join(list1)) + int(''.join(list2))