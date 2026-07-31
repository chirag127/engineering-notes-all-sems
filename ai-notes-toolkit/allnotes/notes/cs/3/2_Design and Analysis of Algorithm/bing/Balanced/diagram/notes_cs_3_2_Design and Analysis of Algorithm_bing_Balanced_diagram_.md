

## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An algorithm is a finite sequence of well-defined instructions for solving a problem or performing a task.
- Analyzing algorithms is the process of determining the amount of resources (such as time and space) that an algorithm requires to execute.
- Complexity of algorithms is a measure of the amount of resources that an algorithm consumes as a function of the input size.
- Growth of functions is a way of comparing the asymptotic behavior of different functions, such as the running time of different algorithms.
- Performance measurements are the empirical methods of evaluating the efficiency and correctness of algorithms, such as experiments, benchmarks, and simulations.
- Sorting and order statistics are the problems of arranging a set of elements in a certain order and finding the kth smallest or largest element in a set.
- Shell sort is a sorting algorithm that is based on the insertion sort algorithm. It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted. It avoids large shifts as in insertion sort, where the smaller value is on the far right and must be moved to the far left    .
- Quick sort is a sorting algorithm that is based on the divide-and-conquer paradigm. It partitions the array into two subarrays around a pivot element, such that all elements in the left subarray are smaller than the pivot and all elements in the right subarray are larger than the pivot. It then recursively sorts the subarrays until the array is sorted.
- Merge sort is a sorting algorithm that is also based on the divide-and-conquer paradigm. It divides the array into two equal halves, recursively sorts each half, and then merges the two sorted halves into one sorted array.
- Heap sort is a sorting algorithm that is based on the heap data structure. It builds a max-heap or a min-heap from the array, and then repeatedly extracts the maximum or minimum element from the heap and places it at the end of the array, until the array is sorted.
- Comparison of sorting algorithms is the process of evaluating the advantages and disadvantages of different sorting algorithms based on various criteria, such as time complexity, space complexity, stability, adaptability, and simplicity.
- Sorting in linear time is the problem of sorting a set of elements in O(n) time, where n is the number of elements. This is possible only when the elements have some special properties, such as being integers in a fixed range, or having a common radix or base. Some examples of linear-time sorting algorithms are counting sort, radix sort, and bucket sort.



Hello, I am Sydney, your AI assistant. I can help you with your topic on algorithms for sorting and order statistics. Here are some notes that you can use for your study material:

### Algorithms for Sorting and Order Statistics

- Sorting is the process of rearranging a sequence of elements into a specific order, such as ascending or descending, based on some comparison criterion.
- Order statistics are the elements that occupy certain positions in a sorted sequence, such as the minimum, maximum, median, or the ith smallest or largest element.
- Sorting and order statistics are fundamental problems in computer science and have many applications in data analysis, searching, cryptography, and more.
- There are different algorithms for sorting and order statistics, each with different time and space complexities, advantages and disadvantages, and implementation details. Some of the common algorithms are:

  - Shell sort: A variation of insertion sort that uses a gap sequence to sort elements that are far apart first, then reduces the gap until it becomes one. It has an average time complexity of O(n^1.5^), where n is the number of elements, and is easy to implement and efficient for small data sets.
  - Quick sort: A divide-and-conquer algorithm that partitions the sequence around a pivot element, such that all elements smaller than the pivot are on its left and all elements larger than the pivot are on its right, then recursively sorts the left and right sub-sequences. It has an average time complexity of O(n log n), where n is the number of elements, and is one of the fastest and most widely used sorting algorithms. However, it has a worst-case time complexity of O(n^2^) when the pivot is chosen poorly, and it is not stable, meaning that it may change the relative order of equal elements.
  - Merge sort: A divide-and-conquer algorithm that splits the sequence into two halves, recursively sorts each half, then merges the two sorted halves into one sorted sequence. It has a time complexity of O(n log n), where n is the number of elements, and is stable and suitable for large data sets. However, it requires extra space for the merging process, and it is not adaptive, meaning that it does not take advantage of the existing order in the sequence.
  - Heap sort: A comparison-based algorithm that uses a data structure called a heap, which is a complete binary tree that satisfies the heap property, meaning that each node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap). It repeatedly extracts the root of the heap, which is the maximum or minimum element, and restores the heap property by moving the last element to the root and sifting it down. It has a time complexity of O(n log n), where n is the number of elements, and is in-place, meaning that it does not require extra space. However, it is not stable and it has a high constant factor, meaning that it is slower than other O(n log n) algorithms in practice.
  - Comparison of sorting algorithms: The choice of the best sorting algorithm depends on various factors, such as the size and distribution of the data, the available memory and disk space, the stability and adaptability requirements, and the desired trade-off between speed and simplicity. Some general guidelines are:

    - For small data sets, insertion sort or shell sort are simple and efficient.
    - For large data sets, quick sort or merge sort are fast and scalable.
    - For nearly sorted data sets, insertion sort or bubble sort are adaptive and perform well.
    - For data sets with many equal elements, counting sort or radix sort are linear and stable.
    - For data sets with a known range of values, bucket sort or radix sort are linear and suitable.
  - Sorting in linear time: Most comparison-based sorting algorithms have a lower bound of O(n log n) time complexity, where n is the number of elements, which means that they cannot sort faster than that in the worst case. However, there are some non-comparison-based sorting algorithms that can sort in linear time, O(n), by using some additional information about the data, such as the range of values, the number of digits, or the distribution of frequencies. Some of these algorithms are:

    - Counting sort: An algorithm that counts the number of occurrences of each distinct value in the sequence, then uses the counts to determine the position of each element in the sorted sequence. It has a time complexity of O(n + k), where n is the number of elements and k is the range of values, and is stable and suitable for data sets with small



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Design and Analysis of Algorithm. Here is the content for the topic of Analyzing Algorithms for the notes of the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

### Analyzing Algorithms

- An algorithm is a finite sequence of well-defined instructions for solving a problem or performing a task.
- Analyzing an algorithm means estimating the resources (such as time and space) that the algorithm requires to execute.
- The complexity of an algorithm is a measure of the amount of resources needed by the algorithm as a function of the input size.
- The growth of a function is the rate at which the function increases as the input size increases.
- The performance of an algorithm can be measured by the number of basic operations (such as comparisons, swaps, arithmetic operations, etc.) that the algorithm performs on the input data.
- Sorting is the process of arranging a sequence of items (such as numbers, words, records, etc.) in a certain order (such as ascending, descending, alphabetical, etc.).
- Order statistics are the elements that occupy certain positions in a sorted sequence, such as the minimum, maximum, median, kth smallest, etc.
- Shell sort is a sorting algorithm that sorts the elements by comparing and swapping elements that are far apart by a certain gap, which decreases in each iteration until it becomes one.
- Quick sort is a sorting algorithm that partitions the sequence into two sub-sequences based on a pivot element, such that all the elements in the left sub-sequence are smaller than or equal to the pivot, and all the elements in the right sub-sequence are larger than or equal to the pivot, and then recursively sorts the sub-sequences.
- Merge sort is a sorting algorithm that divides the sequence into two equal or nearly equal sub-sequences, recursively sorts them, and then merges them into a single sorted sequence.
- Heap sort is a sorting algorithm that builds a binary heap (a complete binary tree where each node is larger than or equal to its children) from the sequence, and then repeatedly extracts the maximum element from the heap and places it at the end of the sequence, until the heap is empty.
- Comparison of sorting algorithms can be done based on various criteria, such as the time complexity, the space complexity, the stability, the adaptability, the simplicity, etc. of the algorithms.
- Sorting in linear time is possible for some special cases of input data, such as when the elements are integers in a fixed range, or when the elements have a common attribute that can be used as a key. Some examples of linear-time sorting algorithms are counting sort, radix sort, and bucket sort.



### Complexity of Algorithms

- Complexity of an algorithm is a measure of how long an algorithm would take to complete given an input of size n.
- Complexity is calculated asymptotically as n approaches infinity, to capture the behavior of the algorithm for large inputs.
- Complexity is about the algorithm itself, not the actual execution time or the hardware used.
- Complexity is expressed using the big O notation, which gives the upper bound of the number of operations executed by an algorithm as a function of n.
- For example, an algorithm that has a complexity of O(n) means that the number of operations grows linearly with the input size n.
- Complexity can be classified into two types: time complexity and space complexity.
- Time complexity is the amount of time required by the algorithm to solve the problem.
- Space complexity is the amount of memory or storage required by the algorithm to solve the problem.
- Both time and space complexity depend on the input size n, the algorithm design, and the implementation details.
- The goal of algorithm design and analysis is to find algorithms that have low complexity, preferably polynomial or sublinear, and avoid algorithms that have high complexity, such as exponential or factorial.



### Growth of Functions

- Growth of functions is a way of measuring and comparing the efficiency of algorithms based on their input size and execution time.
- Growth of functions helps us to ignore the constants and lower order terms that are less significant for large inputs.
- Growth of functions also helps us to use asymptotic notation to express the upper bound, lower bound, or tight bound of an algorithm's running time.
- Growth of functions can be classified into different categories based on their rate of increase, such as constant, linear, logarithmic, polynomial, exponential, etc.
- Growth of functions can be compared using the order of magnitude, which is the highest power of the input size in the function.
- Growth of functions can be visualized using graphs, tables, or formulas to show how they change with different input sizes.
- Growth of functions can be used to analyze the best case, worst case, and average case scenarios of an algorithm's performance.
- Growth of functions can be influenced by the choice of data structures, implementation details, and hardware specifications of the algorithm.



### Performance Measurements

- Performance measurements are used to evaluate the efficiency and effectiveness of an algorithm in solving a specific computational problem.
- Performance measurements can be based on different criteria, such as:
  - Space complexity: the amount of memory or storage space required by the algorithm to perform its task. It consists of both program and data space.
  - Time complexity: the amount of time or number of steps required by the algorithm to perform its task. It depends on the size and nature of the input, the hardware and software environment, and the implementation details of the algorithm.
  - Asymptotic complexity: the behavior of the algorithm as the input size grows indefinitely. It is usually expressed using the big-O notation, which gives the upper bound of the growth rate of the algorithm's complexity.
  - Best-case, worst-case, and average-case complexity: the minimum, maximum, and expected complexity of the algorithm for different inputs. They can be used to compare the performance of different algorithms for the same problem.
  - Practical complexity: the actual performance of the algorithm in real-world scenarios, taking into account factors such as input distribution, caching, parallelism, and optimization techniques.
- Performance measurements can help to design, analyze, compare, and improve algorithms, as well as to choose the most suitable algorithm for a given problem and context.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Design and Analysis of Algorithm. Here is the content for the topic of Sorting and Order Statistics - Shell Sort.

### Sorting and Order Statistics - Shell Sort

