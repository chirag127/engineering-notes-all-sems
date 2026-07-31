

## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An **algorithm** is a finite sequence of well-defined instructions for solving a problem or performing a task.
- **Analyzing algorithms** is the process of determining the amount of resources (such as time and space) that an algorithm requires to execute.
- The **complexity of algorithms** is a measure of how the resource requirements of an algorithm vary with the size of the input.
- The **growth of functions** is a way of comparing the asymptotic behavior of different functions, such as the running time of algorithms, as the input size grows.
- **Performance measurements** are empirical methods of evaluating the efficiency and effectiveness of algorithms, such as running experiments, benchmarking, and profiling.
- **Sorting** is the process of arranging a collection of items in a certain order, such as ascending or descending. **Order statistics** are the values of the items at specific positions in a sorted collection, such as the minimum, maximum, median, or kth smallest or largest element.
- **Shell sort** is a sorting algorithm that repeatedly applies insertion sort to subarrays of the input, with decreasing gaps between the elements of each subarray, until the entire array is sorted.
- **Quick sort** is a sorting algorithm that partitions the input array into two subarrays based on a pivot element, such that all elements in the left subarray are less than or equal to the pivot and all elements in the right subarray are greater than or equal to the pivot, and then recursively sorts the subarrays.
- **Merge sort** is a sorting algorithm that divides the input array into two halves, recursively sorts each half, and then merges the two sorted halves into one sorted array.
- **Heap sort** is a sorting algorithm that builds a binary heap from the input array, and then repeatedly extracts the maximum element from the heap and places it at the end of the output array, until the heap is empty.
- **Comparison of sorting algorithms** is the evaluation of the advantages and disadvantages of different sorting algorithms, based on criteria such as time complexity, space complexity, stability, adaptability, and simplicity.
- **Sorting in linear time** is the design and analysis of sorting algorithms that have a worst-case running time of O(n), where n is the size of the input, such as counting sort, radix sort, and bucket sort. These algorithms are usually based on assumptions about the input, such as the range of values, the number of digits, or the distribution of keys.



# Algorithms for the notes of the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

## Introduction

- An algorithm is a finite sequence of well-defined instructions for solving a problem or performing a task.
- Analyzing algorithms is the process of determining the amount of resources (such as time and space) that an algorithm consumes when executed on a given input.
- Complexity of algorithms is the measure of how the resource consumption of an algorithm grows as the input size increases.
- Growth of functions is the mathematical notation for describing how fast a function increases or decreases as its argument changes.
- Performance measurements are the empirical methods for evaluating the efficiency and correctness of algorithms on real or simulated data.
- Sorting and order statistics are two fundamental problems in computer science that involve arranging a sequence of items in a certain order or finding the item with a given rank in the sequence.

## Sorting and Order Statistics

- Sorting is the computational process of rearranging a given sequence of items from some total order into ascending or descending order.
- Order statistics is the problem of finding the ith smallest (or largest) item in a sequence, where i is a given rank.
- Sorting and order statistics are closely related, as sorting can be used to solve order statistics, and some order statistics algorithms can be used to sort partially or completely.
- Sorting and order statistics have many applications in data processing, searching, selection, ranking, median finding, and more.

## Shell Sort

- Shell sort is a sorting algorithm that is based on the idea of insertion sort, but improves its performance by reducing the number of comparisons and swaps.
- Shell sort works by dividing the sequence into several sub-sequences, each of which is sorted by insertion sort. The sub-sequences are formed by choosing a gap size, which determines how far apart the elements in each sub-sequence are. The gap size is gradually reduced until it becomes one, at which point the whole sequence is sorted.
- Shell sort has an average time complexity of O(n^1.5), where n is the number of items in the sequence. The best and worst case time complexities depend on the choice of the gap size sequence.
- Shell sort is an in-place and unstable sorting algorithm, meaning that it does not require extra space and does not preserve the relative order of equal items.

## Quick Sort

- Quick sort is a sorting algorithm that is based on the idea of divide and conquer, which means breaking down a large problem into smaller and easier sub-problems, solving them recursively, and combining their solutions.
- Quick sort works by choosing a pivot element from the sequence, and partitioning the sequence into two sub-sequences, one with elements smaller than or equal to the pivot, and one with elements larger than the pivot. The pivot is then placed in its correct position, and the sub-sequences are sorted recursively by the same method.
- Quick sort has an average time complexity of O(n log n), where n is the number of items in the sequence. The best case occurs when the pivot is always the median of the sequence, and the worst case occurs when the pivot is always the smallest or largest element of the sequence, resulting in a time complexity of O(n^2).
- Quick sort is an in-place and unstable sorting algorithm, meaning that it does not require extra space and does not preserve the relative order of equal items.

## Merge Sort

- Merge sort is a sorting algorithm that is also based on the idea of divide and conquer, but uses a different approach than quick sort.
- Merge sort works by dividing the sequence into two equal or nearly equal sub-sequences, sorting them recursively by the same method, and merging them into a sorted sequence. The merging process involves comparing the first elements of the two sub-sequences, and moving the smaller one to the output sequence, until one of the sub-sequences is empty, and then appending the remaining elements of the other sub-sequence to the output sequence.
- Merge sort has a time complexity of O(n log n), where n is the number of items in the sequence, in all cases. This is because the dividing and merging steps take O(n) time each, and the recursion depth is O(log n).
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal items, but it is not in-place, meaning that it requires extra space proportional to the size of the sequence.

## Heap Sort

- Heap sort is a sorting algorithm that is based on the data structure of



# Analyzing Algorithms

- Analyzing algorithms is the process of finding the **computational complexity** of algorithms, which is the amount of **time, storage, or other resources** needed to execute them .
- Analyzing algorithms helps to **predict** the behavior and efficiency of an algorithm without implementing it on a specific computer, and to **compare** different algorithms for the same problem.
- The most common measures of computational complexity are **time complexity** and **space complexity**, which relate the length of an algorithm's input to the number of steps it takes or the number of storage locations it uses, respectively .
- Time complexity and space complexity are usually expressed using **asymptotic notation**, such as **big O**, **big Ω**, and **big Θ**, which describe the **growth rate** of a function as the input size approaches infinity .
- The growth rate of a function depends on the **dominant term** of the function, which is the term with the highest power or exponent. For example, the dominant term of f(n) = 3n^2 + 5n + 2 is 3n^2, so f(n) is O(n^2).
- The growth rate of a function also depends on the **leading coefficient** of the dominant term, which is the constant factor that multiplies the term. For example, the leading coefficient of 3n^2 is 3. However, asymptotic notation ignores the leading coefficient, because it does not affect the order of magnitude of the function.
- Some common classes of time complexity are **constant** (O(1)), **logarithmic** (O(log n)), **linear** (O(n)), **linearithmic** (O(n log n)), **quadratic** (O(n^2)), **cubic** (O(n^3)), and **exponential** (O(2^n)). The lower the class, the faster the algorithm.
- Some common classes of space complexity are **constant** (O(1)), **linear** (O(n)), and **quadratic** (O(n^2)). The lower the class, the less memory the algorithm uses.
- To analyze the time complexity of an algorithm, we need to count the number of **basic operations** or **elementary steps** that the algorithm performs, such as arithmetic operations, comparisons, assignments, etc. The number of basic operations depends on the **input size** and the **structure** of the algorithm.
- To analyze the space complexity of an algorithm, we need to count the amount of **memory** or **storage** that the algorithm allocates, such as variables, arrays, stacks, queues, etc. The amount of memory depends on the **input size** and the **data structures** used by the algorithm.
- The time and space complexity of an algorithm can vary depending on the **input values** or the **input distribution**. Therefore, we usually consider three cases: the **best case**, the **worst case**, and the **average case**.
- The best case is the scenario where the algorithm performs the **minimum** number of basic operations or uses the **minimum** amount of memory for a given input size. The worst case is the scenario where the algorithm performs the **maximum** number of basic operations or uses the **maximum** amount of memory for a given input size. The average case is the scenario where the algorithm performs the **expected** number of basic operations or uses the **expected** amount of memory for a given input size.
- The best case, worst case, and average case can be different for different algorithms or different problems. For example, the best case time complexity of **linear search** is O(1), when the target element is the first element in the array. The worst case time complexity of linear search is O(n), when the target element is the last element in the array or not in the array at all. The average case time complexity of linear search is O(n/2), when the target element is equally likely to be in any position in the array.
- The best case, worst case, and average case can also be the same for some algorithms or some problems. For example, the best case, worst case, and average case time complexity of **binary search** are all O(log n), because the algorithm always divides the array



# Complexity of Algorithms

- An algorithm is a finite sequence of well-defined instructions that can be executed to solve a problem or perform a task.
- The complexity of an algorithm is the amount of resources required to run it, such as time and space.
- The complexity of an algorithm depends on the size of the input, denoted by n, and the number of elementary operations performed by the algorithm.
- The complexity of an algorithm can be expressed using asymptotic notation, such as Big O, Big Theta, and Big Omega, which describe the upper bound, tight bound, and lower bound of the algorithm's performance, respectively.
- The complexity of an algorithm can be classified into different types, such as constant, logarithmic, linear, polynomial, exponential, and factorial, based on the growth rate of the function that represents the algorithm's performance.
- The complexity of an algorithm can be analyzed using different methods, such as recurrence relations, master theorem, and amortized analysis, which help to derive the asymptotic bounds of the algorithm's performance.
- The complexity of an algorithm can be used to compare the efficiency and scalability of different algorithms that solve the same problem, and to choose the best algorithm for a given situation.
- Sorting and order statistics are two important problems in computer science that involve arranging a set of elements in a certain order or finding the kth smallest or largest element in a set.
- Shell sort, quick sort, merge sort, heap sort, and linear time sorting are some of the common algorithms that can be used to sort a set of elements, each with different complexity and performance characteristics.
- Shell sort is an algorithm that sorts a set of elements by using a sequence of gap values to divide the set into sublists, and then applying insertion sort on each sublist. The complexity of shell sort depends on the choice of the gap sequence, and can range from O(n^2) to O(n log^2 n) in the worst case.
- Quick sort is an algorithm that sorts a set of elements by using a pivot element to partition the set into two sublists, such that all the elements in the left sublist are smaller than the pivot and all the elements in the right sublist are larger than the pivot, and then recursively applying the same procedure on the sublists. The complexity of quick sort is O(n log n) in the average case and O(n^2) in the worst case.
- Merge sort is an algorithm that sorts a set of elements by recursively dividing the set into two sublists, sorting each sublist using merge sort, and then merging the two sorted sublists into one sorted list. The complexity of merge sort is O(n log n) in the best, average, and worst case.
- Heap sort is an algorithm that sorts a set of elements by using a data structure called a heap, which is a binary tree that satisfies the heap property, such that the value of each node is greater than or equal to the value of its children. The algorithm builds a max-heap from the set of elements, and then repeatedly swaps the root element with the last element in the heap, and reduces the size of the heap by one, until the heap is empty. The complexity of heap sort is O(n log n) in the best, average, and worst case.
- Linear time sorting is a class of algorithms that can sort a set of elements in O(n) time, where n is the size of the set. These algorithms are based on the assumption that the elements belong to a finite set of discrete values, such as integers, and use techniques such as counting sort, radix sort, and bucket sort to sort the elements.
- The comparison of sorting algorithms can be done based on various factors, such as the complexity, the stability, the adaptability, the in-place property, the parallelizability, and the practical performance of the algorithms.



# Growth of Functions

- Growth of functions is a way of measuring the efficiency and performance of algorithms based on their input size and execution time.
- Growth of functions helps us to compare different algorithms and choose the most suitable one for a given problem.
- Growth of functions is expressed using asymptotic notation, which simplifies the function by ignoring the constants and lower order terms that are less significant for large inputs.
- Asymptotic notation includes three types: big-O, big-Ω, and big-Θ, which represent the upper bound, lower bound, and tight bound of the function respectively.
- The rate of growth of a function indicates how fast or slow the function increases or decreases as the input size grows.
- The rate of growth of a function can be classified into different categories, such as constant, linear, logarithmic, polynomial, exponential, etc.
- The rate of growth of a function affects the efficiency and complexity of an algorithm. Generally, a lower rate of growth means a faster and more efficient algorithm, while a higher rate of growth means a slower and less efficient algorithm.
- For example, a linear search algorithm has a growth of function of Θ(n), which means it takes linear time to search for an element in an array of size n. A binary search algorithm has a growth of function of Θ(log n), which means it takes logarithmic time to search for an element in a sorted array of size n. Therefore, binary search is more efficient than linear search for large inputs.



