### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by **partitioning** it into two subarrays and then recursively sorting them.
- The partitioning step chooses a **pivot** element from the array and **rearranges** the array so that all elements less than or equal to the pivot are in the left subarray and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its **correct position** in the sorted array, and the subarrays are recursively sorted.
- The algorithm can be implemented **in-place**, meaning that it does not require additional memory to store the subarrays.
- The **average-case** running time of quick sort is **O(n log n)**, where n is the number of elements in the array, assuming that the pivot is chosen randomly or approximately median.
- The **worst-case** running time of quick sort is **O(n^2)**, which occurs when the pivot is always the smallest or the largest element in the array, resulting in unbalanced partitions.
- The **best-case** running time of quick sort is also **O(n log n)**, which occurs when the pivot is always the median of the array, resulting in balanced partitions.
- Quick sort is often **faster** than other sorting algorithms in practice, because it has a low **constant factor** and it can exploit the **locality** of the data.
- Quick sort is **not stable**, meaning that it does not preserve the relative order of equal elements in the array.
- Quick sort can be **improved** by using different strategies for choosing the pivot, such as **median-of-three**, **randomized**, or **hybrid** methods, or by using a different algorithm for small subarrays, such as **insertion sort** or **selection sort**.