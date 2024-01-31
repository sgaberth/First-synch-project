import time

# =============================================================================
# start = time.time()
# list_1 = []
# for i in range(10) :
#     list_1.append(i**2)
#     
# print(list_1)
# end = time.time()
# print(end - start)
# 
# 
# 
# list_2 = [i**2 for i in range(10)]
# print(list_2)
# =============================================================================
start = time.time()
list_1 = []
for i in range(1000000) :
    list_1.append(i**2)
end = time.time()
print(end - start)

# Liste comprehension
start = time.time()
list_2 = [i**2 for i in range(1000000)]
end = time.time()
print(end - start)


