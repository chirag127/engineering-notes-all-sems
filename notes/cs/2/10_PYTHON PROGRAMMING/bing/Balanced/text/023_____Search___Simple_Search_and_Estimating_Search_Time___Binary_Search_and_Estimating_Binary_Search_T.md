### Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

- Searching algorithms are implemented to search for elements and retrieve their values from any data structure.
- Based on the search operation, searching algorithms can be classified into two categories:
  - Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.
  - Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: Binary Search, Jump Search, Interpolation Search.
- Simple Search or Linear Search is a method for finding an element within a list or array. It sequentially checks each element of the list until a match is found or the whole list has been searched.
- The time complexity of Linear Search is O(n), where n is the number of elements in the list. This means that the worst case scenario is that the algorithm has to check every element in the list to find the target or conclude that it is not present.
- Binary Search is a searching algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array; if they are unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful or the remaining half is empty.
- The time complexity of Binary Search is O(log n), where n is the number of elements in the array. This means that the algorithm divides the search space in half at each step, reducing the number of comparisons needed to find the target or conclude that it is not present.
- To implement Binary Search in Python, we need to use a recursive function that takes the sorted array, the target value, and the left and right indices as parameters. The base case is when the left index is greater than the right index, which means the target is not in the array. The recursive case is when the left index is less than or equal to the right index, which means the target may be in the array. In this case, we calculate the middle index and compare the value at that index with the target. If they are equal, we return the middle index. If the target is smaller than the value at the middle index, we call the function again with the right index as the middle index minus one. If the target is larger than the value at the middle index, we call the function again with the left index as the middle index plus one.
- Here is an example of Binary Search in Python:

```python
# Define a recursive function for binary search
def binary_search(array, target, left, right):
  # Base case: left index is greater than right index
  if left > right:
    return -1 # Target not found
  # Recursive case: left index is less than or equal to right index
  else:
    # Calculate the middle index
    middle = (left + right) // 2
    # Compare the value at the middle index with the target
    if array[middle] == target:
      return middle # Target found
    elif target < array[middle]:
      # Call the function again with the right index as the middle index minus one
      return binary_search(array, target, left, middle - 1)
    else:
      # Call the function again with the left index as the middle index plus one
      return binary_search(array, target, middle + 1, right)

# Test the function on a sorted array
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
result = binary_search(array, target, 0, len(array) - 1)
print(result) # Output: 6
```