- Shell sort is a generalization of insertion sort that allows the exchange of items that are far apart.
- The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list. Such a list is said to be h-sorted.
- It can also be thought of as h interleaved lists, each individually sorted.
- By performing insertion sort on each of the h sublists, we get a better list (less number of inversions). Now we repeat the process, with a smaller value of h, until we reach the last pass, with h=1, which is just an ordinary insertion sort.
- The sequence of values of h is called the increment sequence or the gap sequence. The performance of shell sort depends on this sequence.
- A common gap sequence is powers of 2, that is, 1, 2, 4, 8, 16, ... However, this sequence is not very efficient, and it is better to use a sequence that alternates between odd and even numbers, such as 1, 3, 7, 15, 31, ...
- The worst-case time complexity of shell sort depends on the gap sequence, which is hard to analyze. For the powers of 2 sequence, the worst-case time complexity is O(n^2). For some other sequences, the worst-case time complexity is known to be O(n^(3/2)) or O(n^(4/3)).
- The best-case time complexity of shell sort is O(n), which occurs when the list is already sorted.
- The average-case time complexity of shell sort is also hard to analyze, and depends on the gap sequence. For the powers of 2 sequence, the average-case time complexity is O(n^(3/2)). For some other sequences, the average-case time complexity is O(n^(7/6)) or O(n^(5/4)).
- Shell sort is an in-place sorting algorithm, as it only requires a constant amount of extra memory space.
- Shell sort is an unstable sorting algorithm, as it may change the relative order of elements with equal values.
- Shell sort is more efficient than insertion sort, as it can move elements faster to their correct positions. However, it is less efficient than some other sorting algorithms, such as quick sort, merge sort, or heap sort.



### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle, and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The algorithm has an average-case running time of **O(n log n)**, where n is the number of elements in the array, and a worst-case running time of **O(n^2)**, which occurs when the pivot element is always the smallest or the largest element in the array.
- The algorithm is **in-place**, meaning that it does not require additional memory to sort the array, and **unstable**, meaning that it does not preserve the relative order of equal elements.
- The algorithm can be implemented as follows:

```python
# A function to partition an array around a pivot element
def partition(A, p, r):
  # Choose the last element as the pivot
  x = A[r]
  # Initialize the index of the smaller element
  i = p - 1
  # Loop through the array from p to r - 1
  for j in range(p, r):
    # If the current element is less than or equal to the pivot
    if A[j] <= x:
      # Increment the index of the smaller element
      i = i + 1
      # Swap the current element with the smaller element
      A[i], A[j] = A[j], A[i]
  # Swap the pivot element with the element at i + 1
  A[i + 1], A[r] = A[r], A[i + 1]
  # Return the index of the pivot element
  return i + 1

# A function to sort an array using quick sort
def quick_sort(A, p, r):
  # If the array has more than one element
  if p < r:
    # Partition the array around a pivot element
    q = partition(A, p, r)
    # Recursively sort the left subarray
    quick_sort(A, p, q - 1)
    # Recursively sort the right subarray
    quick_sort(A, q + 1, r)
```
- An example of quick sort on an array of 10 elements is shown below:

Quick sort example

- The advantages of quick sort are that it is fast on average, it does not require extra space, and it can be easily parallelized or adapted to different data structures.
- The disadvantages of quick sort are that it is sensitive to the choice of the pivot element, it has a poor worst-case performance, and it is unstable.



### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  1. If the array has only one element, return it as the sorted array.
  2. Otherwise, divide the array into two subarrays of equal or nearly equal size.
  3. Recursively sort the left and right subarrays using merge sort.
  4. Merge the sorted left and right subarrays into a single sorted array.

- The merge operation takes two sorted arrays and combines them into one sorted array. It can be implemented as follows:

  1. Initialize an empty array to store the merged result.
  2. Initialize two pointers, one for each input array, to track the current element to be compared.
  3. While both input arrays have elements remaining, compare the elements pointed by the pointers and append the smaller one to the result array. Increment the pointer of the array that provided the smaller element.
  4. If one input array is exhausted, append the remaining elements of the other input array to the result array.
  5. Return the result array as the merged array.

- The pseudocode for merge sort is:

  ```
  MERGE-SORT(A, p, r)
    // A is the input array, p and r are the indices of the first and last elements
    if p < r
      q = floor((p + r) / 2) // find the middle point
      MERGE-SORT(A, p, q) // recursively sort the left subarray
      MERGE-SORT(A, q + 1, r) // recursively sort the right subarray
      MERGE(A, p, q, r) // merge the sorted subarrays
  ```

  ```
  MERGE(A, p, q, r)
    // A is the input array, p, q, and r are the indices of the first, middle, and last elements of the subarray to be merged
    n1 = q - p + 1 // the length of the left subarray
    n2 = r - q // the length of the right subarray
    create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
    for i = 1 to n1
      L[i] = A[p + i - 1] // copy the left subarray to L
    for j = 1 to n2
      R[j] = A[q + j] // copy the right subarray to R
    L[n1 + 1] = infinity // sentinel value to mark the end of L
    R[n2 + 1] = infinity // sentinel value to mark the end of R
    i = 1 // pointer for L
    j = 1 // pointer for R
    for k = p to r
      if L[i] <= R[j]
        A[k] = L[i] // copy the smaller element from L to A
        i = i + 1 // increment the pointer for L
      else
        A[k] = R[j] // copy the smaller element from R to A
        j = j + 1 // increment the pointer for R
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge operation takes O(n) time to combine the subarrays. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm creates temporary arrays of size n/2 at each level of recursion, and there are log n levels of recursion. Therefore, the total space is O(n).
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array. This is because the merge operation always chooses the element from the left subarray when there is a tie, and the left subarray contains the elements that appeared earlier in the input array.
- Merge sort is not an in-place sorting algorithm, meaning that it uses extra space to store the temporary arrays. This can be a disadvantage when the input array is large and the available memory is limited.



### Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: building the heap and extracting the elements from the heap.
- Building the heap: the algorithm converts the input array into a max-heap or a min-heap by repeatedly applying a procedure called heapify, which maintains the heap property from the bottom up. This phase takes O(n) time, where n is the number of elements in the array.
- Extracting the elements from the heap: the algorithm repeatedly swaps the root element of the heap with the last element of the heap, reduces the size of the heap by one, and restores the heap property by applying heapify from the top down. This phase takes O(n log n) time, where n is the number of elements in the heap.
- The overall time complexity of heap sort is O(n log n), where n is the number of elements in the input array. The space complexity is O(1), as the algorithm only requires constant extra space to perform the swaps.
- Heap sort is an in-place, unstable, and adaptive sorting algorithm. It is in-place because it does not require extra space to sort the array. It is unstable because it does not preserve the relative order of equal elements. It is adaptive because it performs better on partially sorted arrays than on random arrays.
- Heap sort has several advantages and disadvantages compared to other sorting algorithms. Some of the advantages are:
  - It has a guaranteed worst-case time complexity of O(n log n), which is better than some other comparison-based algorithms such as bubble sort, insertion sort, or selection sort.
  - It does not require extra space to sort the array, which is better than some other algorithms such as merge sort or quick sort with large stack space.
  - It can be easily implemented using an array as the underlying data structure, without requiring pointers or linked lists.
- Some of the disadvantages are:
  - It is not a stable sorting algorithm, which means it may change the relative order of equal elements, which may be undesirable in some applications.
  - It is not a cache-friendly algorithm, which means it may cause many cache misses and reduce the performance on modern hardware.
  - It is not a very efficient algorithm in practice, as it has a large hidden constant factor in the time complexity, and it performs poorly on partially sorted arrays.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the comparison of sorting algorithms for your notes.

### Comparison of Sorting Algorithms

- Sorting algorithms are methods of arranging a list of elements in a certain order, such as ascending or descending.
- Sorting algorithms can be classified into two categories: comparison-based and non-comparison-based.
- Comparison-based sorting algorithms use a comparison operator, such as < or =, to compare two elements and determine their relative order in the final sorted list.
- Non-comparison-based sorting algorithms do not use comparisons, but rely on other techniques, such as counting, hashing, or radix conversion, to sort the elements.
- Comparison-based sorting algorithms have a lower bound of Ω(n log n) on the number of comparisons they need to perform in the worst case, where n is the number of elements to be sorted.
- Non-comparison-based sorting algorithms can achieve a lower complexity than Ω(n log n) in some cases, but they may have other drawbacks, such as requiring more space or being sensitive to the range and distribution of the elements.

#### Comparison of Time Complexity

- Time complexity is a measure of how fast an algorithm can sort a list of elements, depending on the size of the list and the number of operations it performs.
- Time complexity is usually expressed using the big O notation, which gives an upper bound on the worst-case performance of the algorithm.
- The table below shows the time complexities for some of the most commonly used sorting algorithms, in terms of the best case, average case, and worst case scenarios.

| Algorithm | Best case | Average case | Worst case |
|-----------|-----------|--------------|------------|
| Bubble sort | O(n) | O(n^2) | O(n^2) |
| Selection sort | O(n^2) | O(n^2) | O(n^2) |
| Insertion sort | O(n) | O(n^2) | O(n^2) |
| Merge sort | O(n log n) | O(n log n) | O(n log n) |
| Quick sort | O(n log n) | O(n log n) | O(n^2) |
| Heap sort | O(n log n) | O(n log n) | O(n log n) |
| Shell sort | O(n) | O(n^1.5) | O(n^2) |
| Counting sort | O(n + k) | O(n + k) | O(n + k) |
| Radix sort | O(nk) | O(nk) | O(nk) |

- Note: k is the range of the elements, and n is the number of elements.

#### Comparison of Space Complexity

- Space complexity is a measure of how much extra memory an algorithm needs to sort a list of elements, besides the input list itself.
- Space complexity is also usually expressed using the big O notation, which gives an upper bound on the worst-case performance of the algorithm.
- The table below shows the space complexities for some of the most commonly used sorting algorithms, in terms of the auxiliary space they require.

| Algorithm | Space complexity |
|-----------|------------------|
| Bubble sort | O(1) |
| Selection sort | O(1) |
| Insertion sort | O(1) |
| Merge sort | O(n) |
| Quick sort | O(log n) |
| Heap sort | O(1) |
| Shell sort | O(1) |
| Counting sort | O(k) |
| Radix sort | O(n + k) |

#### Stable and Unstable Algorithms

- A sorting algorithm is stable if it preserves the relative order of elements that are equal in the input list.
- A sorting algorithm is unstable if it may change the relative order of elements that are equal in the input list.
- Stability is important when sorting elements that have multiple attributes, such as records or objects, and the sorting is based on one of the attributes.
- The table below shows which of the sorting algorithms are stable and which are unstable.

| Algorithm | Stability |
|-----------|-----------|
| Bubble sort | Stable |
| Selection sort | Unstable |
| Insertion sort | Stable |
| Merge sort | Stable |
| Quick sort | Unstable |
| Heap sort | Unstable |
| Shell sort | Unstable |
| Counting sort | Stable |
| Radix sort | Stable |

#### Sorting Algorithms – Fields Tests

- The theoretical analysis of sorting algorithms gives an idea of how they perform in terms of time and space complexity, but it does not account



### Sorting in Linear Time

- Sorting in linear time means sorting a sequence of n elements in O(n) time, where n is the number of elements to be sorted.
- Sorting in linear time is possible only when some special assumptions are made about the input sequence, such as the range of values, the distribution of elements, or the structure of the keys.
- Some examples of sorting algorithms that run in linear time are counting sort, radix sort, and bucket sort. These algorithms are also called non-comparison sorts, because they do not compare the elements directly to determine their order.
- Counting sort assumes that the input consists of integers in a small range . It counts the number of occurrences of each integer in the input, and then uses these counts to determine the position of each element in the output array.
- Radix sort assumes that the input consists of integers or strings that have a fixed number of digits or characters . It sorts the elements by each digit or character, starting from the least significant one, and using a stable sorting algorithm (such as counting sort) for each pass.
- Bucket sort assumes that the input is generated by a random process that distributes elements uniformly over the interval [0, 1) . It divides the interval into n equal-sized buckets, and then distributes the elements into the buckets based on their values. Then, it sorts each bucket using another sorting algorithm (such as insertion sort), and concatenates the sorted buckets to form the output array.



## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

- Advanced data structures are data structures that provide more efficient ways to store, manipulate, and access data, especially for applications that require complex operations or large amounts of data.
- Some of the advanced data structures that we will study in this unit are:

  - Red-black trees: A type of self-balancing binary search tree that maintains the height of the tree as O(log n) by enforcing some properties on the color and structure of the nodes. Red-black trees are useful for implementing associative arrays, such as dictionaries or maps, that support fast insertion, deletion, and search operations.
  - B-trees: A type of multi-way search tree that can store multiple keys in each node and have a variable number of children depending on the size of the node. B-trees are useful for implementing databases, file systems, and indexes, as they can reduce the number of disk accesses and handle large amounts of data efficiently.
  - Binomial heaps: A type of heap data structure that consists of a collection of binomial trees, which are ordered trees that have a specific shape and size. Binomial heaps are useful for implementing priority queues, as they support fast merge, insert, and delete-min operations.
  - Fibonacci heaps: A type of heap data structure that is an improvement over binomial heaps, as they can perform insert and decrease-key operations in constant amortized time. Fibonacci heaps are useful for implementing algorithms that rely on efficient priority queues, such as Dijkstra's algorithm and Prim's algorithm for finding shortest paths and minimum spanning trees.
  - Tries: A type of tree data structure that stores strings or sequences of symbols in a compact and efficient way, by using common prefixes to share nodes. Tries are useful for implementing applications that require fast prefix searching, such as spell checkers, auto-complete, text compression, and pattern matching.
  - Skip lists: A type of probabilistic data structure that consists of multiple linked lists, each with a different level of granularity, that allow fast search, insertion, and deletion operations in expected O(log n) time. Skip lists are useful for implementing sorted sets and maps, as they can handle dynamic data and support range queries.



Hello, I am Sydney, your AI assistant. I can help you with your topic of red-black trees. Here are some notes for you:

### Red-Black Trees

- A red-black tree is a special type of binary search tree, used in computer science to organize pieces of comparable data, such as text fragments or numbers.
- A red-black tree is self-balancing, meaning that it maintains a roughly equal height for its left and right subtrees, which ensures a good efficient worst case running time complexity of O(log n) for basic operations like insertion, deletion, and search .
- A red-black tree has the following properties  :
  - Every node is either red or black, this can be saved in memory as a single bit (e.g. 'red' = 1, 'black' = 0).
  - The root of the tree is always black.
  - Every leaf (null pointer) is black.
  - If a node is red, then both its children are black.
  - Every simple path from a node to a descendant leaf contains the same number of black nodes, this is called the black-height of the node.
- To maintain these properties, a red-black tree performs rotations and recoloring operations after inserting or deleting a node  .
  - A rotation is a local operation that changes the structure of the tree without affecting the order of the nodes. There are two types of rotations: left and right.
  - A recoloring is a local operation that changes the color of a node and its parent and uncle (if they exist). There are two cases of recoloring: flip and push.
- Red-black trees can be used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - Implementing associative arrays, such as dictionaries, maps, and sets.
  - Implementing range queries, such as finding all elements between a given range of values.
  - Implementing augmented data structures, such as interval trees, order statistic trees, and rank trees.



### B – Trees

B-trees are a type of self-balancing tree data structure that maintain sorted data and allow efficient operations such as searches, insertions, and deletions in logarithmic time. B-trees generalize the binary search tree, allowing for nodes with more than two children. B-trees are also known as height-balanced m-way trees or large key trees.

Some properties of B-trees are:

- A B-tree has a minimum degree `t` that determines the minimum and maximum number of keys and children in a node.
- A B-tree of degree `t` has the following characteristics:
  - Every node, except the root, has at least `t-1` keys and at most `2t-1` keys.
  - Every node, except the leaf nodes, has at least `t` children and at most `2t` children.
  - The root node has at least one key and at most `2t-1` keys. It has no children if it is the only node in the tree, otherwise it has at least two children.
  - All the leaf nodes are at the same level, which is the height of the tree.
  - The keys in a node are stored in sorted order, and the keys in the subtree of a key are either greater than or equal to (for the left subtree) or less than (for the right subtree) that key.
- The basic operations on a B-tree are:
  - Search: To search for a key in a B-tree, we start from the root node and compare the key with the keys in the node. If the key is found, we return the node and the index of the key. If the key is not found, we recursively search in the appropriate child of the node, based on the comparison result. The search operation takes `O(log n)` time, where `n` is the number of keys in the tree.
  - Insert: To insert a key in a B-tree, we first search for the key and find the leaf node where the key should be inserted. If the leaf node has less than `2t-1` keys, we simply insert the key in the node in sorted order. If the leaf node is full, we split the node into two nodes and move the middle key to the parent node, creating a new child pointer. This may cause the parent node to become full, in which case we repeat the splitting process until we reach a node that is not full or the root node. The insert operation takes `O(log n)` time, where `n` is the number of keys in the tree.
  - Delete: To delete a key from a B-tree, we first search for the key and find the node that contains the key. If the key is in a leaf node, we simply remove the key from the node. If the key is in an internal node, we replace the key with its predecessor (the rightmost key in the left subtree) or its successor (the leftmost key in the right subtree) and delete the predecessor or successor from the leaf node. In both cases, if the node has less than `t-1` keys after the deletion, we perform a balancing operation to ensure that the node has at least `t-1` keys. The balancing operation may involve borrowing a key from a sibling node or merging two sibling nodes and moving a key from the parent node. This may cause the parent node to have less than `t-1` keys, in which case we repeat the balancing process until we reach a node that has at least `t-1` keys or the root node. The delete operation takes `O(log n)` time, where `n` is the number of keys in the tree.

A diagram of a B-tree of degree 3 is shown below:

```
            +---+---+---+
            | 8 | 16|   |
            +---+---+---+
           /    |    |    \
          /     |    |     \
