Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

- Constant # O(1) Time Complexity as values are being directly accessed, not iterated through

2. What is the space complexity of your ring buffer's `append` function?

- Constant # O(1) Space Complexity as nothing is happening but reassignment

3. What is the runtime complexity of your ring buffer's `get` method?

- Linear # O(n) as it loops through each value in n checking if it is None, could be further optimized to break the loop when it hits a None value

4. What is the space complexity of your ring buffer's `get` method?

- Up to Linear # O(n) worst case because a new array is being created with all the present elements, best case would be a get called when the storage is empty and the new array is empty

5. What is the runtime complexity of the provided code in `names.py`?

- The provided solution was on the order of O(n^2) as it contained a nested for loop in it. because the 2 lists start at the same length we can keep it at just looking at n and not add in a second m factor I think
- UPDATE as per https://wiki.python.org/moin/TimeComplexity, the runtime of `x in s` is also O(n), so the provided solution is O(n^3)?

6. What is the space complexity of the provided code in `names.py`?

- The provided solution was on the order of O(n) Space Complexity with n being the number of duplicates between the 2 lists

7. What is the runtime complexity of your optimized code in `names.py`?

- optimized solution is on the order of O(n) as i have a single loop going through the first list. All other comparisons are done in Constant time (not sure of the time complexity of built in if loop when seeing if the name is in there, but it is faster than any loop we code)
- UPDATE as per https://wiki.python.org/moin/TimeComplexity, the runtime of `x in s` is also O(n), so the optimized solution is O(n^2)?

8. What is the space complexity of your optimized code in `names.py`?

- Optimized Space complexity is still on the order of O(n) with n being the number of duplicates present
