## Program for Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements. It works by building a max heap from the input list, and then repeatedly swapping the root element (the largest element) with the last element of the heap, and reducing the size of the heap by one. After each swap, the heap property is restored by sifting down the new root element. The algorithm terminates when the heap size becomes one or zero.

The steps of the heap sort algorithm are:

1. Build a max heap from the input list. This can be done in linear time by using a bottom-up approach, starting from the last non-leaf node and sifting it down if necessary. Repeat this process for all the nodes above it, until the root node is reached. The result is a complete binary tree where every node is greater than or equal to its children.
2. Swap the root element (the largest element) with the last element of the heap. This moves the largest element to its correct position in the sorted list, and reduces the heap size by one.
3. Sift down the new root element to restore the heap property. This involves comparing the root element with its children, and swapping it with the larger child if necessary. Repeat this process until the node reaches a position where it is greater than or equal to its children, or it becomes a leaf node.
4. Repeat steps 2 and 3 until the heap size becomes one or zero. This means that all the elements have been sorted in ascending order.

The following is a pseudocode for the heap sort algorithm:

```
function heap_sort(list):
  # build a max heap from the list
  heapify(list)

  # loop from the end of the heap to the beginning
  for i in range(len(list) - 1, 0, -1):
    # swap the root element with the last element of the heap
    swap(list, 0, i)
    # reduce the heap size by one
    heap_size = i
    # sift down the new root element to restore the heap property
    sift_down(list, 0, heap_size)

# helper function to build a max heap from a list
function heapify(list):
  # start from the last non-leaf node and sift it down if necessary
  for i in range((len(list) // 2) - 1, -1, -1):
    sift_down(list, i, len(list))

# helper function to sift down a node in a heap
function sift_down(list, i, heap_size):
  # get the index of the left and right child of the node
  left = 2 * i + 1
  right = 2 * i + 2
  # assume the node is the largest element
  largest = i
  # compare the node with its left child
  if left < heap_size and list[left] > list[largest]:
    # update the largest element
    largest = left
  # compare the node with its right child
  if right < heap_size and list[right] > list[largest]:
    # update the largest element
    largest = right
  # check if the node needs to be swapped with its larger child
  if largest != i:
    # swap the node with its larger child
    swap(list, i, largest)
    # recursively sift down the child node
    sift_down(list, largest, heap_size)

# helper function to swap two elements in a list
function swap(list, i, j):
  # store the value of the ith element
  temp = list[i]
  # assign the value of the jth element to the ith element
  list[i] = list[j]
  # assign the value of the temp variable to the jth element
  list[j] = temp
```

The following is a possible implementation of the heap sort algorithm in Python:

```python
# function to sort a list using heap sort
def heap_sort(list):
  # build a max heap from the list
  heapify(list)

  # loop from the end of the heap to the beginning
  for i in range(len(list) - 1, 0, -1):
    # swap the root element with the last element of the heap
    swap(list, 0, i)
    # reduce the heap size by one
    heap_size = i
    # sift down the new root element to restore the heap property
    sift_down(list, 0, heap_size)

# helper function

```
