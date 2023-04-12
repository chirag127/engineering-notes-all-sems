## Program for Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements. It works by dividing the list into two regions: a sorted region and an unsorted region. It iteratively shrinks the unsorted region by extracting the largest element from it and inserting it into the sorted region. Here are the main steps of the heap sort algorithm:

- Build a max heap from the input list. A max heap is a complete binary tree where each node is greater than or equal to its children. The root node is the largest element in the heap. This can be done in linear time by using a bottom-up approach (see Binary heap § Building a heap).
- Swap the root node (the largest element) with the last node in the heap. This moves the largest element to the end of the list, which is now part of the sorted region.
- Reduce the size of the heap by one and heapify the root node. Heapify is a process of restoring the heap property by swapping the node with its largest child until it is greater than or equal to both of its children. This can be done in logarithmic time by using a top-down approach (see Binary heap § Heapify).
- Repeat steps 2 and 3 until the heap size is one. This means that the list is fully sorted.

Here is an example of heap sort in action:

![Heap sort example](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)

The following is a pseudocode for heap sort:

```
function heap_sort(list)
  n = length(list)
  build_max_heap(list, n) // build a max heap from the list
  for i from n to 2 // iterate from the last node to the second node
    swap list[1] and list[i] // swap the root node with the last node
    n = n - 1 // reduce the heap size by one
    heapify(list, 1, n) // heapify the root node
  end for
end function

function build_max_heap(list, n)
  for i from floor(n/2) to 1 // iterate from the last parent node to the root node
    heapify(list, i, n) // heapify each node
  end for
end function

function heapify(list, i, n)
  left = 2 * i // get the index of the left child
  right = 2 * i + 1 // get the index of the right child
  largest = i // assume the current node is the largest
  if left <= n and list[left] > list[largest] // if the left child is larger
    largest = left // update the largest
  end if
  if right <= n and list[right] > list[largest] // if the right child is larger
    largest = right // update the largest
  end if
  if largest != i // if the current node is not the largest
    swap list[i] and list[largest] // swap the current node with the largest child
    heapify(list, largest, n) // heapify the largest child
  end if
end function
```

The following are some implementations of heap sort in different programming languages:

- Python:

```python
def heap_sort(lst):
  n = len(lst)
  build_max_heap(lst, n) # build a max heap from the list
  for i in range(n-1, 0, -1): # iterate from the last node to the second node
    lst[0], lst[i] = lst[i], lst[0] # swap the root node with the last node
    n = n - 1 # reduce the heap size by one
    heapify(lst, 0, n) # heapify the root node

def build_max_heap(lst, n):
  for i in range(n//2 - 1, -1, -1): # iterate from the last parent node to the root node
    heapify(lst, i, n) # heapify each node

def heapify(lst, i, n):
  left = 2 * i + 1 # get the index of the left child
  right = 2 * i + 2 # get the index of the right child
  largest = i # assume the current node is the largest
  if left < n and lst[left] > lst[largest]: # if the left child is larger
    largest

```