# Performance Measurements

Performance measurements are used to evaluate the efficiency and effectiveness of an algorithm in solving a problem. They help to compare different algorithms and choose the best one for a given situation. Performance measurements can be based on various factors, such as:

- **Space complexity**: The amount of memory or space required by an algorithm to perform its task. It consists of both program and data space. Space complexity can be measured in terms of the input size, the output size, or the total size of the algorithm.
- **Time complexity**: The amount of time or number of steps required by an algorithm to perform its task. It depends on the speed of the processor, the size and nature of the input, and the design of the algorithm. Time complexity can be measured in terms of the best case, the worst case, or the average case scenario.
- **Network complexity**: The amount of communication or data transfer required by an algorithm to perform its task. It depends on the network topology, the bandwidth, the latency, and the protocol. Network complexity can be measured in terms of the number of messages, the size of messages, or the total amount of data exchanged.
- **Other factors**: Depending on the problem domain, there may be other factors that affect the performance of an algorithm, such as accuracy, reliability, security, scalability, etc. These factors can be measured in terms of the error rate, the failure rate, the encryption level, the number of users, etc.

One of the common ways to measure the performance of an algorithm is to use the **Big O notation**, which expresses the asymptotic behavior of the algorithm as the input size grows. The Big O notation gives an upper bound on the growth rate of the algorithm's complexity, ignoring the constant factors and the lower order terms. For example, an algorithm with a time complexity of O(n^2) means that the algorithm's running time is proportional to the square of the input size, and it will grow faster than an algorithm with a time complexity of O(n) or O(log n).

Performance measurements are important for designing and analyzing algorithms, as they help to understand the trade-offs and limitations of different approaches, and to optimize the algorithm's performance for a given problem.



# Sorting and Order Statistics - Shell Sort

- Shell sort is a sorting algorithm that is based on the idea of insertion sort, but improves its efficiency by reducing the number of comparisons and swaps.
- Shell sort works by dividing the input array into several subarrays, each of which is sorted by insertion sort. The subarrays are created by using a gap sequence, which determines how far apart the elements in each subarray are.
- The gap sequence can be chosen in different ways, but a common one is to start with a large gap and reduce it by half in each iteration, until the gap is one. For example, if the input array has 16 elements, the gap sequence can be 8, 4, 2, 1.
- In each iteration, shell sort performs insertion sort on each subarray, starting from the first element with the given gap and moving forward. For example, if the gap is 4, shell sort will sort the elements at indices 0, 4, 8, 12, then the elements at indices 1, 5, 9, 13, and so on.
- As the gap decreases, the subarrays become larger and more sorted, until the final iteration, when the gap is one and the whole array is sorted by insertion sort.
- Shell sort has a better performance than insertion sort, because it moves elements closer to their final positions in fewer steps, reducing the number of comparisons and swaps. However, the exact running time of shell sort depends on the choice of the gap sequence, and it is not easy to analyze theoretically.
- The best known upper bound for the worst-case running time of shell sort is O(n^(3/2)), where n is the number of elements in the input array. However, some gap sequences can achieve a better performance, such as O(n^(4/3)) or O(n*log^2(n)).
- Shell sort is an in-place and unstable sorting algorithm, meaning that it does not require extra space and it does not preserve the relative order of equal elements.



# Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle and last elements of the array.
- The partitioning step rearranges the array such that all the elements that are **less than or equal to** the pivot are in the **left subarray**, and all the elements that are **greater than** the pivot are in the **right subarray**.
- The pivot element is then placed in its **correct position** in the sorted array, and the subarrays are sorted recursively by the same procedure.
- The algorithm terminates when the subarray size is one or zero, which means it is already sorted.
- Quick sort is an **in-place** algorithm, meaning it does not require additional memory to store the subarrays, but it modifies the original array.
- Quick sort is also an **unstable** algorithm, meaning it does not preserve the relative order of equal elements in the array.
- The **best-case** scenario for quick sort is when the pivot element always divides the array into two equal or nearly equal subarrays, resulting in a balanced recursion tree. In this case, the running time is **O(n log n)**, where n is the number of elements in the array.
- The **worst-case** scenario for quick sort is when the pivot element is always the smallest or the largest element in the array, resulting in an unbalanced recursion tree. In this case, the running time is **O(n^2)**, which is as bad as the insertion sort or the selection sort algorithms.
- The **average-case** scenario for quick sort is when the pivot element is chosen randomly or by a good heuristic, resulting in a moderately balanced recursion tree. In this case, the running time is also **O(n log n)**, which is asymptotically optimal for comparison-based sorting algorithms.
- Quick sort is a **practical** and **efficient** algorithm for sorting large arrays, as it has a low constant factor in its running time and it can exploit the cache memory of modern processors. However, it is not suitable for sorting small arrays, as the overhead of recursion and partitioning may outweigh the benefits of divide-and-conquer. It is also not suitable for sorting arrays that are already sorted or nearly sorted, as it may degenerate to the worst-case scenario. In these cases, other algorithms such as insertion sort or merge sort may perform better.



# Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The main idea of merge sort is to divide the problem of sorting an array of n elements into two subproblems of sorting two subarrays of n/2 elements each, and then combine the solutions of the subproblems by merging the two sorted subarrays.
- The algorithm can be described as follows:

  - **Base case:** If the array has zero or one element, it is already sorted and no further action is needed.
  - **Recursive case:** If the array has more than one element, do the following steps:
    - Divide the array into two subarrays of equal or nearly equal size.
    - Recursively sort the left subarray using merge sort.
    - Recursively sort the right subarray using merge sort.
    - Merge the two sorted subarrays into a single sorted array.

- The merge operation takes two sorted subarrays and combines them into a single sorted array. It can be implemented as follows:

  - Initialize three pointers: i to point to the first element of the left subarray, j to point to the first element of the right subarray, and k to point to the first element of the output array.
  - While i and j are both less than the size of their respective subarrays, do the following steps:
    - Compare the elements at A[i] and A[j], where A is the input array.
    - If A[i] <= A[j], copy A[i] to the output array at index k, and increment i and k by one.
    - If A[i] > A[j], copy A[j] to the output array at index k, and increment j and k by one.
  - If i reaches the end of the left subarray, copy the remaining elements of the right subarray to the output array.
  - If j reaches the end of the right subarray, copy the remaining elements of the left subarray to the output array.

