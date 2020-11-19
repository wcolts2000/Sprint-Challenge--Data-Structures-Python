import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

bst = BinarySearchTree(names_1[0])  # O(1)
for num in range(1, len(names_1)):
    if names_1[num] is not None:
        bst.insert(names_1[num])
# print(type(names_1[num]))

print(bst.contains('Daphne Phillips'))
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

# first_group = set(names_1)  # O(1)
# second_group = set(names_2)  # O(1)
# print('firstgroup length: ', len(first_group),
#       '\nsecondgroup length: ', len(second_group))
# for name in first_group:  # O(n)
#     if name in second_group: # O(1) in a set
#         duplicates.append(name)  # O(1)

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


# def binary_search(arr, target): # Not correctly returning data, on;y produces 38 or 39 duplicates depending which list is sorted and searched

#     if len(arr) == 0:
#         return -1  # array empty

#     low = 0
#     high = len(arr)-1

#     # TO-DO: add missing code
#     while low < high:
#         mid = int((low+high)/2)
#         midpoint = arr[mid]
#         if midpoint == target:
#             return mid
#         elif midpoint > target:
#             high = mid - 1
#         else:
#             low = mid + 1

# return -1  # not found


# for name in names_1:
#     if binary_search(first_group_list, name) is not -1:
#         duplicates.append(name)
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
