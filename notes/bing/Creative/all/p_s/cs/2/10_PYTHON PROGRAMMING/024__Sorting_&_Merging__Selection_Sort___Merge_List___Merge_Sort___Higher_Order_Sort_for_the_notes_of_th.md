### Sorting & Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

Sorting and merging are two common operations on lists that can be implemented using different algorithms. In this section, we will discuss four of them: selection sort, merge list, merge sort, and higher order sort.

#### Selection Sort

Selection sort is a simple sorting algorithm that works by repeatedly finding the smallest element in the unsorted part of the list and moving it to the sorted part. The algorithm can be implemented as follows:

- Initialize an empty list to store the sorted elements.
- Loop over the original list until it is empty.
- Find the smallest element in the original list and remove it.
- Append the smallest element to the sorted list.
- Return the sorted list.

The following is an example of selection sort in Python:

```python
def selection_sort(lst):
  # Initialize an empty list to store the sorted elements
  sorted_lst = []
  # Loop over the original list until it is empty
  while lst:
    # Find the smallest element in the original list and remove it
    smallest = min(lst)
    lst.remove(smallest)
    # Append the smallest element to the sorted list
    sorted_lst.append(smallest)
  # Return the sorted list
  return sorted_lst
```

The time complexity of selection sort is O(n^2), where n is the length of the list, because it needs to loop over the list n times and find the minimum element in each iteration. The space complexity is O(n), because it needs to create a new list to store the sorted elements.

Some advantages of selection sort are:

- It is easy to implement and understand.
- It does not require any extra space apart from the output list.
- It performs well on small lists.

Some disadvantages of selection sort are:

- It is inefficient on large lists, because it has a quadratic time complexity.
- It is not stable, meaning that it does not preserve the relative order of equal elements.

#### Merge List

Merge list is an operation that takes two sorted lists and merges them into one sorted list. The algorithm can be implemented as follows:

- Initialize an empty list to store the merged elements.
- Initialize two pointers, one for each input list, to track the current element to be compared.
- Loop until both input lists are exhausted.
- Compare the current elements of the two input lists and append the smaller one to the merged list.
- Increment the pointer of the list that provided the smaller element.
- If one of the input lists is exhausted, append the remaining elements of the other list to the merged list.
- Return the merged list.

The following is an example of merge list in Python:

```python
def merge_list(lst1, lst2):
  # Initialize an empty list to store the merged elements
  merged_lst = []
  # Initialize two pointers, one for each input list, to track the current element to be compared
  i = 0 # Pointer for lst1
  j = 0 # Pointer for lst2
  # Loop until both input lists are exhausted
  while i < len(lst1) and j < len(lst2):
    # Compare the current elements of the two input lists and append the smaller one to the merged list
    if lst1[i] < lst2[j]:
      merged_lst.append(lst1[i])
      # Increment the pointer of the list that provided the smaller element
      i += 1
    else:
      merged_lst.append(lst2[j])
      # Increment the pointer of the list that provided the smaller element
      j += 1
  # If one of the input lists is exhausted, append the remaining elements of the other list to the merged list
  if i < len(lst1):
    merged_lst.extend(lst1[i:])
  if j < len(lst2):
    merged_lst.extend(lst2[j:])
  # Return the merged list
  return merged_lst
```

The time complexity of merge list is O(n), where n is the total number of elements in the two input lists, because it needs to loop over the elements once and compare them. The space complexity is O(n), because it needs to create a new list to store the merged elements.

Some advantages of merge list are:

- It is efficient, because it has a linear time complexity.
- It is stable, meaning that it preserves the relative order of equal elements.

Some disadvantages of merge list are:

- It requires extra space to store the output list.
- It only works on sorted input lists.

#### Merge Sort

Merge sort is a recursive sorting algorithm that works by dividing the list into smaller sublists, sorting them using merge list, and then merging them back into one sorted list. The algorithm can be implemented as follows:

- Base case

- If the list has zero or one element, return the list as it is already sorted.
- Recursive case
- Divide the list into two roughly equal halves.
- Sort the left half recursively using merge sort.
- Sort the right half recursively using merge sort.
- Merge the two sorted halves using merge list.
- Return the merged list.

The following is an example of merge sort in Python:

```python
def merge_sort(lst):
  # Base case: if the list has zero or one element, return the list as it is already sorted
  if len(lst) <= 1:
    return lst
  # Recursive case: divide the list into two roughly equal halves
  mid = len(lst) // 2
  left = lst[:mid]
  right = lst[mid:]
  # Sort the left half recursively using merge sort
  left = merge_sort(left)
  # Sort the right half recursively using merge sort
  right = merge_sort(right)
  # Merge the two sorted halves using merge list
  lst = merge_list(left, right)
  # Return the merged list
  return lst
```

The time complexity of merge sort is O(n log n), where n is the length of the list, because it needs to divide the list into log n levels and sort each level in O(n) time. The space complexity is O(n), because it needs to create new lists for each level of recursion.

Some advantages of merge sort are:

- It is efficient, because it has a logarithmic time complexity.
- It is stable, meaning that it preserves the relative order of equal elements.
- It can handle large lists, because it does not depend on the available memory.

Some disadvantages of merge sort are:

- It requires extra space to store the intermediate lists.
- It is not adaptive, meaning that it does not take advantage of the existing order in the list.

#### Higher Order Sort

Higher order sort is a sorting algorithm that uses a higher order function, such as a lambda function or a key function, to customize the sorting criteria. The algorithm can be implemented as follows:

- Define a higher order function that takes an element of the list and returns a value that can be compared.
- Use the built-in sorted function or the list.sort method to sort the list based on the higher order function.

The following is an example of higher order sort in Python:

```python
# Define a higher order function that takes a string and returns its length
def length(s):
  return len(s)

# Use the sorted function to sort a list of strings based on their length
lst = ["apple", "banana", "cherry", "date", "elderberry"]
lst = sorted(lst, key=length)
print(lst) # ['date', 'apple', 'banana', 'cherry', 'elderberry']

# Define a lambda function that takes a tuple and returns its second element
key = lambda x: x[1]

# Use the list.sort method to sort a list of tuples based on their second element
lst = [(1, 4), (2, 3), (3, 2), (4, 1)]
lst.sort(key=key)
print(lst) # [(4, 1), (3, 2), (2, 3), (1, 4)]
```

The time complexity of higher order sort depends on the underlying sorting algorithm used by the sorted function or the list.sort method, which is usually O(n log n), where n is the length of the list. The space complexity also depends on the underlying sorting algorithm, which is usually O(n) or O(1), depending on whether it is a stable sort or not.

Some advantages of higher order sort are:

- It is flexible, because it allows the user to define the sorting criteria based on their needs.
- It is concise, because it uses a higher order function to express the sorting criteria.

Some disadvantages of higher order sort are:

- It may be slower, because it needs to call the higher order function for each element of the list.
- It may be less readable, because it uses a lambda function or a key function that may not be clear to the reader.

Some mnemonics and learning tricks for the topic are:

- To remember the steps of selection sort, think of the acronym S.A.M.E: Smallest, Append, Move, End.
- To remember the steps of merge list, think of the acronym C.A.M.E.R.A: Compare, Append, Move, Exhaust, Remain, Append.
- To remember the steps of merge sort, think of the acronym D.R.E.A.M: Divide, Recur, End, Merge.
- To remember the difference between merge list and merge sort, think of the words list and sort. List means two