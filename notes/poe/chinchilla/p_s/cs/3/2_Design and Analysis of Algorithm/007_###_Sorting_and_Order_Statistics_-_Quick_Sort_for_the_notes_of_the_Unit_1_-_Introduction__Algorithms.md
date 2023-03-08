### Sorting and Order Statistics - Quick Sort

Quick Sort is an efficient, recursive and in-place sorting algorithm which is widely used for sorting large datasets. It works on the principle of divide and conquer where the array is divided into sub-arrays and these sub-arrays are sorted recursively. Quick Sort was invented by Tony Hoare in 1959.

#### Algorithm

The algorithm for Quick Sort is as follows:

1. Choose a pivot element from the array. This pivot element can be chosen randomly or as the first, last or middle element of the array.
2. Partition the array such that all elements less than the pivot are to its left and all elements greater than the pivot are to its right.
3. Recursively apply the above two steps to the left and right sub-arrays until the entire array is sorted.

#### Example

Let's consider an unsorted array {9, 5, 7, 3, 8, 4, 2, 6, 1}. We choose the first element, 9, as the pivot. After partitioning, the array becomes {5, 7, 3, 8, 4, 2, 6, 1, 9}. Now, we recursively apply the same steps to the left and right sub-arrays until the entire array is sorted.

Left sub-array {5, 7, 3, 8, 4, 2, 6, 1}:
- Choose the first element, 5, as the pivot. After partitioning, the sub-array becomes {3, 4, 2, 1, 5, 7, 8, 6}.
- Choose the first element, 3, as the pivot. After partitioning, the sub-array becomes {2, 1, 3, 4, 5, 7, 8, 6}.
- Choose the first element, 2, as the pivot. After partitioning, the sub-array becomes {1, 2, 3, 4, 5, 7, 8, 6}.
- Choose the first element, 1, as the pivot. After partitioning, the sub-array becomes {1, 2, 3, 4, 5, 7, 8, 6}.
- The left sub-array is sorted.

Right sub-array {7, 8, 6}:
- Choose the first element, 7, as the pivot. After partitioning, the sub-array becomes {6, 7, 8}.
- The right sub-array is sorted.

After sorting the left and right sub-arrays, the entire array becomes {1, 2, 3, 4, 5, 6, 7, 8, 9}.

#### Advantages

- Quick Sort is very efficient for large datasets and is widely used in practice.
- It is an in-place sorting algorithm i.e. it does not require any extra space to sort the array.
- It has a relatively small constant factor and has good cache performance.

#### Disadvantages

- Quick Sort has a worst-case time complexity of O(n^2) when the pivot element is chosen poorly. This can be avoided by choosing a good pivot element.
- It is not a stable sorting algorithm i.e. it does not preserve the relative order of elements with equal keys.

#### Applications

- Quick Sort is used in many programming languages for their built-in sorting functions.
- It is used in database systems for sorting large datasets.
- It is used in numerical analysis for numerical simulations.

#### Comparison with Other Sorting Algorithms

Quick Sort is more efficient than many other sorting algorithms like Bubble Sort, Insertion Sort and Selection Sort. However, it is less efficient than Merge Sort and Heap Sort in the worst case.

#### Conclusion

Quick Sort is an efficient, recursive and in-place sorting algorithm which is widely used for sorting large datasets. It works on the principle of divide and conquer where the array is divided into sub-arrays and these sub-arrays are sorted recursively. It has a worst-case time complexity of O(n^2) when the pivot element is chosen poorly, but this can be avoided by choosing a good pivot element. Quick Sort is used in many programming languages for their built-in sorting functions and in database systems for sorting large datasets.