- The pseudocode for merge sort is as follows:

  ```
  MERGE-SORT(A, p, r)
  // A is the input array, p is the starting index, r is the ending index
  // The subarray A[p..r] is sorted in place
  if p < r
    q = floor((p + r) / 2) // find the middle point
    MERGE-SORT(A, p, q) // sort the left subarray
    MERGE-SORT(A, q + 1, r) // sort the right subarray
    MERGE(A, p, q, r) // merge the two sorted subarrays

  MERGE(A, p, q, r)
  // A is the input array, p is the starting index of the left subarray, q is the ending index of the left subarray, r is the ending index of the right subarray
  // The subarrays A[p..q] and A[q + 1..r] are merged into a single sorted array A[p..r]
  n1 = q - p + 1 // the size of the left subarray
  n2 = r - q // the size of the right subarray
  create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
  for i = 1 to n1
    L[i] = A[p + i - 1] // copy the left subarray to L
  for j = 1 to n2
    R[j] = A[q + j] // copy the right subarray to R
  L[n1 + 1] = infinity // a sentinel value to mark the end of the left subarray
  R[n2 + 1] = infinity // a sentinel value to mark the end of the right subarray
  i = 1 // the pointer for the left subarray
  j = 1 // the pointer for the right subarray
  for k = p to r
    if L[i] <= R[j]
      A[k] = L[i] // copy the smaller element to the output array
      i = i + 1 // increment the pointer for the left subarray
    else
      A[k] = R[j] // copy the smaller element to the output array
      j = j + 1 // increment the pointer for the right subarray
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the



# Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: building the heap and extracting the elements from the heap.
- Building the heap: the algorithm rearranges the elements of the array into a max-heap or a min-heap, depending on the desired sorting order. This can be done in linear time using a bottom-up approach that starts from the last non-leaf node and moves up to the root, applying a procedure called heapify to each node. Heapify ensures that the subtree rooted at a given node satisfies the heap property by swapping the node with its largest or smallest child if necessary, and recursively heapifying the affected subtree.
- Extracting the elements from the heap: the algorithm repeatedly removes the root element of the heap, which is the largest or smallest element in the array, and places it at the end of the sorted output. Then, it restores the heap property by heapifying the reduced heap. This process is repeated until the heap is empty and the array is sorted.
- Heap sort has a worst-case time complexity of O(n log n), where n is the number of elements in the array. This is because building the heap takes O(n) time and extracting each element takes O(log n) time. Heap sort is also an in-place algorithm, meaning that it does not require additional space to sort the array, except for a constant number of variables.
- Heap sort is not a stable algorithm, meaning that it does not preserve the relative order of equal elements in the array. For example, if the array contains two elements with the same value but different attributes, heap sort may swap them and change their original order.
- Heap sort is suitable for sorting large data sets that do not fit in memory, as it can be implemented using external memory such as disks or tapes. Heap sort can also be used to implement a priority queue, a data structure that supports efficient insertion and extraction of the highest or lowest priority element.



# Comparison of Sorting Algorithms

Sorting algorithms are methods of arranging a list of elements in a certain order, such as ascending or descending. There are many different sorting algorithms, each with different advantages and disadvantages. Some of the factors that can be used to compare sorting algorithms are:

- Time complexity: how the running time of the algorithm grows as the input size increases.
- Space complexity: how much extra memory the algorithm requires to sort the list.
- Stability: whether the algorithm preserves the relative order of elements with equal keys.
- Comparison-based: whether the algorithm only compares elements with a comparison operator, or uses other information such as the range or distribution of the keys.

Some of the most commonly used sorting algorithms are:

- Shell sort: an improvement of insertion sort that uses gaps between elements to reduce the number of comparisons and shifts.
- Quick sort: a divide-and-conquer algorithm that partitions the list around a pivot element and recursively sorts the sublists.
- Merge sort: another divide-and-conquer algorithm that splits the list into two halves, recursively sorts them, and merges them together.
- Heap sort: a selection sort that uses a binary heap data structure to find the largest or smallest element in the list and move it to the end or the beginning.
- Counting sort: a non-comparison-based algorithm that counts the number of occurrences of each key in the list and uses them to determine the final position of each element.

The following table summarizes the time and space complexity of these algorithms, as well as their stability and comparison-based property. The time complexity is given in terms of the best, average, and worst case scenarios, using the big O notation.

| Algorithm | Time complexity (best) | Time complexity (average) | Time complexity (worst) | Space complexity | Stable | Comparison-based |
|-----------|------------------------|---------------------------|-------------------------|------------------|--------|------------------|
| Shell sort | O(n) | O(n log n) | O(n^2) | O(1) | No | Yes |
| Quick sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | No | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Yes |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes | No |

Here, n is the number of elements in the list, and k is the range of the keys.

Some of the advantages and disadvantages of these algorithms are:

- Shell sort: it is easy to implement and has a low space complexity, but it is not stable and has a high worst case time complexity.
- Quick sort: it is fast and has a low space complexity, but it is not stable and has a high worst case time complexity, which depends on the choice of the pivot element.
- Merge sort: it is stable and has a low worst case time complexity, but it has a high space complexity and requires extra memory for merging.
- Heap sort: it has a low worst case time complexity and a low space complexity, but it is not stable and it is not adaptive, meaning that it does not take advantage of the existing order in the list.
- Counting sort: it is stable and has a low time complexity, but it has a high space complexity and it is not comparison-based, meaning that it only works for integer keys within a known range.



# Sorting in Linear Time

- Sorting in linear time means arranging a sequence of elements in a specific order in O(n) time, where n is the number of elements.
- Sorting in linear time is possible only when some special assumptions are made about the input sequence, such as the range of values, the distribution of elements, or the representation of data.
- Some examples of sorting algorithms that run in linear time are counting sort, radix sort, and bucket sort.

## Counting Sort

- Counting sort assumes that the input consists of integers in a small range, such as [0, k] for some integer k.
- Counting sort works by counting the number of occurrences of each value in the input sequence and then using those counts to determine the positions of the elements in the sorted output.
- Counting sort has a time complexity of O(n + k), where n is the number of elements and k is the range of values. It also requires O(n + k) space to store the counts and the output.

## Radix Sort

- Radix sort assumes that the input consists of integers or strings that have a fixed length and can be represented in some base b, such as binary, decimal, or hexadecimal.
- Radix sort works by sorting the elements according to their digits, starting from the least significant digit to the most significant digit. For each digit, a stable sorting algorithm, such as counting sort, is used to sort the elements.
- Radix sort has a time complexity of O(d(n + b)), where d is the number of digits, n is the number of elements, and b is the base. It also requires O(n + b) space to store the intermediate and final results.

## Bucket Sort

- Bucket sort assumes that the input is generated by a random process that distributes the elements uniformly over the interval [0, 1).
- Bucket sort works by dividing the interval into n equal-sized buckets and then distributing the elements into the buckets based on their values. For each bucket, a sorting algorithm, such as insertion sort, is used to sort the elements within the bucket. Then, the elements are concatenated in the order of the buckets to form the sorted output.
- Bucket sort has an average time complexity of O(n), where n is the number of elements, but it can be as bad as O(n^2) in the worst case. It also requires O(n) space to store the buckets and the output.



# Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

- Advanced data structures are data structures that provide more efficient ways to store, manipulate, and access data, especially for applications that require complex operations or large amounts of data.
- Some of the advanced data structures that we will study in this unit are:

  - Red-black trees: A type of self-balancing binary search tree that maintains the height of the tree as O(log n) by enforcing some properties on the color and structure of the nodes. Red-black trees are useful for implementing associative arrays, such as dictionaries or maps, that support fast insertion, deletion, and search operations.
  - B-trees: A type of multi-way search tree that can have more than two children per node and store multiple keys per node. B-trees are designed to minimize the number of disk accesses by keeping the tree as balanced and shallow as possible. B-trees are widely used for implementing database indexes, file systems, and other applications that require efficient storage and retrieval of large amounts of data.
  - Binomial heaps: A type of heap data structure that consists of a collection of binomial trees, which are rooted trees that follow a specific shape and size property. Binomial heaps support fast merge operations, which can be useful for implementing priority queues or disjoint-set data structures.
  - Fibonacci heaps: A type of heap data structure that is a variation of binomial heaps, with some modifications that allow faster decrease-key and delete operations. Fibonacci heaps are useful for implementing algorithms that rely on efficient priority queues, such as Dijkstra's algorithm or Prim's algorithm for finding shortest paths or minimum spanning trees.
  - Tries: A type of tree data structure that stores strings or sequences of symbols in a compact and efficient way. Each node in a trie represents a prefix of some strings, and the children of a node are the possible extensions of that prefix. Tries are useful for implementing applications that require fast prefix searching, such as spell checkers, auto-complete, or text compression.
  - Skip lists: A type of probabilistic data structure that consists of a series of linked lists, each of which is a subset of the previous one, with some elements skipped. Skip lists allow fast search, insertion, and deletion operations in expected O(log n) time by using randomization to create shortcuts in the lists. Skip lists are an alternative to balanced trees for implementing ordered sets or maps.



# Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and have a **guaranteed time complexity of O(log n)** for basic operations like insertion, deletion, and search .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**. This can be stored as a single bit in memory (e.g. 'red' = 1, 'black' = 0).
  - The **root** of the tree is always **black**.
  - Every **leaf** (null pointer) is considered **black**.
  - If a node is **red**, then both its **children** are **black**.
  - Every **simple path** from a node to a descendant leaf contains the **same number** of **black nodes**. This number is called the **black height** of the node.
- Red-black trees maintain these properties by performing **rotations** and **recoloring** operations after insertion or deletion of nodes. These operations ensure that the tree remains **approximately balanced** and that the **height** of the tree is **logarithmic** in the number of nodes .
- Red-black trees are used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - **C++ STL** (Standard Template Library) uses red-black trees to implement **map**, **multimap**, **set**, and **multiset** containers.
  - **Java Collections Framework** uses red-black trees to implement **TreeMap**, **TreeSet**, and **ConcurrentSkipListMap** classes.
  - **Linux kernel** uses red-black trees to manage **virtual memory areas**, **epoll** (event polling) system call, and **timer** data structures.
  - **Git** (version control system) uses red-black trees to store **directory contents** and **file names**.
  - **MongoDB** (database system) uses red-black trees to implement **indexes** on collections and documents.



# B-Trees

- A B-tree is a **self-balancing** tree data structure that maintains **sorted** data and allows **searches, sequential access, insertions, and deletions** in logarithmic time   .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children  .
- A B-tree of order m has the following properties  :
  - Each node can have up to m children and m-1 keys.
  - Each node must have at least ⌈m/2⌉ children (except the root).
  - The root must have at least 2 children (unless it is a leaf).
  - All the leaves must be at the same level.
  - The keys in each node must be in ascending order and act as separators for the subtrees.
- The height of a B-tree of order m with n keys is O(logm n) .
- The search operation in a B-tree is similar to the binary search tree, but instead of comparing the key with one value, it compares with m-1 values in each node .
- The insertion operation in a B-tree involves finding the appropriate leaf node to insert the key and splitting the node if it is full .
- The deletion operation in a B-tree involves finding the key to delete and replacing it with its predecessor or successor if it is in an internal node, and merging or borrowing nodes if they become underfull .
- B-trees are widely used in **database systems** and **file systems** to store and retrieve large amounts of data efficiently  .



# Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- The binomial heap operations are as follows:
  - Create: create an empty binomial heap.
  - Insert: insert a new node into the binomial heap by creating a binomial tree of order 0 and merging it with the existing heap.
  - Get Minimum: find the root node with the minimum key in the binomial heap by scanning the roots of all binomial trees.
  - Extract Minimum: remove the root node with the minimum key from the binomial heap by deleting it and merging its children with the existing heap.
  - Union: merge two binomial heaps into one by combining the binomial trees of the same order and adjusting the heap property.
  - Decrease Key: decrease the key of a given node in the binomial heap by swapping it with its parent until the heap property is restored.
  - Delete: delete a given node from the binomial heap by decreasing its key to negative infinity and extracting the minimum.



# Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- Fibonacci heaps are used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- The key advantage of a Fibonacci heap over other heap data structures is its fast amortized running time for operations such as insert, find-minimum, and decrease-key.
- The insert and find-minimum operations work in constant (O(1)) amortized time. The decrease-key operation also works in constant amortized time.
- The delete and delete-minimum operations work in O(log n) amortized time, where n is the number of nodes in the heap.
- The merge operation, which combines two Fibonacci heaps into one, works in constant (O(1)) actual time.
- The structure of a Fibonacci heap is more flexible than a binary heap or a binomial heap, as it allows arbitrary degrees of nodes and does not enforce a strict shape of the trees.
- A Fibonacci heap maintains a pointer to the minimum node and a list of roots of the trees. Each node stores its key, degree, parent, child, left sibling, and right sibling pointers.
- A Fibonacci heap also maintains a potential function, which is a measure of how unbalanced the heap is. The potential function is used to analyze the amortized running time of the operations.
- A Fibonacci heap uses two techniques to improve the efficiency of its operations: lazy insertion and cascading cuts. Lazy insertion means that new nodes are simply added to the root list without any restructuring. Cascading cuts means that when a node loses a child due to a decrease-key operation, it may also be cut from its parent and added to the root list, and this process may continue recursively.
- A Fibonacci heap performs a consolidation operation when a delete or delete-minimum operation is performed. Consolidation reduces the number of trees in the heap by merging trees of equal degree until there is at most one tree of each degree.
- A Fibonacci heap can be represented by a circular, doubly linked list of roots, and each root can be the head of a circular, doubly linked list of children. The following diagram shows an example of a Fibonacci heap with 15 nodes and 5 trees:

Fibonacci heap example

: Fibonacci heap - Wikipedia
: Fibonacci Heap | Brilliant Math & Science Wiki
: Fibonacci Heap | Set 1 (Introduction) - GeeksforGeeks



# Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**trie**val, which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has at most k children, and each child corresponds to a character in the alphabet.
- A trie can store any strings over an alphabet, but it is especially useful for storing words that share common prefixes .
- A trie can perform the following operations efficiently  :
  - Insert: To insert a string into a trie, we start from the root node and follow the path corresponding to the characters of the string. If the path does not exist, we create new nodes along the way. When we reach the end of the string, we mark the last node as a terminal node, indicating that it represents a valid string.
  - Search: To search for a string in a trie, we start from the root node and follow the path corresponding to the characters of the string. If the path exists and the last node is a terminal node, we return true, indicating that the string is present in the trie. Otherwise, we return false, indicating that the string is not present in the trie.
  - Delete: To delete a string from a trie, we first search for the string in the trie. If the string is not present, we do nothing. If the string is present, we unmark the last node as a terminal node, indicating that it no longer represents a valid string. Then, we delete any nodes that have no children and are not terminal nodes, starting from the last node and moving upwards, until we reach a node that has either children or is a terminal node.
- A trie has the following advantages over a hash table :
  - A trie can handle collisions better than a hash table, as it does not use hashing to store the strings, and hence does not depend on the quality of the hash function.
  - A trie can support prefix-based queries, such as finding all the strings that start with a given prefix, or finding the longest common prefix of a set of strings, which are not possible with a hash table.
  - A trie can support ordered traversal of the strings, as it stores the strings in a lexicographical order, which is not possible with a hash table.
- A trie has the following disadvantages over a hash table :
  - A trie can consume more space than a hash table, as it creates a node for each character in the string, and may have many empty nodes that do not store any valid strings.
  - A trie can have a higher insertion and deletion cost than a hash table, as it may require creating or deleting multiple nodes for each operation, whereas a hash table can perform these operations in constant time.
- A trie can be implemented using an array or a map to store the children of each node  .
  - An array implementation can be faster and more space-efficient, as it can access the children of a node in constant time, and can use a fixed-size array for each node. However, it can also waste space if the alphabet size is large and the node has few children.
  - A map implementation can be more flexible and adaptable, as it can store only the existing children of a node, and can use any data structure for the map, such as a hash table or a tree. However, it can also be slower and less space-efficient, as it can take more time to access the children of a node, and can use more space for the map and its entries.



# Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis .

## Basic Idea

- A skip list is composed of several layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The lowest layer contains all the elements of the sorted list, and is called the base list.
- The higher layers contain a subset of the elements of the lower layers, and are called the skip lists.
- Each element in a skip list has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- The highest layer contains only one element, called the head, which points to the first element of each layer.
- To search for an element in a skip list, we start from the head and follow the pointers in the highest layer until we find an element that is larger than or equal to the target element. Then, we move down to the lower layer and repeat the process until we reach the base list. If we find the target element in the base list, we return it. Otherwise, we return null.
- To insert an element in a skip list, we first search for the position where it should be inserted in the base list. Then, we insert it in the base list and randomly decide whether to promote it to the higher layer. If we promote it, we repeat the process until we reach the highest layer or we decide not to promote it. We also update the pointers of the elements around the inserted element accordingly.
- To delete an element from a skip list, we first search for it in the base list. If we find it, we delete it from the base list and all the higher layers where it appears. We also update the pointers of the elements around the deleted element accordingly.

## Complexity Analysis

- The expected time complexity of search, insertion and deletion in a skip list is O(log n), where n is the number of elements in the base list. This is because the expected number of elements in each layer is half of the number of elements in the lower layer, and the expected number of layers is O(log n).
- The expected space complexity of a skip list is O(n), where n is the number of elements in the base list. This is because the expected number of elements in all the layers is O(n).
- The worst-case time complexity of search, insertion and deletion in a skip list is O(n), where n is the number of elements in the base list. This is because the worst-case number of elements in each layer is n, and the worst-case number of layers is n.
- The worst-case space complexity of a skip list is O(n^2), where n is the number of elements in the base list. This is because the worst-case number of elements in all the layers is O(n^2).

## Advantages and Disadvantages

- Some advantages of skip lists are:
  - They are simpler to implement than balanced trees, such as red-black trees or B-trees.
  - They are faster and use less space than balanced trees in practice.
  - They are easy to parallelize and support concurrent operations.
- Some disadvantages of skip lists are:
  - They are probabilistic and have a high variance in performance.
  - They require random number generation, which may be costly or insecure.
  - They are not widely supported by standard libraries or languages.



## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

- Divide and conquer is a technique of breaking a problem into smaller subproblems, solving them recursively, and combining the solutions to obtain the final answer.
- Some examples of divide and conquer algorithms are:
  - Sorting: Merge sort, quick sort, and heap sort are examples of sorting algorithms that use divide and conquer. They split the input array into smaller subarrays, sort them recursively, and merge or rearrange them to obtain the sorted array.
  - Matrix multiplication: Strassen's algorithm is an example of matrix multiplication that uses divide and conquer. It splits the input matrices into smaller submatrices, performs some multiplications and additions on them recursively, and combines the results to obtain the final product matrix.
  - Convex hull: Graham scan and Jarvis march are examples of convex hull algorithms that use divide and conquer. They split the input set of points into smaller subsets, find the convex hull of each subset recursively, and merge the hulls to obtain the final convex hull.
  - Searching: Binary search and interpolation search are examples of searching algorithms that use divide and conquer. They split the input sorted array into smaller subarrays, compare the target element with the middle or a suitable element of each subarray, and recursively search in the appropriate subarray until the target element is found or the subarray is empty.

- Greedy methods are a technique of making a locally optimal choice at each step, hoping to obtain a globally optimal solution.
- Some examples of greedy algorithms are:
  - Optimal reliability allocation: This is a problem of allocating a given budget to improve the reliability of different components of a system, such that the overall system reliability is maximized. A greedy algorithm for this problem is to sort the components by their cost-effectiveness ratio, which is the ratio of the reliability improvement to the cost, and allocate the budget to the components in decreasing order of this ratio, until the budget is exhausted or all components are improved.
  - Knapsack: This is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized. A greedy algorithm for this problem is to sort the items by their value-to-weight ratio, and pack the items in decreasing order of this ratio, until the knapsack is full or all items are packed.
  - Minimum spanning trees: This is a problem of finding a subset of edges of a weighted undirected graph, such that the subset connects all the vertices, has the minimum total weight, and has no cycles. Two greedy algorithms for this problem are Prim's algorithm and Kruskal's algorithm. Prim's algorithm starts with an arbitrary vertex and adds the edge with the minimum weight that connects a vertex in the current tree to a vertex outside the current tree, until all vertices are included. Kruskal's algorithm starts with an empty set of edges and adds the edge with the minimum weight that does not create a cycle, until all vertices are connected.
  - Single source shortest paths: This is a problem of finding the shortest paths from a given source vertex to all other vertices in a weighted directed graph. Two greedy algorithms for this problem are Dijkstra's algorithm and Bellman-Ford algorithm. Dijkstra's algorithm maintains a set of visited vertices and a set of unvisited vertices, and iteratively updates the shortest distance and the predecessor of each unvisited vertex, based on the minimum distance among the visited vertices, until all vertices are visited. Bellman-Ford algorithm relaxes all the edges of the graph for a number of times equal to the number of vertices minus one, and updates the shortest distance and the predecessor of each vertex, based on the minimum distance among its adjacent vertices, until no more updates are possible.



# Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer has three main steps:
  - Divide: Split the problem into smaller subproblems of the same type.
  - Conquer: Solve the subproblems recursively. If the subproblems are small enough, solve them directly.
  - Combine: Merge the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer is useful for solving problems that have the following characteristics:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems can be solved independently and in parallel.
  - The subproblems are not too many and not too small.
  - The solution for the original problem can be obtained by combining the solutions of the subproblems in a simple and efficient way.
- Some examples of problems that can be solved by divide and conquer are:

## Sorting
- Sorting is the problem of arranging a sequence of elements in a specific order, such as ascending or descending.
- Sorting can be done by divide and conquer by splitting the sequence into two halves, sorting them recursively, and merging them in a sorted order.
- Some sorting algorithms that use divide and conquer are:
  - Merge sort: Divide the sequence into two halves, sort them recursively, and merge them in a sorted order. The time complexity is O(n log n), where n is the number of elements.
  - Quick sort: Choose a pivot element, partition the sequence into two subarrays such that the elements in the left subarray are smaller than or equal to the pivot and the elements in the right subarray are larger than the pivot, sort the subarrays recursively, and concatenate them. The time complexity is O(n log n) on average, but O(n^2) in the worst case, where n is the number of elements.
  - Heap sort: Build a max-heap or a min-heap from the sequence, repeatedly extract the root element and place it at the end of the sequence, and reduce the heap size by one. The time complexity is O(n log n), where n is the number of elements.

## Matrix Multiplication
- Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining a product matrix.
- Matrix multiplication can be done by divide and conquer by splitting the matrices into four submatrices of equal size, multiplying them recursively, and adding or subtracting the results to obtain the product matrix.
- Some matrix multiplication algorithms that use divide and conquer are:
  - Strassen's algorithm: Divide the matrices into four submatrices of size n/2 x n/2, compute seven products of submatrices using recursive calls, and combine them using addition and subtraction to obtain the product matrix. The time complexity is O(n^2.81), where n is the dimension of the matrices.
  - Coppersmith-Winograd algorithm: Divide the matrices into submatrices of size n^(1/3) x n^(1/3), compute 23 products of submatrices using recursive calls, and combine them using addition and subtraction to obtain the product matrix. The time complexity is O(n^2.375), where n is the dimension of the matrices.

## Convex Hull
- Convex hull is the problem of finding the smallest convex polygon that contains a set of points in the plane.
- Convex hull can be done by divide and conquer by splitting the points into two subsets by a vertical line, finding the convex hulls of the subsets recursively, and merging them by finding the upper and lower tangents. The time complexity is O(n log n), where n is the number of points.

## Searching
- Searching is the problem of finding an element in a sequence or a data structure that satisfies a given condition or matches a given value.
- Searching can be done by divide and conquer by splitting the sequence or the data structure into two parts, checking the condition or the value in one part, and searching recursively in the other part if needed.
- Some searching algorithms that use divide and conquer are:
  - Binary search: Given a sorted sequence and a value, find the index of the value in the sequence or return -1 if not found. Compare the value with the middle element of the sequence, and search recursively in the left or right half depending on the comparison result. The time complexity is O(log n), where n is the number of elements.
  - Interpolation search: Given a sorted sequence and a value, find the index of the value in the sequence or return -1 if not found. Estimate



# Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer has three steps:
  - Divide: Split the problem into smaller and independent subproblems of the same type.
  - Conquer: Solve the subproblems recursively. If the subproblems are small enough, solve them directly.
  - Combine: Merge the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer is useful for problems that have the following properties:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems can be solved independently and recursively.
  - The solutions of the subproblems can be combined efficiently to obtain the solution for the original problem.
- Some examples of problems that can be solved by divide and conquer are sorting, matrix multiplication, convex hull, and searching.

## Matrix Multiplication

- Matrix multiplication is the operation of multiplying two matrices of compatible dimensions to obtain a third matrix.
- The standard algorithm for matrix multiplication takes O(n^3) time, where n is the number of rows and columns of the matrices.
- Divide and conquer can be used to improve the time complexity of matrix multiplication by splitting the matrices into smaller submatrices, multiplying them recursively, and adding the results to obtain the final matrix.
- One of the divide and conquer algorithms for matrix multiplication is Strassen's algorithm, which takes O(n^log7) time, where n is the number of rows and columns of the matrices.
- Strassen's algorithm works as follows:
  - Divide: Split each matrix into four submatrices of equal size by dividing the rows and columns in half.
  - Conquer: Compute seven products of submatrices recursively, using the following formulas:

    - P1 = (A11 + A22) * (B11 + B22)
    - P2 = (A21 + A22) * B11
    - P3 = A11 * (B12 - B22)
    - P4 = A22 * (B21 - B11)
    - P5 = (A11 + A12) * B22
    - P6 = (A21 - A11) * (B11 + B12)
    - P7 = (A12 - A22) * (B21 + B22)

  - Combine: Compute the four submatrices of the final matrix by adding and subtracting the products, using the following formulas:

    - C11 = P1 + P4 - P5 + P7
    - C12 = P3 + P5
    - C21 = P2 + P4
    - C22 = P1 - P2 + P3 + P6

- Strassen's algorithm reduces the number of recursive multiplications from eight to seven, which leads to a lower time complexity. However, it also increases the number of additions and subtractions, which leads to a higher space complexity and constant factor. Therefore, Strassen's algorithm is more efficient than the standard algorithm only for large matrices.



# Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps:
  - Divide: Split the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: Solve the subproblems recursively, either directly or by applying the divide and conquer approach again.
  - Combine: Merge the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient, as they reduce the problem size exponentially at each level of recursion, and they are suitable for parallel and distributed computing.
- Some examples of divide and conquer algorithms are:
  - Merge sort: A sorting algorithm that divides the array into two halves, sorts them recursively, and then merges the sorted halves.
  - Quick sort: A sorting algorithm that partitions the array around a pivot element, such that all elements smaller than the pivot are on its left and all elements larger than the pivot are on its right, and then sorts the two subarrays recursively.
  - Binary search: A search algorithm that finds the position of a target value in a sorted array by repeatedly comparing the target with the middle element and halving the search range accordingly.
  - Strassen's algorithm: A matrix multiplication algorithm that divides each matrix into four submatrices, computes seven products of submatrices recursively, and then combines them to get the final product.
  - Fast Fourier transform: A numerical algorithm that computes the discrete Fourier transform of a sequence of complex numbers by dividing the sequence into two subsequences of even and odd indices, computing their Fourier transforms recursively, and then combining them using complex roots of unity.
  - Convex hull: A geometric algorithm that finds the smallest convex polygon that contains a set of points in the plane by dividing the set into two subsets, finding their convex hulls recursively, and then merging them using a linear-time algorithm.



# Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

Divide and conquer is a powerful algorithmic paradigm that solves a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer. Divide and conquer algorithms often have a logarithmic or sublinear complexity, which makes them efficient and scalable. Some examples of divide and conquer algorithms are:

- **Sorting**: Sorting is the process of arranging a collection of items in a certain order. There are many sorting algorithms that use divide and conquer, such as merge sort, quicksort, and heap sort. These algorithms divide the input array into smaller subarrays, sort them recursively, and merge or rearrange them to get the sorted array. The average time complexity of these algorithms is O(n log n), where n is the number of items in the array .
- **Matrix multiplication**: Matrix multiplication is the operation of multiplying two matrices to get a third matrix. A naive algorithm for matrix multiplication takes O(n^3) time, where n is the dimension of the matrices. However, there are divide and conquer algorithms that can multiply matrices faster, such as Strassen's algorithm, which takes O(n^2.8074) time. These algorithms divide the matrices into smaller submatrices, multiply them recursively, and combine them to get the final matrix .
- **Convex hull**: Convex hull is the smallest convex polygon that contains a set of points in a plane. A convex polygon is a polygon that has no interior angles greater than 180 degrees. A naive algorithm for finding the convex hull of n points takes O(n^3) time, by checking every possible subset of points. However, there are divide and conquer algorithms that can find the convex hull faster, such as Graham's scan, which takes O(n log n) time. These algorithms divide the points into smaller subsets, find their convex hulls recursively, and merge them to get the final convex hull.
- **Searching**: Searching is the process of finding a specific item or value in a collection of items or values. There are many searching algorithms that use divide and conquer, such as binary search, interpolation search, and exponential search. These algorithms divide the search space into smaller subspaces, search them recursively, and return the result. The average time complexity of these algorithms is O(log n) or O(log log n), where n is the size of the search space .

# Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy methods are a class of algorithms that make the locally optimal choice at each step, hoping to find the globally optimal solution. Greedy algorithms are often simple, fast, and easy to implement, but they may not always guarantee the optimal solution. Some examples of greedy algorithms are:

- **Optimal reliability allocation**: Optimal reliability allocation is the problem of allocating a given budget to improve the reliability of a system composed of several components. A greedy algorithm for this problem is to allocate the budget to the component that has the highest marginal benefit, i.e., the ratio of the increase in reliability to the cost of improvement, until the budget is exhausted or the reliability reaches a desired level.
- **Knapsack**: Knapsack is the problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized. A greedy algorithm for this problem is to sort the items by their value-to-weight ratio, and pack them in decreasing order of this ratio, until the knapsack is full or no more items can be packed.
- **Minimum spanning trees**: Minimum spanning trees are the subgraphs of a weighted undirected graph that connect all the vertices with the minimum total edge weight. A greedy algorithm for this problem is to start with an empty tree, and add the edge with the minimum weight that does not create a cycle, until all the vertices are connected. There are two famous greedy algorithms for this problem, Prim's algorithm and Kruskal's algorithm.
- **Single source shortest paths**: Single source shortest paths are the paths from a given source vertex to all other vertices in a weighted directed graph that have the minimum total edge weight. A greedy algorithm for this problem is to start with a set of tentative distances



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Design and Analysis of Algorithm. Here is the content for the topic of Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

# Greedy Methods

- Greedy methods are a class of algorithms that make a series of local optimal choices to find a global optimal solution.
- Greedy methods do not always guarantee the optimal solution, but they are often efficient and easy to implement.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: The optimal solution to the problem can be obtained by combining the optimal solutions to its subproblems.
  - Greedy choice property: A locally optimal choice at each step leads to a globally optimal solution.
- Some examples of greedy methods are:

## Optimal Reliability Allocation

- Optimal reliability allocation is a problem of allocating a given budget to improve the reliability of a system composed of several components.
- The objective is to maximize the overall reliability of the system, which is the probability that all components function correctly.
- A greedy method for this problem is to allocate the budget to the component with the lowest reliability-cost ratio at each step, until the budget is exhausted or all components reach their maximum reliability.
- The reliability-cost ratio of a component is the ratio of the increase in reliability to the increase in cost when the component is improved by one unit.
- The greedy method can be implemented as follows:

  - Initialize the total reliability R to 1 and the total cost C to 0.
  - Repeat until the budget is exhausted or all components reach their maximum reliability:
    - Find the component i with the lowest reliability-cost ratio r_i/c_i among the components that have not reached their maximum reliability.
    - If C + c_i <= B, where B is the budget, then:
      - Update R to R * (1 - r_i), where r_i is the reliability of component i.
      - Update C to C + c_i, where c_i is the cost of improving component i by one unit.
      - Update r_i to r_i * (1 - r_i), where r_i is the new reliability of component i.
    - Else, break the loop.
  - Return R as the optimal reliability of the system.

## Knapsack

- Knapsack is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity.
- The objective is to maximize the total value of the items in the knapsack, without exceeding the capacity.
- A greedy method for this problem is to sort the items by their value-weight ratio in decreasing order, and then pack the items in that order, until the knapsack is full or no more items can be packed.
- The value-weight ratio of an item is the ratio of its value to its weight.
- The greedy method can be implemented as follows:

  - Sort the items by their value-weight ratio v_i/w_i in decreasing order.
  - Initialize the total value V to 0 and the total weight W to 0.
  - Repeat for each item i in the sorted order:
    - If W + w_i <= C, where C is the capacity of the knapsack, then:
      - Update V to V + v_i, where v_i is the value of item i.
      - Update W to W + w_i, where w_i is the weight of item i.
    - Else, break the loop.
  - Return V as the optimal value of the knapsack.

## Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

- A minimum spanning tree (MST) of a weighted undirected graph is a subset of the edges that connects all the vertices with the minimum total weight.
- A greedy method for finding an MST is to start with an empty set of edges, and then add the edge with the lowest weight that does not create a cycle, until all the vertices are connected.
- There are two popular algorithms that implement this greedy method: Prim's algorithm and Kruskal's algorithm.
- Prim's algorithm starts with an arbitrary vertex, and then grows the MST by adding the edge with the lowest weight that connects a vertex in the MST to a vertex outside the MST, until all the vertices are included.
- Kruskal's algorithm starts with an empty set of edges, and then adds the edge with the lowest weight that does not create a cycle, until all the vertices are connected.
- Both algorithms can be implemented using a priority queue to store the edges by



# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem contains optimal solutions to its subproblems.
- Greedy choice property means that a locally optimal choice is also part of an optimal solution.

Some examples of greedy methods are:

- **Fractional knapsack problem**: Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, find the maximum value of items that can be packed in the knapsack. The items can be split into fractions. A greedy method for this problem is to sort the items by their value per unit weight, and then pack the items in that order until the knapsack is full or no more items are left. This method gives an optimal solution.
- **Minimum spanning tree problem**: Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. A greedy method for this problem is to start with an empty set of edges, and then repeatedly add the edge with the minimum weight that does not create a cycle, until all the vertices are connected. This method gives an optimal solution. There are two well-known algorithms based on this method: Prim's algorithm and Kruskal's algorithm.
- **Single source shortest path problem**: Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex. A greedy method for this problem is to maintain a set of vertices whose shortest distance from the source is known, and then repeatedly select the vertex with the minimum distance from the source that is not in the set, and update the distances of its adjacent vertices. This method gives an optimal solution. There are two well-known algorithms based on this method: Dijkstra's algorithm and Bellman-Ford algorithm.
- **Activity selection problem**: Given a set of activities, each with a start and finish time, find the maximum number of activities that can be performed by a single person, assuming that the person can only do one activity at a time. A greedy method for this problem is to sort the activities by their finish time, and then select the first activity, and then repeatedly select the next activity that starts after the finish of the previous activity, until no more activities can be selected. This method gives an optimal solution.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Design and Analysis of Algorithm. Here is the content for the topic of Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms.

# Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

## Greedy Methods
- A greedy method is a problem-solving technique that makes a locally optimal choice at each step, hoping to find a global optimum.
- A greedy method does not consider the future consequences of its choices, and may end up with a suboptimal solution.
- A greedy method is suitable for problems that have the following properties:
  - Optimal substructure: An optimal solution to the problem contains optimal solutions to its subproblems.
  - Greedy choice property: A locally optimal choice is also globally optimal, and can be made without solving the subproblems first.

## Minimum Spanning Trees
- A minimum spanning tree (MST) of a connected, undirected, weighted graph is a subgraph that is a tree and connects all the vertices of the graph, with the minimum possible total edge weight.
- A graph may have more than one MST, but the total weight of any MST is unique.
- Finding an MST is useful for applications such as network design, clustering, image segmentation, etc.
- There are two well-known greedy algorithms for finding an MST: Prim's algorithm and Kruskal's algorithm.

## Prim's Algorithm
- Prim's algorithm starts with an arbitrary vertex and grows the MST by adding the cheapest edge that connects a vertex in the MST to a vertex not in the MST, until all the vertices are included.
- Prim's algorithm can be implemented using a priority queue to store the edges and their weights, and a boolean array to mark the visited vertices.
- The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.

## Kruskal's Algorithm
- Kruskal's algorithm sorts the edges of the graph by their weights in ascending order, and adds them to the MST one by one, as long as they do not create a cycle, until all the vertices are connected.
- Kruskal's algorithm can be implemented using a disjoint-set data structure to keep track of the connected components of the MST, and a boolean array to mark the selected edges.
- The time complexity of Kruskal's algorithm is O(E log E), or O(E log V) if the edges are already sorted, where E is the number of edges and V is the number of vertices in the graph.



# Greedy Methods with Examples

Greedy methods are a class of algorithms that solve optimization problems by making locally optimal choices at each step, hoping to find a global optimum. Greedy algorithms are simple, fast, and easy to implement, but they do not always guarantee the optimal solution. Greedy algorithms work well for problems that have the following properties:

- **Optimal substructure**: The optimal solution to the problem can be obtained by using optimal solutions to its subproblems.
- **Greedy choice property**: A globally optimal solution can be reached by making the locally optimal choice at each step.

Some examples of greedy algorithms are:

- **Single source shortest paths - Dijkstra's algorithm**: This algorithm finds the shortest path from a given source node to all other nodes in a weighted graph. It works by maintaining a set of nodes whose shortest distance from the source is known, and repeatedly selecting the node with the minimum distance from the source and relaxing its adjacent edges. The algorithm terminates when all nodes have been visited or the destination node is reached.
- **Single source shortest paths - Bellman-Ford algorithm**: This algorithm also finds the shortest path from a given source node to all other nodes in a weighted graph, but it can handle negative edge weights. It works by relaxing all the edges of the graph for |V| - 1 times, where |V| is the number of nodes in the graph. The algorithm can also detect negative cycles, which are cycles whose total weight is negative.
- **Optimal reliability allocation**: This problem involves allocating a given budget to improve the reliability of a system composed of n components. Each component has a cost and a reliability function, which gives the probability of the component functioning correctly. The goal is to maximize the overall reliability of the system, which is the product of the reliabilities of the components. A greedy algorithm for this problem works by sorting the components in decreasing order of their marginal reliability per unit cost, and then allocating the budget to the components in that order until the budget is exhausted or all components are improved.
- **Knapsack problem**: This problem involves packing a set of items, each with a weight and a value, into a knapsack with a limited capacity. The goal is to maximize the total value of the items in the knapsack. A greedy algorithm for this problem works by sorting the items in decreasing order of their value per unit weight, and then adding the items to the knapsack in that order until the knapsack is full or all items are considered.
- **Minimum spanning tree - Prim's algorithm**: This algorithm finds a minimum spanning tree of a connected, undirected, weighted graph. A spanning tree is a subgraph that connects all the nodes of the graph and has no cycles. A minimum spanning tree is a spanning tree that has the minimum total weight among all possible spanning trees. Prim's algorithm works by starting with an arbitrary node and growing the tree by adding the edge with the minimum weight that connects a node in the tree to a node outside the tree, until all nodes are in the tree.
- **Minimum spanning tree - Kruskal's algorithm**: This algorithm also finds a minimum spanning tree of a connected, undirected, weighted graph. It works by sorting the edges of the graph in increasing order of their weight, and then adding the edges to the tree one by one, as long as they do not create a cycle, until the tree has |V| - 1 edges, where |V| is the number of nodes in the graph.



# Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## Dynamic Programming
- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which leads to wasteful computation.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming avoids repeated computation by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have a recursive formulation, where the problem can be divided into smaller and simpler subproblems of the same type.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up.
- Top-down approach starts with the original problem and recursively solves the subproblems until the base cases are reached. The results of subproblems are stored in a table and looked up when needed.
- Bottom-up approach starts with the base cases and iteratively builds up the solution of larger subproblems using the results of smaller subproblems stored in a table.
- Dynamic programming can be used to solve problems such as knapsack, all pair shortest paths, resource allocation, etc.

## Knapsack Problem
- Knapsack problem is a problem of finding the most valuable subset of items that can be packed into a knapsack with a limited capacity.
- Knapsack problem can be classified into two types: 0-1 knapsack and fractional knapsack.
- 0-1 knapsack problem means that each item can be either taken or left out, and the value and weight of each item are integers.
- Fractional knapsack problem means that each item can be taken partially, and the value and weight of each item are real numbers.
- 0-1 knapsack problem can be solved using dynamic programming, while fractional knapsack problem can be solved using a greedy approach.
- To solve 0-1 knapsack problem using dynamic programming, we define a table K[n+1][W+1], where n is the number of items and W is the capacity of the knapsack.
- K[i][j] represents the maximum value that can be obtained by using the first i items and a knapsack of capacity j.
- The base cases are K[0][j] = 0 for all j and K[i][0] = 0 for all i, meaning that no value can be obtained with no items or no capacity.
- The recursive formula is K[i][j] = max(K[i-1][j], K[i-1][j-w[i]] + v[i]), where w[i] and v[i] are the weight and value of the ith item, respectively.
- The first term K[i-1][j] means that the ith item is not taken, and the second term K[i-1][j-w[i]] + v[i] means that the ith item is taken and the remaining capacity is j-w[i].
- The maximum value is K[n][W], and the optimal subset can be traced back by checking which items are taken or not.
- The time complexity of this algorithm is O(nW), and the space complexity is O(nW).

## All Pair Shortest Paths
- All pair shortest paths problem is a problem of finding the shortest paths between every pair of vertices in a weighted graph.
- All pair shortest paths problem can be solved using dynamic programming, such as Warshal's and Floyd's algorithms.
- Warshal's algorithm is a special case of Floyd's algorithm for unweighted graphs, where the edge weights are either 0 or 1, representing the absence or presence of an edge.
- Warshal's algorithm uses a boolean matrix A[n][n], where n is the number of vertices in the graph.
- A[i][j] represents whether there is a path from vertex i to vertex j in the graph.
- The base case is A[i][j] = true if there is an edge from i to j, and A[i][j] = false otherwise.
- The recursive formula is A[i][j] = A[i][j] or (A[i][k] and A[k][j]), where k is an intermediate vertex.
- The first term A[i][j] means that there is a direct path from i to j, and the second term (A[i][k] and A[k][j]) means that there is a path



# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be divided into smaller subproblems of the same type, and the solutions of the subproblems can be combined to obtain the solution of the original problem.
- Dynamic programming can reduce the time complexity of solving a problem by avoiding recomputation of the same subproblems, and can also save space by storing the solutions of the subproblems in a table or an array.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. In the top-down approach, the problem is solved recursively by breaking it into smaller subproblems, and the solutions of the subproblems are stored in a table or an array for future use. In the bottom-up approach, the problem is solved iteratively by starting from the smallest subproblems and building up the solution of the original problem by using the solutions of the subproblems.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which is stated as follows:

## 0/1 Knapsack Problem

- Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
- The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, and there is no fractional inclusion of any item.
- The 0/1 knapsack problem can be solved using dynamic programming by defining a function `f(i, w)` that returns the maximum value that can be obtained by using the first `i` items and a knapsack of capacity `w`.
- The function `f(i, w)` can be computed recursively as follows:

```
f(i, w) = 0, if i = 0 or w = 0
f(i, w) = f(i - 1, w), if wi > w
f(i, w) = max(f(i - 1, w), f(i - 1, w - wi) + vi), if wi <= w
```

- Where `wi` and `vi` are the weight and value of the `i`-th item, respectively.
- The base case of the recursion is when `i = 0` or `w = 0`, which means that there are no items or no capacity left, and the maximum value is zero.
- The recursive case has two possibilities: either the `i`-th item is not included in the optimal solution, in which case the maximum value is the same as using the first `i - 1` items and the same capacity, or the `i`-th item is included in the optimal solution, in which case the maximum value is the sum of the value of the `i`-th item and the maximum value of using the first `i - 1` items and the remaining capacity after subtracting the weight of the `i`-th item.
- The optimal solution of the 0/1 knapsack problem is given by `f(n, W)`, where `n` is the number of items and `W` is the capacity of the knapsack.
- The function `f(i, w)` can be computed using a two-dimensional array of size `(n + 1) x (W + 1)`, where each element `f[i][w]` stores the value of `f(i, w)`.
- The array can be filled up in a bottom-up manner, starting from the base case of `f[0][w] = 0` for all `w`, and `f[i][0] = 0` for all `i`, and then using the recursive formula to compute the rest of the elements.
- The time complexity of this algorithm is `O(nW)`, and the space complexity is also `O(nW)`.
- The following is an example of solving the 0/1 knapsack problem using dynamic programming:

### Example

- Find an optimal solution for the following 0/1 knapsack problem using dynamic programming:

```
Number of items n = 4
Knapsack capacity W =

