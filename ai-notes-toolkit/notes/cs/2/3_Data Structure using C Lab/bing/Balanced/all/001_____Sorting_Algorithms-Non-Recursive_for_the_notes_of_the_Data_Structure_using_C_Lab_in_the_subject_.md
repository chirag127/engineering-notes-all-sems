# Sorting Algorithms-Non-Recursive

Sorting algorithms are a set of instructions that take an array or list as an input and arrange the items into a particular order. Sorting algorithms can be classified into two categories: recursive and non-recursive.

- A recursive sorting algorithm calls on itself to sort a smaller part of the array, then combining the partially sorted results. For example, merge sort and quick sort are recursive sorting algorithms.
- A non-recursive sorting algorithm does the sorting all at once, without calling itself. For example, insertion sort and selection sort are non-recursive sorting algorithms.

Some of the advantages of non-recursive sorting algorithms are:

- They are easier to implement and understand than recursive algorithms.
- They do not use extra memory or stack space for recursive calls.
- They are faster and more efficient for small input sizes.

Some of the disadvantages of non-recursive sorting algorithms are:

- They are less elegant and more verbose than recursive algorithms.
- They have a higher time complexity and lower performance for large input sizes.
- They are not suitable for parallel or distributed computing.

Some of the common non-recursive sorting algorithms are:

- Insertion sort: This algorithm sorts the array by inserting each element into its correct position in the sorted part of the array. It has a time complexity of O(n^2) in the worst case and O(n) in the best case.
- Selection sort: This algorithm sorts the array by finding the smallest element in the unsorted part of the array and swapping it with the first element of the unsorted part. It has a time complexity of O(n^2) in all cases.
- Bubble sort: This algorithm sorts the array by repeatedly swapping adjacent elements that are out of order. It has a time complexity of O(n^2) in the worst case and O(n) in the best case.
- Heap sort: This algorithm sorts the array by using a binary heap data structure to store the elements. It has a time complexity of O(n log n) in all cases.
- Shell sort: This algorithm sorts the array by using a sequence of gap values to divide the array into subarrays and applying insertion sort on each subarray. It has a time complexity of O(n^2) in the worst case and O(n log n) in the best case.
- Counting sort: This algorithm sorts the array by using an auxiliary array to store the frequency of each element in the input array. It has a time complexity of O(n + k) in all cases, where k is the range of the input elements.
- Radix sort: This algorithm sorts the array by using a digit-by-digit comparison of the elements. It has a time complexity of O(nk) in all cases, where k is the number of digits in the input elements.
- Bucket sort: This algorithm sorts the array by using a hash function to distribute the elements into buckets and applying another sorting algorithm on each bucket. It has a time complexity of O(n + k) in the average case and O(n^2) in the worst case, where k is the number of buckets.