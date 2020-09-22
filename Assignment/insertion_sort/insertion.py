sort_list = [3, 5, 2, 1, 4]
for i in range(1, 5):
    while i > 0 and sort_list[i] < sort_list[i-1]:
        sort_list[i-1], sort_list[i] = sort_list[i], sort_list[i-1]
        i -= 1