```




# Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

## What is Dynamic Programming?

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure .
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to optimize the time and space complexity of recursive solutions by storing the results of subproblems in a table (memoization) or by computing the results of subproblems in a bottom-up manner (tabulation) .
- Dynamic programming can be applied to various types of problems, such as optimization, counting, and decision making.

## Examples of Dynamic Programming Problems

### Knapsack Problem

- Given a set of items, each with a weight and a value, determine the number of each item to include in a knapsack so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- This problem has overlapping subproblems, because the optimal solution for a smaller knapsack can be used to find the optimal solution for a larger knapsack.
- This problem also has optimal substructure, because the optimal solution for a knapsack can be obtained by adding or excluding an item from the optimal solution for a smaller knapsack.
- A dynamic programming solution for this problem can use a two-dimensional array to store the maximum value that can be obtained for each weight limit and each item.
- The base case is when the weight limit or the number of items is zero, in which case the value is zero.
- The recursive case is when the weight limit or the number of items is positive, in which case the value is the maximum of two cases: including the current item (if it does not exceed the weight limit) or excluding the current item.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- Given a weighted graph, find the shortest path between every pair of vertices.
- This problem has overlapping subproblems, because the shortest path between two vertices can be composed of the shortest paths between intermediate vertices.
- This problem also has optimal substructure, because the shortest path between two vertices is the minimum of the shortest paths between them and all possible intermediate vertices.
- A dynamic programming solution for this problem can use a three-dimensional array to store the shortest distance between every pair of vertices for every possible number of intermediate vertices.
- The base case is when the number of intermediate vertices is zero, in which case the distance is the direct edge weight between the vertices (or infinity if there is no edge).
- The recursive case is when the number of intermediate vertices is positive, in which case the distance is the minimum of two cases: using the current intermediate vertex or not using it.
- Warshal's algorithm is a special case of this problem when the graph is unweighted and the distance is measured by the number of edges.
- Floyd's algorithm is a general case of this problem when the graph is weighted and the distance is measured by the sum of edge weights.



# Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- A problem has overlapping subproblems if the same subproblem is solved repeatedly in the process of finding the optimal solution.
- A problem has optimal substructure if the optimal solution of the original problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can handle deterministic or stochastic transitions.
- The main idea of dynamic programming is to break down a complex problem into simpler subproblems, and store the results of these subproblems in a table or a matrix, so that they can be reused later.
- The general steps of dynamic programming are:

  1. Identify the state variables that describe the problem.
  2. Define the optimal value function that gives the maximum (or minimum) return for each state.
  3. Find the recurrence relation that relates the optimal value function of a state to the optimal value functions of its successor states.
  4. Solve the recurrence relation using a bottom-up or a top-down approach, and fill in the table or matrix with the optimal values.
  5. Trace back the optimal solution from the final state to the initial state, using the table or matrix.

- An example of a problem that can be solved by dynamic programming is the resource allocation problem, where a fixed amount of a resource (such as money, time, or energy) has to be allocated to a number of independent activities (such as projects, tasks, or investments) in order to maximize the total return (such as profit, utility, or satisfaction).
- The resource allocation problem can be formulated as follows:

  - Let N be the number of activities, and M be the amount of resource available.
  - Let R(i,j) be the return obtained from allocating j units of resource to activity i, where i = 1, 2, ..., N and j = 0, 1, ..., M.
  - Let x(i) be the amount of resource allocated to activity i, where x(i) is an integer between 0 and M, and the sum of x(i) over all i is equal to M.
  - The objective is to find the optimal allocation x(i) for all i that maximizes the total return R(x) = sum of R(i,x(i)) over all i.

- The resource allocation problem can be solved by dynamic programming as follows:

  1. The state variables are the activity index i and the remaining resource x.
  2. The optimal value function is S(i,x), which gives the maximum return obtainable from activities i through N, given x units of resource remaining to be allocated.
  3. The recurrence relation is S(i,x) = max of R(i,j) + S(i+1,x-j) over all j = 0, 1, ..., x, with the base case S(N+1,x) = 0 for all x.
  4. The recurrence relation can be solved by a bottom-up approach, starting from i = N and x = 0, and filling in a table of size (N+1) x (M+1) with the optimal values S(i,x).
  5. The optimal solution can be traced back from S(1,M) by finding the value of j that maximizes R(1,j) + S(2,M-j), and then repeating the same process for i = 2, 3, ..., N. The optimal allocation is x(i) = j for each i.



# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a finite set of possible solutions. They both use a state-space tree to represent the solution space and apply pruning strategies to eliminate suboptimal or infeasible solutions. However, they differ in the way they traverse the tree and the criteria they use for pruning.

## Backtracking

Backtracking is an algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions. It works by exploring the solution space in a depth-first manner, starting from an empty or partial solution and extending it one step at a time. At each step, it checks whether the current solution satisfies the constraints of the problem. If it does, it recursively explores the next step. If it does not, it backtracks to the previous step and tries a different option. This process continues until all possible solutions are found or no more options are available.

Backtracking can be applied to problems such as:

- Sudoku: The problem is to fill a 9x9 grid with digits from 1 to 9 such that each row, column, and 3x3 subgrid contains exactly one of each digit. A backtracking algorithm can start from an empty grid and try to place a digit in each cell, checking whether it violates any constraint. If it does, it removes the digit and tries another one. If it does not, it moves to the next cell. If all cells are filled, a solution is found. Otherwise, the algorithm backtracks to the last cell and tries a different digit.
- N-Queens: The problem is to place N queens on an NxN chessboard such that no two queens attack each other. A backtracking algorithm can start from an empty board and try to place a queen in each row, checking whether it conflicts with any previously placed queen. If it does, it removes the queen and tries another column. If it does not, it moves to the next row. If all rows are filled, a solution is found. Otherwise, the algorithm backtracks to the last row and tries a different column.
- Graph Coloring: The problem is to assign a color to each vertex of a graph such that no two adjacent vertices have the same color. A backtracking algorithm can start from an empty coloring and try to assign a color to each vertex, checking whether it clashes with any neighboring vertex. If it does, it removes the color and tries another one. If it does not, it moves to the next vertex. If all vertices are colored, a solution is found. Otherwise, the algorithm backtracks to the last vertex and tries a different color.

## Branch and Bound

Branch and bound is an algorithm for discrete and combinatorial optimization problems and mathematical optimization. It works by dividing the solution space into smaller and smaller subsets (branches) and evaluating a lower or upper bound (bound) for the optimal value of each subset. It then discards (prunes) any subset whose bound is worse than the best known solution so far. It also keeps track of the best solution found so far and updates it whenever a better one is found. This process continues until the optimal solution is found or the solution space is exhausted.

Branch and bound can be applied to problems such as:

- 0/1 Knapsack: The problem is to select a subset of items with given weights and values such that the total value is maximized and the total weight does not exceed a given capacity. A branch and bound algorithm can start from an empty knapsack and consider each item in turn, either including it or excluding it from the knapsack. At each step, it calculates a bound for the value of the optimal solution that can be obtained from the current subset of items. If the bound is better than the best known solution so far, it recursively explores the next item. If the bound is worse, it prunes the branch. If all items are considered, a solution is found. The bound can be computed by using a greedy or a dynamic programming approach.
- Travelling Salesman Problem: The problem is to find the shortest tour that visits each city in a given set of cities exactly once and returns to the starting city. A branch and bound algorithm can start from an arbitrary city and consider each possible next city in turn, adding the distance between them to the current tour length. At each step, it calculates a bound for the length of the optimal tour that can be obtained from the current partial tour. If the bound is better than the best known solution so



# Backtracking, Branch and Bound with Examples Such as Graph Coloring

- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large number of possibilities. It works by trying out different choices and undoing them if they lead to a dead end or an invalid solution.
- Branch and bound is a technique to solve optimization problems that involve finding the best solution among a large number of possibilities. It works by exploring a tree of partial solutions and pruning the branches that cannot lead to a better solution than the current best one.
- Graph coloring is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. It has applications in scheduling, map coloring, register allocation, etc.
- Some examples of graph coloring algorithms using backtracking and branch and bound are:

  - Backtracking algorithm for m-coloring problem  :
    - Given an undirected connected graph G and m colors, use these colors to color the vertices of the graph, with one color for each vertex.
    - The algorithm works as follows:
      - Start with the first vertex and assign it the first color.
      - For each subsequent vertex, try to assign it a color that is different from the colors of its adjacent vertices. If there is no such color, backtrack and try a different color for the previous vertex.
      - Repeat this process until all vertices are colored or there is no feasible solution.
      - If a solution is found, print the color configuration and return.
    - The algorithm can be implemented using recursion or a stack.
    - The time complexity of the algorithm is O(m^n), where n is the number of vertices and m is the number of colors.

  - Branch and bound algorithm for m-coloring problem:
    - Given an undirected connected graph G and m colors, use these colors to color the vertices of the graph, with one color for each vertex, such that the number of colors used is minimized.
    - The algorithm works as follows:
      - Start with an empty color configuration and a lower bound of 1 for the number of colors needed.
      - For each vertex, generate all possible color assignments that are consistent with the current configuration and the lower bound. Each color assignment represents a branch in the solution tree.
      - For each branch, compute an upper bound for the number of colors needed by using a greedy algorithm that colors the remaining vertices with the least possible number of colors.
      - Prune the branches that have an upper bound greater than or equal to the current best solution.
      - Select the branch with the smallest upper bound and expand it further.
      - Repeat this process until a leaf node is reached or the solution tree is empty.
      - If a leaf node is reached, update the best solution and return.
    - The algorithm can be implemented using a priority queue or a heap.
    - The time complexity of the algorithm is O(n!m^n), where n is the number of vertices and m is the number of colors. However, the algorithm can be much faster in practice due to pruning.



# Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm reduces the problem to the call `backtrack(root(P))`, where `backtrack` is the following recursive procedure: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- The procedure `backtrack` takes two arguments: a problem `P` and a candidate `c`. The problem `P` defines the constraints and the goal of the problem, and the candidate `c` is a partial solution that may or may not satisfy the constraints or the goal. 
- The procedure `reject` tests whether the candidate `c` violates any of the constraints of `P`. If it does, the procedure returns `true` and the candidate is discarded. Otherwise, it returns `false` and the candidate is further explored. 
- The procedure `accept` tests whether the candidate `c` satisfies the goal of `P`. If it does, the procedure returns `true` and the candidate is output as a solution. Otherwise, it returns `false` and the candidate is extended. 
- The procedure `first` returns the first extension of the candidate `c` that is consistent with the constraints of `P`. If there is no such extension, it returns `NULL`. 
- The procedure `next` returns the next extension of the candidate `c` that is consistent with the constraints of `P`, after the previous extension `s`. If there is no such extension, it returns `NULL`. 
- The backtracking algorithm can be applied to a variety of problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. 
- One example of a problem that can be solved by backtracking is the n-queen problem, which is to place n queens on an n×n chessboard such that no two queens attack each other. 
- The n-queen problem can be formulated as follows: 
  - The problem `P` is to place n queens on an n×n chessboard.
  - A candidate `c` is an array of size n, where `c[i]` represents the column of the queen in the i-th row. The array is initialized with all zeros, meaning no queens are placed yet.
  - The procedure `reject` returns `true` if any of the following conditions are true: 
    - `c[i]` is zero, meaning the i-th row is empty.
    - `c[i]` is equal to `c[j]` for some `j < i`, meaning two queens are in the same column.
    - `|c[i] - c[j]|` is equal to `|i - j|` for some `j < i`, meaning two queens are in the same diagonal.
  - The procedure `accept` returns `true` if `i` is equal to `n`, meaning all rows are filled with queens. 
  - The procedure `first` returns `1` if `c[i]` is zero, meaning the i-th row is empty. Otherwise, it returns `NULL`. 
  - The procedure `next` returns `c[i] + 1` if `c[i] < n`, meaning the i-th row can be extended to the next column. Otherwise, it returns `NULL`. 
- The following is an example of a solution to the 4-queen problem, where `c = [2, 4, 1, 3]`: 

```
. Q . .
. . . Q

