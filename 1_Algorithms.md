# Algorithms

## Multiplication

## Insertion Sort

```Python
sort_list = [3, 5, 2, 1, 4]
for i in range(1, 5):
    while i > 0 and sort_list[i] < sort_list[i-1]:
        sort_list[i-1], sort_list[i] = sort_list[i], sort_list[i-1]
        i -= 1
```

## Merge Sort

```Python
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
```

## Analysis of Algorithms

A “fast algorithm” is an algorithm whose worst-case running time grows slowly with the input size. For almost all of problems we’ll discuss, the holy grail is a linear-time algorithm, meaning an algorithm with running time proportional to the input size.

Asymptotic notation suppresses constant factors and lower-order terms. 

For example, the upper bound on its running time of merge sort is:

$$
6n \log_2 n+6n
$$

primitive operations, where n is the length of the input array. The lower-order term here is the $6n$, as $n$ grows more slowly than $n \log_2 n$, it will be suppressed in asymptotic notation. The leading constant factor of $6$ also gets suppressed, leaving us with the much simpler expression of $n \log n$. We would then say that the running time of merge sort is $O(n \log n)$

### Big-O Notation

$T(n)=O(f(n))$ if and only if there exist positive constants $c$ and $n_0$ such that

$$
T(n) \leq c \cdot f(n)
$$

for all $n \geq n_0$.

### Big-Omega Notation

$T(n)=\Omega(f(n))$ if and only if there exist positive constants $c$ and $n_0$ such that

$$
T(n) \geq c \cdot f(n)
$$

for all $n \geq n_0$.

### Big-Theta Notation
$T(n)=\Theta(f(n))$ if and only if there exist positive constants $c_1$, $c_2$ and $n_0$ such that

$$
c_1 \cdot f(n) \leq  T(n) \leq c_2 \cdot f(n)
$$

for all $n \geq n_0$.

### Little-O Notation
If big-O notation is analogous to “less than or equal to,” little-o notation is analogous to “strictly less than.” $T(n)=O(f(n))$ if and only if for every positive constant $c > 0$, there exists a choice of $n_0$ such that

$$
T(n) \leq c \cdot f(n)
$$

for all $n \geq n_0$.