+---+---+---+  +---+---+---+  +---+---+---+  +---+---+---+
| 1 | 3 | 5 |  | 9 | 12| 14|  | 17| 19| 21|  | 24| 27| 30|
+---+---+---+  +---+---+---+  +---+---+---+  +---+---+---+
```



### Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- A binomial heap can support the following operations in O(log n) time, where n is the number of nodes in the heap :
  - Insert: add a new node to the heap as a binomial tree of order 0, then merge any trees of the same order until the heap property is restored.
  - Get Minimum: find the root node with the smallest key among all the binomial trees in the heap.
  - Extract Minimum: remove the root node with the smallest key from the heap, then add its children as separate binomial trees to the heap, then merge any trees of the same order until the heap property is restored.
  - Union: merge two binomial heaps into one by adding the corresponding binomial trees of the same order, then merge any trees of the same order until the heap property is restored.
  - Decrease Key: decrease the key of a given node in the heap, then swap it with its parent until the heap property is restored.
  - Delete: decrease the key of a given node to negative infinity, then extract the minimum node from the heap.

Here is an example of a binomial heap with 13 nodes and 4 binomial trees of orders 0, 1, 2, and 3:

```
      3
    / | \
   7  9  25
  /|  |  / \
 10 8  12 14
/|     |
11 15  18
```

: Binomial heap - Wikipedia
: Binomial Heap | Brilliant Math & Science Wiki
: Binomial Heap - GeeksforGeeks



### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A heap-ordered tree is a tree that satisfies the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent.
- The minimum key is always at the root of one of the trees.
- The structure of a Fibonacci heap is more flexible than a binary heap or a binomial heap, allowing for faster amortized running time for some operations .
- A Fibonacci heap supports the following operations :
  - `find-min`: returns the root of the tree containing the minimum key in constant (O(1)) amortized time.
  - `insert`: adds a new node to the heap in constant (O(1)) amortized time.
  - `decrease-key`: decreases the key of a given node in the heap in constant (O(1)) amortized time.
  - `delete-min`: removes and returns the minimum node from the heap in O(log n) amortized time, where n is the number of nodes in the heap.
  - `delete`: removes a given node from the heap in O(log n) amortized time.
  - `merge`: combines two Fibonacci heaps into one in constant (O(1)) time .
- A Fibonacci heap is named after the Fibonacci numbers, which are used in its running time analysis.
- A Fibonacci heap is used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- A Fibonacci heap is represented as a circular doubly linked list of roots of the trees, with a pointer to the minimum node .
- The trees in a Fibonacci heap are not constrained by any shape or order, unlike a binary heap or a binomial heap .
- The trees in a Fibonacci heap are ranked by their degree, which is the number of children of the root .
- The degree of a tree in a Fibonacci heap is bounded by O(log n), where n is the number of nodes in the tree .
- The trees in a Fibonacci heap are marked to indicate whether they have lost a child since the last time they were made the child of another node .
- The marking of the trees is used to maintain the potential function of the heap, which is used to analyze the amortized running time of the operations .
- The `delete-min` operation involves removing the minimum node, making its children new roots, and consolidating the roots by linking the trees of equal degree until at most one tree of each degree remains .
- The `decrease-key` operation involves decreasing the key of a given node, cutting it from its parent if it violates the heap property, and cascading the cuts to its ancestors if they are marked .
- The `delete` operation involves decreasing the key of a given node to negative infinity, and then calling `delete-min`.
- The `merge` operation involves concatenating the root lists of the two heaps, and updating the minimum pointer .

: Fibonacci heap - Wikipedia
: Fibonacci Heap | Brilliant Math & Science Wiki
: Fibonacci Heap | Set 1 (Introduction) - GeeksforGeeks



### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**TRIE**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has k children, one for each character in the alphabet.
- If two strings have a common prefix, then they will have the same ancestor in the trie.
- The root node of the trie represents an empty string.
- Each node in the trie has two fields: a value and an array of pointers to its children.
- The value field can store any data associated with the string represented by the node.
- The array of pointers has a fixed size equal to the size of the alphabet.
- Each pointer in the array corresponds to a character in the alphabet.
- If a node has a child for a character, then the pointer at that index is not null.
- If a node does not have a child for a character, then the pointer at that index is null.
- A node is a leaf node if all its pointers are null.
- A node is a terminal node if it represents the end of a string.
- A terminal node may or may not be a leaf node.
- A trie can support two main operations: insert and search.
- To insert a string into a trie, we start from the root node and follow the pointers corresponding to the characters in the string.
- If a pointer is null, we create a new node and link it to the parent node.
- If a pointer is not null, we move to the next node and repeat the process.
- When we reach the end of the string, we mark the last node as a terminal node and optionally store some value in it.
- To search for a string in a trie, we start from the root node and follow the pointers corresponding to the characters in the string.
- If a pointer is null, we return false, as the string is not in the trie.
- If a pointer is not null, we move to the next node and repeat the process.
- When we reach the end of the string, we check if the last node is a terminal node.
- If the last node is a terminal node, we return true, as the string is in the trie.
- If the last node is not a terminal node, we return false, as the string is a prefix of some other string in the trie.
- The time complexity of both insert and search operations is O(m), where m is the length of the string.
- The space complexity of a trie is O(nk), where n is the number of strings and k is the size of the alphabet.
- A trie can be used for various applications, such as autocomplete, spell checking, prefix matching, word search, etc  .

Here is an example of a trie that stores the strings "allot", "alone", "ant", "and", "are", "bat", and "bad":

```
    root
    /  \
   a    b
  / \    \
 l   n    a