```




# Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps.
- Backtracking can be viewed as a depth-first search of a state space tree, where each node represents a partial candidate, and the branches are the possible extensions of the candidate. The algorithm traverses the tree by exploring one branch at a time until a solution is found or a dead end is reached .
- The algorithm can be implemented using recursion or iteration. A recursive implementation typically uses a procedure that takes a partial candidate as a parameter and performs the following steps:
  - If the candidate is a solution, output it or store it in a list.
  - If the candidate is not a solution, but can be extended, generate the possible extensions and recursively call the procedure for each extension.
  - If the candidate is not a solution and cannot be extended, return or backtrack to the previous level.
- A common way to implement backtracking iteratively is to use a stack to store the partial candidates and the possible extensions at each level. The algorithm pops a candidate from the stack, checks if it is a solution or can be extended, and pushes the extensions back to the stack. The algorithm terminates when the stack is empty or a solution is found.
- Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems.
- However, backtracking can be very inefficient, as it can generate a lot of candidates that are eventually rejected. The worst-case time complexity of backtracking is exponential in the size of the problem, and the space complexity is linear in the depth of the recursion.
- To improve the efficiency of backtracking, some techniques can be applied, such as pruning, ordering, caching, and heuristics. Pruning is the process of discarding candidates that are guaranteed to be invalid or suboptimal, based on some criteria or constraints. Ordering is the process of choosing the order of generating and exploring the candidates, based on some criteria or heuristics, to reduce the number of backtracks. Caching is the process of storing the results of previously computed subproblems, to avoid recomputing them. Heuristics are rules of thumb that guide the search towards promising candidates, based on some domain knowledge or experience.
- One example of a problem that can be solved by backtracking is the Hamiltonian cycle problem. A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem is to determine whether a given graph has a Hamiltonian cycle, and if so, to find one or all of them.
- A possible backtracking algorithm for the Hamiltonian cycle problem is as follows:
  - Start from any vertex and mark it as visited.
  - For each adjacent vertex that is not visited, add it to the cycle and recursively check if the cycle can be extended from that vertex.
  - If the cycle cannot be extended, remove the last vertex from the cycle and backtrack to the previous vertex.
  - If the cycle can be extended and the last vertex is adjacent to the first vertex, output the cycle or store it in a list.
  - Return true if a cycle is found, or false otherwise.
- The following is a pseudocode implementation of the algorithm:

```python
# Input: a graph G and a starting vertex v
# Output: true if G has a Hamiltonian cycle, or false otherwise
# Side effect: print or store the cycle if found
def hamiltonian_cycle(G, v):
  # Initialize an empty list to store the cycle
  cycle = []
  # Initialize a set to store the visited vertices
  visited = set()
  # Call the recursive helper function
  return hamiltonian_cycle_helper(G, v, cycle, visited)

