### Search: Simple Search and Estimating Search Time, Binary Search and Estimating Binary Search Time

- Search is a process of finding a specific item or value in a collection of items or values.
- Search algorithms are methods or procedures that can perform search efficiently and effectively.
- Two common types of search algorithms are simple search and binary search.

#### Simple Search

- Simple search, also known as linear search or sequential search, is a search algorithm that checks each item in a collection one by one until it finds the target item or reaches the end of the collection.
- Simple search can be implemented using a loop or a recursion.
- Simple search works on any type of collection, whether it is sorted or unsorted, and does not require any prior knowledge about the collection.
- The pseudocode for simple search is as follows:

```
# Assume collection is a list of items and target is the item to be searched
# Return the index of target in collection, or -1 if not found

def simple_search(collection, target):
  # Loop through each item in collection
  for i in range(len(collection)):
    # If the current item is equal to target, return its index
    if collection[i] == target:
      return i
  # If the loop ends without finding target, return -1
  return -1
```

- The Python code for simple search is similar to the pseudocode, except that we can use the `in` operator to check if target is in collection, and the `index` method to get its index.

```
# Assume collection is a list of items and target is the item to be searched
# Return the index of target in collection, or -1 if not found

def simple_search(collection, target):
  # Check if target is in collection
  if target in collection:
    # Return its index using index method
    return collection.index(target)
  # If target is not in collection, return -1
  else:
    return -1
```

#### Estimating Search Time for Simple Search

- The search time for simple search depends on the size of the collection and the position of the target item in the collection.
- The best case scenario for simple search is when the target item is the first item in the collection, in which case the search time is constant, or O(1).
- The worst case scenario for simple search is when the target item is the last item in the collection, or not in the collection at all, in which case the search time is linear, or O(n), where n is the number of items in the collection.
- The average case scenario for simple search is when the target item is somewhere in the middle of the collection, in which case the search time is also linear, or O(n), but with a smaller constant factor than the worst case.
- Therefore, the overall search time for simple search is O(n), which means that it grows proportionally to the size of the collection.

#### Binary Search

- Binary search, also known as logarithmic search or half-interval search, is a search algorithm that divides the collection into two halves and compares the target item with the middle item of the collection.
- Binary search can only work on a sorted collection, and requires prior knowledge about the order of the collection.
- Binary search can be implemented using a loop or a recursion.
- The pseudocode for binary search is as follows:

```
# Assume collection is a sorted list of items and target is the item to be searched
# Return the index of target in collection, or -1 if not found

def binary_search(collection, target):
  # Initialize the left and right boundaries of the search range
  left = 0
  right = len(collection) - 1
  # Loop until the search range is empty
  while left <= right:
    # Find the middle index of the search range
    middle = (left + right) // 2
    # Compare the target with the middle item of the collection
    if target == collection[middle]:
      # If they are equal, return the middle index
      return middle
    elif target < collection[middle]:
      # If the target is smaller, narrow the search range to the left half
      right = middle - 1
    else:
      # If the target is larger, narrow the search range to the right half
      left = middle + 1
  # If the loop ends without finding target, return -1
  return -1
```

- The Python code for binary search is similar to the pseudocode, except that we can use the `bisect` module to perform binary search more efficiently.

```
# Assume collection is a sorted list of items and target is the item

OK, I will try to include some mnemonics and learning tricks for the topic, but only if they are easy to remember. Here is the rest of the content:

```
# to be searched
# Return the index of target in collection, or -1 if not found

def binary_search(collection, target):
  # Import the bisect module
  import bisect
  # Use the bisect_left function to find the insertion point of target in collection
  i = bisect.bisect_left(collection, target)
  # Check if the insertion point is within the collection and the item at that point is equal to target
  if i < len(collection) and collection[i] == target:
    # If yes, return the insertion point as the index of target
    return i
  # If no, return -1
  else:
    return -1
```

#### Estimating Search Time for Binary Search

- The search time for binary search depends on the size of the collection and the position of the target item in the collection.
- The best case scenario for binary search is when the target item is the middle item of the collection, in which case the search time is constant, or O(1).
- The worst case scenario for binary search is when the target item is not in the collection, or is one of the first or last items in the collection, in which case the search time is logarithmic, or O(log n), where n is the number of items in the collection.
- The average case scenario for binary search is when the target item is somewhere in the middle of the collection, in which case the search time is also logarithmic, or O(log n), but with a smaller constant factor than the worst case.
- Therefore, the overall search time for binary search is O(log n), which means that it grows much slower than the size of the collection.

#### Mnemonics and Learning Tricks for Search Algorithms

- One way to remember the difference between simple search and binary search is to think of a game of guess the number, where one player thinks of a number and the other player tries to guess it.
- If the player who guesses uses simple search, they would start from the lowest possible number and increase by one until they find the correct number or reach the highest possible number. This would take a long time and many guesses, especially if the number is large or not in the range.
- If the player who guesses uses binary search, they would start from the middle of the range and ask if the number is higher or lower than their guess. Then they would divide the range into two halves and repeat the process until they find the correct number or the range is empty. This would take much less time and fewer guesses, especially if the number is in the range and the range is large.
- Another way to remember the difference between simple search and binary search is to use the acronym SLUB, which stands for Sorted, Logarithmic, Unsorted, and Binary. This helps to recall that binary search requires a sorted collection and has a logarithmic search time, while simple search can work on an unsorted collection and has a linear search time.