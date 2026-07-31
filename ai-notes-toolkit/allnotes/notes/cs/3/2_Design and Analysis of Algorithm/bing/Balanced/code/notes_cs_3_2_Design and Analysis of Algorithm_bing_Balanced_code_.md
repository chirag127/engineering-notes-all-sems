

## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An **algorithm** is a finite sequence of well-defined steps that can be followed to solve a problem or perform a computation.
- **Analyzing algorithms** is the process of determining the amount of resources (such as time and space) that an algorithm requires to execute.
- The **complexity of algorithms** is a measure of how the resource requirements of an algorithm vary with the size of the input.
- The **growth of functions** is a way of comparing the asymptotic behavior of different functions that describe the complexity of algorithms. For example, the function f(n) = n^2 grows faster than the function g(n) = n log n as n approaches infinity.
- **Performance measurements** are empirical methods of evaluating the efficiency and correctness of algorithms by running them on actual inputs and collecting data such as running time, memory usage, output quality, etc.
- **Sorting** is the process of arranging a collection of items (such as numbers, words, or records) in a certain order (such as ascending, descending, or alphabetical). **Order statistics** are the values that occupy certain positions in a sorted collection, such as the minimum, maximum, median, or kth smallest element.
- **Shell sort** is a sorting algorithm that works by repeatedly applying insertion sort on subarrays of the input array with different gaps between the elements. The gaps are chosen to reduce the number of comparisons and movements of elements. The final gap is always 1, which means the last pass is a regular insertion sort. The average time complexity of shell sort is O(n^(3/2)) and the worst-case time complexity is O(n^2).
- **Quick sort** is a sorting algorithm that works by choosing a pivot element from the input array and partitioning the array into two subarrays: one with elements less than or equal to the pivot and one with elements greater than the pivot. Then, quick sort is recursively applied to the subarrays until they are sorted. The average time complexity of quick sort is O(n log n) and the worst-case time complexity is O(n^2).
- **Merge sort** is a sorting algorithm that works by dividing the input array into two halves, sorting each half recursively, and then merging the two sorted halves into one sorted array. The merge operation is done by comparing the first elements of each half and copying the smaller one to the output array, until one of the halves is exhausted. The time complexity of merge sort is O(n log n) in all cases.
- **Heap sort** is a sorting algorithm that works by building a binary heap (a complete binary tree where each node is greater than or equal to its children) from the input array and then repeatedly extracting the maximum element from the heap and placing it at the end of the output array. The heap is maintained by swapping the root node with the last node and then restoring the heap property by moving the new root node down the tree until it is greater than or equal to its children. The time complexity of heap sort is O(n log n) in all cases.
- **Comparison of sorting algorithms** is the process of evaluating the advantages and disadvantages of different sorting algorithms based on various criteria, such as time complexity, space complexity, stability, adaptability, simplicity, etc. Some general observations are:

  - Insertion sort, selection sort, and bubble sort are simple but inefficient sorting algorithms with O(n^2) time complexity in the average and worst cases. They are suitable for small or nearly sorted arrays, or when the cost of comparisons is high and the cost of movements is low. They are stable and adaptive algorithms.
  - Shell sort, quick sort, and heap sort are more efficient sorting algorithms with O(n log n) time complexity in the average case, but they have O(n^2) time complexity in the worst case (except for heap sort). They are suitable for large or unsorted arrays, or when the cost of comparisons is low and the cost of movements is high. They are unstable and non-adaptive algorithms.
  - Merge sort is an efficient and stable sorting algorithm with O(n log n) time complexity in all cases, but it requires O(n) extra space for the merge operation. It is suitable for arrays that cannot fit in memory, or when the cost of comparisons and movements are similar. It is non-adaptive algorithm.
  - Sorting in linear time is possible for some special cases of sorting problems, such as when the input array consists of only a few distinct values, or when the input array is composed of fixed-length keys that can



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on algorithms for sorting and order statistics:

### Algorithms for Sorting and Order Statistics

- Sorting is the process of rearranging a sequence of elements into a specific order, such as ascending or descending, based on some comparison criterion.
- Order statistics are the elements that occupy certain positions in a sorted sequence, such as the minimum, maximum, median, or the ith smallest or largest element.
- Sorting and order statistics are fundamental problems in computer science and have many applications in data analysis, searching, cryptography, and more.
- There are different algorithms for sorting and order statistics, each with different time and space complexities, advantages and disadvantages, and implementation details.
- Some of the common sorting algorithms are:

  - **Shell sort**: This is a variation of insertion sort that divides the sequence into sub-sequences with a certain gap and sorts each sub-sequence using insertion sort. The gap is gradually reduced until it becomes one, which means the whole sequence is sorted. Shell sort is faster than insertion sort, but still has a worst-case time complexity of O(n^2).
  - **Quick sort**: This is a divide-and-conquer algorithm that partitions the sequence around a pivot element, such that all the elements smaller than the pivot are on its left and all the elements larger than the pivot are on its right. Then, it recursively sorts the left and right sub-sequences until the whole sequence is sorted. Quick sort is one of the fastest sorting algorithms, with an average time complexity of O(n log n), but it has a worst-case time complexity of O(n^2) if the pivot is chosen poorly.
  - **Merge sort**: This is another divide-and-conquer algorithm that splits the sequence into two equal halves and recursively sorts each half. Then, it merges the two sorted halves into one sorted sequence using a linear-time merging procedure. Merge sort has a stable time complexity of O(n log n) in all cases, but it requires extra space for the merging process.
  - **Heap sort**: This is a selection-based algorithm that uses a data structure called a heap, which is a binary tree that satisfies the heap property: every node is larger (or smaller) than its children. Heap sort builds a max-heap (or min-heap) from the sequence, and then repeatedly extracts the root (which is the maximum or minimum element) and places it at the end of the sequence, until the heap is empty and the sequence is sorted. Heap sort has a time complexity of O(n log n) in all cases, and it does not require extra space, but it is not stable (it may change the relative order of equal elements).
  - **Comparison of sorting algorithms**: The choice of the best sorting algorithm depends on several factors, such as the size and distribution of the input, the available space and time, the stability requirement, and the implementation difficulty. Some general guidelines are:

    - For small inputs, insertion sort or shell sort may be faster than other algorithms, as they have low overhead and can exploit partial order.
    - For large inputs, quick sort or merge sort may be preferred, as they have logarithmic depth and can exploit the divide-and-conquer paradigm.
    - For inputs that are already sorted or nearly sorted, insertion sort or bubble sort may be optimal, as they have linear time complexity in the best case and can detect the sortedness of the input.
    - For inputs that have a limited range of values, counting sort or radix sort may be efficient, as they have linear time complexity and can avoid comparisons.
    - For inputs that have duplicate values, merge sort or heap sort may be stable, as they preserve the relative order of equal elements.

- Some of the common algorithms for order statistics are:

  - **Selection algorithm**: This is a generalization of quick sort that finds the ith smallest element in a sequence. It partitions the sequence around a pivot element, and then recursively searches in the left or right sub-sequence depending on the rank of the pivot. The selection algorithm has an average time complexity of O(n), but it has a worst-case time complexity of O(n^2) if the pivot is chosen poorly.
  - **Median-of-medians algorithm**: This is an improvement of the selection algorithm that guarantees a good pivot choice. It divides the sequence into groups of five elements, finds the median of each group, and then recursively finds the median of the medians. This median-of-medians is used as the pivot for the partitioning step. The median-of-medians algorithm has a worst-case time complexity of O



### Analyzing Algorithms

- Analyzing algorithms is the process of finding the **computational complexity** of algorithms, which is the amount of time, storage, or other resources needed to execute them .
- The computational complexity of an algorithm is usually expressed as a **function** of the length of its input, denoted by **n**. For example, an algorithm that takes **n** steps to sort an array of **n** elements has a time complexity of **O(n)**, where **O** is the **big-O notation** that represents the **upper bound** or the **worst-case** scenario of the algorithm's performance.
- Analyzing algorithms is important for several reasons:
  - To **predict** the behavior of an algorithm without implementing it on a specific computer.
  - To **compare** different algorithms for the same problem and choose the most efficient one.
  - To **estimate** the resources required by an algorithm to solve a specific computational problem.
  - To **verify** the correctness of an algorithm over all possible inputs by reasoning formally or mathematically about it.
- Analyzing algorithms involves two main steps:
  - **Designing** an algorithm that solves the given problem correctly and efficiently.
  - **Measuring** the performance of the algorithm in terms of time and space complexity, using mathematical tools and techniques.
- Some of the common tools and techniques for analyzing algorithms are:
  - **Asymptotic analysis**, which focuses on the **growth rate** of the complexity function as the input size increases, and ignores the constant factors and lower-order terms. It uses the **big-O**, **big-Ω**, and **big-Θ** notations to represent the upper bound, lower bound, and tight bound of the complexity function, respectively.
  - **Recurrence relations**, which describe the complexity of a **recursive** algorithm as a function of the complexity of its smaller subproblems. They can be solved using various methods, such as **substitution**, **iteration**, **master theorem**, or **recursion tree**.
  - **Amortized analysis**, which calculates the **average** complexity of a sequence of operations performed by an algorithm, rather than the worst-case complexity of each individual operation. It uses techniques such as **aggregate analysis**, **accounting method**, or **potential method**.
- Some of the common types of algorithms that are analyzed in terms of their complexity are:
  - **Sorting algorithms**, which arrange a collection of elements in a certain order, such as **ascending** or **descending**. Some examples of sorting algorithms are **shell sort**, **quick sort**, **merge sort**, **heap sort**, and **linear-time sorting algorithms** such as **counting sort**, **radix sort**, and **bucket sort**.
  - **Order statistics algorithms**, which find the **kth smallest** or **kth largest** element in an unsorted array, or the **median** of an array. Some examples of order statistics algorithms are **randomized select**, **median of medians**, and **quick select**.



### Complexity of Algorithms

- Complexity of algorithms is a measure of how long an algorithm would take to complete given an input of size n.
- Complexity is about the algorithm itself, the way it processes the data to solve a given problem. It's a software design concern at the "idea level".
- Complexity is calculated asymptotically as n approaches infinity, to estimate the order of growth of the algorithm's running time.
- Complexity is also called algorithmic complexity or running time.
- Complexity can be classified into two types: time complexity and space complexity .
- Time complexity is the amount of time required by the algorithm to solve the problem. It is measured by counting the number of elementary operations performed by the algorithm, such as arithmetic operations, comparisons, assignments, etc  .
- Space complexity is the amount of memory or storage required by the algorithm to solve the problem. It includes space for input data, output data, variables, constants, etc .
- Complexity can be expressed using different notations, such as big O, big Omega, big Theta, little o, little omega, etc. These notations capture the asymptotic behavior of the algorithm's running time or space usage as a function of the input size .
- Complexity can be analyzed using different models of computation, such as Turing machines, random access machines, parallel machines, etc. These models define the basic operations and their costs that can be performed by the algorithm.
- Complexity can be used to compare different algorithms that solve the same problem, and to choose the best one among them. The best algorithm is the one that has the lowest complexity for the given input size .
- Complexity can also be used to classify problems into different classes, such as P, NP, NP-complete, NP-hard, etc. These classes define the inherent difficulty of the problem and the existence of efficient algorithms to solve them.



### Growth of Functions

- Growth of functions is a way of measuring the efficiency and performance of algorithms based on their input size and execution time.
- Growth of functions helps us to compare different algorithms and choose the most suitable one for a given problem.
- Growth of functions is often expressed using asymptotic notation, which simplifies the function by ignoring constants and lower order terms.
- Asymptotic notation includes three types: big-O, big-Ω, and big-Θ, which represent the upper bound, lower bound, and tight bound of the function respectively.
- The rate of growth of a function can be classified into different categories, such as constant, linear, logarithmic, polynomial, exponential, and factorial.
- The rate of growth of a function indicates how fast or slow the algorithm is, and how it scales with the input size.
- Generally, a lower rate of growth means a faster and more efficient algorithm, and a higher rate of growth means a slower and less efficient algorithm.
- For example, linear search has a rate of growth of Θ(n), which means it takes linear time to search for an element in an array of size n.
- Binary search has a rate of growth of Θ(log n), which means it takes logarithmic time to search for an element in a sorted array of size n.
- Binary search is more efficient than linear search, because log n grows slower than n as n increases.