# Input: a graph G, a current

```




# Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be applied to problems that can be represented as a state space tree, where each node is a partial solution and the leaves are the complete solutions. 
- The backtracking algorithm traverses the state space tree by exploring the children of each node, starting from the root. If a node is found to be invalid or a dead end, the algorithm backtracks to its parent and tries another child. The algorithm terminates when all the nodes have been visited or a solution is found.  
- The backtracking algorithm can be implemented using a recursive function that takes the current node as a parameter and performs the following steps: 
  - If the node is a solution, print or return it.
  - If the node is invalid or a dead end, return.
  - For each child of the node, call the recursive function with the child as the parameter.
- The backtracking algorithm can be optimized by using some techniques, such as pruning, ordering, and bounding, to reduce the number of nodes that need to be explored.  
- One example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value. 
- The sum of subsets problem can be represented as a state space tree, where each node is a subset of the given set and the root is the empty set. The children of a node are obtained by adding one element from the remaining set to the node. The node is a solution if the sum of its elements is equal to the target value. The node is invalid if the sum of its elements is greater than the target value. 
- The following is a pseudocode of the backtracking algorithm for the sum of subsets problem: 

```
function sumOfSubsets(set, target, index, subset, sum):
  # set is the given set of positive integers
  # target is the given target value
  # index is the current position in the set
  # subset is the current subset
  # sum is the current sum of the subset
  if sum == target: # if the subset is a solution
    print subset # print or return the subset
  elif sum < target and index < set.length: # if the subset is not a dead end
    # include the current element in the subset
    subset.add(set[index])
    sumOfSubsets(set, target, index + 1, subset, sum + set[index])
    # exclude the current element from the subset
    subset.remove(set[index])
    sumOfSubsets(set, target, index + 1, subset, sum)
