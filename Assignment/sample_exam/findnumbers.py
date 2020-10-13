def findnumbers(t_number,ls):
    sort_list = sorted(ls)
    i = 0
    res = []
    while t_number >= sort_list[i]:

        diff = t_number - sort_list[i]

        if diff in sort_list:
            res.append((sort_list[i],diff))
            sort_list.remove(diff)
            i = i + 1

        else:
            i = i+1
            return rest_number = 7

ls= [9,4,5,7,2]
findnumbers(t_number,ls)
