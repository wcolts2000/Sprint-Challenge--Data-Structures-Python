from searching import binary_search, binary_search_recursive
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:   # Starter Solution --> time to complete: 7.3630006313323975 seconds with 64 duplicates
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# make names_1 into a set to remove duplicates from on group
first_group = set(names_1)  # O(1)
# first_group_list = sorted(names_1)
# # # print(first_group)
# # # print(names_2)
# # # for name in first_group:  # Using a set and the built in list loop in the if shaves off 6 seconds -> time to complete 1.2062842845916748 seconds with 64 duplicates
# # #     if name in names_2:
# # #         duplicates.append(name)

# # # lets try both as sets
second_group = set(names_2)  # O(1)
print('firstgroup length: ', len(first_group),
      '\nsecondgroup length: ', len(second_group))
for name in first_group:  # O(n) # Using 2 set and the built in set loop in the if shaves off even more time -> time to complete 0.005980491638186594 seconds with 64 duplicates
    # O(1) ? as per https://wiki.python.org/moin/TimeComplexity this is also O(n)
    if name in second_group:
        duplicates.append(name)  # O(1)

# AS Lists
# first_group = list(names_1)
# for name in first_group:  # Using a list and the built in list loop in the if shaves off 6 seconds -> time to complete 1.1823148727416992 seconds with 64 duplicates
#     if name in names_2:
#         duplicates.append(name)

# lets try both as lists
# second_group = list(names_2)
# print('firstgroup length: ', len(first_group),
#       '\nsecondgroup length: ', len(second_group))
# for name in first_group:  # Using 2 lists and the built in lists loop in the if shaves off 6 seconds -> time to complete 1.2013013362884521 seconds with 64 duplicates
#     if name in second_group:
#         duplicates.append(name)

# for name in names_2:
#     if binary_search(first_group_list, name) >= 0:
#         duplicates.append(name)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