### Performance Measurements

- Performance measurements are used to evaluate the efficiency and effectiveness of algorithms.
- Performance measurements can be divided into two categories: **time complexity** and **space complexity**.
- Time complexity measures how long an algorithm takes to run as a function of the input size. It is usually expressed using the **big-O notation**, which gives the upper bound of the growth rate of the running time.
- Space complexity measures how much memory an algorithm uses as a function of the input size. It is also expressed using the big-O notation, which gives the upper bound of the growth rate of the memory usage.
- Performance measurements can be further classified into **worst-case**, **best-case**, and **average-case** analysis, depending on the assumptions made about the input distribution and the behavior of the algorithm.
- Worst-case analysis gives the maximum possible running time or memory usage for any input of a given size. It is useful for providing guarantees and lower bounds on the performance of an algorithm.
- Best-case analysis gives the minimum possible running time or memory usage for any input of a given size. It is useful for showing the potential of an algorithm, but it is often unrealistic and misleading.
- Average-case analysis gives the expected running time or memory usage for a random input of a given size, assuming a certain probability distribution. It is useful for estimating the practical performance of an algorithm, but it is often difficult to obtain and verify.
- Performance measurements can also be influenced by other factors, such as the hardware, the programming language, the compiler, the operating system, and the input characteristics. Therefore, performance measurements should be used with caution and complemented with empirical testing and experimentation.



### Sorting and Order Statistics - Shell Sort

- Shell sort is a sorting algorithm that is based on the idea of insertion sort, but improves its efficiency by using a sequence of gaps to compare and move elements that are far apart.
- Shell sort works by dividing the input array into subarrays, each consisting of elements that are separated by a certain gap size. For each subarray, insertion sort is applied to sort the elements. The gap size is gradually reduced until it becomes one, at which point the array is fully sorted.
- The performance of shell sort depends on the choice of the gap sequence. Different gap sequences have different time complexities and properties. Some examples of gap sequences are:

  - Shell's original sequence: n/2, n/4, ..., 1
  - Hibbard's sequence: 1, 3, 7, ..., 2^k - 1
  - Sedgewick's sequence: 1, 5, 19, 41, ..., 4^k + 3 * 2^(k-1) + 1
  - Knuth's sequence: 1, 4, 13, 40, ..., (3^k - 1) / 2

- The best known time complexity of shell sort is O(n^(3/2)) using Sedgewick's sequence, but it is conjectured that there exists a gap sequence that can achieve O(n * log^2 n) time complexity.
- Shell sort is an in-place and unstable sorting algorithm, meaning that it does not require extra space and it does not preserve the relative order of equal elements.
- Shell sort is suitable for sorting arrays that are mostly sorted or have a small number of inversions, as it can take advantage of the existing order and reduce the number of comparisons and swaps. It is also easy to implement and has low overhead. However, it is not as efficient as other sorting algorithms such as quick sort, merge sort, or heap sort for large or random arrays.



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



### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays, sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  - If the array has only one element, it is already sorted and no further action is needed.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the two sorted subarrays into a single sorted array.

- The merge operation takes two sorted subarrays and combines them into one sorted array. It can be implemented as follows:

  - Initialize two pointers, i and j, to point to the first elements of the left and right subarrays, respectively.
  - Initialize an empty array, C, to store the merged result.
  - While both i and j are within the bounds of their subarrays, compare the elements at A[i] and B[j], and append the smaller one to C. Increment the pointer of the subarray that provided the smaller element.
  - If one of the subarrays is exhausted, append the remaining elements of the other subarray to C.
  - Return C as the merged array.

- The pseudocode for merge sort is given below:

  ```
  MERGE-SORT(A, p, r)
  // A is the array to be sorted
  // p and r are the indices of the first and last elements of the subarray
  // Precondition: 0 <= p <= r < A.length
  // Postcondition: A[p..r] is sorted in ascending order
  1. if p < r
  2.     q = floor((p + r) / 2) // find the middle point of the subarray
  3.     MERGE-SORT(A, p, q) // recursively sort the left subarray
  4.     MERGE-SORT(A, q + 1, r) // recursively sort the right subarray
  5.     MERGE(A, p, q, r) // merge the two sorted subarrays

  MERGE(A, p, q, r)
  // A is the array containing the two sorted subarrays
  // p, q, and r are the indices of the first, middle, and last elements of the subarray
  // Precondition: A[p..q] and A[q + 1..r] are sorted in ascending order
  // Postcondition: A[p..r] is sorted in ascending order
  1. n1 = q - p + 1 // the length of the left subarray
  2. n2 = r - q // the length of the right subarray
  3. create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
  4. for i = 1 to n1
  5.     L[i] = A[p + i - 1] // copy the left subarray to L
  6. for j = 1 to n2
  7.     R[j] = A[q + j] // copy the right subarray to R
  8. L[n1 + 1] = infinity // a sentinel value to mark the end of the left subarray
  9. R[n2 + 1] = infinity // a sentinel value to mark the end of the right subarray
  10. i = 1 // the pointer for the left subarray
  11. j = 1 // the pointer for the right subarray
  12. for k = p to r
  13.     if L[i] <= R[j] // compare the elements at the pointers
  14.         A[k] = L[i] // copy the smaller element to the merged array
  15.         i = i + 1 // increment the pointer of the left subarray
  16.     else
  17.         A[k] = R[j] // copy the smaller element to the merged array
  18.         j = j + 1 // increment the pointer of the right subarray
  ```

- The time complexity of merge sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and performs a linear merge operation



### Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: building the heap and extracting the elements from the heap.
- Building the heap: the algorithm converts the input array into a max-heap or a min-heap by repeatedly applying a procedure called heapify, which ensures that the subtree rooted at a given node satisfies the heap property. This phase takes O(n) time, where n is the number of elements in the array.
- Extracting the elements from the heap: the algorithm repeatedly swaps the root element of the heap with the last element of the heap, and then reduces the size of the heap by one. Then, it applies heapify to the root node to restore the heap property. This phase takes O(n log n) time, where n is the number of elements in the heap.
- The overall time complexity of heap sort is O(n log n), where n is the number of elements in the array. The space complexity is O(1), as the algorithm only requires constant extra space.
- Heap sort is an in-place, unstable, and non-adaptive sorting algorithm. It does not require additional memory, it does not preserve the relative order of equal elements, and it does not take advantage of the existing order in the input array.
- Heap sort is suitable for sorting large data sets, as it has a good asymptotic performance and a low space requirement. However, it is not very efficient for sorting small data sets, as it has a high constant factor and a poor cache performance. It is also not stable, which may be undesirable for some applications.



### Comparison of Sorting Algorithms

Sorting algorithms are methods of arranging a list of elements in a certain order, such as ascending or descending. Sorting algorithms can be classified into two categories: comparison-based and non-comparison-based. Comparison-based algorithms compare elements of the list with each other using a comparison operator, such as less than or equal to. Non-comparison-based algorithms do not use comparisons, but rely on other techniques, such as counting or hashing.

Some of the most commonly used sorting algorithms are:

- Shell sort: A variation of insertion sort that divides the list into sublists and sorts each sublist using insertion sort. The sublists are gradually reduced in size until the whole list is sorted. Shell sort has an average time complexity of O(n^1.5), where n is the number of elements in the list. Shell sort is an unstable algorithm, meaning that it does not preserve the relative order of equal elements.
- Quick sort: A divide-and-conquer algorithm that partitions the list into two sublists based on a pivot element, such that all elements in the left sublist are less than or equal to the pivot and all elements in the right sublist are greater than or equal to the pivot. Then, quick sort recursively sorts the sublists until the whole list is sorted. Quick sort has an average time complexity of O(n log n), but a worst-case time complexity of O(n^2) if the pivot is chosen poorly. Quick sort is also an unstable algorithm.
- Merge sort: Another divide-and-conquer algorithm that splits the list into two halves and recursively sorts each half using merge sort. Then, it merges the two sorted halves into one sorted list using a merge procedure. Merge sort has a time complexity of O(n log n) in all cases, where n is the number of elements in the list. Merge sort is a stable algorithm, meaning that it preserves the relative order of equal elements.
- Heap sort: An algorithm that builds a binary heap (a complete binary tree where each node is greater than or equal to its children) from the list and repeatedly extracts the maximum element from the heap and places it at the end of the list, until the heap is empty and the list is sorted. Heap sort has a time complexity of O(n log n) in all cases, where n is the number of elements in the list. Heap sort is an unstable algorithm.
- Counting sort: A non-comparison-based algorithm that assumes that the list contains only integers in a fixed range. It counts the number of occurrences of each integer in the list and uses this information to determine the position of each element in the sorted list. Counting sort has a time complexity of O(n + k), where n is the number of elements in the list and k is the range of integers. Counting sort is a stable algorithm.
- Bucket sort: Another non-comparison-based algorithm that divides the list into buckets (sublists) based on some criterion, such as the first digit or the decimal place of each element. Then, it sorts each bucket using another sorting algorithm, such as insertion sort, and concatenates the buckets to form the sorted list. Bucket sort has an average time complexity of O(n + k), where n is the number of elements in the list and k is the number of buckets, but a worst-case time complexity of O(n^2) if the elements are not evenly distributed among the buckets. Bucket sort is a stable algorithm.

Some factors that can affect the performance and suitability of sorting algorithms are:

- The size of the list: For small lists, simple algorithms such as insertion sort or selection sort may be faster than more complex algorithms such as quick sort or merge sort. For large lists, algorithms with lower time complexity such as quick sort or heap sort may be preferred.
- The order of the list: For partially sorted or nearly sorted lists, algorithms that take advantage of the existing order such as insertion sort or shell sort may be more efficient than algorithms that ignore the order such as quick sort or heap sort. For lists that are in reverse order or have many duplicates, algorithms that handle these cases well such as merge sort or counting sort may be better than algorithms that perform poorly such as quick sort or heap sort.
- The stability of the algorithm: For lists that contain equal elements that have some additional information or meaning, such as records or objects, a stable algorithm that preserves the relative order of equal elements may be desired, such as merge sort or counting sort. For lists that contain only primitive values, such as numbers or characters, an unstable algorithm that may change the relative order of equal elements may not matter, such as quick sort or heap sort.
- The space complexity



### Sorting in Linear Time

- Sorting in linear time means arranging a sequence of elements in a specific order in O(n) time, where n is the number of elements.
- Most of the comparison-based sorting algorithms, such as shell sort, quick sort, merge sort, and heap sort, have a lower bound of O(n log n) time in the worst case or average case.
- To achieve linear time complexity, some sorting algorithms require special assumptions about the input sequence, such as the range of values, the distribution of elements, or the representation of data.
- Some examples of sorting algorithms that run in linear time are counting sort, radix sort, and bucket sort.

#### Counting Sort
- Counting sort assumes that the input consists of integers in a small range, such as [0, k] for some integer k.
- Counting sort works by counting the number of occurrences of each value in the input sequence and then using those counts to determine the position of each element in the output sequence.
- Counting sort has a time complexity of O(n + k), where n is the number of elements and k is the range of values. It also requires O(n + k) space to store the counts and the output sequence.

#### Radix Sort
- Radix sort assumes that the input consists of integers or strings that have a fixed length and can be represented in some base b, such as binary, decimal, or hexadecimal.
- Radix sort works by sorting the input sequence from the least significant digit to the most significant digit, using a stable sorting algorithm (such as counting sort) for each digit.
- Radix sort has a time complexity of O(d(n + b)), where d is the number of digits, n is the number of elements, and b is the base. It also requires O(n + b) space to store the intermediate and output sequences.

