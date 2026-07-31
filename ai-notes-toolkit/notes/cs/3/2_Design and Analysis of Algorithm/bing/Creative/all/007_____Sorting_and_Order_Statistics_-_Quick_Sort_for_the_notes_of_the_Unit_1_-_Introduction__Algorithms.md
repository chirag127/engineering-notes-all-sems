# Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by **partitioning** it into two subarrays and then recursively sorting them.
- The partitioning step chooses a **pivot** element from the array and rearranges the array so that all elements less than or equal to the pivot are in the left subarray and all elements greater than the pivot are in the right subarray.
- The pivot element is then in its **correct position** in the sorted array.
- The algorithm then recursively sorts the left and right subarrays until they are of size one or zero, which means they are already sorted.
- The pseudocode for quick sort is:

```
QUICK-SORT(A, p, r)
  if p < r
    q = PARTITION(A, p, r) // q is the pivot index
    QUICK-SORT(A, p, q - 1) // sort the left subarray
    QUICK-SORT(A, q + 1, r) // sort the right subarray

PARTITION(A, p, r)
  x = A[r] // choose the last element as the pivot
  i = p - 1 // i is the index of the last element in the left subarray
  for j = p to r - 1 // loop through the array except the pivot
    if A[j] <= x // if the current element is less than or equal to the pivot
      i = i + 1 // increment i
      exchange A[i] with A[j] // swap the current element with the element at i
  exchange A[i + 1] with A[r] // swap the pivot with the element at i + 1
  return i + 1 // return the pivot index
```

- The **best-case** scenario for quick sort is when the partitioning always produces two subarrays of equal or nearly equal size, which means the recursion tree is balanced and has a height of $\Theta(\log n)$, where $n$ is the number of elements in the array. In this case, the running time of quick sort is $\Theta(n \log n)$.
- The **worst-case** scenario for quick sort is when the partitioning always produces one subarray of size zero and one subarray of size $n - 1$, which means the recursion tree is unbalanced and has a height of $\Theta(n)$. In this case, the running time of quick sort is $\Theta(n^2)$.
- The **average-case** scenario for quick sort is when the partitioning produces subarrays of varying sizes, but the sizes are not too skewed. In this case, the running time of quick sort is $\Theta(n \log n)$, which can be shown by using the **master theorem** or by using a **probabilistic analysis**.
- The **performance** of quick sort depends largely on the choice of the pivot element. A good pivot element is one that splits the array into two subarrays of roughly equal size, which leads to a balanced recursion tree and a faster running time. A bad pivot element is one that splits the array into two subarrays of very unequal size, which leads to an unbalanced recursion tree and a slower running time.
- One way to choose a good pivot element is to use a **randomized** version of quick sort, which selects the pivot element randomly from the array instead of using a fixed position such as the first, last, or middle element. This reduces the likelihood of encountering the worst-case scenario and improves the expected running time to $\Theta(n \log n)$.
- Another way to choose a good pivot element is to use the **median-of-three** method, which selects the pivot element as the median of the first, middle, and last elements of the array. This also reduces the likelihood of encountering the worst-case scenario and improves the running time to $\Theta(n \log n)$ for most inputs.
- Quick sort has some **advantages** over other sorting algorithms, such as:
  - It is **in-place**, which means it does not require additional memory to sort the array, unlike merge sort or heap sort.
  - It is **adaptive**, which means it performs better on partially sorted arrays, unlike shell sort or heap sort.
  - It is **parallelizable**, which means it can be easily implemented on multiple processors or cores, unlike insertion sort or bubble sort.
- Quick sort also has some **disadvantages**, such as:
  - It is **unstable**, which means it does not preserve the relative order of equal elements, unlike insertion sort or merge sort.
  - It is **sensitive** to the choice of the pivot