/ \   \    \
l  o   t    t
|  |   |   / \
o  n   *  a   d
|  |      |   |
t  d      r   *
|  |      |  
*  *      e
         |
         *
```

The asterisks (*) denote the terminal nodes. The value field of each node is omitted for simplicity.



### Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis .

- A skip list consists of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The lowest layer contains all the elements of the list in sorted order, and is called the base list.
- The higher layers contain a subset of the elements of the lower layers, chosen randomly with some probability.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the corresponding element in the lower layer.
- The highest layer contains only one element, called the head, which points to the first element of the base list.
- The skip list also has a tail element, which points to the last element of the base list.

Skip list example

- The main advantage of a skip list is that it allows for fast search, insertion and deletion operations, with an expected time complexity of O(log n), where n is the number of elements in the base list.
- The search operation starts from the head element and follows the pointers in the highest layer until it reaches an element that is larger than or equal to the target element, or the tail element.
- Then, it moves down to the lower layer and repeats the process until it reaches the base list, where it either finds the target element or determines that it does not exist in the list.
- The insertion operation first searches for the position where the new element should be inserted in the base list, and then randomly decides whether to insert it in the higher layers as well, with some probability.
- The deletion operation first searches for the element to be deleted in the base list, and then removes it from all the layers where it appears, updating the pointers accordingly.

- The main disadvantage of a skip list is that it requires extra space to store the pointers in the higher layers, and that it is sensitive to the choice of the probability parameter, which affects the balance and performance of the structure.
- The skip list is a probabilistic data structure that seems likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space.



## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

### Divide and Conquer

- Divide and conquer is a technique of solving a complex problem by breaking it into smaller and simpler subproblems that can be solved recursively  .
- The general idea of divide and conquer is to have three steps:
  - Divide the problem into a number of subproblems that are smaller instances of the same problem.
  - Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
  - Combine the solutions to the subproblems into the solution for the original problem.
- Some examples of divide and conquer algorithms are :
  - Binary search: Given a sorted array of elements, find a target element by repeatedly dividing the array into two halves and comparing the middle element with the target. The time complexity is O(log n).
  - Merge sort: Given an array of elements, sort them by dividing the array into two halves, sorting the two halves recursively, and then merging the sorted halves. The time complexity is O(n log n).
  - Quick sort: Given an array of elements, sort them by choosing a pivot element, partitioning the array into two subarrays such that all elements less than the pivot are in the left subarray and all elements greater than or equal to the pivot are in the right subarray, and then sorting the two subarrays recursively. The average time complexity is O(n log n).
  - Strassen's algorithm: Given two matrices, multiply them by dividing each matrix into four submatrices, computing seven products of submatrices recursively, and then combining the products into the final result. The time complexity is O(n^2.8074).
  - Fast Fourier transform: Given a sequence of complex numbers, compute its discrete Fourier transform by dividing the sequence into two subsequences of even and odd indices, computing the Fourier transforms of the subsequences recursively, and then combining them using the butterfly operation. The time complexity is O(n log n).
  - Convex hull: Given a set of points in the plane, find the smallest convex polygon that contains all the points by dividing the set into two subsets, finding the convex hulls of the subsets recursively, and then merging the hulls using the upper and lower tangent algorithm. The time complexity is O(n log n).

### Greedy Methods

- Greedy methods are a technique of solving an optimization problem by making a sequence of choices that are locally optimal, hoping that they will lead to a globally optimal solution.
- The general idea of greedy methods is to have two steps:
  - Make a greedy choice that is the best option at the moment, without considering the future consequences.
  - Reduce the problem to a smaller subproblem that satisfies the feasibility and optimality conditions, and apply the same method recursively.
- Some examples of greedy methods are:
  - Optimal reliability allocation: Given a system of n components, each with a reliability and a cost, and a budget B, find the optimal allocation of the budget to improve the reliability of the components such that the overall reliability of the system is maximized. The greedy method is to sort the components by the ratio of reliability improvement to cost, and then allocate the budget to the components in that order until the budget is exhausted or all components are improved. The time complexity is O(n log n).
  - Knapsack problem: Given a set of items, each with a weight and a value, and a capacity W, find the subset of items that maximizes the total value without exceeding the capacity. The greedy method is to sort the items by the ratio of value to weight, and then select the items in that order until the capacity is reached or all items are considered. The time complexity is O(n log n).
  - Minimum spanning tree: Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. The greedy method is to start with an empty set of edges, and then repeatedly add the edge with the minimum weight that does not create a cycle, until all the vertices are connected. There are two variants of this method: Prim's algorithm and Kruskal's algorithm. The



# Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

## Divide and Conquer

- Divide and conquer is a technique for solving problems that involve breaking the problem into smaller subproblems that are similar to the original problem, solving them recursively, and then combining the results.
- Divide and conquer can reduce the time complexity of some problems from polynomial to logarithmic or even constant.
- Some examples of divide and conquer algorithms are:

### Sorting

- Sorting is the problem of arranging a list of elements in a certain order, such as ascending or descending.
- Some sorting algorithms that use divide and conquer are:

#### Merge Sort

- Merge sort works by dividing the list into two halves, sorting each half recursively, and then merging the two sorted halves into one sorted list.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list.
- The space complexity of merge sort is O(n), as it requires an auxiliary array to store the merged results.

#### Quick Sort

- Quick sort works by choosing a pivot element from the list, partitioning the list into two sublists such that all elements less than the pivot are in the left sublist and all elements greater than or equal to the pivot are in the right sublist, and then sorting each sublist recursively.
- The time complexity of quick sort is O(n log n) on average, but can be O(n^2) in the worst case, where n is the number of elements in the list.
- The space complexity of quick sort is O(log n) on average, but can be O(n) in the worst case, as it requires a stack to store the recursive calls.

### Matrix Multiplication

- Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and producing a third matrix as the result.
- The naive algorithm for matrix multiplication takes O(n^3) time, where n is the dimension of the square matrices.
- A divide and conquer algorithm for matrix multiplication is:

#### Strassen's Algorithm

- Strassen's algorithm works by dividing each matrix into four submatrices of equal size, computing seven products of submatrices using recursive calls, and then combining the results using addition and subtraction operations.
- The time complexity of Strassen's algorithm is O(n^log_2(7)), which is approximately O(n^2.81), where n is the dimension of the square matrices.
- The space complexity of Strassen's algorithm is O(n^2), as it requires auxiliary matrices to store the intermediate results.

### Convex Hull

- Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane.
- A convex polygon is a polygon that has no interior angles greater than 180 degrees, and a point is contained in a polygon if it is either on the boundary or in the interior of the polygon.
- A divide and conquer algorithm for convex hull is:

#### Graham Scan

- Graham scan works by finding the point with the lowest y-coordinate, called the pivot, sorting the rest of the points by the angle they make with the pivot and the x-axis, and then scanning the sorted points in a counterclockwise order, adding them to the convex hull if they make a left turn, and removing them if they make a right turn.
- The time complexity of Graham scan is O(n log n), where n is the number of points in the set.
- The space complexity of Graham scan is O(n), as it requires a stack to store the points in the convex hull.

### Searching

- Searching is the problem of finding a target element in a list of elements, or determining that it does not exist.
- Some searching algorithms that use divide and conquer are:

#### Binary Search

- Binary search works by comparing the target element with the middle element of the list, and then recursively searching the left or right half of the list depending on the comparison result.
- The time complexity of binary search is O(log n), where n is the number of elements in the list.
- The space complexity of binary search is O(log n), as it requires a stack to store the recursive calls.

#### Interpolation Search

- Interpolation search works by estimating the position of the target element in the list based on the values of the first and last elements and the target element, and then recursively searching the sublists around the estimated position depending on the comparison result.
- The time complexity of interpolation search is O(log log n) on average, but can be



### Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a paradigm for designing algorithms that solve a problem by recursively breaking it into smaller subproblems of the same type, until the subproblems are simple enough to be solved directly.
- The solutions of the subproblems are then combined to give a solution to the original problem.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same size and structure as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer algorithm again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by dividing it into smaller and easier parts.
- Some examples of divide and conquer algorithms are:
  - Binary search: This algorithm searches for a target value in a sorted array by repeatedly dividing the array into two halves and checking which half contains the target value.
  - Merge sort: This algorithm sorts an array by recursively dividing it into two halves, sorting each half, and then merging the two sorted halves.
  - Quick sort: This algorithm sorts an array by recursively choosing a pivot element, partitioning the array around the pivot, and then sorting the two subarrays on either side of the pivot.
  - Strassen's algorithm: This algorithm multiplies two matrices by recursively dividing them into four submatrices each, computing seven products of submatrices, and then combining the products to obtain the final result.
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by recursively dividing the sequence into two halves, computing the Fourier transform of each half, and then combining the results using the butterfly operation.



### Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure or properties.
- Some examples of divide and conquer algorithms are:
  - Merge sort: This algorithm sorts an array by dividing it into two halves, sorting each half recursively, and then merging the two sorted halves.
  - Quick sort: This algorithm sorts an array by choosing a pivot element, partitioning the array around the pivot, and then sorting the two subarrays recursively.
  - Binary search: This algorithm searches for a target element in a sorted array by comparing it with the middle element, and then recursively searching in the left or right subarray depending on the comparison result.
  - Strassen's algorithm: This algorithm multiplies two matrices by dividing them into four submatrices each, computing seven products of submatrices recursively, and then combining them to get the final product.
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by dividing it into two sequences of even and odd indices, computing their transforms recursively, and then combining them using complex roots of unity.
  - Convex hull: This algorithm finds the smallest convex polygon that contains a set of points in the plane by dividing the set into two halves, finding the hulls of each half recursively, and then merging the two hulls using a linear scan.



# Divide and Conquer with Examples

Divide and Conquer is a design technique for solving problems that involve breaking the problem into smaller subproblems, solving them recursively, and combining the solutions to get the final answer. This technique can often lead to efficient algorithms that have a lower time complexity than naive or brute-force solutions. Some examples of problems that can be solved using divide and conquer are:

- **Sorting**: Sorting is the process of arranging a collection of data in a certain order, such as ascending or descending. There are many sorting algorithms that use divide and conquer, such as merge sort, quicksort, and heap sort. These algorithms work by dividing the data into smaller parts, sorting them recursively, and merging or partitioning them to get the final sorted result. For example, merge sort splits the data into two halves, sorts them recursively, and then merges the sorted halves using a linear scan. The time complexity of merge sort is O(n log n), where n is the number of elements in the data .

- **Matrix Multiplication**: Matrix multiplication is the operation of multiplying two matrices of compatible dimensions to get a new matrix. A naive algorithm for matrix multiplication would take O(n^3) time, where n is the dimension of the matrices. However, using divide and conquer, we can reduce the time complexity to O(n^2.8074) using Strassen's algorithm, or even lower using other algorithms. Strassen's algorithm works by dividing each matrix into four submatrices, multiplying them recursively using seven multiplications instead of eight, and adding or subtracting them to get the final result .

- **Convex Hull**: Convex hull is the smallest convex polygon that contains a set of points in a plane. A convex polygon is one that has no interior angles greater than 180 degrees. A naive algorithm for finding the convex hull would take O(n^3) time, where n is the number of points. However, using divide and conquer, we can reduce the time complexity to O(n log n) using Graham's scan or Jarvis's march algorithms. These algorithms work by dividing the points into two halves, finding the convex hull of each half recursively, and merging them using a linear scan.

- **Searching**: Searching is the process of finding a specific element or value in a collection of data. There are many searching algorithms that use divide and conquer, such as binary search, interpolation search, and exponential search. These algorithms work by dividing the search space into smaller parts, searching them recursively, and returning the result. For example, binary search splits the data into two halves, compares the middle element with the target value, and discards the half that does not contain the target. The time complexity of binary search is O(log n), where n is the number of elements in the data .

# Greedy Methods with Examples

Greedy methods are a design technique for solving problems that involve making a sequence of choices that maximize or minimize some objective function. Greedy methods work by choosing the best option available at each step, without considering the future consequences. Greedy methods can often lead to optimal or near-optimal solutions for some problems, but not for all. Some examples of problems that can be solved using greedy methods are:

- **Optimal Reliability Allocation**: Optimal reliability allocation is the problem of allocating a given budget to improve the reliability of a system composed of several components. The objective is to maximize the overall reliability of the system. A greedy method for solving this problem is to allocate the budget to the component that has the highest ratio of reliability improvement to cost at each step, until the budget is exhausted or the system reaches a desired reliability level.

- **Knapsack**: Knapsack is the problem of packing a set of items with different weights and values into a knapsack with a limited capacity. The objective is to maximize the total value of the items in the knapsack. A greedy method for solving this problem is to sort the items by their value-to-weight ratio, and pack the items in descending order of this ratio, until the knapsack is full or no more items can be packed.

- **Minimum Spanning Trees**: Minimum spanning tree is the problem of finding a subset of edges in a weighted undirected graph that connects all the vertices and has the minimum total weight. The objective is to minimize the cost of building a network that connects all the nodes. A greedy method for solving this problem is to sort the edges by their weight, and add the edges in ascending order



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on greedy methods in algorithm design.

### Greedy Methods

- Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution.
- Greedy methods do not consider the future consequences of the current choices, and may end up with a suboptimal or even incorrect solution.
- Greedy methods are suitable for problems where the optimal solution can be obtained by making greedy choices, or where an approximate solution is acceptable.
- Greedy methods are often simple, fast, and easy to implement, but they may not work for all problems.

### Examples of Greedy Methods

- Optimal Reliability Allocation: This is a problem of allocating a given budget to improve the reliability of different components of a system, such that the overall system reliability is maximized. A greedy method for this problem is to allocate the budget to the component with the highest marginal benefit, i.e., the component that increases the system reliability the most per unit of budget spent, until the budget is exhausted or all components are improved to their maximum reliability.
- Knapsack Problem: This is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized. A greedy method for this problem is to sort the items by their value-to-weight ratio, and pack the items in decreasing order of this ratio, until the knapsack is full or no more items can be packed.
- Minimum Spanning Tree: This is a problem of finding a subset of edges in a weighted undirected graph that connects all the vertices with the minimum total weight. A greedy method for this problem is to start with an empty set of edges, and add the edge with the smallest weight that does not form a cycle, until all the vertices are connected. This is known as Prim's algorithm. Another greedy method is to sort the edges by their weights, and add the edge with the smallest weight that does not form a cycle, until all the vertices are connected. This is known as Kruskal's algorithm.
- Single Source Shortest Paths: This is a problem of finding the shortest paths from a given source vertex to all other vertices in a weighted directed graph. A greedy method for this problem is to maintain a set of vertices whose shortest paths from the source are known, and a set of vertices whose shortest paths are unknown. Initially, the known set contains only the source vertex, and the unknown set contains all other vertices. At each step, the algorithm selects the vertex in the unknown set that has the smallest distance from the source, and moves it to the known set. Then, the algorithm updates the distances of the adjacent vertices in the unknown set, if they can be reduced by using the newly added vertex. This is repeated until the unknown set is empty. This is known as Dijkstra's algorithm. Another greedy method is to use a queue to store the vertices whose shortest paths are known, and a priority queue to store the vertices whose shortest paths are unknown. Initially, the queue contains only the source vertex, and the priority queue contains all other vertices with their distances from the source. At each step, the algorithm dequeues the vertex from the queue, and relaxes the edges from that vertex to its adjacent vertices in the priority queue, i.e., updates their distances and predecessors if they can be reduced by using the dequeued vertex. Then, the algorithm enqueues the vertex with the smallest distance from the priority queue to the queue, and removes it from the priority queue. This is repeated until the priority queue is empty. This is known as Bellman-Ford algorithm.

: Greedy Algorithms - GeeksforGeeks, https://www.geeksforgeeks.org/greedy-algorithms/



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods are simple, fast and easy to implement, but they do not always guarantee the best possible result. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem can be obtained by using optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be reached by making the locally optimal choice at each step.

Some examples of greedy methods are:

- **Knapsack problem**: Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, find the most valuable subset of items that fit in the knapsack. A greedy method for this problem is to sort the items by their value-to-weight ratio and pick the items with the highest ratio until the knapsack is full or no more items are left. This method may not find the optimal solution, but it is a good approximation.
- **Minimum spanning tree**: Given a connected, undirected and weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. A greedy method for this problem is to start with an empty set of edges and add the edge with the lowest weight that does not form a cycle with the existing edges, until all the vertices are connected. This method is guaranteed to find the optimal solution, and there are two well-known algorithms that implement it: Prim's algorithm and Kruskal's algorithm.
- **Single source shortest path**: Given a weighted graph and a source vertex, find the shortest path from the source to every other vertex in the graph. A greedy method for this problem is to maintain a set of vertices whose shortest distance from the source is known, and a priority queue of vertices whose distance is estimated. At each step, extract the vertex with the minimum distance from the queue, update the distance of its adjacent vertices, and add them to the queue if they are not already in the set. This method is guaranteed to find the optimal solution, and there are two well-known algorithms that implement it: Dijkstra's algorithm and Bellman-Ford algorithm.
- **Optimal reliability allocation**: Given a system composed of n components, each with a reliability and a cost, and a budget B, find the optimal allocation of the budget to improve the reliability of the components, such that the overall reliability of the system is maximized. A greedy method for this problem is to sort the components by their marginal return on investment (MROI), which is the ratio of the increase in reliability to the increase in cost, and allocate the budget to the components with the highest MROI until the budget is exhausted or no more improvement is possible. This method may not find the optimal solution, but it is a good approximation.



# Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast, and easy to implement, but they may not always yield the best solution.
- Greedy methods can be applied to various optimization problems, such as finding the minimum spanning tree, the optimal reliability allocation, the knapsack problem, and the single source shortest paths problem.

## Minimum Spanning Tree

- A spanning tree of a graph G is a subset of the edges of G that form a tree and include all vertices of G.
- A minimum spanning tree (MST) of a graph G is a spanning tree of G that has the minimum possible total edge weight.
- Finding an MST is useful for applications such as network design, clustering, image segmentation, and approximation algorithms.

### Prim's Algorithm

- Prim's algorithm is a greedy algorithm that finds an MST by starting with a single node and adding the cheapest edge that connects it to another node that is not already in the tree.
- The algorithm repeats this process until all nodes are in the tree.
- Prim's algorithm can be implemented using a priority queue to store the edges and their weights, and a set to keep track of the nodes in the tree.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices.

### Kruskal's Algorithm

- Kruskal's algorithm is another greedy algorithm that finds an MST by sorting the edges by their weights and adding them to the tree one by one, as long as they do not create a cycle.
- The algorithm uses a disjoint-set data structure to keep track of the connected components of the tree and to check for cycles.
- The time complexity of Kruskal's algorithm is O(E log E), which is equivalent to O(E log V) since E is at most V^2.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum. Greedy algorithms are often used to solve optimization problems, such as finding the minimum or maximum of a function, or finding the best way to allocate resources. Greedy algorithms have some advantages and disadvantages:

- Advantages:
  - They are easy to implement and understand.
  - They are fast and efficient for some problems.
  - They can provide good approximations for some problems.
- Disadvantages:
  - They are not guaranteed to find the optimal solution for every problem.
  - They can be easily misled by local optima and fail to explore better solutions.
  - They can be hard to prove their correctness and optimality.

Some examples of greedy algorithms are:

- Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms: These algorithms find the shortest path from a given source node to all other nodes in a weighted graph. They use a greedy strategy of selecting the node with the minimum distance from the source and updating the distances of its neighbors. Dijkstra's algorithm works for graphs with non-negative edge weights, while Bellman Ford algorithm works for graphs with negative edge weights as well.
- Optimal Reliability Allocation: This problem involves allocating a fixed budget to improve the reliability of a system composed of n components. Each component has a cost and a reliability function, and the system reliability is the product of the component reliabilities. The greedy algorithm allocates the budget to the component that has the highest marginal increase in system reliability per unit cost, until the budget is exhausted or the system reliability reaches a desired level.
- Knapsack Problem: This problem involves packing a knapsack with a given capacity with items that have different weights and values, such that the total value of the items is maximized. The greedy algorithm sorts the items by their value-to-weight ratio and selects the items with the highest ratio, until the knapsack is full or no more items can be added.
- Minimum Spanning Tree - Prim’s and Kruskal’s Algorithms: These algorithms find a subset of edges in a weighted graph that connects all the nodes with the minimum total weight. They use a greedy strategy of selecting the edge with the minimum weight that does not create a cycle in the spanning tree. Prim's algorithm starts with an arbitrary node and grows the tree by adding the nearest node, while Kruskal's algorithm starts with an empty set of edges and adds the shortest edge that connects two disjoint sets of nodes.
- Activity Selection Problem: This problem involves selecting a maximum number of activities that do not overlap in time, given the start and finish times of each activity. The greedy algorithm sorts the activities by their finish times and selects the activity that finishes the earliest, and then repeats the process for the remaining activities that do not conflict with the selected one.



## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

### Dynamic Programming
- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to problems that can be divided into stages, where each stage has a set of states and decisions. The goal is to find an optimal sequence of decisions that leads to the optimal final state.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. Top-down approach starts from the original problem and recursively breaks it down into smaller subproblems, until the base cases are reached. Bottom-up approach starts from the base cases and iteratively builds up the solution for larger subproblems, until the original problem is solved.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the intermediate results in a table or an array.

### Knapsack Problem
- Knapsack problem is an example of a dynamic programming problem. It is also known as 0-1 knapsack problem, because each item can be either included or excluded from the knapsack.
- The problem is to find the maximum value of items that can be packed into a knapsack of a given capacity, without exceeding the weight limit.
- The problem can be formulated as follows:

  - Let n be the number of items, and W be the capacity of the knapsack.
  - Let w[i] and v[i] be the weight and value of the i-th item, for i = 1, 2, ..., n.
  - Let x[i] be a binary variable that indicates whether the i-th item is included in the knapsack or not, for i = 1, 2, ..., n.
  - The objective is to maximize the total value of the items in the knapsack, given by:

    - `sum(i = 1 to n) x[i] * v[i]`

  - The constraint is to not exceed the weight limit of the knapsack, given by:

    - `sum(i = 1 to n) x[i] * w[i] <= W`

- The problem can be solved using dynamic programming as follows:

  - Define a function `f(i, j)` that returns the maximum value of items that can be packed into a knapsack of capacity j, using only the first i items, for i = 0, 1, ..., n and j = 0, 1, ..., W.
  - The base cases are:

    - `f(0, j) = 0` for all j, because no items can be packed into an empty knapsack.
    - `f(i, 0) = 0` for all i, because no items can be packed into a knapsack of zero capacity.

  - The recursive relation is:

    - `f(i, j) = max(f(i - 1, j), f(i - 1, j - w[i]) + v[i])` for all i > 0 and j > 0, because the optimal solution for a knapsack of capacity j, using the first i items, is either to exclude the i-th item and use the optimal solution for a knapsack of capacity j, using the first i - 1 items, or to include the i-th item and use the optimal solution for a knapsack of capacity j - w[i], using the first i - 1 items.

  - The final solution is given by `f(n, W)`, which is the maximum value of items that can be packed into a knapsack of capacity W, using all n items.
  - The optimal subset of items can be traced back by checking the values of `f(i, j)` and `x[i]` in the table or array.

- The time complexity of this algorithm is O(nW), where n is the number of items and W is the capacity of the knapsack. The space complexity is also O(nW), because a table or an array of size n x W is used to store the intermediate results.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms
- All pair shortest paths problem is another example of



# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which leads to wasteful computation.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming avoids repeated computation by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have the following characteristics:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems are independent of each other, i.e., solving one subproblem does not affect the solution of another subproblem.
  - There is an optimal way of combining the solutions of the subproblems to obtain the solution of the original problem.

## Knapsack Problem

- The knapsack problem is a classic example of a problem that can be solved using dynamic programming.
- The problem statement is as follows:
  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- There are two variants of the knapsack problem: the 0/1 knapsack problem and the fractional knapsack problem.
- In the 0/1 knapsack problem, each item can be either included or excluded from the collection, i.e., the decision is binary.
- In the fractional knapsack problem, each item can be partially included in the collection, i.e., the decision is fractional.

### 0/1 Knapsack Problem using Dynamic Programming

- To solve the 0/1 knapsack problem using dynamic programming, we use a two-dimensional table to store the optimal value for each subproblem.
- The table has n rows and M columns, where n is the number of items and M is the capacity of the knapsack.
- The entry in the i-th row and j-th column of the table, denoted by V[i][j], represents the maximum value that can be obtained by using the first i items and a knapsack of capacity j.
- The table can be filled up using the following recurrence relation:

  - V[i][j] = max(V[i-1][j], V[i-1][j-w[i]] + v[i]), if j >= w[i]
  - V[i][j] = V[i-1][j], otherwise

- The first case corresponds to including the i-th item in the collection, and the second case corresponds to excluding it.
- The base cases are:

  - V[0][j] = 0, for all j
  - V[i][0] = 0, for all i

- The optimal value of the problem is given by V[n][M], which is the bottom-right entry of the table.
- To find the optimal subset of items, we can trace back the table from V[n][M] and check which items were included or excluded at each step.

#### Example

- Consider the following 0/1 knapsack problem:

  - Number of items n = 4
  - Knapsack capacity M = 5
  - Weights (w1, w2, w3, w4) = (2, 3, 4, 5)
  - Values (v1, v2, v3, v4) = (3, 4, 5, 6)

- The table for this problem is shown below:

| i\j | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | - | - | - | - | - | - |
| 0   | 0 | 0 | 0 | 0 | 0 | 0 |
| 1   | 0 | 0 | 3 | 3 | 3 | 3 |
| 2   | 0 | 0 | 3 | 4 | 4 | 7 |
| 3   | 0 | 0 | 3 | 4 | 5 | 7 |
| 4   | 0 | 0 | 3 | 4 | 5 | 7 |

- The optimal value is V[4][5] = 7, which means that the maximum value that can be obtained by using the first



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on dynamic programming with examples such as all pair shortest paths warshal's and floyd's algorithms.

### Dynamic Programming
- Dynamic programming is a technique for solving optimization problems by breaking them down into smaller subproblems and storing the solutions of the subproblems in a table.
- Dynamic programming can be applied to problems that have two properties: optimal substructure and overlapping subproblems.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Overlapping subproblems means that the same subproblems are encountered and solved repeatedly while solving the original problem.

### All Pair Shortest Paths
- All pair shortest paths problem is to find the shortest distance between every pair of vertices in a weighted graph, where the edge weights can be positive, negative or zero.
- There are two main algorithms for solving this problem: Warshal's algorithm and Floyd's algorithm.
- Both algorithms use dynamic programming and have a time complexity of O(V^3), where V is the number of vertices in the graph.
- Both algorithms also require a matrix of size V x V to store the intermediate and final results.

### Warshal's Algorithm
- Warshal's algorithm is also known as the transitive closure algorithm, as it computes the transitive closure of a binary relation on a finite set.
- Transitive closure of a relation R on a set S is the smallest relation that contains R and is transitive, i.e., if (a, b) and (b, c) are in the relation, then (a, c) is also in the relation.
- Warshal's algorithm can be used to find the shortest paths in a graph by considering the edge weights as 0 or 1, where 0 means no edge and 1 means an edge of length 1.
- Warshal's algorithm works by iteratively updating the matrix M, where M[i][j] is 1 if there is a path from i to j, and 0 otherwise.
- The algorithm starts with M[i][j] = 1 if there is an edge from i to j, and 0 otherwise.
- Then, for each vertex k, the algorithm updates M[i][j] by setting it to 1 if M[i][k] and M[k][j] are both 1, i.e., if there is a path from i to j through k.
- The algorithm terminates when no more updates are possible, and the final matrix M contains the transitive closure of the graph.

### Floyd's Algorithm
- Floyd's algorithm is also known as the all-pairs shortest paths algorithm, as it computes the shortest distance between every pair of vertices in a weighted graph.
- Floyd's algorithm can handle negative edge weights, but not negative cycles, i.e., cycles whose total weight is negative.
- Floyd's algorithm works by iteratively updating the matrix D, where D[i][j] is the shortest distance from i to j.
- The algorithm starts with D[i][j] = w(i, j), where w(i, j) is the weight of the edge from i to j, or infinity if there is no edge.
- Then, for each vertex k, the algorithm updates D[i][j] by setting it to min(D[i][j], D[i][k] + D[k][j]), i.e., the minimum of the current distance and the distance through k.
- The algorithm terminates when no more updates are possible, and the final matrix D contains the shortest distances between all pairs of vertices in the graph.



# Dynamic Programming with Examples Such as Resource Allocation Problem

## What is Dynamic Programming?

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can be implemented using either a top-down (memoization) or a bottom-up (tabulation) approach.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the results in a table or an array.

## Resource Allocation Problem

- A resource allocation problem is a type of optimization problem where a resource or resources are allocated to a number of independent activities in order to maximize the total return or minimize the total cost.
- A resource allocation problem can be formulated as a dynamic programming problem if the following conditions are met:
  - The resource or resources are divisible and can be allocated in fractional units.
  - The activities are ordered and the allocation of a resource to an activity depends only on the amount of resource available and the previous allocations.
  - The return or cost function of each activity is concave or convex, respectively, and satisfies the principle of diminishing returns or increasing costs, respectively.
- A resource allocation problem can be solved using dynamic programming by defining the following elements:
  - The state variable: the amount of resource available at each stage (activity).
  - The decision variable: the amount of resource allocated to each activity.
  - The state transition equation: the relation between the state variables of consecutive stages.
  - The return or cost function: the function that gives the return or cost of allocating a certain amount of resource to an activity.
  - The objective function: the function that gives the total return or cost of allocating the resource to all the activities.
  - The boundary conditions: the initial and final values of the state variable.

## Example: Resource Allocation Problem with One Resource and N Activities

- Suppose there is one resource with X units available, and N activities that can use the resource. The return from allocating x units of resource to activity k is given by r_k(x), where r_k(x) is a concave function and satisfies r_k(0) = 0 and r_k'(x) > 0 for all x > 0. The objective is to maximize the total return from allocating the resource to all the activities.
- The dynamic programming formulation of this problem is as follows:
  - The state variable: x_k, the amount of resource available after allocating to activity k, for k = 0, 1, ..., N. Note that x_0 = X and x_N = 0.
  - The decision variable: x_k - x_k+1, the amount of resource allocated to activity k+1, for k = 0, 1, ..., N-1.
  - The state transition equation: x_k+1 = x_k - (x_k - x_k+1), for k = 0, 1, ..., N-1.
  - The return function: r_k+1(x_k - x_k+1), the return from allocating x_k - x_k+1 units of resource to activity k+1, for k = 0, 1, ..., N-1.
  - The objective function: R(x_0, x_1, ..., x_N) = sum_{k=0}^{N-1} r_k+1(x_k - x_k+1), the total return from allocating the resource to all the activities.
  - The boundary conditions: x_0 = X and x_N = 0.
- The optimal solution of this problem can be obtained by using the following recursive relation:

  - R(x_k, x_k+1, ..., x_N) = max_{0 <= x_k - x_k+1 <= x_k} {r_k+1(x_k - x_k+1) + R(x_k+1, x_k+2, ..., x_N)}, for k = 0, 1, ..., N-1.
  - R(x_N) = 0.

- The optimal allocation of the resource to each activity can be found by tracing back the optimal values of x_k, for k = 0, 1, ..., N.



### Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a finite set of possible solutions. Both techniques use a state-space tree to represent the solution space, where each node corresponds to a partial or complete solution. The root node represents an empty solution, and the leaf nodes represent feasible solutions. The goal is to find the optimal solution among the feasible ones, or to determine if there is no feasible solution.

Backtracking is a recursive algorithm that explores the state-space tree in a depth-first manner. It starts from the root node and generates one child node at a time. If the child node is promising, meaning that it could lead to a feasible or optimal solution, the algorithm moves to that node and repeats the process. If the child node is not promising, meaning that it violates some constraints or cannot improve the current best solution, the algorithm backtracks to the parent node and tries another child node. Backtracking can be used to solve problems such as sudoku, n-queen, graph coloring, and Hamiltonian cycles.

Branch and bound is a similar algorithm that also explores the state-space tree in a depth-first manner. However, it uses a bounding function to prune the tree and avoid exploring unpromising nodes. The bounding function computes a lower bound (for minimization problems) or an upper bound (for maximization problems) for the optimal solution that can be obtained from a node. If the bound is worse than the current best solution, the node and its subtree are discarded. Otherwise, the node is expanded and its children are evaluated. Branch and bound can be used to solve problems such as 0/1 knapsack, travelling salesman, and resource allocation.

One example of using branch and bound to solve the travelling salesman problem (TSP) is as follows:

- The TSP is a problem of finding the shortest tour that visits a set of n cities exactly once and returns to the starting city.
- The state-space tree for the TSP has n! leaf nodes, each representing a permutation of the cities. The root node represents an empty tour, and each internal node represents a partial tour that visits some cities.
- The bounding function for the TSP is based on the idea of a minimum spanning tree (MST). Given a partial tour, the bounding function computes the cost of completing the tour by connecting the remaining cities with a MST. This cost is a lower bound for the optimal tour that can be obtained from the node.
- The branch and bound algorithm starts from the root node and computes its bound. If the bound is better than the current best solution, the algorithm expands the node and generates its children. Each child node represents a partial tour that extends the parent tour by one city. The algorithm computes the bound for each child node and compares it with the current best solution. If the bound is worse, the child node is pruned. Otherwise, the algorithm moves to the child node and repeats the process. The algorithm terminates when all nodes are either pruned or expanded, and returns the best solution found.



### Backtracking, Branch and Bound with Examples Such as Graph Coloring

- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large number of possibilities. It works by incrementally building a partial solution and then checking if it satisfies some constraints. If not, it backtracks to the previous state and tries a different option. Backtracking is often used for combinatorial optimization problems, such as Sudoku, n-queens, etc.
- Branch and bound is a technique to solve optimization problems that involve finding the best solution among a large number of possibilities. It works by dividing the problem into smaller subproblems and then bounding the quality of the optimal solution in each subproblem. It then prunes the subproblems that cannot lead to a better solution than the current best one. Branch and bound is often used for problems such as traveling salesman, knapsack, etc.
- Graph coloring is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. It has applications in scheduling, map coloring, register allocation, etc. Graph coloring can be solved using both backtracking and branch and bound techniques.

#### Example of Graph Coloring using Backtracking

- Given a graph G and m colors, the goal is to find a valid coloring of the vertices using at most m colors, or report that no such coloring exists.
- A possible algorithm using backtracking is:

```
# Input: graph G, number of colors m, current vertex v
# Output: a valid coloring of G using at most m colors, or None if no such coloring exists
def graph_coloring(G, m, v):
  # Base case: if all vertices are colored, return the coloring
  if v == len(G):
    return coloring
  # Try each color from 1 to m for the current vertex
  for c in range(1, m+1):
    # Check if the color c is valid for the current vertex, i.e. no adjacent vertex has the same color
    if is_valid(G, coloring, v, c):
      # Assign the color c to the current vertex
      coloring[v] = c
      # Recursively color the next vertex
      result = graph_coloring(G, m, v+1)
      # If a valid coloring is found, return it
      if result is not None:
        return result
      # Otherwise, backtrack and try a different color
      coloring[v] = 0
  # If no color is valid for the current vertex, return None
  return None