#### Bucket Sort
- Bucket sort assumes that the input is generated by a random process that distributes elements uniformly over the interval [0, 1).
- Bucket sort works by dividing the interval into n equal-sized buckets and then distributing the elements into the buckets based on their values. Then, each bucket is sorted individually using another sorting algorithm (such as insertion sort) and the output sequence is obtained by concatenating the sorted buckets.
- Bucket sort has an expected time complexity of O(n), where n is the number of elements, if the input is uniformly distributed and the bucket size is constant. It also requires O(n) space to store the buckets and the output sequence.



## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

- Advanced data structures are data structures that provide more efficient ways to store, manipulate, and access data, especially for applications that require complex operations or large amounts of data.
- Some of the advanced data structures that we will study in this unit are:

  - Red-black trees: A type of self-balancing binary search tree that maintains the height of the tree as O(log n) by enforcing some properties on the color and structure of the nodes. Red-black trees are useful for implementing associative arrays, such as dictionaries or maps, that support fast insertion, deletion, and search operations.
  - B-trees: A type of multi-way search tree that can have more than two children per node and store multiple keys per node. B-trees are designed to minimize the number of disk accesses by keeping the tree as balanced and shallow as possible. B-trees are widely used for implementing database indexes, file systems, and external memory data structures.
  - Binomial heaps: A type of heap data structure that consists of a collection of binomial trees, which are rooted trees that follow some properties on the degree and order of the nodes. Binomial heaps support fast merge operations, which can be useful for implementing priority queues or disjoint-set data structures.
  - Fibonacci heaps: A type of heap data structure that is an improvement over binomial heaps, as it allows for faster decrease-key and delete operations. Fibonacci heaps are composed of a set of rooted trees that follow some properties on the degree and potential of the nodes. Fibonacci heaps are used for implementing efficient algorithms for graph problems, such as Dijkstra's shortest path algorithm or Prim's minimum spanning tree algorithm.
  - Tries: A type of tree data structure that stores strings or sequences of symbols in a compact and efficient way. Tries are also known as prefix trees, as they allow for fast prefix searching and matching operations. Tries are used for implementing spell checkers, auto-complete features, text compression, and pattern matching algorithms.
  - Skip lists: A type of probabilistic data structure that consists of a series of linked lists, each of which is a subset of the previous one, and contains pointers to skip over some nodes. Skip lists are used to implement ordered sets or maps that support fast insertion, deletion, and search operations with an expected O(log n) time complexity.



### Red-Black Trees

- Red-black trees are a type of **self-balancing binary search trees** that guarantee a **logarithmic time complexity** for basic operations like insertion, deletion, and search .
- Red-black trees have the following properties :
  - Every node is either red or black. This can be stored as a single bit in memory (e.g. 'red' = 1, 'black' = 0).
  - The root of the tree is always black.
  - Every leaf node (null pointer) is black.
  - If a node is red, then both its children are black.
  - Every simple path from a node to a descendant leaf node has the same number of black nodes. This number is called the **black height** of the node.
- Red-black trees maintain these properties by performing **rotations** and **recoloring** operations after insertion or deletion of nodes. These operations restore the balance of the tree and ensure that the height of the tree is at most 2*log(n+1), where n is the number of nodes.
- Red-black trees can be used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - Implementing associative arrays or dictionaries.
  - Implementing sets or multisets.
  - Implementing priority queues or heaps.
  - Implementing interval trees or segment trees.
  - Implementing order statistics or rank queries.



### B-Trees

- A B-tree is a **self-balancing** tree data structure that maintains **sorted** data and allows **searches, sequential access, insertions, and deletions** in logarithmic time   .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children .
- A B-tree of order m has the following properties :
  - Each node can have at most m children and m-1 keys.
  - Each node, except the root and the leaves, must have at least ⌈m/2⌉ children and ⌈m/2⌉-1 keys.
  - The root must have at least two children if it is not a leaf node.
  - All the leaves must be at the same level, and they have no children.
  - The keys in each node are stored in ascending order, and they act as separators for the subtrees.
  - A key k in a node n means that all the keys in the subtree rooted at the left child of n are less than k, and all the keys in the subtree rooted at the right child of n are greater than or equal to k.
- The height of a B-tree with n keys and order m is bounded by log<sub>m/2</sub>(n+1) and log<sub>m</sub>(n+1) .
- The main operations on a B-tree are search, insert, and delete .
  - Search: To search for a key k in a B-tree, we start from the root and compare k with the keys in the current node. If k is found, we return the node and the index of k. If k is not found, we recursively search in the appropriate child subtree, or return null if there is no such child.
  - Insert: To insert a key k in a B-tree, we first search for the leaf node where k should be inserted. If the leaf node has less than m-1 keys, we simply insert k in the correct position and update the node. If the leaf node is full, we split it into two nodes and insert the middle key into the parent node, repeating this process until we reach a node that is not full or the root.
  - Delete: To delete a key k from a B-tree, we first search for the node that contains k. If k is in a leaf node, we simply remove it from the node and update the node. If k is in an internal node, we replace it with either its predecessor or successor in the tree, and then delete that key from the leaf node. If the deletion causes any node to have less than ⌈m/2⌉ children, we either borrow a key from a sibling node or merge two sibling nodes and delete a key from the parent node, repeating this process until we reach a node that has enough children or the root.
- B-trees are useful for storing and retrieving large amounts of data efficiently, especially on disk-based systems   .
  - B-trees minimize the number of disk accesses by keeping the tree height low and storing multiple keys in each node.
  - B-trees maintain the balance of the tree by splitting and merging nodes as needed, ensuring that all operations take logarithmic time.
  - B-trees can handle dynamic data that changes frequently, as they can grow and shrink gracefully.



### Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees, which are defined recursively as follows:
  - A binomial tree of order 0 is a single node
  - A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order)
- A binomial heap is a collection of binomial trees that satisfy the following properties:
  - There is at most one binomial tree of each order in the heap
  - The roots of the binomial trees are arranged in a linked list in increasing order of their order
  - Each binomial tree in the heap is a min-heap, i.e., the key of the root is smaller than or equal to the keys of its children
- The main operations on a binomial heap are:
  - Insert: To insert a new element, create a binomial heap with a single node and merge it with the existing heap
  - DeleteMin: To delete the minimum element, find the root with the smallest key, remove it and its children from the heap, and merge the children into a new heap, then merge the new heap with the existing heap
  - Merge: To merge two binomial heaps, merge their root lists by order, and then combine any two binomial trees of the same order into a larger one by making one tree a child of the other
- The time complexity of the operations on a binomial heap are:
  - Insert: O(log n) amortized
  - DeleteMin: O(log n) amortized
  - Merge: O(log n) amortized
- Binomial heaps are useful for implementing mergeable heaps, which are priority queues that support merging two heaps into one. They are also used in some algorithms for graph problems, such as Dijkstra's algorithm and Prim's algorithm.



### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- A Fibonacci heap is a specific implementation of the heap data structure that makes use of Fibonacci numbers. Fibonacci heaps are used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis. For the Fibonacci heap, the find-minimum operation takes constant (O(1)) amortized time. The insert and decrease key operations also work in constant amortized time. The delete and delete-minimum operations work in O(log n) amortized time, where n is the size of the heap.
- The structure of a Fibonacci heap is more flexible than a binary heap or a binomial heap. A Fibonacci heap does not have a fixed shape, and it allows the trees to have arbitrary degree. The trees are linked together by a circular doubly linked list, which maintains the roots of the trees. The minimum element of the heap can be easily accessed by a pointer to the minimum root .
- A Fibonacci heap supports the following operations:

  - **make-heap**: creates and returns a new empty Fibonacci heap.
  - **insert**: inserts a new node with a given key into the heap.
  - **find-min**: returns the node with the minimum key in the heap.
  - **union**: merges two Fibonacci heaps into one, and returns the resulting heap.
  - **extract-min**: removes and returns the node with the minimum key from the heap, and rearranges the remaining nodes.
  - **decrease-key**: decreases the key of a given node in the heap, and updates the heap structure if necessary.
  - **delete**: removes a given node from the heap, and updates the heap structure if necessary.

- The main idea behind the Fibonacci heap is to delay the work of consolidating the trees until a delete or extract-min operation is performed. This way, the insert and decrease-key operations can be done quickly, and the amortized cost of the other operations can be reduced. The Fibonacci heap uses two techniques to achieve this: lazy insertion and cascading cut.
- Lazy insertion means that when a new node is inserted into the heap, it is simply added to the root list, without merging it with any existing tree. This allows the insert operation to be done in constant time, but it may increase the number of trees in the heap.
- Cascading cut means that when a node is cut from its parent due to a decrease-key operation, it is marked to indicate that it has lost one child. If a marked node loses another child, it is cut from its parent as well, and the parent is marked. This process continues until either the root is reached, or an unmarked node is found. This allows the decrease-key operation to be done in constant time, but it may increase the potential of the heap, which is a measure of how much work is deferred.
- The potential of a Fibonacci heap is defined as:

  - phi(H) = t(H) + 2m(H)

  where t(H) is the number of trees in the root list of H, and m(H) is the number of marked nodes in H.

- The potential of a Fibonacci heap is used to analyze the amortized running time of the operations. The amortized cost of an operation is defined as:

  - hat{c}(i) = c(i) + phi(H_i) - phi(H_{i-1})

  where c(i) is the actual cost of the i-th operation, and H_i is the state of the heap after the i-th operation.

