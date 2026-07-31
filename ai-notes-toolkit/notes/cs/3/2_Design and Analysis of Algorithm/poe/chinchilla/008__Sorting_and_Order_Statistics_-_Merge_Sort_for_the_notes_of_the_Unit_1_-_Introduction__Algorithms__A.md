### Merge Sort

Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges the two sorted halves to produce the final sorted output.

#### Algorithm

The Merge Sort algorithm can be described as follows:

1. Divide the input array into two halves, until the subarrays have length 1 or 0.
2. Recursively sort each subarray.
3. Merge the two sorted subarrays into a single sorted array.

#### Pseudocode

The Merge Sort algorithm can be implemented using the following pseudocode:

```
merge_sort(A, p, r)
    if p < r
        q = (p + r) / 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

merge(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    L[1..n1+1] and R[1..n2+1] are new arrays
    for i = 1 to n1
        L[i] = A[p+i-1]
    for j = 1 to n2
        R[j] = A[q+j]
    L[n1+1] = infinity
    R[n2+1] = infinity
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1
```

#### Analysis

The Merge Sort algorithm has a worst-case time complexity of O(n log n), which is optimal for comparison-based sorting algorithms. It also has a worst-case space complexity of O(n) due to the need for additional space to store the sorted subarrays during the merge step.

#### Advantages

Some advantages of Merge Sort are:

- Stable sorting: Merge Sort is a stable sorting algorithm, which means that it maintains the relative order of equal elements in the input array.
- Guaranteed worst-case performance: Merge Sort has a worst-case time complexity of O(n log n), which is optimal for comparison-based sorting algorithms.
- Parallelizable: Merge Sort is easily parallelizable, which means that it can be run on multiple processors or cores to speed up the sorting process.

#### Disadvantages

Some disadvantages of Merge Sort are:

- Extra space requirement: Merge Sort requires additional space to store the sorted subarrays during the merge step, which can be a disadvantage for large input arrays or in memory-constrained environments.
- Recursive: Merge Sort is a recursive algorithm, which means that it can have a high overhead due to the need to store and manage recursive calls.
- Not in-place: Merge Sort is not an in-place sorting algorithm, which means that it requires additional space to store the sorted output.