```

#### Example of Graph Coloring using Branch and Bound

- Given a graph G and m colors, the goal is to find the minimum number of colors needed to color the vertices of G, or report that no such coloring exists.
- A possible algorithm using branch and bound is:

```
# Input: graph G, number of colors m
# Output: the minimum number of colors needed to color G, or None if no such coloring exists
def graph_coloring(G, m):
  # Initialize the best solution as None
  best = None
  # Initialize the queue of subproblems as empty
  queue = []
  # Enqueue the initial subproblem, which is to color the first vertex with any color
  queue.append((0, [0] * len(G)))
  # While the queue is not empty
  while queue:
    # Dequeue the first subproblem
    v, coloring = queue.pop(0)
    # If the subproblem is complete, i.e. all vertices are colored
    if v == len(G):
      # Update the best solution if it is better than the current one
      if best is None or max(coloring) < best:
        best = max(coloring)
    # Otherwise, if the subproblem is feasible, i.e. the number of colors used so far is less than or equal to m
    elif max(coloring) <= m:
      # For each color from 1 to m
      for c in range(1, m+1):
        # Check if the color c is valid for the current vertex, i.e. no adjacent vertex has the same color
        if is_valid(G, coloring, v, c):
          # Assign the color c to the current vertex
          coloring[v] = c
          # Enqueue the next subproblem, which is to color the next vertex with any color
          queue.append((v+1, coloring.copy()))
  # Return the best solution
  return best
