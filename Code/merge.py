def reduce(left_list, right_list):
    left_i = 0
    right_i = 0
    result_i = 0
    result_list = []
    while left_i < len(left_list) and right_i < len(right_list):
        if left_list[left_i] < right_list[right_i]:
            result_list.append(left_list[left_i])
            left_i += 1
        else:
            result_list.append(right_list[right_i])
            right_i += 1
        result_i += 1
    result_list.extend(left_list[left_i:])
    result_list.extend(right_list[right_i:])
    return result_list

def merge_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    else:
        n= len(sort_list)
        n_mid= n // 2
        left_list = sort_list[: n_mid]
        left_list = merge_sort(left_list)
        right_list = sort_list[n_mid: ]
        right_list = merge_sort(right_list)
        result_list= reduce(left_list, right_list)
        return result_list

result_list= merge_sort([7, 1, 9, 6, 8, 4, 3])
print(result_list)
