 Here is the content in markdown format for the topic **Program for Quick Sort** for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System:

## Program for Quick Sort

Quicksort is a efficient sorting algorithm that sorts elements in an array by recursively splitting the input array into two parts:

1. A left partition that contains all elements less than the pivot
2. A right partition that contains all elements greater than the pivot

The partitions are then sorted recursively. This process continues until the entire array is sorted.

Following are the steps for Quicksort:

1. Pick an element from the array as pivot. This can be the first element, last element, median of first, last and middle elements, etc.
2. Partition the array around the pivot into two subarrays:
- One subarray contains all elements less than the pivot
- Other subarray contains all elements greater than the pivot
3. Recursively call the Quicksort algorithm on both subarrays.

Pseudocode for Quicksort:

    Quicksort(array, left, right) {
        if (left < right) {
            partitionIndex = partition(array, left, right)
            Quicksort(array, left, partitionIndex - 1)
            Quicksort(array, partitionIndex + 1, right)
        }
    }

    partition(array, left, right) {
        pivot = array[right]
        storeIndex = left
        for (i = left to right - 1) {
            if (array[i] <= pivot) {
                swap(array[storeIndex], array[i])
                storeIndex = storeIndex + 1
            }
        }
        swap(array[storeIndex], array[right])
        return storeIndex
    }

Following is a sample input array and the steps involved in applying Quicksort on it:

array = [8, 4, 7, 6, 1, 3, 5, 2]

1. Pick the last element 8 as the pivot
2. The partition step divides the array into two subarrays:
- Left partition: [4, 7, 6, 1, 3, 5, 2]
- Right partition: [8]
3. Recursively quicksort the left partition:
- Pick the last element 2 as the pivot
- The partition step divides the left partition into two subarrays:
-- Left partition: [4, 1]
-- Right partition: [7, 6, 3, 5]
4. Continue this process recursively until the entire array is sorted.

The time complexity of Quicksort is O(nlogn) average case and O(n^2) worst case. The space complexity is O(logn) for call stack.

Advantages:
- Efficient algorithm with time complexity of O(nlogn) average and worst case.
- In-place sorting (doesn't require additional storage space).
- Efficient for large data sets.

Disadvantages:
- Difficult to specify a good pivot value. A bad choice of pivot can lead to worst case time complexity of O(n^2).
- Not a stable sort (can change the relative order of elements with equal keys).

Applications:
- Used extensively in database management systems to sort records.
- Used in compression algorithms to generate lexicographic ordering.
- Used in graphics and geometric algorithms to order vertices/points.