```

- The following is an example of the sum of subsets problem with the set {10, 7, 5, 18, 12, 20, 15} and the target value 35: 

```
The state space tree for the problem is:

               {} (0)
              /      \
          {10} (10)   {} (0)
          /   \       /   \
      {10,7} (17) {7} (7) {5} (5) {} (0)
      /  \    / \   / \   / \   / \
  {10,7,5} (22) ... ... ... ... ... ...
  /  \    / \
{10,7,5,18} (40) {10,7,5,12} (34) {10,7,5,20} (42) {10,7,5,15} (37)
/ \ / \ / \ / \
... ... ... ... ... ...

The solutions are:

{10, 7, 18}
{10, 5, 20}
{

```




# Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets

- NP-Completeness is a concept that relates to the difficulty of solving certain computational problems. A problem is NP-complete if it belongs to the class NP (nondeterministic polynomial time) and every other problem in NP can be reduced to it in polynomial time.
- NP problems are those that can be verified in polynomial time, but not necessarily solved in polynomial time. For example, given a solution to the travelling salesman problem (TSP), we can check if it is optimal by comparing its cost with the costs of all other possible solutions, which can be done in polynomial time. However, finding the optimal solution itself may take more than polynomial time.
- NP-complete problems are the hardest problems in NP, meaning that if we can find a polynomial-time algorithm for any one of them, we can find a polynomial-time algorithm for all of them. However, no such algorithm is known, and many computer scientists believe that none exists. Therefore, NP-complete problems are considered intractable or unsolvable in practice.
- Some examples of NP-complete problems are:
  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest possible route that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, assign one of k colors to each vertex of the graph such that no two adjacent vertices have the same color. The goal is to minimize k.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other (i.e., no two queens share the same row, column, or diagonal).
  - Hamiltonian Cycle: Given a graph, find a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target value, find a subset of the set that sums up to the target value.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. Optimization problems are those that seek to find the best solution among many possible solutions, such as minimizing the cost or maximizing the profit. Approximation algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal one in polynomial time  .
- Approximation algorithms have two main characteristics: the running time and the approximation ratio. The running time is the amount of time the algorithm takes to find a solution, which should be polynomial in the size of the input. The approximation ratio is the measure of how close the solution is to the optimal one, which is usually expressed as a factor or a percentage  .
- For example, an approximation algorithm for the TSP may have a running time of O(n^2) and an approximation ratio of 2, meaning that it can find a solution in quadratic time and that the solution is at most twice as long as the optimal one  .
- Some examples of approximation algorithms are:
  - Nearest Neighbor Algorithm for TSP: Start from any city and repeatedly visit the nearest unvisited city until all cities are visited, then return to the starting point. This algorithm has a running time of O(n^2) and an approximation ratio of 2  .
  - Greedy Algorithm for Graph Coloring: Assign the first color to the first vertex, then assign the next color to the next vertex that is not adjacent to any vertex with the same color, and repeat until all vertices are colored. This algorithm has a running time of O(n + m), where n is the number of vertices and m is the number of edges, and an approximation ratio of Δ + 1, where Δ is the maximum degree of the graph  .
  - Backtracking Algorithm for n-Queen Problem: Place the first queen in the first column, then try to place the next queen in the next column such that it does not attack the previous queen, and repeat until all queens are placed or no valid position is found. If no valid position



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-completeness is a concept that relates to the difficulty of solving certain problems in polynomial time.
- A problem is said to be in NP if it can be verified in polynomial time, given a possible solution.
- A problem is said to be NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm for them.
- Some examples of NP-complete problems are: satisfiability, vertex cover, clique, subset sum, traveling salesman problem, etc.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem.
- This technique does not guarantee the best solution, but rather a solution that is close to the optimal one, within some error bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the cost of the solution produced by the algorithm and the cost of the optimal solution.
- Some examples of approximation algorithms are: greedy algorithm, local search, randomized algorithm, etc.

## Examples of NP-Complete Problems and Approximation Algorithms

### Travelling Salesman Problem

- The travelling salesman problem (TSP) is to find the shortest tour that visits every city in a given set of cities and returns to the starting city.
- The TSP is NP-complete, and there is no polynomial time algorithm that can find the optimal tour.
- One approximation algorithm for the TSP is the nearest neighbor algorithm, which starts from a random city and repeatedly visits the nearest unvisited city until all cities are visited.
- The nearest neighbor algorithm has an approximation ratio of 2, which means that the cost of the tour produced by the algorithm is at most twice the cost of the optimal tour.

### Graph Coloring

- The graph coloring problem is to assign colors to the vertices of a graph such that no two adjacent vertices have the same color, using the minimum number of colors.
- The graph coloring problem is NP-complete, and there is no polynomial time algorithm that can find the optimal coloring.
- One approximation algorithm for the graph coloring problem is the greedy algorithm, which assigns colors to the vertices in some order, using the first available color that does not conflict with any previously colored neighbor.
- The greedy algorithm has an approximation ratio of ∆ + 1, where ∆ is the maximum degree of the graph, which means that the number of colors used by the algorithm is at most ∆ + 1 times the number of colors used by the optimal coloring.

### n-Queen Problem

- The n-queen problem is to place n queens on an n x n chessboard such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
- The n-queen problem is NP-complete, and there is no polynomial time algorithm that can find a valid placement of the queens.
- One approximation algorithm for the n-queen problem is the backtracking algorithm, which tries to place a queen in each row, starting from the first row, and recursively explores the possible positions for the remaining queens, backtracking if a conflict occurs.
- The backtracking algorithm has an approximation ratio of 1, which means that it always finds a valid placement of the queens, if one exists.

### Hamiltonian Cycles

- A Hamiltonian cycle is a cycle that visits every vertex of a graph exactly once and returns to the starting vertex.
- The Hamiltonian cycle problem is to determine whether a given graph has a Hamiltonian cycle or not.
- The Hamiltonian cycle problem is NP-complete, and there is no polynomial time algorithm that can solve it.
- One approximation algorithm for the Hamiltonian cycle problem is the Christofides algorithm, which works for graphs that are complete and have non-negative edge weights.
- The Christofides algorithm first finds a minimum spanning tree of the graph, then adds the minimum weight matching of the odd degree vertices of the tree, and finally shortcuts the resulting Eulerian cycle to obtain a Hamiltonian cycle.
- The Christofides algorithm has an approximation ratio of 3/2, which means that the cost of the cycle produced by the algorithm is at most 3/2 times the cost of the optimal cycle.

### Sum of Sub



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer.
- A decision problem is in the class P if there is a polynomial-time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A decision problem is in the class NP if there is a polynomial-time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A decision problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial-time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial-time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science and mathematics.
- Examples of NP-complete problems are:

  - Satisfiability (SAT): Given a Boolean formula with n variables and m clauses, is there an assignment of true or false values to the variables that satisfies all the clauses?
  - Traveling Salesman Problem (TSP): Given a set of n cities and the distances between them, is there a tour that visits each city exactly once and has a total length at most k?
  - Graph Coloring: Given a graph with n vertices and m edges, and a positive integer k, is there a way to assign one of k colors to each vertex such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a positive integer n, is there a way to place n queens on an n x n chessboard such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph with n vertices and m edges, is there a cycle that visits each vertex exactly once?
  - Subset Sum: Given a set of n positive integers and a target value k, is there a subset of the integers that adds up to k?

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function.
- An approximation algorithm is a polynomial-time algorithm that produces a solution that is close to the optimal one, within some guaranteed factor or bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, without necessarily finding it.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution. The smaller the ratio, the better the approximation.
- For minimization problems, the approximation ratio is defined as:

  - Approximation ratio = (value of algorithm solution) / (value of optimal solution)

- For maximization problems, the approximation ratio is defined as:

  - Approximation ratio = (value of optimal solution) / (value of algorithm solution)

- An approximation algorithm is called an alpha-approximation algorithm if its approximation ratio is at most alpha for any instance of the problem, where alpha is a constant greater than or equal to one.
- Examples of approximation algorithms are:

  - Vertex Cover: A vertex cover of a graph is a subset of vertices that touches every edge, i.e., for every edge, at least one of its endpoints is in the vertex cover. The vertex cover problem is to find the minimum size vertex cover of a given graph. There is a 2-approximation algorithm for this problem, which works as follows:

    - Start with an empty vertex cover.
    - While there are edges in the graph, pick an arbitrary edge and add both of its endpoints to the vertex cover. Remove all the edges incident to these vertices from the graph.
    - Return the vertex cover.

    - This algorithm is a 2-approximation algorithm because the size of the vertex cover it produces is at most twice the size of the optimal vertex cover. To see this, note that every edge in the graph contributes at least one vertex to the optimal vertex cover, and the algorithm adds at most two vertices for each edge.

  - TSP: The traveling salesman problem is to find the minimum length tour that visits each city exactly once



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for every problem in NP.
- Some examples of NP-complete problems are: 3-SAT, Clique, Vertex Cover, Subset Sum, Hamiltonian Cycle, Travelling Salesman Problem, etc.
- To prove that a problem is NP-complete, we need to show two things:
  - The problem is in NP, i.e., there is a polynomial time algorithm to verify a given solution.
  - The problem is NP-hard, i.e., there is a polynomial time reduction from any other problem in NP to this problem.
- To show that a problem is NP-hard, we can use the technique of reduction. This means that we can transform an instance of a known NP-hard problem into an instance of the problem we want to prove NP-hard, such that the answer is preserved. For example, we can reduce 3-SAT to Clique by constructing a graph where each vertex represents a literal and each edge represents a clause, and finding a k-clique in this graph is equivalent to finding a satisfying assignment for the 3-SAT formula.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution. The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- An approximation algorithm has a performance ratio, which is the ratio of the cost of the solution produced by the algorithm to the cost of the optimal solution. For example, if the optimal solution has a cost of 100 and the algorithm produces a solution with a cost of 120, then the performance ratio is 120/100 = 1.2. The smaller the performance ratio, the better the approximation.
- Some examples of approximation algorithms are: 2-approximation for Vertex Cover, 7/8-approximation for Max 3-SAT, 2-approximation for Travelling Salesman Problem with triangle inequality, etc.
- To design an approximation algorithm, we can use different techniques, such as:
  - Greedy: Choose the best option at each step, without looking ahead.
  - Rounding: Relax the problem to make it easier to solve, and then round the solution to make it feasible.
  - Randomization: Use random choices to explore different possibilities and avoid getting stuck in local optima.
  - Linear Programming: Formulate the problem as a linear program, and then use the optimal solution of the linear program as a guide to construct a feasible solution for the original problem.

## Examples of NP-Complete Problems and Approximation Algorithms

### Travelling Salesman Problem (TSP)

- The Travelling Salesman Problem is to find the shortest tour that visits every city in a given set of cities and returns to the starting city.
- The TSP is NP-complete, as we can reduce Hamiltonian Cycle to it by assigning a unit distance to every edge in the graph and finding the shortest tour in the resulting metric space.
- A 2-approximation algorithm for TSP with triangle inequality is to find a minimum spanning tree of the cities, and then traverse the tree in a preorder fashion, skipping any repeated cities. The cost of this tour is at most twice the cost of the optimal tour, as the cost of the tree is a lower bound on the optimal tour, and the cost of the preorder traversal is at most twice the cost of the tree.

### Graph Coloring

- The Graph Coloring problem is to assign colors to the vertices of a graph such that no two adjacent vertices have the same color, and the number of colors used is minimized.
- The Graph Coloring problem is NP-complete, as we can reduce 3-SAT to it by constructing a graph where each vertex represents a literal and each edge represents a clause, and finding a 3-coloring of this graph is equivalent to finding a satisfying assignment for the 3-SAT formula.
- A simple approximation algorithm for Graph Coloring is to order the vertices in some arbitrary way, and then assign the smallest available color to each vertex



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP-complete if it is both NP and NP-hard. NP means that there is a polynomial time algorithm that can verify a given solution to the problem. NP-hard means that any other NP problem can be reduced to this problem in polynomial time, meaning that this problem is at least as hard as any other NP problem. If there is a polynomial time algorithm that can solve any NP-complete problem, then P = NP, which is one of the most famous open questions in computer science.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions. Optimization problems often have an objective function that measures the quality of a solution, such as the cost, the profit, the length, the weight, etc. The goal of an approximation algorithm is to find a solution that is close to the optimal solution in polynomial time, without necessarily finding the exact optimal solution. Approximation algorithms often have a performance guarantee, which is a ratio that bounds how far the solution can be from the optimal solution  .
- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting city. This problem is NP-complete, and there is no polynomial time approximation algorithm that can achieve a constant ratio for the general case. However, there are some special cases, such as the metric TSP, where the triangle inequality holds, that can be approximated within a constant factor. For example, the nearest neighbor heuristic, which starts from a city and always visits the closest unvisited city, can achieve a 2-approximation for the metric TSP .
  - Graph Coloring: Given an undirected graph, assign a color to each vertex such that no two adjacent vertices have the same color, and minimize the number of colors used. This problem is NP-complete, and there is no polynomial time approximation algorithm that can achieve a constant ratio for the general case. However, there are some special cases, such as the planar graphs, where the graph can be drawn on a plane without crossing edges, that can be approximated within a constant factor. For example, the greedy algorithm, which colors the vertices in any order and assigns the smallest available color to each vertex, can achieve a 6-approximation for the planar graphs .
  - n-Queen Problem: Given an n x n chessboard, place n queens on the board such that no two queens attack each other, and maximize the number of queens placed. This problem is NP-complete, and there is no polynomial time approximation algorithm that can achieve a constant ratio for the general case. However, there are some special cases, such as the even n case, where n is an even number, that can be approximated within a constant factor. For example, the diagonal placement algorithm, which places a queen on every other diagonal cell of the board, can achieve a 2-approximation for the even n case .
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting vertex. This problem is NP-complete, and there is no polynomial time approximation algorithm that can achieve a constant ratio for the general case. However, there are some special cases, such as the metric Hamiltonian cycle, where the triangle inequality holds, that can be approximated within a constant factor. For example, the Christofides algorithm, which finds a minimum spanning tree of the graph, duplicates the odd-degree vertices, finds a perfect matching on them, and combines the two subgraphs into a cycle, can achieve a 3/2-approximation for the metric Hamiltonian cycle .
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the set that sums to the target, and minimize the number of elements in the subset. This problem is NP-complete, and there is no polynomial time approximation algorithm that can achieve a constant



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for all NP problems, and P = NP.
- Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- To prove that a problem is NP-complete, one can use the following steps:
  - Show that the problem is in NP, i.e., given a solution, it can be verified in polynomial time.
  - Choose a known NP-complete problem and show that it can be reduced to the given problem in polynomial time, i.e., given an instance of the known NP-complete problem, it can be transformed into an instance of the given problem in polynomial time, such that the answer is preserved.
- To cope with NP-completeness, one can use the following strategies:
  - Restrict the problem to a special case that is solvable in polynomial time, e.g., bipartite graph coloring, 2-SAT, etc.
  - Use heuristics or approximation algorithms that can find good solutions in polynomial time, but not necessarily the optimal ones.
  - Use exponential time algorithms that can solve small instances of the problem, or use randomized algorithms that can find the optimal solution with high probability.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution. The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- An approximation algorithm has a performance ratio, which is the ratio of the cost of the solution found by the algorithm to the cost of the optimal solution. The performance ratio can be either a constant, a function of the input size, or a function of some parameter of the problem. The smaller the performance ratio, the better the approximation algorithm.
- Some examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem, etc.
- To design an approximation algorithm, one can use the following techniques:
  - Greedy method: Choose the best option at each step, without looking ahead.
  - Rounding: Relax the problem to a linear program and round the fractional solution to an integer solution.
  - Randomization: Use random choices to find a good solution with high probability.
  - Local search: Start with a feasible solution and improve it by making local changes.



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- A reduction is a way of transforming one problem into another problem, such that solving the second problem also solves the first problem.
- NP-complete problems are important because they capture the essence of computational complexity and intractability.
- If there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for all NP-complete problems, which would imply P = NP.
- Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem.
- This technique does not guarantee the best solution, but a solution that is close to the optimal solution in polynomial time.
- The goal of an approximation algorithm is to achieve a good trade-off between the quality of the solution and the running time of the algorithm.
- The quality of an approximation algorithm is measured by the approximation ratio, which is the ratio between the cost of the solution produced by the algorithm and the cost of the optimal solution.
- The lower the approximation ratio, the better the approximation algorithm.
- Some examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem, etc.

