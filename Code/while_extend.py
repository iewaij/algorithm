import time

list_left = list(range(100000))
list_right = list(range(100000))

start = time.time()
list_left.extend(list_right)
end = time.time()
print("Extend costs:", end - start, "seconds.")

start = time.time()
for i in range(100000):
    list_right.append(i)
end = time.time()
print("While costs:", end - start, "seconds.")