- The amortized running time of the Fibonacci heap operations are as follows:

  - **make-heap**: O(1) (actual and amortized)
  - **insert**: O(1) (actual and amortized)
  - **find-min**: O(1) (actual and amortized)
  - **union**: O(1) (actual and amortized)
  - **extract-min**: O(log n) (amortized)
  - **decrease-key**: O(



### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings over an alphabet .
- The word trie comes from the word re**trie**val, which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has k children, one for each character in the alphabet.
- A trie can store any finite set of strings, such as words, phone numbers, URLs, etc.
- A trie can perform the following operations efficiently:
  - Insert: To add a new string to the trie, we start from the root and follow the path corresponding to the characters of the string. If the path does not exist, we create new nodes along the way. We mark the last node as the end of the string.
  - Search: To search for a string in the trie, we start from the root and follow the path corresponding to the characters of the string. If the path exists and the last node is marked as the end of the string, we return true. Otherwise, we return false.
  - Delete: To delete a string from the trie, we first search for it. If it is not present, we do nothing. If it is present, we unmark the last node as the end of the string. Then, we delete the nodes from the bottom up, until we reach a node that has more than one child or is marked as the end of another string.
- A trie has the following advantages over a hash table:
  - A trie can handle prefix queries, such as finding all the strings that start with a given prefix, efficiently .
  - A trie can handle substring queries, such as finding all the strings that contain a given substring, efficiently .
  - A trie can handle wildcard queries, such as finding all the strings that match a given pattern with some unknown characters, efficiently .
  - A trie can handle approximate matching queries, such as finding all the strings that are within a given edit distance from a given string, efficiently .
  - A trie can save space by sharing common prefixes among the strings .
- A trie has the following disadvantages over a hash table:
  - A trie can have a high memory overhead, especially if the alphabet is large and the strings are short .
  - A trie can have a high traversal cost, especially if the strings are long and the trie is deep .
  - A trie can have a high insertion and deletion cost, especially if the strings are long and the trie is deep .
- A trie can be modified or optimized in various ways, such as using compression, hashing, arrays, bitmaps, etc., to improve its performance and reduce its space .



### Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis .

- A skip list consists of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The bottom layer contains all the elements of the sorted list, and the top layer contains only a few elements that act as shortcuts for faster traversal.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- The elements in the higher layers are chosen randomly with some probability, such that the expected number of elements in each layer is half of the previous one.
- The skip list has a special element called the head, which is present in all the layers and points to the first element of each layer. It also has a special element called the tail, which is present in all the layers and points to null.
- The skip list also has a variable called the level, which stores the current number of layers in the skip list.

The following image shows an example of a skip list with four layers:

skip list example

- To search for an element in a skip list, we start from the head of the top layer and compare the element with the next element in the same layer. If the element is smaller, we move to the next element. If the element is larger, we move down to the lower layer and repeat the process. If the element is equal, we have found the element. If we reach the bottom layer and the element is not found, we conclude that the element is not in the list.
- To insert an element in a skip list, we first search for the element and find the position where it should be inserted in the bottom layer. Then, we create a new node with the element and insert it in the bottom layer. Next, we toss a coin and decide whether to insert the element in the next higher layer or not. If the coin is heads, we insert the element in the next higher layer and repeat the coin toss. If the coin is tails, we stop the insertion. If we reach the top layer and the coin is still heads, we create a new layer and insert the element in it, and update the level of the skip list.
- To delete an element from a skip list, we first search for the element and find all the nodes that contain it in different layers. Then, we remove all the nodes that contain the element and update the pointers of the previous and next nodes. If the top layer becomes empty after the deletion, we remove the top layer and update the level of the skip list.

The following are some advantages and disadvantages of skip lists:

- Advantages:
  - Skip lists are simpler to implement than balanced trees, and use less space.
  - Skip lists can handle dynamic insertion and deletion of elements without rebalancing the structure.
  - Skip lists can support range queries and ordered operations efficiently.
- Disadvantages:
  - Skip lists are probabilistic, meaning that their performance is not guaranteed in the worst case.
  - Skip lists require extra space for storing the pointers and the random number generator.
  - Skip lists are sensitive to the choice of the probability parameter, which affects the balance and the height of the structure.

The following are some applications and variations of skip lists:

- Applications:
  - Skip lists can be used to implement sorted sets and maps, which support fast lookup, insertion and deletion of key-value pairs.
  - Skip lists can be used to implement priority queues, which support fast insertion and extraction of elements with different priorities.
  - Skip lists can be used to implement concurrent data structures, which allow multiple threads to access and modify the structure without locking.
- Variations:
  - Deterministic skip lists, which use a deterministic rule to decide the height of each element, instead of a random coin toss.
  - Indexable skip lists, which allow fast access to the element at a given rank or position in the sorted list.
  - Multi-level skip lists, which use multiple skip lists with different probability parameters to achieve better performance.
  - Skip graphs, which extend skip lists to support distributed and dynamic data structures.

: Skip list - Wikipedia
: Skip List | Set 1 (Introduction) -



# Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

## Divide and Conquer
- Divide and conquer is a technique of solving complex problems by breaking them into smaller and simpler subproblems that can be solved independently and then combining the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer has three steps:
  - Divide: Split the problem into smaller subproblems of the same type.
  - Conquer: Solve each subproblem recursively or directly if they are simple enough.
  - Combine: Merge the solutions of the subproblems to get the solution of the original problem.
- Divide and conquer is useful for problems that have the following properties:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems can be solved independently and their solutions can be combined efficiently.
  - The subproblems are not too many or too small, otherwise the overhead of dividing and combining may outweigh the benefits of solving them separately.

### Examples of Divide and Conquer
- Sorting: Sorting is the problem of arranging a list of elements in a certain order, such as ascending or descending. Sorting can be done using divide and conquer by splitting the list into two halves, sorting each half recursively, and then merging the two sorted halves into one sorted list. This is the idea behind merge sort and quick sort algorithms, which have a time complexity of O(n log n) in the average case, where n is the number of elements in the list.
- Matrix Multiplication: Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining a new matrix as the result. Matrix multiplication can be done using divide and conquer by splitting each matrix into four submatrices of equal size, multiplying each pair of submatrices recursively, and then adding the results to get the final matrix. This is the idea behind Strassen's algorithm, which has a time complexity of O(n^2.81), where n is the dimension of the matrices.
- Convex Hull: Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane. Convex hull can be done using divide and conquer by splitting the set of points into two halves, finding the convex hull of each half recursively, and then merging the two convex hulls into one convex hull. This is the idea behind Graham scan and Chan's algorithm, which have a time complexity of O(n log n) and O(n log h), where n is the number of points and h is the number of vertices in the convex hull.
- Searching: Searching is the problem of finding a target element in a list of elements or a key in a dictionary of key-value pairs. Searching can be done using divide and conquer by splitting the list or the dictionary into two halves, checking which half contains the target element or the key, and then searching that half recursively. This is the idea behind binary search and interpolation search algorithms, which have a time complexity of O(log n) and O(log log n) in the average case, where n is the number of elements or the size of the dictionary.

## Greedy Methods
- Greedy methods are a technique of solving optimization problems by making a sequence of choices that look best at the moment, without considering the future consequences of those choices. Greedy methods are based on the assumption that a locally optimal choice will lead to a globally optimal solution.
- Greedy methods have two steps:
  - Selection: Choose the next element that offers the most benefit or the least cost according to some criterion.
  - Feasibility: Check if the chosen element is compatible with the current solution and the problem constraints.
- Greedy methods are useful for problems that have the following properties:
  - The problem can be decomposed into a sequence of choices or steps.
  - There is a clear criterion to compare and rank the choices or steps.
  - There is an optimal substructure, meaning that an optimal solution to the problem contains optimal solutions to the subproblems.
  - There is a greedy choice property, meaning that a locally optimal choice is always part of an optimal solution.

### Examples of Greedy Methods
- Optimal Reliability Allocation: Optimal reliability allocation is the problem of allocating a given budget to improve the reliability of a system composed of n components, such that the overall reliability of the system is maximized. Optimal reliability allocation can be done using greedy methods by choosing the component that has the highest marginal increase in reliability per unit cost at each step, until



### Divide and Conquer with Examples Such as Sorting for the notes of the Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms. in the subject of Design and Analysis of Algorithm

#### Divide and Conquer
- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer can reduce the time complexity of some problems from polynomial to logarithmic or even constant.
- Divide and conquer can also reduce the space complexity of some problems by using less memory or auxiliary data structures.
- Some examples of problems that can be solved by divide and conquer are:

##### Sorting
- Sorting is the problem of arranging a sequence of elements in a certain order, such as ascending or descending.
- Sorting can be done by divide and conquer by splitting the sequence into two halves, sorting each half recursively, and merging the two sorted halves into one sorted sequence.
- Some sorting algorithms that use divide and conquer are:
  - Merge sort: splits the sequence into two equal halves, sorts each half, and merges them using a linear scan.
  - Quick sort: chooses a pivot element, partitions the sequence into two sub-sequences such that all elements less than the pivot are in the left sub-sequence and all elements greater than or equal to the pivot are in the right sub-sequence, sorts each sub-sequence recursively, and concatenates them.
  - Heap sort: builds a heap (a binary tree where each node is greater than or equal to its children) from the sequence, repeatedly extracts the maximum element from the heap and appends it to the end of the sorted sequence, and restores the heap property after each extraction.

##### Matrix Multiplication
- Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining their product matrix.
- Matrix multiplication can be done by divide and conquer by splitting each matrix into four sub-matrices of equal size, multiplying each pair of sub-matrices recursively, and adding or subtracting the results to obtain the product sub-matrices.
- Some matrix multiplication algorithms that use divide and conquer are:
  - Strassen's algorithm: reduces the number of recursive multiplications from eight to seven by using clever algebraic identities, and achieves a time complexity of O(n^2.807).
  - Coppersmith-Winograd algorithm: further reduces the number of recursive multiplications by using more sophisticated algebraic identities, and achieves a time complexity of O(n^2.376).

##### Convex Hull
- Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane.
- Convex hull can be done by divide and conquer by splitting the set of points into two halves by a vertical line, finding the convex hull of each half recursively, and merging the two convex hulls by finding their upper and lower tangents.
- Some convex hull algorithms that use divide and conquer are:
  - Graham scan: sorts the points by their polar angle with respect to the lowest point, and scans them in a counterclockwise order, adding each point to the convex hull and removing any previous point that makes a right turn with the last two points, until the starting point is reached again.
  - Jarvis march: starts with the leftmost point, and repeatedly finds the next point that forms the smallest positive angle with the last edge, until the starting point is reached again.

##### Searching
- Searching is the problem of finding an element in a sequence or a data structure that satisfies a given condition or matches a given value.
- Searching can be done by divide and conquer by splitting the sequence or the data structure into two halves, checking which half contains the element or satisfies the condition, and searching that half recursively.
- Some searching algorithms that use divide and conquer are:
  - Binary search: assumes that the sequence is sorted, and compares the middle element with the target value, discarding the half that does not contain the target, and repeating until the target is found or the sequence is empty.
  - Interpolation search: assumes that the sequence is sorted and uniformly distributed, and estimates the position of the target value based on the first and last elements, discarding the half that does not contain the target, and repeating until the target is found or the sequence is empty.
  - Bisection method: assumes that the sequence is a continuous function that changes sign at the target value, and finds the midpoint of the interval, discarding the



### Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer has three main steps:
  - Divide: Split the problem into smaller and simpler subproblems, usually of the same type as the original problem.
  - Conquer: Solve the subproblems recursively, either directly or by applying divide and conquer again.
  - Combine: Combine the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer is useful for solving problems that have the following characteristics:
  - The problem can be divided into smaller and simpler subproblems of the same type.
  - The subproblems can be solved independently and in parallel.
  - The subproblems are not too small or too many, otherwise the overhead of dividing and combining may outweigh the benefits of parallelism and simplicity.
  - The solutions of the subproblems can be combined efficiently to obtain the solution for the original problem.
- Some examples of problems that can be solved by divide and conquer are:
  - Sorting: Given an array of n elements, sort them in ascending or descending order. For example, merge sort and quick sort are divide and conquer algorithms that sort an array by dividing it into two halves, sorting them recursively, and merging or partitioning them respectively.
  - Matrix multiplication: Given two matrices A and B of size n x n, compute their product C = A x B. For example, Strassen's algorithm is a divide and conquer algorithm that multiplies two matrices by dividing them into four submatrices of size n/2 x n/2, computing seven products of submatrices recursively, and combining them to obtain the final product.
  - Convex hull: Given a set of n points in the plane, find the smallest convex polygon that contains all the points. For example, Graham scan is a divide and conquer algorithm that finds the convex hull by sorting the points by their polar angle, dividing them into upper and lower halves, finding the upper and lower hulls recursively, and merging them to obtain the final hull.
  - Searching: Given a sorted array of n elements and a target value, find the index of the target value in the array or report that it does not exist. For example, binary search is a divide and conquer algorithm that searches for a target value by comparing it with the middle element of the array, dividing the array into two halves depending on the comparison result, and searching recursively in the appropriate half.



### Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is an algorithm design paradigm that recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
- The solutions to the sub-problems are then combined to give a solution to the original problem.
- Divide and conquer algorithms are naturally adapted for execution in multi-processor machines, especially shared-memory systems where the communication of data between processors does not need to be planned in advance because distinct sub-problems can be executed on different processors.
- Divide and conquer algorithms have three main steps:
  - Divide the problem into a number of sub-problems that are smaller instances of the same problem.
  - Conquer the sub-problems by solving them recursively. If they are small enough, solve the sub-problems as base cases.
  - Combine the solutions to the sub-problems into the solution for the original problem.
- Some examples of divide and conquer algorithms are:
  - Sorting algorithms such as merge sort, quick sort and heap sort.
  - Matrix multiplication algorithms such as Strassen's algorithm and Coppersmith–Winograd algorithm.
  - Convex hull algorithms such as Graham scan and Chan's algorithm.
  - Searching algorithms such as binary search and interpolation search.

- A convex hull of a set of points is the smallest convex polygon that contains all the points.
- A convex polygon is a polygon in which no line segment between two points on the boundary ever goes outside the polygon.
- Finding the convex hull of a set of points is a fundamental problem in computational geometry, with applications in pattern recognition, image processing, statistics, geographic information systems, robotics and more.
- There are many algorithms for finding the convex hull of a set of points, some of which are based on the divide and conquer approach.
- One such algorithm is the Graham scan, which works as follows:
  - Choose a point p with the lowest y-coordinate (if there are ties, choose the one with the lowest x-coordinate as well). This point is the first vertex of the convex hull and is called the pivot.
  - Sort the remaining points by the angle they make with the pivot and the positive x-axis, in counterclockwise order. If two points have the same angle, keep the one that is closer to the pivot.
  - Push the pivot and the first two sorted points onto a stack.
  - For each remaining point in the sorted order, do the following:
    - While the angle formed by the top two points on the stack and the current point makes a right turn or is collinear, pop the top point from the stack.
    - Push the current point onto the stack.
  - The points remaining on the stack form the vertices of the convex hull in counterclockwise order.



### Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer .
- Divide and conquer algorithms have three main steps: divide, conquer, and combine .
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, usually of the same type as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure and properties.
- Some examples of divide and conquer algorithms are:
  - Sorting: Sorting is the problem of arranging a list of elements in a certain order, such as ascending or descending. Some sorting algorithms that use divide and conquer are:
    - Merge sort: This algorithm divides the list into two halves, sorts each half recursively, and then merges the two sorted halves into one sorted list .
    - Quick sort: This algorithm partitions the list around a pivot element, such that all elements smaller than the pivot are on its left and all elements larger than the pivot are on its right. Then it sorts the two sublists recursively .
  - Matrix multiplication: Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining a new matrix as the result. A naive algorithm for matrix multiplication takes O(n^3) time, where n is the dimension of the matrices. A divide and conquer algorithm that improves the time complexity is:
    - Strassen's algorithm: This algorithm divides each matrix into four submatrices of equal size, and then computes the product of the two matrices using seven multiplications and some additions and subtractions of the submatrices. The algorithm can be applied recursively to reduce the number of multiplications to O(n^2.8974) time .
  - Convex hull: Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane. A convex polygon is one that has no interior angles greater than 180 degrees. A divide and conquer algorithm for convex hull is:
    - Graham scan: This algorithm first finds the point with the lowest y-coordinate, and then sorts the rest of the points by the angle they make with the horizontal line passing through the lowest point. Then it scans the sorted points from left to right, and maintains a stack of points that form the convex hull so far. At each step, it checks if the next point makes a left or right turn with the top two points on the stack, and discards the top point if it makes a right turn. The algorithm takes O(n log n) time, where n is the number of points.
  - Searching: Searching is the problem of finding a target element in a list or a data structure. Some searching algorithms that use divide and conquer are:
    - Binary search: This algorithm assumes that the list is sorted, and then repeatedly divides the list into two halves, and compares the middle element with the target. If the target is equal to the middle element, it returns its index. If the target is smaller than the middle element, it searches in the left half. If the target is larger than the middle element, it searches in the right half. The algorithm takes O(log n) time, where n is the length of the list .
    - Interpolation search: This algorithm also assumes that the list is sorted and uniformly distributed, and then estimates the position of the target based on the first and last elements of the list. If the target is equal to the estimated position, it returns its index. If the target is smaller than the estimated position, it searches in the left subarray. If the target is larger than the estimated position, it searches in the right subarray. The algorithm takes O(log log n) time on average, but O(n) time in the worst case, where n is the length of the list.

### Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms



### Greedy Methods with Examples

A greedy method is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy methods are often used to solve optimization problems, where the goal is to find the best solution according to a given criterion. Greedy methods are easy to implement and usually fast, but they may not always produce the optimal solution.

Some examples of greedy methods are:

- **Optimal Reliability Allocation**: This is a problem of allocating a given budget to improve the reliability of a system composed of several components. A greedy method would choose the component that has the highest ratio of reliability improvement to cost at each step, until the budget is exhausted or all components are improved.
- **Knapsack Problem**: This is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity. A greedy method would choose the item that has the highest value per unit weight at each step, until the knapsack is full or no more items are left.
- **Minimum Spanning Tree**: This is a problem of finding a subset of edges in a weighted graph that connects all the vertices with the minimum total weight. A greedy method would choose the edge that has the lowest weight at each step, as long as it does not create a cycle in the tree.
- **Single Source Shortest Paths**: This is a problem of finding the shortest paths from a given source vertex to all other vertices in a weighted graph. A greedy method would choose the vertex that has the lowest distance from the source at each step, and update the distances of its adjacent vertices accordingly. There are two famous greedy methods for this problem: Dijkstra's algorithm and Bellman-Ford algorithm.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step, without considering the future consequences.

Some examples of greedy methods are:

- **Fractional Knapsack Problem**: Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, find the maximum value that can be obtained by filling the knapsack with fractions of items. The greedy choice is to pick the item with the highest value-to-weight ratio first, and then the next highest, and so on, until the knapsack is full or no more items are left.
- **Minimum Spanning Tree**: Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. The greedy choice is to pick the edge with the lowest weight that does not form a cycle with the already selected edges, and repeat until all the vertices are connected or no more edges are left.
- **Single Source Shortest Path**: Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex. The greedy choice is to pick the vertex with the smallest distance from the source that has not been visited yet, and update the distances of its adjacent vertices, and repeat until all the vertices are visited or no more vertices are reachable.
- **Activity Selection Problem**: Given a set of activities, each with a start and finish time, find the maximum number of activities that can be performed by a single person, assuming that a person can only work on one activity at a time. The greedy choice is to pick the activity that finishes the earliest, and then the next earliest, and so on, until no more activities are compatible with the already selected ones.
- **Job Sequencing Problem**: Given a set of jobs, each with a deadline and a profit, find the maximum profit that can be earned by scheduling the jobs on a single machine, assuming that each job takes one unit of time and only one job can be done at a time. The greedy choice is to sort the jobs in decreasing order of profit, and assign the highest profit job to the first available slot, and so on, until no more jobs or slots are left.
- **Huffman Code Generation**: Given a set of characters and their frequencies, find a variable-length binary code that minimizes the total number of bits required to encode a given message. The greedy choice is to merge the two characters with the lowest frequencies into a new node, and assign them 0 and 1 as their codes, and repeat until only one node is left, which is the root of the Huffman tree. The code for each character is obtained by traversing the tree from the root to the leaf corresponding to that character.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that solve optimization problems by making locally optimal choices at each step, hoping to find a global optimum. Greedy algorithms are often simple, fast, and easy to implement, but they may not always produce the best solution for every problem.

Some of the characteristics of greedy algorithms are:

- They make a sequence of choices, each of which is the best available option at the time.
- They do not reconsider the previous choices, nor do they look ahead to the future consequences of the current choice.
- They terminate when they reach a final state, which may or may not be optimal.

Some of the advantages and disadvantages of greedy algorithms are:

- Advantages:
  - They are usually efficient and have a low time complexity.
  - They are often intuitive and easy to code.
  - They can be used as a heuristic or approximation for some hard problems.
- Disadvantages:
  - They may not always find the optimal solution, especially if the problem has a global structure that is not captured by the local choices.
  - They may be difficult to prove correct or analyze for their performance.
  - They may not work well for problems that require backtracking or dynamic programming.

Some of the examples of greedy algorithms are:

- Minimum Spanning Trees (MST): A minimum spanning tree is a subset of edges of a connected, undirected, weighted graph that connects all the vertices with the minimum possible total edge weight. There are two popular greedy algorithms for finding MST: Prim's algorithm and Kruskal's algorithm .
  - Prim's algorithm: This algorithm starts with an arbitrary vertex and grows the MST by adding the cheapest edge that connects a vertex in the MST to a vertex outside the MST, until all the vertices are included.
  - Kruskal's algorithm: This algorithm sorts all the edges by their weight and adds them to the MST one by one, as long as they do not create a cycle, until all the vertices are connected.
- Single Source Shortest Paths (SSSP): A single source shortest path problem is to find the shortest paths from a given source vertex to all other vertices in a weighted, directed or undirected graph. There are two well-known greedy algorithms for solving SSSP: Dijkstra's algorithm and Bellman-Ford algorithm .
  - Dijkstra's algorithm: This algorithm maintains a set of vertices whose shortest distance from the source is known, and a priority queue of vertices whose shortest distance is tentative. It repeatedly extracts the vertex with the minimum tentative distance from the queue, updates the distance of its neighbors, and adds them to the queue, until the queue is empty or the destination is reached.
  - Bellman-Ford algorithm: This algorithm relaxes all the edges of the graph for a number of times equal to the number of vertices minus one, updating the distance of each vertex to the minimum of its current distance and the distance of its predecessor plus the edge weight. It can also detect negative cycles in the graph, which make the shortest path problem undefined.
- Knapsack problem: A knapsack problem is to find the maximum value of items that can be packed into a knapsack with a limited capacity, given the weight and value of each item. There are two variants of the knapsack problem: 0-1 knapsack and fractional knapsack .
  - 0-1 knapsack: This problem only allows to take an item either completely or not at all. There is no greedy algorithm that can solve this problem optimally, but there are some heuristics that can give approximate solutions, such as sorting the items by their value-to-weight ratio and taking the most valuable ones until the capacity is reached or exceeded.
  - Fractional knapsack: This problem allows to take a fraction of an item, as long as the total weight does not exceed the capacity. There is a greedy algorithm that can solve this problem optimally, which is to sort the items by their value-to-weight ratio and take the most valuable ones until the capacity is reached or exceeded, and then take a fraction of the next item to fill the remaining space.
- Optimal Reliability Allocation: An optimal reliability allocation problem is to allocate a given budget to improve the reliability of a system composed of several components, such that the overall system reliability is maximized. There are several greedy algorithms that can solve this problem, such as the equal increment algorithm, the proportional algorithm, and the Lagrange multiplier algorithm[^



# Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast, and easy to implement, but they may not always yield the best solution.
- Greedy methods can be applied to various problems, such as optimal reliability allocation, knapsack, minimum spanning trees, and single source shortest paths.

## Single Source Shortest Paths

- The single source shortest paths problem is to find the shortest paths from a given source vertex to all other vertices in a weighted graph.
- The graph may contain positive or negative edge weights, but no negative cycles (a cycle whose total weight is negative).
- There are two well-known greedy algorithms for this problem: Dijkstra's algorithm and Bellman-Ford algorithm.

### Dijkstra's Algorithm

- Dijkstra's algorithm is a greedy algorithm that works for graphs with non-negative edge weights.
- The algorithm maintains a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined.
- The algorithm repeatedly extracts the vertex with the minimum distance from the source from the priority queue, and updates the distances of its adjacent vertices.
- The algorithm terminates when the priority queue is empty or the destination vertex is extracted.
- The time complexity of Dijkstra's algorithm is O((V+E)logV), where V is the number of vertices and E is the number of edges in the graph.
- Dijkstra's algorithm can be implemented using a Fibonacci heap, a binary heap, or an array as the priority queue.

### Bellman-Ford Algorithm

- Bellman-Ford algorithm is a greedy algorithm that works for graphs with negative edge weights, but no negative cycles.
- The algorithm iterates over all the edges of the graph V-1 times, where V is the number of vertices in the graph.
- In each iteration, the algorithm relaxes each edge, that is, it updates the distance of the destination vertex if it can be reduced by using the edge.
- The algorithm detects a negative cycle if it can relax any edge in the V-th iteration.
- The time complexity of Bellman-Ford algorithm is O(VE), where V is the number of vertices and E is the number of edges in the graph.
- Bellman-Ford algorithm is simpler than Dijkstra's algorithm and suits well for distributed systems.



# Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## Dynamic Programming
- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which leads to wasteful computation.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming avoids repeated computation by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have a recursive formulation, where the problem can be divided into smaller and simpler subproblems of the same type.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up.
- Top-down approach starts with the original problem and recursively solves the subproblems until the base cases are reached. The results of subproblems are stored in a table and retrieved when needed.
- Bottom-up approach starts with the base cases and iteratively builds up the solution of larger subproblems using the results of smaller subproblems stored in a table.
- Dynamic programming can be used to solve various problems such as knapsack, all pair shortest paths, resource allocation, etc.

## Knapsack Problem
- Knapsack problem is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized.
- Knapsack problem can be formulated as follows:

  - Let n be the number of items, W be the capacity of the knapsack, w[i] be the weight of the i-th item, and v[i] be the value of the i-th item, for i = 1, 2, ..., n.
  - Let x[i] be a binary variable that indicates whether the i-th item is packed or not, for i = 1, 2, ..., n.
  - The objective is to maximize the total value of the packed items, which is given by:

    - `sum(v[i] * x[i]) for i = 1, 2, ..., n`

  - The constraint is that the total weight of the packed items does not exceed the capacity of the knapsack, which is given by:

    - `sum(w[i] * x[i]) for i = 1, 2, ..., n <= W`

- Knapsack problem can be solved using dynamic programming by defining a subproblem as follows:

  - Let K[i][j] be the maximum value that can be obtained by packing items from 1 to i into a knapsack with capacity j, for i = 0, 1, 2, ..., n and j = 0, 1, 2, ..., W.
  - The base cases are:

    - K[0][j] = 0 for j = 0, 1, 2, ..., W, since no item can be packed.
    - K[i][0] = 0 for i = 0, 1, 2, ..., n, since the knapsack has no capacity.

  - The recursive relation is:

    - K[i][j] = max(K[i-1][j], K[i-1][j-w[i]] + v[i]) for i = 1, 2, ..., n and j = 1, 2, ..., W, since the i-th item can be either packed or not packed.

  - The optimal solution is given by K[n][W], which is the maximum value that can be obtained by packing items from 1 to n into a knapsack with capacity W.
  - The optimal subset of items can be traced back by checking the table K and comparing the values of K[i][j] and K[i-1][j] for i = n, n-1, ..., 1 and j = W, W-w[i], ..., 0.

- Knapsack problem can be solved using a top-down or a bottom-up approach, depending on whether the table K is filled recursively or iteratively.

## All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms
- All pair shortest paths problem is a problem of finding the shortest paths between every pair of vertices in a weighted graph, where the weight of an edge represents the distance or cost between the two vertices.
- All pair shortest paths problem can be formulated as follows:

  - Let G



### Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to avoid recomputing the same subproblem multiple times, by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have two properties: a recursive formulation and a memoization function.
- A recursive formulation is a way of expressing the problem in terms of smaller instances of the same problem, such as a recurrence relation or a recursive function.
- A memoization function is a way of mapping each subproblem to a unique index, such as a tuple of parameters or a hash value, that can be used to store and retrieve the results of subproblems in a table.
- Dynamic programming can be implemented in two ways: top-down and bottom-up.
- Top-down dynamic programming starts with the original problem and recursively solves the subproblems, while storing and reusing the results in a table. This approach is also known as memoization or lazy evaluation.
- Bottom-up dynamic programming starts with the smallest subproblems and iteratively solves larger subproblems, while storing and reusing the results in a table. This approach is also known as tabulation or eager evaluation.
- Dynamic programming can be used to solve various types of problems, such as optimization, counting, decision making, and path finding.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which is an optimization problem.

#### 0/1 Knapsack Problem

- The 0/1 knapsack problem is defined as follows: given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, and there is no fractional or partial inclusion of items.
- The 0/1 knapsack problem can be formulated as a recursive function as follows:

```
// K(n, W) is the maximum value that can be obtained by using items 1 to n with a weight limit of W
// w[i] and v[i] are the weight and value of item i, respectively
// n is the number of items and W is the weight limit

K(n, W) = 0, if n == 0 or W == 0 // base case
K(n, W) = K(n - 1, W), if w[n] > W // item n cannot be included
K(n, W) = max(K(n - 1, W), v[n] + K(n - 1, W - w[n])), if w[n] <= W // item n can be included or excluded
```

- The 0/1 knapsack problem can be solved using top-down dynamic programming by implementing the recursive function with a memoization table, such as a two-dimensional array, that stores the results of subproblems and avoids recomputing them.

```
// K[n][W] is the memoization table that stores the results of subproblems
// K[i][j] is the maximum value that can be obtained by using items 1 to i with a weight limit of j
// w[i] and v[i] are the weight and value of item i, respectively
// n is the number of items and W is the weight limit

// initialize the table with -1 values to indicate that the subproblems are not solved yet
for i = 0 to n
  for j = 0 to W
    K[i][j] = -1

// define the recursive function with memoization
K(n, W) = 0, if n == 0 or W == 0 // base case
K(n, W) = K[n][W], if K[n][W] != -1 // subproblem already solved
K(n, W) = K(n - 1, W), if w[n] > W // item n cannot be included
K(n, W) = max(K(n - 1, W), v[n] + K(n - 1, W - w[n])), if w[n] <= W //

```




### Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- Dynamic programming is a technique for solving optimization problems by breaking them down into smaller subproblems, and storing the solutions of the subproblems in a table to avoid recomputation.
- Dynamic programming can be applied to problems that have two properties: optimal substructure and overlapping subproblems.
- Optimal substructure means that the optimal solution of a problem can be obtained by using the optimal solutions of its subproblems.
- Overlapping subproblems means that the same subproblems are encountered and solved many times during the computation.
- One example of a problem that can be solved by dynamic programming is the all pair shortest path problem, which is to find the shortest distance between every pair of vertices in a weighted graph.
- There are two algorithms that can solve the all pair shortest path problem using dynamic programming: Warshal's algorithm and Floyd's algorithm.
- Warshal's algorithm is based on the idea of transitive closure, which is the set of all pairs of vertices that are reachable from each other in a graph.
- Warshal's algorithm works by initializing a matrix that contains the adjacency matrix of the graph, and then updating the matrix by adding intermediate vertices one by one, until all vertices are considered.
- Warshal's algorithm can be used to find the shortest paths in a graph that has only binary weights (0 or 1), or to find the reachability matrix of a graph.
- Floyd's algorithm is based on the idea of relaxation, which is the process of improving an estimate of the shortest distance between two vertices by using a third vertex as a intermediate point.
- Floyd's algorithm works by initializing a matrix that contains the weight matrix of the graph, and then updating the matrix by relaxing the edges one by one, until all edges are considered.
- Floyd's algorithm can be used to find the shortest paths in a graph that has any weights, positive or negative, as long as there are no negative cycles in the graph.
- Both Warshal's and Floyd's algorithms have a time complexity of O(n^3), where n is the number of vertices in the graph, and a space complexity of O(n^2), where n is the number of vertices in the graph.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on dynamic programming with examples such as resource allocation problem.

### Dynamic Programming

- Dynamic programming is a method of solving complex problems by breaking them down into simpler subproblems, and storing the results of the subproblems to avoid recomputing them.
- Dynamic programming can be applied to problems that have two main characteristics: optimal substructure and overlapping subproblems.
- Optimal substructure means that the optimal solution of a problem can be obtained by using the optimal solutions of its subproblems.
- Overlapping subproblems means that the same subproblems are encountered repeatedly while solving the problem, and hence their solutions can be reused.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up.
- Top-down approach starts with the original problem and divides it into smaller subproblems, until the base cases are reached. Then, the solutions of the subproblems are combined to obtain the solution of the original problem.
- Bottom-up approach starts with the base cases and builds up the solutions of larger subproblems, until the solution of the original problem is obtained.
- Dynamic programming can be used to solve various types of problems, such as shortest paths, longest common subsequence, knapsack, matrix chain multiplication, etc.

### Resource Allocation Problem

- Resource allocation problem is a type of optimization problem, where a limited amount of resources (such as time, money, materials, etc.) have to be allocated among several competing activities (such as projects, tasks, etc.) in order to maximize the total benefit or minimize the total cost.
- Resource allocation problem can be formulated as a linear programming problem, where the objective function and the constraints are linear functions of the decision variables.
- Resource allocation problem can also be solved using dynamic programming, if the problem has a discrete and finite set of decision variables, and the objective function and the constraints have the optimal substructure and overlapping subproblems properties.
- Dynamic programming can be applied to resource allocation problem by defining the state of the problem as the amount of resources available at each stage, and the decision as the amount of resources allocated to each activity at each stage.
- The objective function can be defined as the total benefit or cost obtained from the allocation of resources, and the constraints can be defined as the limits on the resources available and the resources required by each activity.
- The optimal solution can be obtained by finding the maximum or minimum value of the objective function over all possible states and decisions, using a recursive formula or a table.
- An example of resource allocation problem is the knapsack problem, where a knapsack with a limited capacity has to be filled with items that have different weights and values, in order to maximize the total value of the items in the knapsack.



# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a large space of possible solutions. They both use a recursive approach to explore the solution space in a systematic way, but they differ in how they prune the search tree and estimate the quality of partial solutions.

## Backtracking

Backtracking is a technique that tries to find all possible solutions to a problem by building a solution incrementally, one component at a time, and backtracking whenever a component of the solution cannot be extended to a complete solution. Backtracking is useful for solving problems that have a finite number of solutions, such as the n-queen problem, the sum of subsets problem, and the graph coloring problem.

The general algorithm for backtracking is as follows:

- Start with an empty solution vector and a set of constraints that define the problem.
- Choose a component of the solution vector and assign a value to it that satisfies the constraints.
- If the solution vector is complete, then print or store the solution and return.
- If the solution vector is not complete, then recursively try to extend the solution vector by choosing another component and assigning a value to it.
- If no value can be assigned to a component without violating the constraints, then backtrack to the previous component and try a different value.

The backtracking algorithm can be implemented using a stack data structure to store the solution vector and the current component. The algorithm can also be modified to stop after finding the first solution, or to find the best solution according to some objective function.

## Branch and Bound

Branch and bound is a technique that tries to find an optimal solution to a problem by exploring a subset of the solution space that contains the optimal solution. Branch and bound is useful for solving problems that have a continuous or discrete solution space, such as the travelling salesman problem, the knapsack problem, and the resource allocation problem.

The general algorithm for branch and bound is as follows:

- Start with an empty solution vector and a set of constraints that define the problem.
- Choose a component of the solution vector and assign a value to it that satisfies the constraints.
- Compute a lower bound and an upper bound for the objective function of the partial solution.
- If the lower bound is equal to the upper bound, then the partial solution is optimal and return it.
- If the lower bound is greater than the current best solution, then prune the branch and backtrack to the previous component.
- If the lower bound is less than the current best solution, then branch into subproblems by choosing another component and assigning different values to it.
- Repeat the above steps until all branches are explored or pruned.

The branch and bound algorithm can be implemented using a priority queue data structure to store the partial solutions and their bounds. The priority queue can be ordered by the lower bound, the upper bound, or a combination of both. The algorithm can also be modified to find all optimal solutions, or to find an approximate solution within a given error tolerance.

## Examples

### Travelling Salesman Problem

The travelling salesman problem (TSP) is a problem of finding the shortest tour that visits a given set of cities exactly once and returns to the starting city. The TSP can be formulated as a graph problem, where the cities are the vertices and the distances between them are the edge weights. The TSP is an NP-hard problem, meaning that there is no known polynomial-time algorithm that can solve it exactly.

One way to solve the TSP using branch and bound is as follows:

- Start with an empty tour and a set of unvisited cities.
- Choose a city and add it to the tour as the starting and ending city.
- Compute a lower bound for the tour length by adding the minimum edge weight incident to each unvisited city and dividing by two. This is known as the 1-tree relaxation of the TSP.
- Compute an upper bound for the tour length by using a heuristic algorithm, such as the nearest neighbor algorithm, to construct a feasible tour from the current city.
- If the lower bound is equal to the upper bound, then the tour is optimal and return it.
- If the lower bound is greater than the current best tour, then prune the branch and backtrack to the previous city.
- If the lower bound is less than the current best tour, then branch into subproblems by choosing another city and adding it to the tour.
- Repeat the above steps until all branches are explored or pruned.

### Graph Coloring

The graph coloring problem is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same



### Backtracking, Branch and Bound with Examples Such as Graph Coloring

Backtracking and branch and bound are two techniques for solving optimization problems that involve searching a large space of possible solutions. Both techniques use a state-space tree to represent the solution space and explore it in a systematic way. However, they differ in how they prune the tree and select the next node to visit.

#### Backtracking

Backtracking is a technique that tries to find a feasible solution by incrementally building a partial solution and then backtracking (undoing) the last decision if it leads to a dead end. Backtracking uses a depth-first search strategy to explore the state-space tree. It applies a bounding function to check whether the current partial solution can be extended to a complete solution or not. If not, it backtracks to the previous node and tries a different option. Backtracking can be used to solve problems that have a yes/no answer, such as whether a given graph can be colored with m colors or not.

An example of backtracking is the graph coloring problem. Given a graph and a number of colors m, the problem is to assign a color to each vertex of the graph such that no two adjacent vertices have the same color. A possible algorithm using backtracking is:

- Start with an empty color assignment (an array of size n, where n is the number of vertices).
- Pick the first vertex and assign it the first color.
- Recursively assign colors to the remaining vertices, starting from the second vertex.
- For each vertex, check if the current color assignment is safe, i.e., no two adjacent vertices have the same color. If yes, proceed to the next vertex. If no, backtrack and try a different color.
- If all vertices are colored, print the color assignment and return true. If no color assignment is possible, return false.

#### Branch and Bound

Branch and bound is a technique that tries to find an optimal solution by exploring only the promising branches of the state-space tree. Branch and bound uses a breadth-first search strategy to explore the state-space tree. It applies a bounding function to estimate the lower and upper bounds of the optimal solution for each node. It then uses these bounds to prune the nodes that cannot lead to a better solution than the current best solution. Branch and bound can be used to solve problems that have a numerical answer, such as finding the minimum cost of traveling through a set of cities.

An example of branch and bound is the traveling salesman problem. Given a set of n cities and the distances between them, the problem is to find the shortest tour that visits each city exactly once and returns to the starting city. A possible algorithm using branch and bound is:

- Start with an empty tour (a list of size n+1, where n is the number of cities).
- Pick the first city as the starting and ending point of the tour.
- Recursively add cities to the tour, starting from the second city.
- For each city, calculate the cost of the current tour and the lower bound of the remaining tour using a heuristic function (such as the minimum spanning tree of the unvisited cities).
- If the cost of the current tour plus the lower bound is less than the current best cost, proceed to the next city. If not, prune the current node and backtrack to the previous city.
- If all cities are visited, update the current best cost and tour if the current tour is better. Return the current best cost and tour.



# Backtracking with Examples Such as n-Queen Problem

- Backtracking is a technique to solve problems that involve finding all possible solutions or configurations that satisfy some constraints or criteria.
- Backtracking works by exploring the solution space incrementally, making a partial choice at each step, and then checking if the choice is feasible or not.
- If the choice is feasible, then the algorithm continues to make further choices until a complete solution is found or no more choices are available.
- If the choice is not feasible, then the algorithm backtracks, i.e., it undoes the last choice and tries a different alternative.
- Backtracking is often implemented using recursion, where each recursive call represents a choice and the base case represents a solution or a dead end.
- Backtracking can be applied to many problems, such as puzzles, games, combinatorial optimization, constraint satisfaction, etc.

## n-Queen Problem

- n-Queen problem is one of the most common examples of backtracking.
- n-Queen problem is defined as, “given n x n chess board, arrange n queens in such a way that no two queens attack each other by being in same row, column or diagonal”.
- For n = 1, this is a trivial case. For n = 2 or n = 3, there is no solution. For n >= 4, there are one or more solutions.
- One way to solve the n-Queen problem using backtracking is as follows:

  - Start from the first row of the board and place a queen in the first column.
  - Move to the next row and try to place a queen in each column, checking if it is safe or not. A queen is safe if it does not share the same row, column or diagonal with any other queen on the board.
  - If a safe column is found, place the queen and recurse for the next row. If no safe column is found, backtrack to the previous row and move the queen to the next safe column.
  - Repeat this process until all the rows are filled with queens or no more safe columns are left.

- The pseudocode for the algorithm is given below:

```
# n is the size of the board
# board is a 2D array of size n x n, initialized with 0
# row is the current row to place a queen

def solve_n_queen(n, board, row):
  # base case: all rows are filled with queens
  if row == n:
    return True
  
  # try each column in the current row
  for col in range(n):
    # check if the queen can be placed safely
    if is_safe(board, row, col):
      # place the queen
      board[row][col] = 1
      # recurse for the next row
      if solve_n_queen(n, board, row + 1):
        return True
      # backtrack if the next row cannot be solved
      board[row][col] = 0
  
  # no solution for the current row
  return False

def is_safe(board, row, col):
  # check the same column
  for i in range(row):
    if board[i][col] == 1:
      return False
  
  # check the upper left diagonal
  i = row - 1
  j = col - 1
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1
  
  # check the upper right diagonal
  i = row - 1
  j = col + 1
  while i >= 0 and j < len(board):
    if board[i][j] == 1:
      return False
    i -= 1
    j += 1
  
  # the queen is safe
  return True
```

- The time complexity of the algorithm is O(n^n), where n is the size of the board. This is because there are n possible choices for each row, and there are n rows to fill.
- The space complexity of the algorithm is O(n^2), where n is the size of the board. This is because the board is a 2D array of size n x n, and the recursive call stack can go up to n levels deep.



### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- Backtracking can be viewed as a depth-first search of a state space tree, where each node represents a partial solution, and the branches are the possible extensions of the partial solution. 
- Backtracking can be applied to problems that involve making a sequence of decisions, such as finding a path in a maze, placing queens on a chessboard, or coloring a graph. 
- A general backtracking algorithm can be described as follows: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- Here, P is the problem instance, c is a candidate solution, reject is a function that checks if c is invalid, accept is a function that checks if c is a complete solution, output is a function that prints or stores the solution, first is a function that returns the first extension of c, and next is a function that returns the next extension of c.
- An example of a problem that can be solved by backtracking is the Hamiltonian cycle problem, which asks whether there is a cycle in a given graph that visits every vertex exactly once. 
- A possible backtracking algorithm for this problem is: 

```
procedure hamiltonian(G, v) is
    if v is the first vertex then
        mark v as visited
        add v to the cycle
    if all vertices are visited then
        if there is an edge from v to the first vertex then
            output the cycle
            return true
        else
            return false
    for each neighbor u of v do
        if u is not visited then
            mark u as visited
            add u to the cycle
            if hamiltonian(G, u) then
                return true
            else
                unmark u as visited
                remove u from the cycle
    return false
```

- Here, G is the graph, v is the current vertex, and the cycle is a list of vertices that forms the potential solution. The algorithm starts from an arbitrary vertex, and recursively explores all possible extensions of the cycle, backtracking when a dead end is reached. The algorithm outputs the cycle if it finds one, or returns false otherwise.



### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm reduces the problem to the call `backtrack (root (P))`, where `backtrack` is the following recursive procedure: 

```
procedure backtrack (P, c) is
    if reject (P, c) then return
    if accept (P, c) then output (P, c)
    s ← first (P, c)
    while s ≠ NULL do
        backtrack (P, s)
        s ← next (P, s)
```

- The procedure `backtrack` takes two arguments: a problem `P` and a candidate `c`. The problem `P` defines the constraints and the goal of the problem, and the candidate `c` is a partial solution that may or may not satisfy the constraints or the goal. 
- The procedure `reject` returns `true` if the candidate `c` violates any of the constraints of `P`, and `false` otherwise. The procedure `accept` returns `true` if the candidate `c` satisfies the goal of `P`, and `false` otherwise. The procedure `output` prints or stores the solution `c`. 
- The procedure `first` returns the first extension of the candidate `c`, and the procedure `next` returns the next extension of the candidate `c`, or `NULL` if there is no more extension. The extensions are the possible ways of adding one more element to the partial solution `c`. 
- The backtracking algorithm works by exploring the state space tree of the problem, where each node represents a partial solution. The root node is the empty solution, and the leaves are the complete solutions. The algorithm traverses the tree in depth-first order, pruning the branches that do not lead to valid solutions. 
- An example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value. 
- The sum of subsets problem can be formulated as follows: 

```
Given a set S = {s1, s2, ..., sn} of n positive integers and a target value t, find all the subsets of S that sum up to t.
```

- A possible solution using backtracking is to use an array `x` of size `n` to store the inclusion status of each element in `S`. That is, `x[i] = 1` if `si` is included in the subset, and `x[i] = 0` otherwise. 
- The algorithm starts with an empty subset (`x[i] = 0` for all `i`) and a sum of zero. It then tries to add the first element `s1` to the subset, and checks if the sum is equal to, less than, or greater than the target value. If the sum is equal to the target value, it outputs the subset and backtracks. If the sum is less than the target value, it recursively explores the remaining elements. If the sum is greater than the target value, it prunes the branch and backtracks. 
- The algorithm repeats the same process for the case when the first element `s1` is not included in the subset, and continues until all the elements are considered. 
- The pseudocode of the algorithm is as follows: 

```
procedure sum_of_subsets (S, t) is
    n ← length of S
    x ← an array of size n initialized to 0
    backtrack (S, t, x, 0, 0)

procedure backtrack (S, t, x, k, sum) is
    if sum = t then
        output x
    else if sum < t and k < n then

```




## Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the difficulty of solving certain problems in polynomial time. A problem is said to be NP-complete if it belongs to the class NP (nondeterministic polynomial time) and every other problem in NP can be reduced to it in polynomial time. This means that if there is an efficient algorithm for solving one NP-complete problem, then there is an efficient algorithm for solving all NP problems. However, no such algorithm is known to exist, and many computer scientists believe that none exists.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. Optimization problems are those that seek to find the best solution among a set of feasible solutions, according to some objective function. For example, the Travelling Salesman Problem (TSP) is to find the shortest tour that visits a given set of cities exactly once and returns to the starting city. An approximation algorithm does not guarantee the best solution, but rather a solution that is close to the optimal one, within some error bound. The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time  .
- Some examples of NP-complete problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): As mentioned above, this problem is to find the shortest tour that visits a given set of cities exactly once and returns to the starting city. One approximation algorithm for this problem is the nearest neighbor heuristic, which starts from a random city and repeatedly visits the nearest unvisited city until all cities are visited. This algorithm has a worst-case approximation ratio of 2, which means that the length of the tour produced by the algorithm is at most twice the length of the optimal tour.
  - Graph Coloring: This problem is to assign colors to the vertices of a graph such that no two adjacent vertices have the same color, and the number of colors used is minimized. One approximation algorithm for this problem is the greedy algorithm, which assigns colors to the vertices in some order, and for each vertex, chooses the smallest available color that does not conflict with any of its neighbors. This algorithm has a worst-case approximation ratio of Δ + 1, where Δ is the maximum degree of the graph.
  - n-Queen Problem: This problem is to place n queens on an n x n chessboard such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. One approximation algorithm for this problem is the backtracking algorithm, which tries to place a queen in each row, and if a conflict occurs, backtracks to the previous row and tries a different column. This algorithm has a worst-case time complexity of O(n^n), which is exponential, but it always finds a solution if one exists.
  - Hamiltonian Cycle: This problem is to find a cycle that visits every vertex of a graph exactly once and returns to the starting vertex. One approximation algorithm for this problem is the Christofides algorithm, which works as follows: first, find a minimum spanning tree of the graph, then find a minimum weight perfect matching of the odd-degree vertices in the tree, and finally, combine the tree and the matching to form a cycle. This algorithm has a worst-case approximation ratio of 3/2, which means that the length of the cycle produced by the algorithm is at most 3/2 times the length of the optimal cycle.
  - Sum of Subsets: This problem is to find a subset of a given set of positive integers that sums up to a given target value, or determine that no such subset exists. One approximation algorithm for this problem is the greedy algorithm, which sorts the integers in descending order, and then adds them to the subset one by one, as long as the sum does not exceed the target value. This algorithm has a worst-case approximation ratio of 2, which means that the sum of the subset produced by the algorithm is at most twice the target value.

: https://www.geeksforgeeks.org/approximation-algorithms/
: https://www.javatpoint.com/daa-approximate-algorithms
: https://iq.opengenus.org/approximation-algorithms-intro/
: https://iq.opengenus.org/n-queen



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A decision problem is NP-complete if it satisfies two conditions:
  - It is in NP, which means that a given solution can be verified in polynomial time.
  - It is NP-hard, which means that any other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are believed to be very hard to solve, as no polynomial time algorithm is known for any of them. If a polynomial time algorithm is found for one NP-complete problem, then it can be used to solve all other NP-complete problems as well. This is called the P vs NP problem, and it is one of the most important open questions in computer science.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. For example, finding the shortest path between two points, or the minimum number of colors needed to color a graph. Optimization problems can be formulated as decision problems by asking whether there exists a solution that is better than a given threshold.
  - An Approximation Algorithm does not guarantee the best solution, but rather a solution that is close to the optimal one. The goal of an Approximation Algorithm is to find a solution that has a provable quality guarantee, which is usually expressed as a ratio between the value of the solution found and the value of the optimal solution. This ratio is called the approximation factor or the approximation ratio.
  - For example, an approximation algorithm for the vertex cover problem, which asks for the minimum number of vertices needed to cover all the edges of a graph, can guarantee that the solution found is at most twice as large as the optimal one. This means that the approximation factor is 2.
  - Approximation Algorithms are useful when finding the optimal solution is too hard or too time-consuming, and a good enough solution is acceptable. Approximation Algorithms can also provide insights into the structure and properties of the problem, and sometimes lead to better algorithms or lower bounds for the optimal solution.

## Examples of NP-Complete Problems and Approximation Algorithms

- Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - This problem is NP-complete, as it can be shown that the Hamiltonian cycle problem, which asks for a cycle that visits each vertex of a graph exactly once, can be reduced to it in polynomial time.
  - One approximation algorithm for the TSP is the nearest neighbor heuristic, which starts from a random city and repeatedly visits the nearest unvisited city until all cities are visited. This algorithm can guarantee that the tour found is at most twice as long as the optimal one, if the distances satisfy the triangle inequality, which means that the distance between any two cities is no more than the sum of the distances between them and a third city.
- Graph Coloring: Given a graph, assign a color to each vertex such that no two adjacent vertices have the same color. Minimize the number of colors used.
  - This problem is NP-complete, as it can be shown that the 3-colorability problem, which asks whether a graph can be colored with at most three colors, can be reduced to it in polynomial time.
  - One approximation algorithm for the graph coloring problem is the greedy algorithm, which assigns colors to the vertices in some order, and always chooses the smallest available color for each vertex. This algorithm can guarantee that the number of colors used is at most the maximum degree of the graph plus one, where the degree of a vertex is the number of edges incident to it.
- n-Queen Problem: Given an n x n chessboard, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
  - This problem is NP-complete, as it can be shown that the exact cover problem, which asks whether a given set of subsets of a finite set can cover the whole set without overlapping, can be reduced to it in polynomial time.
  - One approximation algorithm for the n-queen problem is



### NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP-complete if it is in NP, which means that a yes answer can be verified in polynomial time, and it is also NP-hard, which means that any other problem in NP can be reduced to it in polynomial time. NP-complete problems are believed to be the hardest problems in NP, and no polynomial time algorithm is known for them. Examples of NP-complete problems are the Travelling Salesman Problem, the Graph Coloring Problem, the n-Queen Problem, the Hamiltonian Cycle Problem, and the Sum of Subsets Problem.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. An approximation algorithm does not guarantee the best solution, but it tries to come as close as possible to the optimal solution in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm. Examples of approximation algorithms are the 2-approximation algorithm for the Vertex Cover Problem, the 7/8-approximation algorithm for the Max 3-SAT Problem, and the Christofides algorithm for the Travelling Salesman Problem    .



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes that I have prepared for you based on the web search results.

### NP-Completeness and Approximation Algorithms with Examples

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, given a certificate or a witness for the answer. A problem is NP-complete if it is NP and every other NP problem can be reduced to it in polynomial time. This means that NP-complete problems are the hardest problems in NP, and if any of them can be solved in polynomial time, then all of them can. However, it is widely believed that P ≠ NP, which means that there is no polynomial time algorithm for any NP-complete problem.

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions. Optimization problems can be classified into two types: maximization problems, which seek to maximize an objective function, and minimization problems, which seek to minimize an objective function. For example, the Travelling Salesman Problem (TSP) is a minimization problem, where the objective is to find the shortest tour that visits every city exactly once. The Graph Coloring Problem (GCP) is a maximization problem, where the objective is to find the minimum number of colors needed to color every vertex of a graph such that no two adjacent vertices have the same color.

- An Approximation Algorithm does not guarantee the best solution, but rather a solution that is close to the optimal solution in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution obtained by the algorithm and the value of the optimal solution. For maximization problems, the approximation ratio is the value of the algorithm solution divided by the value of the optimal solution, and for minimization problems, it is the value of the optimal solution divided by the value of the algorithm solution. The smaller the approximation ratio, the better the algorithm. For example, an approximation ratio of 2 means that the algorithm solution is at most twice as bad as the optimal solution, and an approximation ratio of 1 means that the algorithm solution is optimal.

- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of n cities and the distances between them, find the shortest tour that visits every city exactly once. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a constant approximation ratio. However, there are some heuristics that can give good solutions in practice, such as the nearest neighbor algorithm, the greedy algorithm, and the 2-opt algorithm. There are also some approximation algorithms that can achieve a logarithmic approximation ratio, such as the Christofides algorithm, which has an approximation ratio of 3/2, and the Held-Karp algorithm, which has an approximation ratio of 4/3.

  - Graph Coloring Problem (GCP): Given a graph G = (V, E), find the minimum number of colors needed to color every vertex of G such that no two adjacent vertices have the same color. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a constant approximation ratio. However, there are some heuristics that can give good solutions in practice, such as the greedy algorithm, which colors the vertices in some order and assigns the smallest available color to each vertex, and the Welsh-Powell algorithm, which colors the vertices in decreasing order of their degrees and assigns the smallest available color to each vertex. There are also some approximation algorithms that can achieve a logarithmic approximation ratio, such as the Lovasz Local Lemma algorithm, which has an approximation ratio of O(log n), where n is the number of vertices.

  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a constant approximation ratio. However, there are some heuristics that can give good solutions in practice, such as the backtracking algorithm, which tries to place a queen on each row and backtracks if a conflict occurs, and the genetic algorithm, which generates a population of solutions and applies crossover and mutation operators to improve them. There are also some approximation algorithms that can achieve a logarithmic approximation ratio, such as the randomized algorithm, which



# NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, i.e., problems that have a yes or no answer.
- A problem is NP if it can be verified in polynomial time, i.e., given a solution, we can check if it is correct in polynomial time.
- A problem is NP-Complete if it is NP and every other NP problem can be reduced to it in polynomial time, i.e., it is the hardest problem in NP.
- Examples of NP-Complete problems are: Hamiltonian Cycle, Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Sum of Subsets, etc.
- If there is a polynomial time algorithm for any NP-Complete problem, then there is a polynomial time algorithm for all NP problems, which implies P = NP. However, this is widely believed to be false.
- Approximation Algorithms are a way of dealing with NP-Completeness for optimization problems, i.e., problems that have a numerical objective function to minimize or maximize.
- An Approximation Algorithm does not guarantee the optimal solution, but it guarantees a solution that is close to the optimal within a certain factor or bound, called the approximation ratio.
- The approximation ratio is the ratio of the cost of the solution obtained by the algorithm to the cost of the optimal solution, for minimization problems, or the inverse for maximization problems.
- The goal of an Approximation Algorithm is to achieve the best possible approximation ratio in polynomial time, for a given optimization problem.
- Examples of Approximation Algorithms are: 2-Approximation for Vertex Cover, 7/8-Approximation for Max 3-SAT, 2-Approximation for Travelling Salesman Problem with triangle inequality, etc.



# NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A decision problem is NP if it can be verified in polynomial time, given a certificate or a witness for a yes answer.
- A decision problem is NP-Complete if it is NP and every other NP problem can be reduced to it in polynomial time, using a transformation that preserves the yes or no answer.
- NP-Complete problems are believed to be intractable, meaning that there is no polynomial time algorithm that can solve them, unless P=NP, which is a major open question in computer science.
- Examples of NP-Complete problems are: 
  - Travelling Salesman Problem (TSP): Given a set of cities and distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine if the graph can be colored with k colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other.
  - Hamiltonian Cycle: Given a graph, find a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target value, determine if there is a subset of the set that sums up to the target value.

- Approximation Algorithms are a way of dealing with NP-Completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, according to some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time, with some provable bound on the quality of the solution.
- The quality of an approximation algorithm is measured by the approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution, for the worst-case input.
- The approximation ratio depends on whether the optimization problem is a minimization problem or a maximization problem. For minimization problems, the ratio is always greater than or equal to 1, and for maximization problems, the ratio is always less than or equal to 1.
- Examples of Approximation Algorithms are:
  - TSP: A 2-approximation algorithm is to find a minimum spanning tree of the graph, and then traverse the tree in a preorder fashion, skipping any visited vertices. The length of the tour is at most twice the length of the optimal tour .
  - Graph Coloring: A simple approximation algorithm is to assign colors to the vertices in any order, using the smallest available color for each vertex. The number of colors used is at most one more than the maximum degree of the graph, which is a lower bound for the optimal number of colors .
  - n-Queen Problem: A heuristic algorithm is to place the queens one by one, starting from the first row, and choosing the column that has the least number of conflicts with the previous queens. If there is no such column, backtrack and try a different column for the previous queen. The algorithm may or may not find a solution, depending on the size of the board and the initial choices.
  - Hamiltonian Cycle: A 2-approximation algorithm is to find a minimum spanning tree of the graph, and then double each edge of the tree. The resulting graph is Eulerian, meaning that it has a cycle that visits each edge exactly once. By skipping any visited vertices, the cycle becomes a Hamiltonian cycle. The length of the cycle is at most twice the length of the optimal cycle .
  - Sum of Subsets: A greedy algorithm is to sort the set in decreasing order, and then add the elements to the subset one by one, as long as the sum does not exceed the target value. The algorithm may or may not find a solution, depending on the set and the target value. The sum of the subset is at least half of the optimal sum .



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP-complete if it is in the class NP, which means that a yes answer can be verified in polynomial time, and it is also NP-hard, which means that any other problem in NP can be reduced to it in polynomial time. NP-complete problems are believed to be the hardest problems in NP, and no polynomial time algorithm is known to solve them. Examples of NP-complete problems are the satisfiability problem, the vertex cover problem, the clique problem, the subset sum problem, and the traveling salesman problem .
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. An approximation algorithm does not guarantee the best solution, but it tries to come as close as possible to the optimal solution in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm. Examples of approximation algorithms are the greedy algorithm for the set cover problem, the Christofides algorithm for the metric traveling salesman problem, the local search algorithm for the graph coloring problem, the backtracking algorithm for the n-queen problem, and the dynamic programming algorithm for the knapsack problem   .

## Travelling Salesman Problem
- The traveling salesman problem (TSP) is an optimization problem that asks to find the shortest tour that visits a given set of cities and returns to the starting point. The tour must visit each city exactly once, and the distance between any two cities is given by a symmetric matrix. The TSP is NP-complete, which means that no polynomial time algorithm is known to solve it exactly. The TSP can be formulated as an integer linear program, but solving it using linear programming techniques is impractical for large instances.
- An approximation algorithm for the TSP is an algorithm that finds a tour that is not necessarily optimal, but is close to the optimal length in polynomial time. One such algorithm is the Christofides algorithm, which works for metric TSP instances, where the distance between any two cities satisfies the triangle inequality. The Christofides algorithm has an approximation ratio of 3/2, which means that the length of the tour found by the algorithm is at most 3/2 times the length of the optimal tour. The Christofides algorithm works as follows :
  - Find a minimum spanning tree of the given graph, which is a tree that connects all the cities with the minimum total edge weight.
  - Find the set of odd-degree vertices in the tree, which are the vertices that have an odd number of edges incident to them.
  - Find a minimum weight perfect matching of the odd-degree vertices, which is a set of edges that pairs up the odd-degree vertices such that the total edge weight is minimized.
  - Combine the tree and the matching to form a multigraph, which is a graph that may have multiple edges between the same pair of vertices.
  - Find an Eulerian circuit of the multigraph, which is a closed walk that traverses each edge exactly once.
  - Convert the Eulerian circuit into a Hamiltonian cycle, which is a closed walk that visits each vertex exactly once, by skipping repeated vertices. This is the final tour returned by the algorithm.