```



### Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be applied to problems that can be represented as a state space tree, where each node is a partial solution and the leaves are the complete solutions. 
- The basic idea of backtracking is to explore the nodes of the state space tree in a depth-first manner, and prune the branches that do not lead to a feasible solution. 
- The backtracking algorithm can be described as follows :

```
procedure backtrack(P, c) is
  if reject(P, c) then return
  if accept(P, c) then output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate solution, reject(P, c) is a function that returns true if c is not a valid solution, accept(P, c) is a function that returns true if c is a complete and valid solution, output(P, c) is a function that prints or stores the solution c, first(P, c) is a function that returns the first extension of c, and next(P, c, s) is a function that returns the next extension of c after s.
- An example of a problem that can be solved by backtracking is the n-queen problem, where the goal is to place n queens on an n x n chessboard such that no two queens attack each other. 
- A possible state space tree for the n-queen problem is shown below, where each node represents a partial placement of queens on the board, and the leaves are the complete placements. The nodes marked with X are pruned by the reject function, as they violate the constraint that no two queens can be on the same row, column, or diagonal. The nodes marked with O are the valid solutions.

n-queen state space tree

- The pseudocode for the n-queen problem using backtracking is given below :

```
procedure nqueen(n) is
  create an empty array board of size n
  placeQueens(board, 0, n)

procedure placeQueens(board, row, n) is
  if row == n then
    output(board)
    return
  for col from 0 to n - 1 do
    if isSafe(board, row, col, n) then
      board[row] = col
      placeQueens(board, row + 1, n)
      board[row] = -1 // backtrack

function isSafe(board, row, col, n) is
  for i from 0 to row - 1 do
    if board[i] == col or abs(board[i] - col) == abs(i - row) then
      return false
  return true
```

