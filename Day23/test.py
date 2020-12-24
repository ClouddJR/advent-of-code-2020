import time

test_set = set(list(range(1,10000000)))
test_list = list(range(1,1000000))
dd = {i: True for i in test_list}

start = time.time()
print(5000000 in test_set)
end = time.time()
print(f"time for set: {end-start} seconds")

start = time.time()
print(5000000 in test_list)
end = time.time()
print(f"time for list: {end-start} seconds")

start = time.time()
print(5000000 in dd)
end = time.time()
print(f"time for dict: {end-start} seconds")

start = time.time()
for i in dd:
    dd[i] = True
end = time.time()
print(f"time for loop: {end-start} seconds")