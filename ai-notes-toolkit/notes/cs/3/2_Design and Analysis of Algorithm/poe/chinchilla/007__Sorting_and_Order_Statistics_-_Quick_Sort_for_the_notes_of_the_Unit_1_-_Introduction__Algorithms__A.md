### Quick Sort

Quick Sort is a popular sorting algorithm that follows the divide-and-conquer approach. It is an efficient algorithm that has an average time complexity of O(n log n). Quick Sort is widely used in practice because of its simplicity and efficiency.

#### Algorithm

The Quick Sort algorithm follows these steps:

1. Choose a pivot element from the array. The pivot element can be any element from the array, but for simplicity, we usually choose the last element of the array.

2. Partition the array around the pivot element. This means that we rearrange the elements of the array such that all elements smaller than the pivot element are on the left side of the pivot element, and all elements greater than the pivot element are on the right side of the pivot element.

3. Recursively apply the above two steps to the left and right subarrays.

#### Partitioning

The partitioning step of Quick Sort is the most important and time-consuming step. The partitioning step works as follows:

1. Choose a pivot element from the array.

2. Initialize two pointers, i.e., the left pointer and the right pointer. The left pointer points to the first element of the array, and the right pointer points to the last element of the array.

3. Move the left pointer to the right until it points to an element greater than or equal to the pivot element.

4. Move the right pointer to the left until it points to an element smaller than or equal to the pivot element.

5. If the left pointer is less than or equal to the right pointer, swap the elements pointed by these pointers.

6. Repeat steps 3 to 5 until the left pointer is greater than the right pointer.

7. Swap the pivot element with the element pointed by the left pointer.

8. Return the index of the pivot element.

#### Complexity

The time complexity of Quick Sort depends on the choice of pivot element. If the pivot element is chosen such that the array is partitioned into two nearly equal halves, then the time complexity of Quick Sort is O(n log n). However, if the pivot element is always the smallest or largest element of the array, then the time complexity of Quick Sort is O(n^2).

#### Advantages

1. Quick Sort is an efficient sorting algorithm.

2. Quick Sort is widely used in practice because of its simplicity and efficiency.

3. Quick Sort can be easily implemented in-place, i.e., it does not require any additional memory.

#### Disadvantages

1. Quick Sort has a worst-case time complexity of O(n^2) if the pivot element is always the smallest or largest element of the array.

2. Quick Sort is not a stable sorting algorithm, i.e., it does not preserve the relative order of equal elements.

3. Quick Sort is not suitable for sorting large datasets because of its worst-case time complexity.