- Here, board is an array that stores the column index of the queen placed in each row, row is the current row to place a queen, n is the size of the board, output(board) is a function that prints or stores the board configuration, and isSafe(board, row, col, n) is a function that checks if placing a queen at (row, col) does not conflict with the previous queens.



### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve a computational problem.
- Backtracking works by recursively trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).
- Backtracking can be applied to solve problems that involve finding all (or some) of the solutions to a problem, such as generating permutations, combinations, or subsets of a set of elements; solving puzzles such as Sudoku, N-Queens, or crossword; and finding an optimal solution for optimization problems such as the knapsack problem or the traveling salesman problem.
- Backtracking is often implemented using recursion, where the recursive calls correspond to exploring the subproblems of the original problem, and the base cases correspond to reaching a leaf node in the search tree, where a solution is either found or rejected.
- Backtracking can be optimized by using some heuristics or pruning techniques to avoid exploring parts of the search space that are guaranteed to be irrelevant or suboptimal.

#### Hamiltonian Cycles

- A Hamiltonian cycle (or Hamiltonian circuit) is a cycle in an undirected graph that visits each vertex exactly once and also returns to the starting vertex.
- Finding a Hamiltonian cycle in a given graph is an NP-complete problem, meaning that there is no known efficient algorithm that can solve it in polynomial time for all possible inputs.
- However, backtracking can be used to find a Hamiltonian cycle (if it exists) in a given graph, by trying to extend a partial solution (a path that visits some of the vertices) until it becomes a cycle that covers all the vertices.
- The algorithm works as follows:

  - Start from any vertex and mark it as visited.
  - For each adjacent vertex that is not visited, add it to the path and recursively check if this path can be extended to a Hamiltonian cycle.
  - If the path cannot be extended, remove the last vertex from the path and backtrack to the previous vertex.
  - If the path can be extended to a cycle that visits all the vertices, return the path as a solution.
  - If all the adjacent vertices are visited and the path is not a cycle, return false.

- The algorithm can be implemented using a boolean array to keep track of the visited vertices, and a list or an array to store the path.
- The algorithm can be optimized by using some heuristics, such as ordering the vertices by their degree (the number of adjacent vertices) or using a bitset instead of a boolean array to reduce the space complexity.



### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be viewed as a way of traversing a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem.
- The basic idea of backtracking is to start from the root of the state space tree and explore the branches of the tree until a solution is found or all the possibilities are exhausted.
- The backtracking algorithm can be defined as follows:

