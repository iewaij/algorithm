"""
Common Element

Explaination: We first determine which row has the smallest last element, we call this row smallest row. Then we determine whether each element in the row with smallest last element has appeared in every other row without comaparing the values that are lager than the last and largest element in the smallest row. Because the row is sorted in a strictly increasing order, the first common element is also the smallest. Therefore, we return the first common element. If there is no such value found, return -1.

Time Complexity: In the worst case, every row has the same last element. Assume the matrix has y rows and x columns. Sorting takes ylog(y) operations and we assume it is very small and can be ignored. After sorting, x elements in the first row need to determine whether they are in other y-1 rows. That is x(y-1) operations. The total number of values is n=xy. Therefore the number of operations n-n/y. Using the Big-O notation, the complexity is O(n). 
"""


def common_element(mat):
    common_list = []
    mat = sorted(mat, key=lambda x: x[-1])
    largest_element = mat[0][-1]
    for i in mat[0]:
        i_common = True
        for j in mat[1:]:
            j_truncate = [t for t in j if t <= largest_element]
            if i not in j_truncate:
                i_common = False
                break
        if i_common:
            return i
    return -1