```
procedure backtrack(P, c) is
  if reject(P, c) then return
  if accept(P, c) then output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate solution, reject(P, c) is a function that returns true if c is not a valid solution or cannot be extended to a valid solution, accept(P, c) is a function that returns true if c is a valid solution, output(P, c) is a function that prints or stores the solution c, first(P, c) is a function that returns the first extension of c, and next(P, c, s) is a function that returns the next extension of c after s.
- An example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value.
- The state space tree for the sum of subsets problem can be constructed as follows:
  - The root node represents an empty subset with sum 0.
  - Each node has two children, one representing the inclusion of the next element in the subset, and the other representing the exclusion of the next element in the subset.
  - The nodes are labeled with the sum of the elements in the subset and the index of the next element to be considered.
  - The nodes that have a sum greater than the target value or have exhausted all the elements are rejected and pruned from the tree.
  - The nodes that have a sum equal to the target value and have exhausted all the elements are accepted and output as solutions.
- For example, consider the set {10, 7, 5, 18, 12, 20, 15} and the target value 35. The state space tree for this problem is shown below, where the nodes in green are accepted, the nodes in red are rejected, and the nodes in black are intermediate.

State space tree for sum of subsets problem

- The solutions are {10, 7, 18}, {10, 5, 20}, {10, 12, 15}, {7, 5, 12, 15}, and {5, 18, 12}.



## Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the difficulty of solving certain problems in polynomial time. A problem is NP-complete if it belongs to the class NP (nondeterministic polynomial time) and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for all NP problems, which is considered unlikely by most computer scientists.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions. An approximation algorithm does not guarantee the best solution, but rather a solution that is close to the optimal one in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution  .
- Some examples of NP-complete problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting city. This problem is NP-complete, and there is no known polynomial time algorithm that can find the optimal tour. However, there are some approximation algorithms that can find tours that are within a constant factor of the optimal one, such as the Christofides algorithm, which guarantees a 3/2-approximation ratio.
  - Graph Coloring: Given an undirected graph, assign a color to each vertex such that no two adjacent vertices have the same color, and use the minimum number of colors possible. This problem is NP-complete, and there is no known polynomial time algorithm that can find the optimal coloring. However, there are some approximation algorithms that can find colorings that use at most a constant factor more colors than the optimal one, such as the greedy algorithm, which guarantees a (Δ+1)-approximation ratio, where Δ is the maximum degree of the graph.
  - n-Queen Problem: Given an n x n chessboard, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem is NP-complete, and there is no known polynomial time algorithm that can find a solution for any n. However, there are some algorithms that can find solutions for some values of n, such as the backtracking algorithm, which tries different placements of queens and backtracks if a conflict is found.
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting vertex. This problem is NP-complete, and there is no known polynomial time algorithm that can find a Hamiltonian cycle. However, there are some approximation algorithms that can find cycles that visit most of the vertices, such as the greedy algorithm, which starts from a vertex and adds the closest unvisited vertex to the cycle until no more vertices can be added.
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the integers that adds up to the target sum. This problem is NP-complete, and there is no known polynomial time algorithm that can find a solution. However, there are some approximation algorithms that can find subsets that are close to the target sum, such as the greedy algorithm, which sorts the integers in decreasing order and adds the largest one that does not exceed the remaining sum until the sum is reached or no more integers can be added.



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that there is a nondeterministic algorithm that can solve the problem in polynomial time.
- NP-hard means that any problem in NP can be reduced to the problem in polynomial time, which means that the problem is at least as hard as any problem in NP.
- NP-complete problems are the hardest problems in NP, and there is no known polynomial time algorithm to solve them, unless P = NP, which is a major open question in computer science.
- Examples of NP-complete problems are: satisfiability problem (SAT), traveling salesman problem (TSP), graph coloring problem, n-queen problem, Hamiltonian cycle problem, and sum of subsets problem.

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions.
- Approximation algorithms do not guarantee the optimal solution, but they aim to come as close as possible to the optimal solution in polynomial time.
- Approximation algorithms have a performance guarantee, which is a ratio between the value of the solution obtained by the algorithm and the value of the optimal solution.
- For example, a 2-approximation algorithm for the vertex cover problem guarantees that the size of the vertex cover found by the algorithm is at most twice the size of the optimal vertex cover.
- Examples of approximation algorithms are: greedy algorithm for the set cover problem, Christofides algorithm for the metric TSP, local search algorithm for the graph coloring problem, backtracking algorithm for the n-queen problem, and dynamic programming algorithm for the sum of subsets problem.



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in O(n^k) time for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in O(n^k) time whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science.
- Examples of NP-complete problems are: 
  - Satisfiability (SAT): Given a boolean formula with variables and logical operators, is there an assignment of true or false values to the variables that makes the formula true?
  - Traveling Salesman Problem (TSP): Given a set of cities and distances between them, is there a tour that visits each city exactly once and has a total length less than or equal to a given limit?
  - Graph Coloring: Given a graph and a number of colors, is there a way to assign a color to each vertex such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a chessboard of size n x n, is there a way to place n queens on the board such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits each vertex exactly once?
  - Subset Sum: Given a set of integers and a target sum, is there a subset of the integers that adds up to the target sum?

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, usually by minimizing or maximizing some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal in polynomial time, usually by giving a performance guarantee or an approximation ratio.
- An approximation ratio is a measure of how good the solution found by the algorithm is compared to the optimal solution. For example, if the algorithm finds a solution that is at most twice as bad as the optimal solution, then the approximation ratio is 2. The lower the approximation ratio, the better the algorithm.
- Examples of approximation algorithms are:
  - TSP: There is a 2-approximation algorithm that uses a minimum spanning tree to construct a tour that is at most twice as long as the optimal tour.
  - Graph Coloring: There is a (Δ+1)-approximation algorithm that uses a greedy strategy to color the vertices with at most Δ+1 colors, where Δ is the maximum degree of the graph.
  - n-Queen Problem: There is a (n/2)-approximation algorithm that places n/2 queens on the main diagonal and n/2 queens on the secondary diagonal, which is at most half as good as the optimal solution of n queens.
  - Hamiltonian Cycle: There is a 2-approximation algorithm that uses a minimum spanning tree to construct a cycle that is at most twice as long as the optimal cycle.
  - Subset Sum: There is a (1+ε)-approximation algorithm that uses dynamic programming to find a subset that sums up to a value that is within ε of the target sum, where ε is a small positive constant.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the topic you requested:

# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP stands for non-deterministic polynomial time, which is a class of problems that can be verified in polynomial time, but not necessarily solved in polynomial time.
- NP-complete problems are the hardest problems in NP, meaning that any problem in NP can be reduced to an NP-complete problem in polynomial time.
- If there is a polynomial time algorithm for any NP-complete problem, then P = NP, which is one of the most famous open problems in computer science. However, most experts believe that P ≠ NP, which implies that there is no polynomial time algorithm for any NP-complete problem.
- Some examples of NP-complete problems are:
  - Travelling Salesman Problem (TSP): Given a set of cities and distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, assign a color to each vertex such that no two adjacent vertices have the same color, using at most k colors.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other (i.e., no two queens share the same row, column, or diagonal).
  - Hamiltonian Cycle: Given a graph, find a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target value, find a subset of the set that sums up to the target value.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution, but rather a solution that is close to the optimal one, within some factor or bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, while providing a measure of the quality of the solution, such as the approximation ratio or the performance guarantee.
- The approximation ratio of an algorithm is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution, for any instance of the problem. The performance guarantee of an algorithm is the worst-case approximation ratio over all possible instances of the problem.
- Some examples of approximation algorithms are:
  - TSP: There is a 2-approximation algorithm that uses a minimum spanning tree and a depth-first traversal to construct a tour. The approximation ratio is 2 because the length of the tour is at most twice the length of the optimal tour.
  - Graph Coloring: There is a simple greedy algorithm that assigns the smallest available color to each vertex in some order. The approximation ratio is ∆ + 1, where ∆ is the maximum degree of the graph, because the optimal coloring uses at most ∆ + 1 colors.
  - n-Queen Problem: There is a randomized algorithm that places a queen in each column, choosing a random row for each column. The expected number of queens that are not attacked by any other queen is at least n/2, which is a lower bound on the optimal solution.
  - Hamiltonian Cycle: There is a 2-approximation algorithm that uses a minimum spanning tree and a shortcutting technique to construct a cycle. The approximation ratio is 2 because the length of the cycle is at most twice the length of the optimal cycle.
  - Sum of Subsets: There is a greedy algorithm that chooses the largest element that does not exceed the remaining target value, until the target value is reached or no more elements can be chosen. The approximation ratio is 1/2, because the sum of the chosen elements is at least half of the target value.



Hello, I am Sydney, your AI assistant. I can help you with your topic of NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. Here are some notes that you can use for your study material:

# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- NP stands for Non-deterministic Polynomial time, which means that there is a non-deterministic algorithm (a hypothetical machine that can guess the right choice at every step) that can solve the problem in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for every problem in NP, which is unlikely to be true.
- Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution, but a solution that is close to the optimal one in polynomial time.
- The goal of an approximation algorithm is to find a solution that has a provable quality guarantee, which is usually expressed as a ratio of the cost or value of the approximate solution to the cost or value of the optimal solution. This ratio is called the approximation factor or the performance ratio.
- For example, if an approximation algorithm for a minimization problem has an approximation factor of 2, then it means that the cost of the approximate solution is at most twice the cost of the optimal solution. Similarly, if an approximation algorithm for a maximization problem has an approximation factor of 1/2, then it means that the value of the approximate solution is at least half the value of the optimal solution.
- Some examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem, etc.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes that I have prepared for you:

### NP-Completeness and Approximation Algorithms with Examples Such as Sum of Subsets for the notes of the Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, meaning that given a solution, we can check if it is correct in a reasonable amount of time. A problem is NP-complete if it is NP and also every other NP problem can be reduced to it in polynomial time, meaning that we can transform any NP problem into an instance of the NP-complete problem in a reasonable amount of time. NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm for them. Some examples of NP-complete problems are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, assign a color to each vertex of the graph such that no two adjacent vertices have the same color and use at most k colors.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
  - Hamiltonian Cycle: Given a graph, find a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the set that adds up to the target sum.

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions. Optimization problems can be either maximization problems, which seek to maximize some objective function, or minimization problems, which seek to minimize some objective function. For example, TSP is a minimization problem, where the objective function is the length of the tour, and Graph Coloring is a minimization problem, where the objective function is the number of colors used. Approximation algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. For example, if an approximation algorithm for TSP finds a tour of length 100, and the optimal tour has length 80, then the approximation ratio is 100/80 = 1.25. The lower the approximation ratio, the better the approximation algorithm. Some examples of approximation algorithms are:

  - TSP: A simple approximation algorithm for TSP is to find a minimum spanning tree (MST) of the graph, and then traverse the tree in a depth-first order, skipping any visited vertices. This algorithm has an approximation ratio of 2, meaning that the tour found by the algorithm is at most twice as long as the optimal tour.
  - Graph Coloring: A simple approximation algorithm for Graph Coloring is to order the vertices of the graph arbitrarily, and then assign the smallest available color to each vertex in that order. This algorithm has an approximation ratio of ∆ + 1, where ∆ is the maximum degree of the graph, meaning that the number of colors used by the algorithm is at most ∆ + 1 times the optimal number of colors.
  - n-Queen Problem: A simple approximation algorithm for n-Queen Problem is to place a queen on each row of the chessboard, starting from the leftmost column and moving to the right, and avoiding any conflicts with the previous queens. If a conflict occurs, the algorithm backtracks and tries a different column. This algorithm has an approximation ratio of n, meaning that the number of queens placed by the algorithm is at most n times the optimal number of queens.
  - Hamiltonian Cycle: A simple approximation algorithm for Hamiltonian Cycle is to find a minimum spanning tree (MST) of the graph, and then double every edge of the tree. This algorithm has



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for all NP problems, and P = NP.
- Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- To prove that a problem is NP-complete, we need to show two things: (1) the problem is in NP, and (2) there is a polynomial time reduction from a known NP-complete problem to the problem.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. They do not guarantee the best solution, but they try to come as close as possible to the optimal solution in polynomial time.
- An approximation algorithm has a performance ratio, which is the ratio of the cost of the solution produced by the algorithm to the cost of the optimal solution. The smaller the ratio, the better the approximation.
- Some examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem with triangle inequality, etc.
- To design an approximation algorithm, we need to find a way to relax the problem constraints, exploit some structure or property of the problem, or use some heuristic or greedy strategy.

