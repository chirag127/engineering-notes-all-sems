

## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An **algorithm** is a finite sequence of well-defined instructions for solving a problem or performing a task.
- **Analyzing algorithms** is the process of determining the amount of resources (such as time and space) that an algorithm requires to execute.
- The **complexity of algorithms** is a measure of the resources needed by an algorithm as a function of the input size.
- The **growth of functions** is a way of comparing the asymptotic behavior of different functions, such as the running time of algorithms. Common notations for describing the growth of functions are **big-O**, **big-Ω**, and **big-Θ**.
- **Performance measurements** are empirical methods of evaluating the efficiency and correctness of algorithms, such as experiments, benchmarks, and profiling.
- **Sorting** is the process of arranging a sequence of items in a certain order, such as ascending or descending. **Order statistics** are the values of the items at specific positions in a sorted sequence, such as the minimum, maximum, median, or kth smallest or largest element.
- **Shell sort** is a sorting algorithm that sorts the items by comparing and swapping elements that are far apart, and then reducing the gap between the compared elements until it reaches one. It is an improvement of insertion sort that has an average time complexity of **O(n^1.5)**, where n is the number of items.
- **Quick sort** is a sorting algorithm that sorts the items by choosing a pivot element and partitioning the sequence into two sub-sequences, such that all the elements in the left sub-sequence are smaller than or equal to the pivot, and all the elements in the right sub-sequence are larger than or equal to the pivot. Then, it recursively sorts the two sub-sequences. It has an average time complexity of **O(n log n)**, where n is the number of items, but a worst-case time complexity of **O(n^2)**, which occurs when the pivot is the smallest or largest element.
- **Merge sort** is a sorting algorithm that sorts the items by dividing the sequence into two equal or nearly equal sub-sequences, recursively sorting them, and then merging them into a single sorted sequence. It has a time complexity of **O(n log n)**, where n is the number of items, in both average and worst cases, but it requires additional space for the merging process.
- **Heap sort** is a sorting algorithm that sorts the items by using a data structure called a heap, which is a binary tree that satisfies the heap property: every node is larger than or equal to its children (max-heap) or smaller than or equal to its children (min-heap). It first builds a heap from the sequence, and then repeatedly extracts the root (the largest or smallest element) and places it at the end of the sorted sequence. It has a time complexity of **O(n log n)**, where n is the number of items, in both average and worst cases, and it does not require additional space.
- **Comparison of sorting algorithms** is the process of evaluating and choosing the most suitable sorting algorithm for a given problem, based on various criteria, such as time complexity, space complexity, stability, adaptability, simplicity, and parallelizability. Some general guidelines are:
  - For small input sizes, insertion sort or selection sort may be faster than more complex algorithms, due to their low overhead and simplicity.
  - For large input sizes, merge sort, quick sort, or heap sort may be preferred, due to their logarithmic time complexity and scalability.
  - For nearly sorted input, insertion sort or bubble sort may perform well, due to their adaptability to the existing order.
  - For duplicate values in the input, counting sort or radix sort may be efficient, due to their linear time complexity and stability.
  - For parallel or distributed computing, merge sort or quick sort may be suitable, due to their divide-and-conquer approach and ease of implementation.
- **Sorting in linear time** is the process of sorting a sequence of items in **O(n)** time, where n is the number of items, which is possible only when some additional assumptions or restrictions are made on the input or the output, such as:
  - The items are integers in a fixed range, which allows the use of counting sort, a sorting algorithm that counts the frequency of each value and then outputs the values in sorted order according to their frequencies.
  - The items have a fixed number of digits or bits, which



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

- Shell sort is a sorting algorithm that improves on the insertion sort by breaking the sequence into several sub-sequences and sorting them using insertion sort, then combining the sorted sub-sequences using a gap sequence.
- The gap sequence determines how the sub-sequences are formed and how they are reduced until the whole sequence is sorted.
- The performance of shell sort depends on the choice of the gap sequence. Some common gap sequences are:
  - Shell's original gap sequence: n/2, n/4, ..., 1
  - Hibbard's gap sequence: 1, 3, 7, ..., 2^k - 1
  - Sedgewick's gap sequence: 1, 5, 19, 41, ..., 4^k + 3*2^(k-1) + 1
- The best known worst-case time complexity of shell sort is O(n^(4/3)), achieved by Sedgewick's gap sequence. The average-case time complexity is unknown, but empirically it is faster than O(n^(3/2)).
- The space complexity of shell sort is O(1), as it is an in-place algorithm.

## Quick Sort

- Quick sort is a sorting algorithm that uses the divide-and-conquer strategy to sort a sequence by recursively partitioning it around a pivot element, such that all the elements smaller than the pivot are in the left sub-sequence and all the elements larger than the pivot are in the right sub-sequence, then sorting the sub-sequences recursively.
- The pivot element can be chosen in different ways, such as the first element, the last element, the median of three elements, or a random element. The choice of the pivot affects the performance of quick sort.
- The worst-case time complexity of quick sort is O(n^2), which occurs when the pivot is always the smallest or the largest element, resulting in unbalanced partitions. The average-case and best-case time complexity of quick sort is O(n log n), which occurs when the pivot is close to the median, resulting in balanced partitions.
- The space complexity of quick sort is O(log n) in the best case and O(n) in the worst case, due to the recursive calls. The space complexity can be reduced to O(log n) in the worst case by using tail recursion or iterative methods.



# Analyzing Algorithms

- Analyzing algorithms is the process of finding the **computational complexity** of algorithms, which is the amount of time, storage, or other resources needed to execute them .
- Analyzing algorithms helps us to compare different algorithms for the same problem and choose the most efficient one.
- Analyzing algorithms also helps us to estimate the performance of algorithms on different inputs and hardware platforms.
- There are two main types of analysis of algorithms: **asymptotic analysis** and **empirical analysis**.
  - Asymptotic analysis is a theoretical approach that focuses on the **growth of functions** that describe the time or space complexity of algorithms as the input size increases. It ignores the constant factors and lower-order terms that may affect the actual running time or space usage of algorithms.
  - Empirical analysis is a practical approach that involves **measuring** the actual running time or space usage of algorithms on real inputs and hardware platforms. It can provide more accurate results, but it may be affected by external factors such as compiler optimizations, system load, or input distribution.
- There are different ways to express the asymptotic complexity of algorithms, such as **big O notation**, **big Omega notation**, and **big Theta notation**. These notations capture the **upper bound**, **lower bound**, and **tight bound** of the growth of functions, respectively.
  - Big O notation is used to describe the **worst-case** complexity of algorithms, which is the maximum amount of time or space required by the algorithm for any input of size n. For example, O(n^2) means that the algorithm takes at most n^2 steps or units of space for any input of size n.
  - Big Omega notation is used to describe the **best-case** complexity of algorithms, which is the minimum amount of time or space required by the algorithm for any input of size n. For example, Ω(n) means that the algorithm takes at least n steps or units of space for any input of size n.
  - Big Theta notation is used to describe the **average-case** complexity of algorithms, which is the amount of time or space required by the algorithm for most inputs of size n. For example, Θ(n log n) means that the algorithm takes n log n steps or units of space for most inputs of size n.
- There are different types of problems that algorithms can solve, such as **sorting**, **searching**, **graph**, **optimization**, **cryptography**, and **machine learning** problems. Each type of problem may have different algorithms that can solve it with different complexities and trade-offs.
  - Sorting is the problem of arranging a set of items in a certain order, such as ascending or descending. Some common sorting algorithms are **shell sort**, **quick sort**, **merge sort**, **heap sort**, and **counting sort**. These algorithms have different time and space complexities, such as O(n^2), O(n log n), O(n log n), O(n log n), and O(n + k), respectively, where n is the number of items and k is the range of values.
  - Searching is the problem of finding a specific item or a set of items that satisfy some criteria in a collection of items. Some common searching algorithms are **linear search**, **binary search**, **hashing**, and **bloom filter**. These algorithms have different time and space complexities, such as O(n), O(log n), O(1), and O(m), respectively, where n is the number of items and m is the size of the filter.
  - Graph is the problem of representing and manipulating a set of objects and their relationships, such as networks, maps, or social media. Some common graph algorithms are **breadth-first search**, **depth-first search**, **Dijkstra's algorithm**, and **Kruskal's algorithm**. These algorithms have different time and space complexities, such as O(V + E), O(V + E), O(V log V + E), and O(E log V), respectively, where V is the number of vertices and E is the number of edges.
  - Optimization is the problem of finding the best or optimal solution among a set of possible solutions, such as scheduling, routing, or packing. Some common optimization algorithms are **greedy algorithm**, **dynamic programming**, **branch and bound**, and **genetic algorithm**. These algorithms have different time and space complexities, such as O(n), O(n^2), O(b^n), and O(nm), respectively, where n is the number of items



# Complexity of Algorithms

- Complexity of algorithms is a measure of how long an algorithm would take to complete given an input of size n.
- Complexity is about the algorithm itself, the way it processes the data to solve a given problem. It's a software design concern at the "idea level".
- Complexity is calculated asymptotically as n approaches infinity, to capture the behavior of the algorithm for large inputs.
- Complexity is also called algorithmic complexity or running time.
- Complexity is important for evaluating the efficiency and scalability of algorithms.
- Complexity can be measured in terms of time and space.
  - Time complexity: Time taken by the algorithm to solve the problem. It is measured by calculating the number of iterations of loops, recursive calls, comparisons, etc.
  - Space complexity: Space taken by the algorithm to solve the problem. It includes space for input, output, variables, constants, etc.
- Complexity can be expressed using different notations, such as big O, big Theta, big Omega, etc.
  - Big O notation: It gives the upper bound of the complexity, or the worst-case scenario. It is denoted by O(f(n)), where f(n) is some function of n.
  - Big Theta notation: It gives the tight bound of the complexity, or the average-case scenario. It is denoted by Θ(f(n)), where f(n) is some function of n.
  - Big Omega notation: It gives the lower bound of the complexity, or the best-case scenario. It is denoted by Ω(f(n)), where f(n) is some function of n.
- Complexity can be classified into different classes, such as constant, logarithmic, linear, polynomial, exponential, etc.
  - Constant complexity: It means the complexity does not depend on the input size. It is denoted by O(1).
  - Logarithmic complexity: It means the complexity grows as the logarithm of the input size. It is denoted by O(log n).
  - Linear complexity: It means the complexity grows as the input size. It is denoted by O(n).
  - Polynomial complexity: It means the complexity grows as some power of the input size. It is denoted by O(n^k), where k is some constant.
  - Exponential complexity: It means the complexity grows as some exponential function of the input size. It is denoted by O(a^n), where a is some constant.
- Complexity can be compared using the order of growth, or the rate at which the complexity increases as the input size increases.
  - For example, O(n) is better than O(n^2), because O(n) grows slower than O(n^2) as n increases.
  - Similarly, O(log n) is better than O(n), because O(log n) grows slower than O(n) as n increases.
  - The best complexity is O(1), because it does not depend on the input size at all.
  - The worst complexity is O(n!), because it grows faster than any other complexity as n increases.



# Growth of Functions

- Growth of functions is a concept that helps us to compare the efficiency and performance of different algorithms based on their input size and execution time.
- The growth of a function is the rate at which it increases or decreases as the input size changes. For example, a function that grows linearly has a constant rate of growth, while a function that grows exponentially has an increasing rate of growth.
- The growth of a function can be expressed using asymptotic notation, which is a mathematical tool that simplifies the function by ignoring the constants and lower order terms that are less significant for large inputs.
- There are three types of asymptotic notation: big-O, big-Ω, and big-Θ. Each of them represents a different way of bounding the growth of a function from above, below, or both.
- Big-O notation gives the upper bound of a function, meaning that the function is always less than or equal to a constant multiple of another function. For example, f(n) = O(g(n)) means that f(n) ≤ c*g(n) for some constant c and sufficiently large n.
- Big-Ω notation gives the lower bound of a function, meaning that the function is always greater than or equal to a constant multiple of another function. For example, f(n) = Ω(g(n)) means that f(n) ≥ c*g(n) for some constant c and sufficiently large n.
- Big-Θ notation gives the tight bound of a function, meaning that the function is both upper and lower bounded by a constant multiple of another function. For example, f(n) = Θ(g(n)) means that c1*g(n) ≤ f(n) ≤ c2*g(n) for some constants c1 and c2 and sufficiently large n.
- Some commonly used functions and their comparison are:
  - Constant functions: f(n) = 1. These functions take a constant amount of time regardless of the input size.
  - Linear functions: f(n) = n. These functions grow linearly with the input size.
  - Quadratic functions: f(n) = n^2. These functions grow faster than linear functions, but slower than exponential functions.
  - Logarithmic functions: f(n) = log n. These functions grow very slowly with the input size, and are often used in divide-and-conquer algorithms.
  - Exponential functions: f(n) = 2^n. These functions grow very fast with the input size, and are often infeasible to compute in practice.
- The growth of functions can help us to analyze the time and space complexity of algorithms, which are measures of how much time and memory an algorithm requires to solve a problem. The time complexity of an algorithm is the function that gives the number of basic operations performed by the algorithm as a function of the input size. The space complexity of an algorithm is the function that gives the amount of memory used by the algorithm as a function of the input size.
- The growth of functions can also help us to compare the best case, worst case, and average case scenarios of an algorithm, which are the minimum, maximum, and expected values of the time or space complexity of the algorithm for different inputs. For example, the best case time complexity of linear search is O(1), the worst case time complexity is O(n), and the average case time complexity is O(n/2).
- The growth of functions can also help us to choose the most suitable algorithm for a given problem, depending on the input size, the desired output, and the available resources. For example, for sorting a large array of numbers, quick sort is usually faster than merge sort, but merge sort is more stable and requires less space.



# Performance Measurements

Performance measurements are used to evaluate the efficiency and effectiveness of an algorithm in solving a problem. They help to compare different algorithms and choose the best one for a given situation. Performance measurements can be based on various factors, such as:

- **Space complexity**: The amount of memory or space required by an algorithm to perform its task. It consists of both program and data space. Space complexity can affect the performance of an algorithm in terms of speed, cost, and reliability.
- **Time complexity**: The amount of time or number of steps required by an algorithm to perform its task. It depends on the size and nature of the input, the speed of the processor, and the implementation of the algorithm. Time complexity can affect the performance of an algorithm in terms of responsiveness, throughput, and scalability.
- **Network complexity**: The amount of communication or data transfer required by an algorithm to perform its task. It depends on the distribution and connectivity of the data, the bandwidth and latency of the network, and the protocol of the communication. Network complexity can affect the performance of an algorithm in terms of availability, security, and consistency.

Performance measurements can be expressed using different notations, such as:

- **Big O notation**: The upper bound or worst-case scenario of the performance of an algorithm. It indicates the maximum amount of space, time, or network required by an algorithm as the input size grows indefinitely. For example, O(n) means that the performance of an algorithm is proportional to the input size n, and O(n^2) means that the performance of an algorithm is proportional to the square of the input size n.
- **Big Omega notation**: The lower bound or best-case scenario of the performance of an algorithm. It indicates the minimum amount of space, time, or network required by an algorithm as the input size grows indefinitely. For example, Ω(n) means that the performance of an algorithm is at least proportional to the input size n, and Ω(n^2) means that the performance of an algorithm is at least proportional to the square of the input size n.
- **Big Theta notation**: The average or expected scenario of the performance of an algorithm. It indicates the range of space, time, or network required by an algorithm as the input size grows indefinitely. For example, Θ(n) means that the performance of an algorithm is both O(n) and Ω(n), and Θ(n^2) means that the performance of an algorithm is both O(n^2) and Ω(n^2).

Performance measurements can be used to analyze and compare different algorithms for solving the same problem. For example, sorting and order statistics are common problems that can be solved by different algorithms, such as:

- **Shell sort**: A sorting algorithm that divides the input into sublists and sorts them using insertion sort. It has a time complexity of O(n^2) in the worst case and O(n log n) in the best case, and a space complexity of O(1).
- **Quick sort**: A sorting algorithm that partitions the input into two sublists based on a pivot element and recursively sorts them. It has a time complexity of O(n^2) in the worst case and O(n log n) in the average case, and a space complexity of O(log n).
- **Merge sort**: A sorting algorithm that divides the input into two sublists and recursively sorts them, then merges them. It has a time complexity of O(n log n) in all cases, and a space complexity of O(n).
- **Heap sort**: A sorting algorithm that builds a heap data structure from the input and repeatedly extracts the maximum element. It has a time complexity of O(n log n) in all cases, and a space complexity of O(1).
- **Comparison of sorting algorithms**: The performance of different sorting algorithms can vary depending on the input size, distribution, and order. Generally, merge sort and heap sort are more stable and efficient than shell sort and quick sort, but they require more space. Quick sort is faster than merge sort and heap sort on average, but it can be slow on sorted or nearly sorted inputs. Shell sort is simple and easy to implement, but it can be slow on large or random inputs.

- **Sorting in linear time**: Some sorting algorithms can achieve a time complexity of O(n) or linear time, but they have some limitations or assumptions. For example, counting sort and radix sort are sorting algorithms that can sort integers in linear time, but they require a fixed range of values and a constant number of digits. Bucket sort is a sorting algorithm that can sort floating-point numbers in linear time, but it



# Sorting and Order Statistics - Shell Sort

- Shell sort is a highly efficient sorting algorithm that is based on the insertion sort algorithm .
- It avoids large shifts of elements, as in insertion sort, where the smaller value is on the far right and must be moved to the far left .
- It first sorts elements that are far apart from each other and successively reduces the interval between the elements to be sorted .
- The interval between the elements is reduced based on the sequence used . A common sequence is N/2, N/4, ..., 1, where N is the size of the array .
- An array is said to be h-sorted if all sublists of every h'th element are sorted .
- The algorithm works as follows :
  - Start with a large value of h and sort the sublists of h elements using insertion sort.
  - Reduce the value of h and repeat the process until h becomes 1.
  - At the end, the array will be fully sorted.
- The time complexity of shell sort depends on the choice of the sequence. The worst-case time complexity is O(N^2), where N is the size of the array.
- The space complexity of shell sort is O(1), as it only requires constant extra space.
- Shell sort is an adaptive, unstable, and in-place sorting algorithm.
  - Adaptive: It adapts to the data and performs better on partially sorted arrays.
  - Unstable: It does not preserve the relative order of elements with equal keys.
  - In-place: It does not require extra space to sort the array.



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



# Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a sorted array.
- The algorithm can be described as follows:

  - If the array has zero or one element, it is already sorted and no further action is needed.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the sorted subarrays into a single sorted array.

- The merge operation takes two sorted arrays and combines them into one sorted array. It can be implemented as follows:

  - Initialize two pointers, i and j, to point to the first elements of the left and right subarrays, respectively.
  - Initialize an empty array, result, to store the merged array.
  - While both i and j are within the bounds of their respective subarrays, compare the elements at A[i] and A[j].
  - If A[i] <= A[j], append A[i] to result and increment i. Otherwise, append A[j] to result and increment j.
  - If either i or j reaches the end of its subarray, append the remaining elements of the other subarray to result.
  - Return result as the merged array.

- The pseudocode for merge sort is as follows:

  ```
  MERGE-SORT(A, p, r)
    if p < r
      q = floor((p + r) / 2)
      MERGE-SORT(A, p, q)
      MERGE-SORT(A, q + 1, r)
      MERGE(A, p, q, r)

  MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    create arrays L[1..n1 + 1] and R[1..n2 + 1]
    for i = 1 to n1
      L[i] = A[p + i - 1]
    for j = 1 to n2
      R[j] = A[q + j]
    L[n1 + 1] = infinity
    R[n2 + 1] = infinity
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

- The time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge operation takes O(n) time to combine the subarrays. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm creates auxiliary arrays of size n/2 at each level of recursion, and there are log n levels of recursion. Therefore, the total space is O(n).
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array. This is because the merge operation always chooses the element from the left subarray over the element from the right subarray when they are equal, thus maintaining their original order.
- Merge sort is not an in-place sorting algorithm, meaning that it requires extra space to store the auxiliary arrays. This can be a disadvantage when the array is large and memory is limited. However, there are variants of merge sort that can reduce the space complexity to O(1) by using clever techniques such as bitonic sorting or in-place merging.



# Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the value of its children (for a max heap) or less than or equal to the value of its children (for a min heap).
- Heap sort can be divided into two steps: heapify and extract.
- Heapify is the process of building a heap from an unsorted list. It can be done in linear time by starting from the last non-leaf node and sifting it down until it satisfies the heap property, and then repeating the same for all the preceding non-leaf nodes.
- Extract is the process of removing the root element of the heap (which is the maximum or minimum element depending on the type of heap) and replacing it with the last element of the heap, and then sifting it down until it satisfies the heap property. This is repeated until the heap is empty, and the extracted elements form a sorted list.
- Heap sort is an in-place algorithm, meaning it does not require extra space to sort the list. However, it is not a stable algorithm, meaning it does not preserve the relative order of equal elements.
- Heap sort has a worst-case, average-case and best-case time complexity of O(n log n), where n is the number of elements in the list. This is because heapify takes O(n) time and extract takes O(log n) time for each element. Heap sort is typically 2-3 times slower than well-implemented quick sort, due to the lack of locality of reference and the overhead of maintaining the heap structure.



# Comparison of Sorting Algorithms

Sorting algorithms are methods of arranging a list of elements in a certain order, such as ascending or descending. There are many different sorting algorithms, each with different advantages and disadvantages. Some of the factors that can be used to compare sorting algorithms are:

- Time complexity: how the running time of the algorithm grows as the input size increases.
- Space complexity: how much extra memory the algorithm requires to sort the list.
- Stability: whether the algorithm preserves the relative order of elements with equal keys.
- Comparison-based: whether the algorithm only compares elements with a comparison operator, or uses other information such as the range or distribution of the keys.

Some of the most commonly used sorting algorithms are:

- Shell sort: an improvement of insertion sort that uses gaps between elements to reduce the number of comparisons and shifts.
- Quick sort: a divide-and-conquer algorithm that partitions the list around a pivot element and recursively sorts the sublists.
- Merge sort: another divide-and-conquer algorithm that splits the list into two halves, recursively sorts them, and merges them back together.
- Heap sort: a selection sort that uses a binary heap data structure to efficiently find the largest or smallest element and place it at the end or the beginning of the list.
- Counting sort: a non-comparison-based algorithm that counts the number of occurrences of each key in the list and uses them to determine the final position of each element.
- Radix sort: another non-comparison-based algorithm that sorts the list by the digits or letters of the keys, starting from the least significant digit or letter and moving to the most significant one.

The following table summarizes the time and space complexities of these algorithms, as well as their stability and comparison-based properties. The time complexities are given in terms of the average case, the best case, and the worst case scenarios.

| Algorithm | Time complexity (average) | Time complexity (best) | Time complexity (worst) | Space complexity | Stable | Comparison-based |
|-----------|---------------------------|------------------------|-------------------------|------------------|--------|------------------|
| Shell sort | O(n^(3/2)) | O(n log n) | O(n^(3/2)) | O(1) | No | Yes |
| Quick sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | No | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Yes |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes | No |
| Radix sort | O(nk) | O(nk) | O(nk) | O(n + k) | Yes | No |

Here, n is the number of elements in the list, and k is the range or the number of digits of the keys.

Some of the advantages and disadvantages of these algorithms are:

- Shell sort: easy to implement, performs well on small or nearly sorted lists, but has a complex analysis and depends on the choice of gaps.
- Quick sort: fast and widely used, has a low space complexity, but has a poor performance on already sorted or nearly sorted lists, and is not stable.
- Merge sort: has a consistent and optimal time complexity, is stable, but has a high space complexity and requires extra memory for merging.
- Heap sort: has a consistent and optimal time complexity, does not require extra memory, but is not stable and performs poorly on cache memory.
- Counting sort: has a linear time complexity, is stable, but requires a large range of keys and extra memory for counting.
- Radix sort: has a linear time complexity, is stable, but requires a fixed length of keys and extra memory for sorting by digits or letters.



# Sorting in Linear Time

- Sorting in linear time means arranging a sequence of elements in a specific order in O(n) time, where n is the number of elements.
- Sorting in linear time is possible only when some special assumptions are made about the input sequence, such as the range of values, the distribution of elements, or the representation of data.
- Some examples of sorting algorithms that run in linear time are counting sort, radix sort, and bucket sort.

## Counting Sort

- Counting sort assumes that the input sequence consists of n integers in the range [0, k], where k is a small constant.
- Counting sort works by counting the number of occurrences of each integer in the input sequence, and then using those counts to determine the positions of each element in the sorted output sequence.
- Counting sort runs in O(n + k) time and O(n + k) space, where n is the number of elements and k is the range of values .

## Radix Sort

- Radix sort assumes that the input sequence consists of n d-digit numbers, where each digit is in the range [0, b-1], where b is the base of the number system.
- Radix sort works by sorting the input sequence by each digit, starting from the least significant digit to the most significant digit, using a stable sorting algorithm such as counting sort.
- Radix sort runs in O(d(n + b)) time and O(n + b) space, where n is the number of elements, d is the number of digits, and b is the base .

## Bucket Sort

- Bucket sort assumes that the input sequence consists of n real numbers that are uniformly distributed over the interval [0, 1).
- Bucket sort works by dividing the interval [0, 1) into n equal-sized buckets, and then distributing the input elements into the buckets according to their values. Then, each bucket is sorted individually using any comparison-based sorting algorithm, and the buckets are concatenated to form the sorted output sequence.
- Bucket sort runs in O(n) time on average and O(n) space, where n is the number of elements, but it can be as bad as O(n^2) in the worst case if all the elements fall into the same bucket .

: http://personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/linearTimeIntro.htm
: https://www.javatpoint.com/daa-linear-time-sorting
: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/bf7d79105762bf79bbc0925438e1468a_MIT6_006F11_lec07.pdf



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information on advanced data structures:

# Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

## Red-Black Trees

- A red-black tree is a type of self-balancing binary search tree, where each node has an extra bit that represents its color, either red or black.
- The color of the nodes is used to maintain the balance of the tree, by following some properties, such as:
  - Every node is either red or black.
  - The root and the leaves (NIL) are black.
  - If a node is red, then both its children are black.
  - Every simple path from a node to a descendant leaf has the same number of black nodes.
- The height of a red-black tree with n nodes is at most 2*log(n+1), which guarantees logarithmic time for search, insert, and delete operations.
- Red-black trees are widely used in applications that require efficient dynamic ordering, such as databases, maps, sets, etc.

## B-Trees

- A B-tree is a type of self-balancing multi-way search tree, where each node can have more than two children, and the data is stored in sorted order in the nodes.
- The number of children of a node is bounded by a parameter t, called the minimum degree of the tree, such that:
  - Every node, except the root, has at least t-1 keys and t children.
  - The root has at least one key and two children, unless it is a leaf.
  - Every node has at most 2t-1 keys and 2t children.
- The height of a B-tree with n keys and minimum degree t is at most log_t(n+1), which guarantees logarithmic time for search, insert, and delete operations.
- B-trees are widely used in applications that require efficient disk access, such as file systems, databases, indexing, etc.

## Binomial Heaps

- A binomial heap is a type of heap data structure, which is a collection of binomial trees that satisfy the heap property.
- A binomial tree of order k is a recursive structure, such that:
  - It has a root node with k children, where the i-th child is a binomial tree of order k-i-1, for i = 0, 1, ..., k-1.
  - The key of the root node is smaller than or equal to the keys of its children.
- A binomial heap is a set of binomial trees, such that:
  - There is at most one binomial tree of each order in the heap.
  - The key of the root node of each binomial tree is smaller than or equal to the keys of the roots of its siblings.
- The operations on a binomial heap, such as find-min, insert, merge, delete-min, and decrease-key, can be performed in logarithmic or constant time, by using some techniques, such as linking, union, and reverse.
- Binomial heaps are widely used in applications that require efficient priority queues, such as Dijkstra's algorithm, Prim's algorithm, etc.

## Fibonacci Heaps

- A Fibonacci heap is a type of heap data structure, which is an improvement over the binomial heap, by allowing some violations of the heap property.
- A Fibonacci heap is a collection of trees that satisfy the min-heap property, such that:
  - The key of a node is greater than or equal to the key of its parent.
  - The key of the root node of each tree is smaller than or equal to the keys of the roots of its siblings.
- A Fibonacci heap also maintains some additional information, such as:
  - The degree of each node, which is the number of its children.
  - The mark of each node, which is a boolean flag that indicates whether the node has lost a child since it became a child of another node.
  - The minimum node, which is a pointer to the root node with the smallest key in the heap.
- The operations on a Fibonacci heap, such as find-min, insert, merge, and decrease-key, can be performed in constant amortized time, by using some techniques, such as cascading cuts, consolidate, and potential function.
- The operations of delete and delete-min can be performed in logarith



# Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing**  , meaning that they can maintain a **logarithmic height** even after insertion and deletion operations .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**.
  - The root of the tree is always **black**.
  - Every leaf node (NIL) is **black**.
  - If a node is **red**, then both its children are **black**.
  - Every simple path from a node to a descendant leaf node has the same number of **black** nodes. This number is called the **black height** of the node.
- Red-black trees can be used to store and retrieve **ordered** data efficiently, such as text fragments or numbers.
- Red-black trees have a **guaranteed time complexity** of O(log n) for basic operations like insertion, deletion, and search .
- Red-black trees use a mechanism called **rotation** to restore the balance of the tree after insertion or deletion . Rotation is a local operation that changes the structure of the tree without affecting the order of the elements.
- Red-black trees can be used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - Implementing **associative arrays** or **maps**, such as the C++ STL map and set, and the Java TreeMap and TreeSet classes.
  - Implementing **priority queues**, such as the C++ STL priority_queue and the Java PriorityQueue class.
  - Implementing **interval trees**, which are used for storing and querying intervals or ranges of values.
  - Implementing **concurrent skip lists**, which are used for concurrent access and modification of ordered data structures.



# B-Trees

- A B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, insertions, and deletions in logarithmic time  .
- A B-tree is optimized for systems that read and write large blocks of data, such as database and file systems .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children. It is also known as a height-balanced m-way tree.
- A B-tree has the following properties  :
  - Every node has a maximum of m children, where m is the order of the tree.
  - Every node (except the root and the leaves) has a minimum of ⌈m/2⌉ children.
  - The root has a minimum of two children if it is not a leaf node.
  - All the leaves are at the same level, and they have no children.
  - Every non-leaf node has one more key than the number of its children. The keys are stored in sorted order.
- A B-tree supports the following operations  :
  - Search: To find a key in the tree, we start from the root and compare the key with the keys in the node. If the key is found, we return the node. If the key is smaller than the smallest key, we go to the leftmost child. If the key is larger than the largest key, we go to the rightmost child. Otherwise, we go to the child that corresponds to the interval of the keys that contains the key. We repeat this process until we find the key or reach a leaf node.
  - Insert: To insert a key in the tree, we first search for the key and find the leaf node where the key should be inserted. If the leaf node has less than m-1 keys, we simply insert the key in the correct position. If the leaf node is full, we split the node into two nodes and move the middle key to the parent node. We then check if the parent node is full, and repeat the splitting process until we reach a node that is not full or the root. If the root is full, we create a new root with the middle key and make the old root and the new node its children.
  - Delete: To delete a key from the tree, we first search for the key and find the node that contains the key. If the key is in a leaf node, we simply remove the key from the node. If the key is in a non-leaf node, we replace the key with its predecessor (the largest key in its left subtree) or its successor (the smallest key in its right subtree), and then delete the predecessor or the successor from the leaf node. After deleting the key, we check if the node has less than ⌈m/2⌉-1 keys, and if so, we perform a balancing operation to restore the B-tree properties. The balancing operation can be either borrowing a key from a sibling node or merging two sibling nodes and moving a key from the parent node. We then check if the parent node is underflow, and repeat the balancing process until we reach a node that is not underflow or the root. If the root has only one key and two children, we make the root the only child and delete the old root.



# Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- A binomial heap supports the following operations in amortized logarithmic time :
  - **insert**: add a new node to the heap
  - **getMin**: return the node with the minimum key in the heap
  - **extractMin**: remove and return the node with the minimum key in the heap
  - **decreaseKey**: decrease the key of a given node in the heap
  - **delete**: remove a given node from the heap
  - **union**: merge two binomial heaps into one
- The union operation is the key to the efficiency of binomial heaps. It can be done by merging the lists of binomial trees of the two heaps and then rearranging the trees to maintain the binomial heap properties .
- The following diagram shows an example of a binomial heap with 13 nodes and four binomial trees of orders 0, 1, 2, and 3:

```
      1
    / | \
   2  3  4
  /|  |
 5 6  7
/| |\
8 9 10 11
        |
        12
        |
        13
```



# Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees  .
- A Fibonacci heap is a collection of trees satisfying the **minimum-heap property**, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- Compared with binomial heaps, the structure of a Fibonacci heap is more flexible. It allows the trees to have any shape, even allowing trees to be single nodes.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- For the Fibonacci heap, the **find-minimum** operation takes constant (**O(1)**) amortized time. The **insert** and **decrease key** operations also work in constant amortized time  .
- The **delete** and **extract-minimum** operations take **O(log n)** amortized time, where **n** is the size of the heap  .
- Fibonacci heaps are used to implement the priority queue element in **Dijkstra’s algorithm** and **Prim's algorithm**, giving the algorithms a very efficient running time .
- Fibonacci heaps are also useful for applications that require frequent updates of key values, such as **network optimization** and **graph algorithms**.

: Fibonacci heap - Wikipedia
: Fibonacci Heap | Brilliant Math & Science Wiki
: Fibonacci Heap | Set 1 (Introduction) - GeeksforGeeks



# Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**TRIE**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has at most k children, and each child corresponds to a character of the alphabet.
- A trie can store any string over a finite alphabet, such as the English alphabet, ASCII characters, or binary digits.
- A trie can perform the following operations efficiently:
  - Insertion: To insert a string into a trie, we start from the root and follow the path corresponding to the characters of the string. If the path does not exist, we create new nodes along the way. We mark the last node as the end of the string.
  - Search: To search for a string in a trie, we start from the root and follow the path corresponding to the characters of the string. If the path exists and the last node is marked as the end of the string, we return true. Otherwise, we return false.
  - Prefix search: To search for all the strings that have a given prefix in a trie, we start from the root and follow the path corresponding to the prefix. If the path exists, we traverse the subtree rooted at the last node and collect all the strings that end at a marked node.
- A trie has the following advantages over a hash table:
  - A trie can handle collisions better than a hash table, as there is no need for hashing or rehashing.
  - A trie can support prefix search and pattern matching, which are not possible with a hash table.
  - A trie can save space by sharing common prefixes among strings, whereas a hash table requires a separate entry for each string.
- A trie has the following disadvantages compared to a hash table:
  - A trie may require more space than a hash table if the strings have few common prefixes or the alphabet is large.
  - A trie may require more time than a hash table to access a string if the string is long or the trie is deep.
  - A trie may be more complex to implement than a hash table.



# Skip List

A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis.  

## Basic Idea

- A skip list is composed of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one.
- The bottom layer contains all the elements of the sorted list, and the top layer contains only a few elements that act as shortcuts or entry points to the lower layers.
- Each element in a layer has a pointer to the next element in the same layer, and a pointer to the element below it in the lower layer.
- To search for an element in a skip list, we start from the top layer and follow the pointers until we find an element that is larger than or equal to the target element. Then, we move down to the lower layer and repeat the process until we reach the bottom layer, where we can find the exact element or determine that it does not exist in the list.
- To insert an element in a skip list, we first search for its position in the bottom layer, and then insert it there. Then, we toss a coin to decide whether to promote the element to the higher layer or not. If the coin lands on heads, we promote the element and repeat the coin toss for the next layer. If the coin lands on tails, we stop the promotion. This way, we ensure that each layer has a smaller number of elements than the previous one, and that the probability of an element being in a layer is inversely proportional to the layer number.
- To delete an element from a skip list, we first search for it in the bottom layer, and then delete it from there. Then, we delete it from all the higher layers where it appears, by updating the pointers of the previous and next elements in each layer.

## Advantages and Disadvantages

- Skip lists have the same asymptotic expected time complexity as balanced trees for search, insertion and deletion operations, which is O(log n), where n is the number of elements in the list.  
- Skip lists are simpler, faster and use less space than balanced trees, as they do not require any rotation or rebalancing operations. 
- Skip lists are easy to implement and modify, as they only require basic operations on linked lists. 
- Skip lists are suitable for concurrent applications, as they allow multiple threads to access and modify different parts of the list without locking or synchronization. 
- Skip lists are probabilistic data structures, meaning that their performance depends on the random choices made during insertion and promotion. This can lead to some worst-case scenarios, where the skip list becomes unbalanced or inefficient. However, these scenarios are very unlikely to occur, and can be avoided by using appropriate parameters and techniques.  
- Skip lists require extra space to store the pointers for each layer, which can be significant if the number of layers is large.  

## References

: Skip list - Wikipedia
: Skip List | Set 1 (Introduction) - GeeksforGeeks
: Skip List | Brilliant Math & Science Wiki
: The Skip List Data Structure | Baeldung on Computer Science



# Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

## Divide and Conquer

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the solution for the original problem  .
- Divide and conquer algorithms have three steps:
  - **Divide**: Split the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - **Conquer**: Solve the subproblems recursively, either directly or by applying the divide and conquer approach again.
  - **Combine**: Merge the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer algorithms are often efficient, as they reduce the problem size exponentially at each level of recursion, and they are suitable for parallel and distributed computing.
- Some examples of divide and conquer algorithms are:
  - **Binary search**: An algorithm that searches for a target value in a sorted array by repeatedly dividing the search interval in half and comparing the target with the middle element .
    - The algorithm can be implemented as follows:

    ```python
    # A recursive function that returns the index of the target value in the array, or -1 if not found
    def binary_search(array, low, high, target):
      # Base case: the search interval is empty
      if low > high:
        return -1
      
      # Find the middle index
      mid = (low + high) // 2
      
      # Compare the target with the middle element
      if target == array[mid]:
        # Found the target
        return mid
      elif target < array[mid]:
        # Target is in the left half
        return binary_search(array, low, mid - 1, target)
      else:
        # Target is in the right half
        return binary_search(array, mid + 1, high, target)
    ```
    - The time complexity of binary search is O(log n), where n is the size of the array, as the search interval is halved at each recursive call.
    - The space complexity of binary search is O(log n), as the maximum depth of the recursion tree is log n.
  - **Merge sort**: An algorithm that sorts an array by dividing it into two halves, sorting them recursively, and then merging the sorted halves .
    - The algorithm can be implemented as follows:

    ```python
    # A helper function that merges two sorted arrays into one sorted array
    def merge(array, low, mid, high):
      # Create temporary arrays to store the left and right halves
      left = array[low:mid + 1]
      right = array[mid + 1:high + 1]
      
      # Initialize indices for the left, right, and merged arrays
      i = 0
      j = 0
      k = low
      
      # Merge the elements from the left and right arrays in sorted order
      while i < len(left) and j < len(right):
        if left[i] <= right[j]:
          # Left element is smaller or equal
          array[k] = left[i]
          i += 1
        else:
          # Right element is smaller
          array[k] = right[j]
          j += 1
        k += 1
      
      # Copy the remaining elements from the left array, if any
      while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
      
      # Copy the remaining elements from the right array, if any
      while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    
    # A recursive function that sorts an array using merge sort
    def merge_sort(array, low, high):
      # Base case: the array has one or zero elements
      if low >= high:
        return
      
      # Find the middle index
      mid = (low + high) // 2
      
      # Sort the left and right halves recursively
      merge_sort(array, low, mid)
      merge_sort(array, mid + 1

```




# Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer  .
- Divide and conquer algorithms have three main steps: divide, conquer, and combine .
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, usually of the same type as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer technique again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure and properties .
- Some examples of divide and conquer algorithms are:
  - Sorting: Sorting algorithms such as merge sort and quicksort use divide and conquer to sort a list of elements by recursively dividing the list into smaller sublists, sorting them, and merging them .
  - Matrix multiplication: Matrix multiplication algorithms such as Strassen's algorithm use divide and conquer to multiply two matrices by recursively dividing them into smaller submatrices, multiplying them, and adding them .
  - Convex hull: Convex hull algorithms such as Graham scan and quickhull use divide and conquer to find the convex hull of a set of points by recursively dividing the points into smaller subsets, finding their convex hulls, and merging them.
  - Searching: Searching algorithms such as binary search and interpolation search use divide and conquer to find an element in a sorted list or array by recursively dividing the list or array into smaller sublists or subarrays, and comparing the element with the middle element of each sublist or subarray .



# Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps:
  - Divide: Split the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: Solve the subproblems recursively, either directly or by applying the divide and conquer approach again.
  - Combine: Merge the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient, as they reduce the problem size exponentially at each level of recursion, and they are suitable for parallel and distributed computing.
- Some examples of divide and conquer algorithms are:
  - Merge sort: A sorting algorithm that divides the array into two halves, sorts them recursively using merge sort, and then merges the two sorted halves into a final sorted array. The time complexity of merge sort is O(n log n), where n is the size of the array.
  - Binary search: A search algorithm that finds the position of a target value in a sorted array by repeatedly dividing the search interval in half and comparing the target with the middle element. The time complexity of binary search is O(log n), where n is the size of the array.
  - Strassen's algorithm: A matrix multiplication algorithm that divides each matrix into four submatrices of equal size, and then recursively computes seven matrix multiplications and four matrix additions to obtain the product matrix. The time complexity of Strassen's algorithm is O(n^2.8074), where n is the dimension of the matrices.
  - Fast Fourier transform: A mathematical algorithm that computes the discrete Fourier transform of a sequence of complex numbers by dividing the sequence into two subsequences of even and odd indices, and then recursively applying the fast Fourier transform on them. The time complexity of the fast Fourier transform is O(n log n), where n is the size of the sequence.



# Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by recursively breaking it into smaller subproblems of the same type, until they become simple enough to be solved directly.
- The solutions of the subproblems are then combined to give a solution to the original problem.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
- Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same size and structure.
- Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
- Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the problem size exponentially and exploit the subproblem structure.
- Some examples of divide and conquer algorithms are:

## Merge Sort
- Merge sort is a sorting algorithm that sorts an array of n elements by recursively dividing it into two halves, sorting each half, and then merging the two sorted halves.
- The divide step splits the array into two subarrays of roughly equal size.
- The conquer step sorts each subarray recursively using merge sort.
- The combine step merges the two sorted subarrays into one sorted array using a linear-time merging procedure.
- Merge sort has a time complexity of O(n log n) and a space complexity of O(n) in the worst case.
- Merge sort is stable, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is an example of a divide and conquer algorithm that uses a balanced divide, where the subproblems have the same size, and a trivial combine, where the subproblem solutions are simply concatenated.

## Binary Search
- Binary search is a search algorithm that finds the position of a target value within a sorted array of n elements by repeatedly comparing the target value with the middle element of the array and discarding half of the array based on the comparison result.
- The divide step reduces the search space to either the left or the right half of the current array, depending on whether the target value is smaller or larger than the middle element, respectively.
- The conquer step checks if the middle element is equal to the target value, and if so, returns its position. Otherwise, it recursively applies binary search to the remaining half of the array.
- The combine step is trivial, as there is nothing to merge or combine.
- Binary search has a time complexity of O(log n) and a space complexity of O(1) in the worst case.
- Binary search is an example of a divide and conquer algorithm that uses an unbalanced divide, where the subproblems have different sizes, and a trivial combine, where the subproblem solutions are simply returned.

## Convex Hull
- Convex hull is a geometric problem that finds the smallest convex polygon that contains a given set of n points in the plane.
- A convex polygon is a polygon whose interior angles are all less than 180 degrees, and a point is contained in a polygon if it lies on the boundary or in the interior of the polygon.
- The divide step partitions the set of points into two subsets by drawing a vertical line through the median x-coordinate of the points.
- The conquer step recursively computes the convex hull of each subset using the same algorithm.
- The combine step merges the two convex hulls into one convex hull using a linear-time merging procedure that discards the points that are not part of the final convex hull.
- The merging procedure works by finding the upper and lower tangent lines that connect the two convex hulls, and removing the points that lie below the upper tangent line or above the lower tangent line.
- Convex hull has a time complexity of O(n log n) and a space complexity of O(n) in the worst case.
- Convex hull is an example of a divide and conquer algorithm that uses a balanced divide, where the subproblems have the same size, and a non-trivial combine, where the subproblem solutions are merged using a sophisticated procedure.



# Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

Divide and conquer is a powerful algorithmic paradigm that can solve many problems efficiently. The basic idea is to break a large problem into smaller subproblems, solve them recursively, and combine the solutions to get the final answer. Some of the advantages of divide and conquer are:

- It can reduce the time complexity of some problems from polynomial to logarithmic, such as sorting, searching, and matrix multiplication.
- It can exploit the parallelism of some problems, such as sorting and matrix multiplication, by dividing the work among multiple processors or threads.
- It can simplify the design and implementation of some algorithms, such as quicksort and mergesort, by using recursion and divide-and-conquer.

Some of the examples of divide and conquer algorithms are:

- **Sorting**: Sorting is the problem of arranging a list of elements in a certain order, such as ascending or descending. There are many sorting algorithms that use divide and conquer, such as quicksort, mergesort, and heapsort. Quicksort, for example, chooses a pivot element from the list, partitions the list into two sublists such that all the elements in the left sublist are smaller than the pivot and all the elements in the right sublist are larger than the pivot, and then recursively sorts the two sublists. The time complexity of quicksort is O(n log n) on average, where n is the number of elements in the list.
- **Matrix multiplication**: Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and producing a third matrix as the result. A naive algorithm for matrix multiplication would take O(n^3) time, where n is the dimension of the matrices. However, using divide and conquer, we can reduce the time complexity to O(n^2.8074) using Strassen's algorithm, or even lower using other algorithms. Strassen's algorithm, for example, divides each matrix into four submatrices of equal size, performs seven multiplications and ten additions on the submatrices, and then combines the results to get the final matrix.
- **Convex hull**: Convex hull is the problem of finding the smallest convex polygon that contains a set of points in the plane. A naive algorithm for convex hull would take O(n^3) time, where n is the number of points. However, using divide and conquer, we can reduce the time complexity to O(n log n) using Graham's scan algorithm, or even lower using other algorithms. Graham's scan algorithm, for example, sorts the points by their polar angle with respect to a reference point, and then scans the points in a counterclockwise order, maintaining a stack of points that form the convex hull so far, and discarding the points that would make the hull concave.
- **Searching**: Searching is the problem of finding an element in a list or a data structure that satisfies a certain condition, such as equality or comparison. There are many searching algorithms that use divide and conquer, such as binary search, interpolation search, and exponential search. Binary search, for example, searches for an element in a sorted list by repeatedly halving the search interval and comparing the middle element with the target. The time complexity of binary search is O(log n), where n is the number of elements in the list.



# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

## Optimal Substructure
A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For example, the shortest path problem has optimal substructure, because the shortest path from A to B consists of the shortest path from A to some intermediate point C and the shortest path from C to B.

## Greedy Choice Property
A problem has the greedy choice property if a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. For example, the fractional knapsack problem has the greedy choice property, because the optimal solution can be obtained by choosing the item with the highest value per unit weight at each step.

## Examples of Greedy Methods

### Optimal Reliability Allocation
The optimal reliability allocation problem is to allocate a given budget to improve the reliability of a system consisting of n components. The objective is to maximize the overall system reliability, which is the probability that all components function properly. The reliability of each component can be improved by investing some amount of money, but the marginal benefit decreases as the reliability increases. The problem can be solved by a greedy method that allocates the budget to the component with the highest marginal benefit at each step.

### Knapsack Problem
The knapsack problem is to fill a knapsack with a given capacity with items that have different weights and values. The objective is to maximize the total value of the items in the knapsack. There are two variants of the problem: the 0-1 knapsack problem, where each item can be either taken or left, and the fractional knapsack problem, where each item can be taken partially. The 0-1 knapsack problem cannot be solved by a greedy method, but the fractional knapsack problem can be solved by choosing the item with the highest value per unit weight at each step.

### Minimum Spanning Tree
The minimum spanning tree problem is to find a subset of edges in a weighted undirected graph that connects all the vertices and has the minimum total weight. The problem can be solved by two greedy methods: Prim's algorithm and Kruskal's algorithm. Prim's algorithm starts with an arbitrary vertex and adds the edge with the minimum weight that connects a vertex in the tree to a vertex outside the tree at each step. Kruskal's algorithm sorts the edges by weight and adds the edge with the minimum weight that does not create a cycle at each step.

### Single Source Shortest Path
The single source shortest path problem is to find the shortest path from a given source vertex to every other vertex in a weighted directed graph. The problem can be solved by two greedy methods: Dijkstra's algorithm and Bellman-Ford algorithm. Dijkstra's algorithm maintains a set of vertices whose shortest distance from the source is known and adds the vertex with the minimum distance to the set at each step. Bellman-Ford algorithm relaxes the distance of each edge at each iteration and repeats the process n-1 times, where n is the number of vertices.



# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

## Optimal Substructure
A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For example, the shortest path problem has optimal substructure, because the shortest path from A to B consists of the shortest path from A to some intermediate point C and the shortest path from C to B.

## Greedy Choice Property
A problem has the greedy choice property if a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. For example, the fractional knapsack problem has the greedy choice property, because the optimal solution can be obtained by choosing the item with the highest value per unit weight at each step.

## Examples of Greedy Methods

### Fractional Knapsack Problem
Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, determine the maximum value that can be obtained by filling the knapsack with a fraction of each item. The fractional knapsack problem can be solved by a greedy method as follows:

- Sort the items in decreasing order of their value per unit weight.
- Initialize the total value to zero and the remaining capacity to the maximum capacity.
- For each item in the sorted order, do the following:
  - If the item's weight is less than or equal to the remaining capacity, then take the whole item and add its value to the total value. Subtract its weight from the remaining capacity.
  - If the item's weight is more than the remaining capacity, then take a fraction of the item that fills the remaining capacity. Add the fraction of the item's value to the total value. Set the remaining capacity to zero.
  - If the remaining capacity is zero, then stop.

### Minimum Spanning Tree
Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. A minimum spanning tree (MST) is such a subset of edges. The minimum spanning tree problem can be solved by two greedy methods: Prim's algorithm and Kruskal's algorithm.

#### Prim's Algorithm
Prim's algorithm starts with an arbitrary vertex and grows the MST one edge at a time. At each step, it adds the minimum weight edge that connects a vertex in the MST to a vertex not in the MST. Prim's algorithm can be implemented as follows:

- Initialize the MST to an empty set and the set of visited vertices to contain the arbitrary vertex.
- While there are still unvisited vertices, do the following:
  - Find the minimum weight edge that connects a visited vertex to an unvisited vertex. Add this edge to the MST and the unvisited vertex to the set of visited vertices.

#### Kruskal's Algorithm
Kruskal's algorithm starts with an empty MST and adds edges one by one in increasing order of weight. At each step, it adds the minimum weight edge that does not create a cycle in the MST. Kruskal's algorithm can be implemented as follows:

- Sort the edges in increasing order of weight.
- Initialize the MST to an empty set and a disjoint-set data structure to contain each vertex as a separate set.
- For each edge in the sorted order, do the following:
  - If the edge connects two vertices that belong to different sets, then add this edge to the MST and union the two sets.

### Single Source Shortest Path
Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex in the graph. The single source shortest path problem can be solved by two greedy methods: Dijkstra's algorithm and Bellman-Ford algorithm.

#### Dijkstra's Algorithm
Dijkstra's algorithm maintains a set of visited vertices and a priority queue of unvisited vertices with their distances from the source. At each step, it extracts the minimum distance vertex from the priority queue and adds it to the set of visited vertices. Then, it relaxes the edges outgoing from the extracted vertex, updating the distances and the priority queue. Dijkstra's algorithm can be implemented as follows:

- Initialize the distance of the source vertex to zero and the distance of every other vertex to infinity. Initialize the set of visited vertices to an empty set and the priority queue of unvisited vertices to contain all the vertices with their



# Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast, and easy to implement, but they may not always yield the best solution.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: An optimal solution to the problem contains optimal solutions to the subproblems.
  - Greedy choice property: A locally optimal choice is always part of an optimal solution.
- One example of a problem that can be solved by greedy methods is the minimum spanning tree (MST) problem.
  - A spanning tree of a graph G is a subset of the edges of G that form a tree and include all vertices of G.
  - A minimum spanning tree of a graph G is a spanning tree of G that has the minimum total weight among all spanning trees of G.
  - The MST problem has both optimal substructure and greedy choice property, as proved by the cut property and the cycle property.
- There are several greedy algorithms for finding MSTs, such as Prim's algorithm and Kruskal's algorithm.
  - Prim's algorithm starts with a single node and keeps adding the cheapest edge that connects a node in the tree to a node outside the tree, until all nodes are included.
  - Kruskal's algorithm starts with an empty set of edges and keeps adding the cheapest edge that does not create a cycle, until all nodes are connected.
  - Both algorithms have a time complexity of O(E log V), where E is the number of edges and V is the number of vertices in the graph.
  - Both algorithms can be implemented using a priority queue and a disjoint-set data structure.



# Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

## Introduction

- Greedy methods are a class of algorithms that make a series of local, optimal choices to find a global, optimal solution.
- Greedy methods do not consider the future consequences of their choices, and may end up with a suboptimal solution in some cases.
- Greedy methods are usually easy to implement and have low time complexity, but they require a proof of correctness and optimality.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: The optimal solution to the problem can be obtained by combining the optimal solutions to its subproblems.
  - Greedy choice property: There is a locally optimal choice that leads to the globally optimal solution, and this choice can be made without considering the subproblems.
  - Matroid: A mathematical structure that captures the notion of independence and exchangeability of subsets.

## Examples

### Single Source Shortest Paths - Dijkstra’s Algorithm

- The problem of finding the shortest paths from a single source vertex to all other vertices in a weighted, directed graph.
- Dijkstra’s algorithm is a greedy method that maintains a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined.
- The algorithm repeatedly extracts the vertex with the minimum distance from the source from the priority queue, and updates the distances of its adjacent vertices.
- The algorithm terminates when the priority queue is empty or the destination vertex is extracted.
- Dijkstra’s algorithm is correct and optimal because it always chooses the vertex with the minimum distance from the source, which is the greedy choice that leads to the shortest path.
- Dijkstra’s algorithm has a time complexity of O((V+E) log V), where V is the number of vertices and E is the number of edges in the graph, using a binary heap as the priority queue.

### Single Source Shortest Paths - Bellman Ford Algorithm

- The problem of finding the shortest paths from a single source vertex to all other vertices in a weighted, directed graph that may contain negative edge weights, but no negative cycles.
- Bellman Ford algorithm is a dynamic programming method that relaxes all the edges of the graph V-1 times, where V is the number of vertices in the graph.
- Relaxing an edge means updating the distance of the destination vertex if it can be reduced by going through the source vertex and the edge weight.
- Bellman Ford algorithm is correct and optimal because it guarantees that after V-1 iterations, the distance of any vertex is equal to the length of the shortest path from the source, or infinity if there is no such path.
- Bellman Ford algorithm has a time complexity of O(VE), where V is the number of vertices and E is the number of edges in the graph.



## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure. It works by breaking down the problem into smaller subproblems, solving them once and storing their solutions in a table, and then using the table to construct the optimal solution for the original problem.
- Knapsack problem is an example of dynamic programming. It is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the items in the knapsack is maximized. The dynamic programming solution for this problem is to define a function `f(i, w)` that returns the maximum value that can be obtained by packing items from `1` to `i` into a knapsack with capacity `w`. The function can be computed recursively as follows:

  - Base case: `f(0, w) = 0` for any `w`.
  - Recursive case: `f(i, w) = max(f(i-1, w), f(i-1, w-wi) + vi)` for any `i` and `w`, where `wi` and `vi` are the weight and value of item `i`, respectively. The first term in the max function represents the case of not including item `i` in the knapsack, and the second term represents the case of including item `i` in the knapsack, if possible.
  - The optimal value for the problem is `f(n, W)`, where `n` is the number of items and `W` is the capacity of the knapsack.

- All pair shortest paths problem is another example of dynamic programming. It is a problem of finding the shortest distance between every pair of vertices in a weighted graph. There are two algorithms for solving this problem using dynamic programming: Warshal's algorithm and Floyd's algorithm. Both algorithms use a matrix `D` to store the shortest distances between vertices, and update the matrix iteratively using the following formula:

  - `D(k)[i][j] = min(D(k-1)[i][j], D(k-1)[i][k] + D(k-1)[k][j])` for any `i`, `j`, and `k`, where `D(k)[i][j]` is the shortest distance between vertices `i` and `j` using only vertices from `1` to `k` as intermediate vertices.
  - The difference between Warshal's algorithm and Floyd's algorithm is the order of updating the matrix. Warshal's algorithm updates the matrix row by row, while Floyd's algorithm updates the matrix in a diagonal fashion. Both algorithms have a time complexity of `O(n^3)`, where `n` is the number of vertices in the graph.

- Resource allocation problem is a problem of allocating a limited amount of resources among a number of competing activities, such that the total profit or benefit is maximized. The dynamic programming solution for this problem is to define a function `g(i, r)` that returns the maximum profit that can be obtained by allocating `r` units of resources to activities from `1` to `i`. The function can be computed recursively as follows:

  - Base case: `g(0, r) = 0` for any `r`.
  - Recursive case: `g(i, r) = max(g(i-1, r), g(i-1, r-ri) + pi)` for any `i` and `r`, where `ri` and `pi` are the resource requirement and profit of activity `i`, respectively. The first term in the max function represents the case of not allocating resources to activity `i`, and the second term represents the case of allocating resources to activity `i`, if possible.
  - The optimal value for the problem is `g(m, R)`, where `m` is the number of activities and `R` is the total amount of resources available.

- Backtracking is a technique for solving problems that involve searching for a solution among a large number of possibilities. It works by exploring the solution space in a depth-first manner, and pruning the branches that do not lead to a feasible or optimal solution. Backtracking can be implemented using recursion or a stack.
- Travelling salesman problem is an example of backtracking. It is a problem of finding the shortest tour that visits every city in a given set of



# Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be divided into smaller subproblems of the same type, such as the knapsack problem, the longest common subsequence problem, the matrix chain multiplication problem, etc.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the results in a table or an array.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. The top-down approach starts from the original problem and recursively solves the subproblems, while the bottom-up approach starts from the base cases and iteratively builds up the solution.

## Knapsack Problem

- The knapsack problem is a classic example of a problem that can be solved using dynamic programming. The problem statement is as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.

- There are two variants of the knapsack problem: the 0/1 knapsack problem and the fractional knapsack problem. The 0/1 knapsack problem only allows to include or exclude an item, while the fractional knapsack problem allows to include a fraction of an item.

- The 0/1 knapsack problem can be solved using dynamic programming by defining a table K[i][j] that stores the maximum value that can be obtained by using items from 1 to i with a weight limit of j. The table can be filled using the following recurrence relation:

  - K[i][j] = max(K[i-1][j], K[i-1][j-w[i]] + v[i]) if w[i] <= j
  - K[i][j] = K[i-1][j] if w[i] > j

  where w[i] and v[i] are the weight and value of the ith item, respectively.

- The time and space complexity of this algorithm is O(nW), where n is the number of items and W is the weight limit.

- The fractional knapsack problem can be solved using a greedy approach by sorting the items in decreasing order of their value per unit weight, and then selecting the items in that order until the weight limit is reached or all the items are exhausted. The time complexity of this algorithm is O(n log n), where n is the number of items.



Hello, I am Sydney, your AI assistant. I can help you with your topic of dynamic programming with examples such as all pair shortest paths, Warshal's and Floyd's algorithms, resource allocation problem, etc. Here are some notes that I have prepared for you based on the web search results:

# Dynamic Programming with Examples

## What is Dynamic Programming?

- Dynamic programming is a technique of solving complex problems by breaking them down into smaller subproblems and reusing the solutions of the subproblems to avoid repeated computations .
- Dynamic programming can be applied to problems that have two main characteristics: optimal substructure and overlapping subproblems.
- Optimal substructure means that the optimal solution of a problem can be obtained by using the optimal solutions of its subproblems.
- Overlapping subproblems means that the same subproblems are encountered multiple times while solving the problem.
- Dynamic programming can be implemented using two approaches: top-down (memoization) or bottom-up (tabulation).
- Top-down approach involves starting from the original problem and recursively solving the subproblems, while storing the results of the subproblems in a data structure (such as an array or a map) to avoid recomputation.
- Bottom-up approach involves starting from the base cases (the smallest subproblems) and iteratively building up the solutions of larger subproblems using the results of the smaller ones.

## Examples of Dynamic Programming Problems

### Fibonacci Sequence

- The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
- The Fibonacci sequence can be defined recursively as:

  - F(0) = 0
  - F(1) = 1
  - F(n) = F(n-1) + F(n-2) for n > 1

- The Fibonacci sequence is an example of a problem that has optimal substructure and overlapping subproblems, and can be solved using dynamic programming.
- A naive recursive solution would involve calling the same function multiple times with the same arguments, leading to exponential time complexity.
- A dynamic programming solution would involve storing the results of the subproblems in an array and using them to calculate the results of larger subproblems, leading to linear time complexity.

### Knapsack Problem

- The knapsack problem is a problem of finding the maximum value of items that can be packed into a knapsack with a given weight capacity.
- The knapsack problem can be defined as:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
  - The items are indivisible, meaning that they cannot be split or fractioned.

- The knapsack problem is an example of a problem that has optimal substructure and overlapping subproblems, and can be solved using dynamic programming.
- A naive recursive solution would involve trying all possible combinations of items and selecting the one with the maximum value, leading to exponential time complexity.
- A dynamic programming solution would involve using a two-dimensional array to store the maximum value that can be obtained for each subproblem (i.e., each combination of items and weight capacity), and using them to calculate the results of larger subproblems, leading to polynomial time complexity.

### All Pair Shortest Paths

- The all pair shortest paths problem is a problem of finding the shortest distances between every pair of vertices in a weighted graph.
- The all pair shortest paths problem can be defined as:

  - Given a weighted graph G = (V, E), where V is the set of vertices, E is the set of edges, and each edge has a weight w(u, v) representing the distance between vertices u and v, find the shortest distance d(u, v) for every pair of vertices u and v in V.
  - The graph may or may not contain negative edge weights, but it should not contain negative cycles (i.e., cycles whose total weight is negative).

- The all pair shortest paths problem is an example of a problem that has optimal substructure and overlapping subproblems, and can be solved using dynamic programming.
- Two common dynamic programming algorithms for solving the all pair shortest paths problem are Warshal's algorithm and Floyd's algorithm.
- Warshal's algorithm is



# Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can be implemented using either a top-down (memoization) or a bottom-up (tabulation) approach.
- A common example of a dynamic programming problem is the knapsack problem, where we have a set of items, each with a weight and a value, and we want to find the maximum value we can obtain by choosing a subset of items that fit in a knapsack with a given capacity.
- Another example of a dynamic programming problem is the resource allocation problem, where we have a set of resources and a set of activities, and we want to find the optimal way to allocate the resources to the activities to maximize the total return.
- The resource allocation problem can be formulated as follows:

  - Let N be the number of activities, and let X be the total amount of resources available.
  - Let x_k be the amount of resources allocated to activity k, and let r_k(x_k) be the return function of activity k, which gives the return from allocating x_k units of resources to activity k.
  - The objective is to maximize the total return, R(x_1, x_2, ..., x_N) = r_1(x_1) + r_2(x_2) + ... + r_N(x_N), subject to the constraint that the sum of the allocated resources does not exceed the total amount available, x_1 + x_2 + ... + x_N <= X.
  - The problem can be solved using dynamic programming by defining a subproblem as follows:

    - Let R_k(x) be the maximum return that can be obtained by optimally allocating x units of resources to the first k activities, 1 <= k <= N.
    - The base case is R_1(x) = r_1(x) for 0 <= x <= X, since there is only one activity to allocate resources to.
    - The recursive case is R_k(x) = max{R_k-1(x), R_k-1(x - x_k) + r_k(x_k)} for 1 < k <= N and 0 <= x <= X, since we can either not allocate any resources to activity k, or allocate x_k units of resources to activity k and the remaining x - x_k units to the first k - 1 activities.
    - The optimal solution is R_N(X), which gives the maximum return from allocating X units of resources to N activities.
    - The optimal allocation can be obtained by tracing back the decisions made at each stage of the recursion.

- A numerical example of the resource allocation problem is as follows:

  - Suppose there are three activities, A, B, and C, and 10 units of resources available.
  - The return functions of the activities are:

    - r_A(x) = 10x - x^2 for 0 <= x <= 10
    - r_B(x) = 12x - x^2 for 0 <= x <= 12
    - r_C(x) = 15x - x^2 for 0 <= x <= 15

  - The dynamic programming table for this problem is shown below, where each cell contains the value of R_k(x) and the corresponding allocation to activity k.

| x \ k | 1 (A) | 2 (B) | 3 (C) |
| ----- | ----- | ----- | ----- |
| 0     | 0 (0) | 0 (0) | 0 (0) |
| 1     | 9 (1) | 11 (1) | 14 (1) |
| 2     | 16 (2) | 20 (2) | 26 (2) |
| 3     | 21 (3) | 27 (3) | 36 (3) |
| 4     | 24 (4) | 32 (4) | 44 (4) |
| 5     | 25 (5) | 35 (5) | 50 (5) |
| 6     | 24 (6) | 36 (6) | 54 (6) |
| 7     | 21 (7



# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a large space of possible solutions. They both use a state-space tree to represent the partial and complete solutions, and they both use a bounding function to prune the tree and eliminate suboptimal or infeasible solutions. However, they differ in the way they explore the tree and the type of problems they can solve.

## Backtracking

Backtracking is an algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Backtracking uses a depth-first search (DFS) method to traverse the state-space tree. When the algorithm begins to explore a solution, it applies a bounding function to check whether the current partial solution satisfies the constraints of the problem. If not, the algorithm backtracks to the previous level and tries another branch. If yes, the algorithm continues to extend the partial solution until it reaches a complete solution or a dead end.

Backtracking can be used to solve problems such as:

- Sudoku
- N-queens
- Hamiltonian cycle
- Graph coloring
- Subset sum
- Cryptarithmetic

## Branch and Bound

Branch and bound is an algorithm for discrete and combinatorial optimization problems and mathematical optimization. It can be used to find optimal solutions (such as minimum or maximum) or to find whether a feasible solution exists.

Branch and bound uses a best-first search (BFS) method to traverse the state-space tree. When the algorithm begins to explore a solution, it applies a bounding function to estimate the lower and upper bounds of the objective function for the current partial solution. If the lower bound is greater than the current best solution, the algorithm prunes the branch and does not explore it further. If the upper bound is less than the current best solution, the algorithm updates the best solution and continues to explore the branch. The algorithm terminates when all branches are pruned or explored.

Branch and bound can be used to solve problems such as:

- 0/1 knapsack
- Travelling salesman
- Job scheduling
- Facility location
- Linear programming

## Examples

### Travelling Salesman Problem

The travelling salesman problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the origin city. It is an NP-hard problem, meaning that there is no known polynomial-time algorithm to solve it exactly.

One way to solve the TSP using branch and bound is to use a minimum spanning tree (MST) as a bounding function. A MST is a subset of edges that connects all the vertices in a graph with the minimum possible total edge weight. A MST can be computed in polynomial time using algorithms such as Prim's or Kruskal's.

The idea is to construct a state-space tree where each node represents a partial tour, and each edge represents the inclusion or exclusion of a city in the tour. The root node represents an empty tour, and the leaf nodes represent complete tours. The algorithm starts from the root node and explores the tree using BFS. For each node, the algorithm computes the lower bound of the tour cost by adding the cost of the partial tour, the cost of the MST of the remaining cities, and the cost of the two edges that connect the partial tour to the MST. If the lower bound is greater than the current best tour cost, the node is pruned. Otherwise, the node is expanded by adding or excluding the next city in the tour. The algorithm updates the best tour cost whenever it finds a complete tour that is better than the current best tour. The algorithm terminates when all nodes are pruned or explored.

The following figure shows an example of the state-space tree for a TSP with four cities A, B, C, and D, and the corresponding MSTs and lower bounds for each node.

TSP example

The optimal tour is A-B-C-D-A with a cost of 10 + 25 + 30 + 15 = 80.



# Backtracking, Branch and Bound with Examples Such as Graph Coloring

Backtracking and branch and bound are two techniques for solving optimization problems that involve searching a finite set of possible solutions. Both techniques use a recursive approach to explore the solution space in a systematic way, but they differ in how they prune the search tree and how they determine the optimal solution.

## Backtracking

Backtracking is a technique that tries to find a feasible solution to a problem by incrementally building a partial solution and then backtracking (undoing) the last decision if it leads to a dead end. Backtracking is often used for solving constraint satisfaction problems, such as sudoku, crossword puzzles, n-queens problem, etc.

The general algorithm for backtracking is as follows:

- Start with an empty partial solution.
- Choose a decision point and try all possible choices for it.
- For each choice, check if it is consistent with the constraints of the problem. If yes, add it to the partial solution and recursively explore the remaining decision points. If no, discard it and try another choice.
- If all decision points are explored and a feasible solution is found, return it. Otherwise, backtrack to the previous decision point and try another choice.
- If no feasible solution is found after trying all possible choices at all decision points, return failure.

The main advantage of backtracking is that it can find all possible solutions to a problem, or prove that none exists. The main disadvantage is that it can be very inefficient, as it may explore a large number of suboptimal or infeasible solutions before finding a good one or giving up.

## Branch and Bound

Branch and bound is a technique that tries to find an optimal solution to a problem by maintaining a lower bound and an upper bound on the objective function value. Branch and bound is often used for solving combinatorial optimization problems, such as travelling salesman problem, knapsack problem, graph coloring problem, etc.

The general algorithm for branch and bound is as follows:

- Start with an empty partial solution and an initial lower bound and upper bound on the objective function value.
- Choose a branching variable and split the solution space into two or more subproblems based on the possible values of the variable.
- For each subproblem, calculate a lower bound and an upper bound on the objective function value using some heuristic or relaxation method. If the lower bound is greater than or equal to the current upper bound, prune the subproblem as it cannot lead to a better solution. If the upper bound is less than the current upper bound, update the upper bound and the best solution found so far. If the lower bound is equal to the upper bound, the subproblem is solved optimally and no further branching is needed.
- Recursively explore the remaining subproblems using the same procedure, until all subproblems are either pruned or solved optimally.
- Return the best solution found or report that the problem is infeasible.

The main advantage of branch and bound is that it can find the optimal solution to a problem, or prove that none exists. The main disadvantage is that it can be very memory-intensive, as it may need to store a large number of subproblems in a queue or a stack.

## Graph Coloring Problem

Graph coloring is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. The minimum number of colors needed to color a graph is called its chromatic number. Graph coloring has applications in scheduling, map coloring, register allocation, etc.

Graph coloring can be solved using both backtracking and branch and bound techniques. The following are some examples of how to apply these techniques to the graph coloring problem.

### Backtracking for Graph Coloring

One way to use backtracking for graph coloring is to assign colors to the vertices one by one, starting from an arbitrary vertex. For each vertex, try all possible colors that are not already used by its adjacent vertices. If a color is consistent, add it to the partial solution and recursively explore the next vertex. If no color is consistent, backtrack to the previous vertex and try another color. If all vertices are colored, return the solution. Otherwise, return failure.

The pseudocode for this algorithm is as follows:

```python
# Input: A graph G with n vertices and m colors
# Output: A coloring of G with m colors or failure

def backtrack(G, n, m):
  # Initialize an array to store the colors of the vertices
  colors = [0] * n
  
  # Start from the first vertex
  if backtrack_helper(G, n, m, colors, 0):
    # If a solution is found,

```




# Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be viewed as a depth-first search of a state space tree, where each node represents a partial solution, and the branches are the possible extensions of the solution. 
- Backtracking can be applied to problems that can be formulated as finding a path from the root to a leaf node in a state space tree, where each leaf node is a possible solution. 
- Backtracking can be implemented using recursion or iteration, with the help of a stack to store the partial solutions. 
- Backtracking can be optimized by using heuristics, pruning, and memoization techniques to reduce the size of the search space and avoid repeated computations. 

## Example: n-Queen Problem

- The n-queen problem is a classic example of a constraint satisfaction problem, where the goal is to place n queens on an n x n chessboard, such that no two queens can attack each other. 
- A queen can attack another queen if they are on the same row, column, or diagonal. 
- A possible solution to the n-queen problem is a configuration of n queens on the board, where none of them can attack each other. 
- A partial solution to the n-queen problem is a configuration of k queens on the board, where k < n, and none of them can attack each other. 
- A partial solution can be extended by placing a queen on an empty row, and checking if it is safe to do so, i.e., it does not conflict with any of the existing queens. 
- If a partial solution cannot be extended, then it is rejected, and the algorithm backtracks to the previous partial solution, and tries a different extension. 
- If a partial solution can be extended to a complete solution, then it is outputted as a valid solution. 
- The algorithm terminates when all possible extensions have been explored, or when a desired number of solutions have been found. 

### Pseudocode

```
procedure nQueen(n)
  create an empty stack S
  push the empty board configuration to S
  while S is not empty
    pop the top configuration C from S
    if C is a complete solution
      output C
    else
      for each possible extension E of C
        if E is safe
          push E to S
```

### Example

- Suppose we want to find one solution to the 4-queen problem. 
- We start with an empty board configuration, and push it to the stack. 
- We pop the top configuration from the stack, and try to extend it by placing a queen on the first row. 
- We have four possible extensions, one for each column. We check if each extension is safe, i.e., it does not conflict with any existing queen. 
- We find that the extension with the queen on the first column is safe, so we push it to the stack. 
- We pop the top configuration from the stack, and try to extend it by placing a queen on the second row. 
- We have four possible extensions, one for each column. We check if each extension is safe, i.e., it does not conflict with any existing queen. 
- We find that the extension with the queen on the fourth column is safe, so we push it to the stack. 
- We pop the top configuration from the stack, and try to extend it by placing a queen on the third row. 
- We have four possible extensions, one for each column. We check if each extension is safe, i.e., it does not conflict with any existing queen. 
- We



# Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be viewed as a way of traversing a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem.
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

- The procedure `backtrack` takes two arguments: a problem instance `P` and a candidate `c`. The procedure `reject` tests whether the candidate is worth completing, and returns true if it is not. The procedure `accept` tests whether the candidate is a solution, and returns true if it is. The procedure `output` processes the solution in some way. The procedure `first` generates the first extension of the candidate, and `next` generates the next alternative extension after a given one. If there are no more extensions, `next` returns NULL.
- A common example of a problem that can be solved by backtracking is the Hamiltonian cycle problem, which is to find a cycle in a graph that visits every vertex exactly once. A possible backtracking algorithm for this problem is as follows:

```
procedure hamiltonian(G, v) is
    if v is the first vertex then
        mark v as visited
        add v to the cycle
    if all vertices are visited then
        if there is an edge from v to the first vertex then
            output the cycle
        else
            return
    for each neighbor u of v do
        if u is not visited then
            mark u as visited
            add u to the cycle
            hamiltonian(G, u)
            remove u from the cycle
            mark u as unvisited
```

- The procedure `hamiltonian` takes two arguments: a graph `G` and a vertex `v`. The procedure marks `v` as visited and adds it to the cycle. If all vertices are visited, it checks if there is an edge from `v` to the first vertex, and outputs the cycle if there is. Otherwise, it returns. Then, it loops through all the neighbors of `v`, and recursively calls `hamiltonian` on each unvisited neighbor, after marking it as visited and adding it to the cycle. After the recursive call, it removes the neighbor from the cycle and marks it as unvisited, and continues with the next neighbor.



# Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be viewed as a way of traversing a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem. The root of the tree is the initial state, and the leaves are the final states. The intermediate nodes are the partial solutions.
- A general pseudo-code for backtracking algorithm is:

```
procedure backtrack(P, c) is
  if reject(P, c) then
    return
  if accept(P, c) then
    output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem, c is the current candidate, reject is a function that checks if the candidate violates any constraint, accept is a function that checks if the candidate is a complete solution, output is a function that prints or stores the solution, first is a function that returns the first extension of the candidate, and next is a function that returns the next extension of the candidate.
- One example of backtracking problem is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value. For example, given the set {10, 7, 5, 18, 12, 20, 15} and the target value 35, the subsets are {10, 7, 18}, {10, 5, 20}, {10, 12, 13}, {7, 5, 12, 15}, {18, 17}, and {20, 15}.
- A possible solution using backtracking is:

```
procedure sum_of_subsets(S, t) is
  n ← length(S)
  x ← array of n boolean values, initialized to false
  backtrack(S, t, 0, 0, x)

procedure backtrack(S, t, i, s, x) is
  if s = t then
    output the subset corresponding to x
  else if i < n then
    x[i] ← true
    backtrack(S, t, i + 1, s + S[i], x)
    x[i] ← false
    backtrack(S, t, i + 1, s, x)
```

- Here, S is the set of integers, t is the target value, n is the size of the set, x is an array of boolean values that indicates whether an element is in the subset or not, i is the index of the current element, and s is the sum of the elements in the subset so far. The algorithm recursively explores all the possible subsets by setting x[i] to true or false, and checks if the sum equals the target value. If so, it outputs the subset. If not, it continues to the next element. The algorithm terminates when all the elements are processed or the sum exceeds the target value.



# Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the difficulty of solving certain problems in polynomial time. A problem is said to be NP-complete if it belongs to the class NP (meaning that a solution can be verified in polynomial time) and if every other problem in NP can be reduced to it in polynomial time.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. These algorithms do not guarantee the best solution, but they aim to come as close as possible to the optimal solution in polynomial time  .
- Some examples of NP-complete problems are Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. These problems have no known efficient algorithms to find the exact optimal solution, but they have some approximation algorithms that can provide near-optimal solutions in reasonable time.
- Travelling Salesman Problem (TSP) is the problem of finding the shortest possible tour that visits each city in a given set of cities exactly once and returns to the starting city. One approximation algorithm for TSP is the nearest neighbor heuristic, which starts from a random city and repeatedly visits the nearest unvisited city until all cities are visited. This algorithm has a worst-case approximation ratio of 2, meaning that the length of the tour it produces is at most twice the length of the optimal tour.
- Graph Coloring is the problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. The minimum number of colors needed to color a graph is called its chromatic number. One approximation algorithm for graph coloring is the greedy algorithm, which assigns colors to the vertices in some order, choosing the smallest available color for each vertex. This algorithm can use at most one more color than the optimal solution, meaning that its approximation ratio is 1 + 1 / (k - 1), where k is the chromatic number of the graph.
- n-Queen Problem is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. One approximation algorithm for n-queen problem is the backtracking algorithm, which tries to place a queen in each row, starting from the first row and moving to the next row only if a safe position is found in the current row. This algorithm can find a solution for any n, but it may take exponential time in the worst case.
- Hamiltonian Cycle is the problem of finding a cycle that visits each vertex of a graph exactly once and returns to the starting vertex. One approximation algorithm for Hamiltonian cycle is the Christofides algorithm, which works for graphs that are complete and have non-negative edge weights. The algorithm first finds a minimum spanning tree of the graph, then adds the minimum number of edges to make the tree Eulerian, and then follows the Eulerian tour to get a Hamiltonian cycle. This algorithm has a worst-case approximation ratio of 3/2, meaning that the length of the cycle it produces is at most 3/2 times the length of the optimal cycle.
- Sum of Subsets is the problem of finding a subset of a given set of positive integers that sums up to a given target value. One approximation algorithm for sum of subsets is the greedy algorithm, which sorts the integers in descending order and adds them to the subset one by one, as long as the sum does not exceed the target value. This algorithm can find a solution that is at least half of the optimal solution, meaning that its approximation ratio is 1/2.



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets

## NP-Completeness

- NP-Completeness is a concept in computational complexity theory that deals with the difficulty of solving certain problems using algorithms.
- A problem is said to be NP (nondeterministic polynomial) if it can be solved in polynomial time by a nondeterministic algorithm, which is an algorithm that can make random choices at each step.
- A problem is said to be NP-Complete if it is NP and also every other NP problem can be reduced to it in polynomial time, which means that there is a way to transform any NP problem into an instance of the NP-Complete problem such that the original problem can be solved by solving the transformed problem.
- NP-Complete problems are the hardest problems in NP, and no efficient algorithm is known to solve them in polynomial time. If any NP-Complete problem can be solved in polynomial time, then all NP problems can be solved in polynomial time, which would imply that P = NP, where P is the class of problems that can be solved in polynomial time by a deterministic algorithm. This is one of the most famous open questions in computer science.
- Some examples of NP-Complete problems are the Travelling Salesman Problem, the Graph Coloring Problem, the n-Queen Problem, the Hamiltonian Cycle Problem, and the Sum of Subsets Problem .

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-Completeness for optimization problems, which are problems that involve finding the best solution among a set of possible solutions according to some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time. Such algorithms are called approximation algorithms  .
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm.
- Some examples of approximation algorithms are the 2-approximation algorithm for the Travelling Salesman Problem, which finds a solution that is at most twice as long as the optimal solution, the greedy algorithm for the Graph Coloring Problem, which finds a solution that uses at most one more color than the optimal solution, the backtracking algorithm for the n-Queen Problem, which finds a solution that places n queens on an n x n chessboard such that no two queens attack each other, the greedy algorithm for the Hamiltonian Cycle Problem, which finds a cycle that visits every vertex of a graph exactly once, and the dynamic programming algorithm for the Sum of Subsets Problem, which finds a subset of a given set of numbers that sums up to a given target value.



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are believed to have no efficient algorithms, unless P = NP, which is a major open question in computer science.
- Examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- To show that a problem is NP-complete, one can use the following steps:
  - Show that the problem is in NP, i.e., given a solution, one can verify its correctness in polynomial time.
  - Choose a known NP-complete problem and reduce it to the given problem in polynomial time, i.e., show how to transform an instance of the known problem into an instance of the given problem such that the answer is preserved.
  - Conclude that the given problem is NP-complete by the transitivity of polynomial-time reductions.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to come as close as possible to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution.
- For a minimization problem, the approximation ratio is defined as:

  - `r = max {C(A)/C(OPT), C(OPT)/C(A)}`

  - where `C(A)` is the cost of the solution produced by the algorithm, and `C(OPT)` is the cost of the optimal solution.

- For a maximization problem, the approximation ratio is defined as:

  - `r = max {C(OPT)/C(A), C(A)/C(OPT)}`

  - where `C(A)` is the value of the solution produced by the algorithm, and `C(OPT)` is the value of the optimal solution.

- An approximation algorithm is called an `r`-approximation algorithm if its approximation ratio is at most `r` for any instance of the problem.
- Examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem with triangle inequality, etc.
- To design an approximation algorithm, one can use the following techniques:
  - Greedy method: Choose the best option at each step, without looking ahead.
  - Rounding: Relax the problem to make it easier to solve, and then round the solution to make it feasible.
  - Randomization: Use random choices to explore different solutions, and then pick the best one.
  - Local search: Start with a feasible solution, and then improve it by making small changes.



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A decision problem is said to be in NP if it can be verified in polynomial time, given a certificate or a witness for the yes instances. For example, the problem of checking whether a graph has a Hamiltonian cycle is in NP, because given a cycle, we can verify in polynomial time that it visits every vertex exactly once and returns to the starting point.
- A decision problem is said to be NP-hard if every problem in NP can be reduced to it in polynomial time. This means that an NP-hard problem is at least as hard as any problem in NP, and finding a polynomial time algorithm for it would imply finding a polynomial time algorithm for all problems in NP. For example, the problem of finding the maximum independent set in a graph is NP-hard, because we can reduce the problem of finding the maximum clique in a graph to it in polynomial time, by taking the complement of the graph.
- A decision problem is said to be NP-complete if it is both in NP and NP-hard. This means that an NP-complete problem is the hardest problem in NP, and finding a polynomial time algorithm for it would solve the famous P vs NP problem, which asks whether every problem in NP can be solved in polynomial time. For example, the problem of determining whether a Boolean formula in conjunctive normal form is satisfiable is NP-complete, because it is in NP (given a satisfying assignment, we can verify it in polynomial time) and NP-hard (we can reduce any problem in NP to it in polynomial time, using a technique called Cook's theorem).
- Some examples of NP-complete problems are:

  - Travelling Salesman Problem: Given a set of cities and distances between them, find the shortest tour that visits every city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine whether the vertices of the graph can be colored with k colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a number n, determine whether n queens can be placed on an n x n chessboard such that no two queens attack each other.
  - Hamiltonian Cycle: Given a graph, determine whether it has a cycle that visits every vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target sum, determine whether there is a subset of the set that adds up to the target sum.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among a set of feasible solutions. For example, the problem of finding the minimum number of colors needed to color a graph is an optimization problem, because we want to find the best coloring among all possible colorings.
- Approximation Algorithms do not guarantee the best solution, but they aim to find a solution that is close to the optimal solution in polynomial time. For example, an approximation algorithm for the graph coloring problem may find a coloring that uses more colors than the minimum, but not too many more.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the cost of the solution found by the algorithm and the cost of the optimal solution. For example, if an approximation algorithm for the graph coloring problem finds a coloring that uses k colors, and the optimal coloring uses k* colors, then the approximation ratio is k/k*. The smaller the approximation ratio, the better the approximation algorithm.
- Some examples of approximation algorithms are:

  - Travelling Salesman Problem: There is a 2-approximation algorithm for the metric version of the problem, where the distances between the cities satisfy the triangle inequality. The algorithm is based on finding a minimum spanning tree of the cities, and then taking a shortcut tour that visits every city in the order they appear in a preorder traversal of the tree. The cost of the tour is at most twice the cost of the optimal tour, because the cost of the tree is a lower bound on the cost of the optimal tour, and the cost of the shortcut tour is at most twice the cost of the tree.
  - Graph Coloring: There is a simple greedy algorithm that colors the vertices of the graph in any order, assigning each vertex the smallest available color



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that a problem is in NP if there is a polynomial time algorithm that can verify a solution given a certificate (or a hint).
- NP-hard means that a problem is at least as hard as any problem in NP, which means that there is a polynomial time reduction from any NP problem to the NP-hard problem.
- A reduction is a way of transforming one problem into another problem, such that solving the second problem also solves the first problem.
- NP-Completeness is important because it shows the limits of efficient computation. If P ≠ NP, then there is no polynomial time algorithm for any NP-complete problem, unless there is a polynomial time algorithm for all NP problems.
- Some examples of NP-complete problems are:

  - SAT: Given a boolean formula in conjunctive normal form, is there an assignment of truth values to the variables that satisfies the formula?
  - 3-SAT: Same as SAT, but the formula is restricted to have clauses of exactly three literals.
  - Clique: Given a graph and a positive integer k, is there a subset of k vertices that are all adjacent to each other?
  - Vertex Cover: Given a graph and a positive integer k, is there a subset of k vertices that covers all the edges, i.e., every edge has at least one endpoint in the subset?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits every vertex exactly once?
  - Travelling Salesman Problem: Given a set of cities and distances between them, is there a tour that visits every city exactly once and has total length at most k?
  - Graph Coloring: Given a graph and a positive integer k, is there a way to assign k colors to the vertices such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a positive integer n, is there a way to place n queens on an n x n chessboard such that no two queens attack each other?
  - Sum of Subsets: Given a set of positive integers and a target sum, is there a subset of the set that adds up to the target sum?

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution.
- The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution.
- For a minimization problem, the approximation ratio is the maximum over all instances of the problem of the ratio between the algorithm's solution and the optimal solution. For a maximization problem, the approximation ratio is the minimum over all instances of the problem of the ratio between the algorithm's solution and the optimal solution.
- An approximation algorithm is called an α-approximation algorithm if its approximation ratio is at most α for a minimization problem, or at least α for a maximization problem.
- Some examples of approximation algorithms are:

  - 2-Approximation Algorithm for Vertex Cover: Given a graph G, find a maximal matching M, i.e., a set of disjoint edges. Then, output the set of vertices that are endpoints of the edges in M. This set is a vertex cover of size at most 2 times the optimal size, because every edge in the graph is covered by at most two vertices in the set, and every edge in the optimal vertex cover is also in the matching.
  - 7/8-Approximation Algorithm for 3-SAT: Given a 3-SAT formula F, randomly assign truth values to the variables with equal probability. Then, output the assignment. This assignment satisfies at least 7/8 of the clauses in expectation, because for each clause, the probability that it is satisfied is 7/8, and the expected number of satisfied clauses is the sum of the probabilities over all clauses.
  - 2-Approximation Algorithm for Travelling Salesman Problem: Given a set of cities and distances between them, find a minimum spanning tree T of the complete graph on the cities. Then, output a tour that follows the preorder traversal of T, i.e., visit



# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science.
- Some examples of NP-complete problems are:

  - Satisfiability (SAT): Given a Boolean formula with n variables and m clauses, is there an assignment of true or false values to the variables that satisfies all the clauses?
  - Traveling Salesman Problem (TSP): Given n cities and a matrix of distances between them, is there a tour that visits each city exactly once and has a total length at most k?
  - Graph Coloring: Given a graph with n vertices and m edges, is there a way to assign k colors to the vertices such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a chessboard of size n x n, is there a way to place n queens on the board such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph with n vertices and m edges, is there a cycle that visits each vertex exactly once and returns to the starting vertex?
  - Sum of Subsets: Given a set of n positive integers and a target value k, is there a subset of the set that sums up to k?

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, such as minimizing or maximizing some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal in polynomial time, i.e., an algorithm that runs in time O(n^k) and produces a solution that has an objective value within a factor of the optimal value.
- The factor by which the approximation algorithm deviates from the optimal value is called the approximation ratio, which is usually expressed as a function of the input size n. For example, an approximation ratio of 2 means that the algorithm produces a solution that is at most twice as bad as the optimal solution, or at least half as good as the optimal solution.
- Approximation Algorithms are useful when the optimal solution is too hard to find or too expensive to compute, and a good enough solution is acceptable for the problem at hand.
- Some examples of approximation algorithms are:

  - 2-Approximation Algorithm for Vertex Cover: A vertex cover of a graph is a subset of vertices that covers all the edges, i.e., every edge has at least one endpoint in the subset. The vertex cover problem is to find the minimum size vertex cover of a given graph. This problem is NP-complete, but there is a simple 2-approximation algorithm that works as follows:

    - Start with an empty vertex cover.
    - While there are uncovered edges, pick any such edge and add both of its endpoints to the vertex cover.
    - Return the vertex cover.

    This algorithm produces a vertex cover that is at most twice as large as the optimal vertex cover, because every edge is covered by at most two vertices, and the optimal vertex cover must cover every edge by at least one vertex.

  - 7/8-Approximation Algorithm for Max 3-SAT: A 3-SAT formula is a Boolean formula with n variables and m clauses, where each clause has exactly three literals. The max 3-SAT problem is to find the maximum number of clauses that can be satisfied by an assignment of true or false values to the variables. This problem is NP-complete, but there is a clever 7/8-approx



# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that a problem is in NP if there is a polynomial time algorithm that can verify a solution given a certificate (or a hint).
- NP-hard means that a problem is at least as hard as any problem in NP, which means that there is no polynomial time algorithm that can solve it unless P = NP.
- P is the class of decision problems that can be solved in polynomial time by a deterministic algorithm.
- The question of whether P = NP is one of the most important open problems in computer science and mathematics.
- If P = NP, then every problem in NP can be solved in polynomial time by a deterministic algorithm, and NP-Completeness becomes irrelevant.
- If P ≠ NP, then there are problems in NP that cannot be solved in polynomial time by any algorithm, and NP-Completeness is a way of identifying such problems.
- A problem is NP-complete if it is both in NP and NP-hard, which means that it is as hard as any problem in NP, and that any problem in NP can be reduced to it in polynomial time.
- A reduction is a way of transforming one problem into another problem, such that solving the second problem also solves the first problem.
- A polynomial time reduction is a reduction that can be done by a polynomial time algorithm.
- If a problem A can be reduced to a problem B in polynomial time, then A is no harder than B, and B is at least as hard as A.
- If a problem B is NP-complete, then any problem A that can be reduced to B in polynomial time is also NP-complete, because A is both in NP and NP-hard.
- To prove that a problem is NP-complete, it is sufficient to show that it is in NP and that it can be reduced from a known NP-complete problem in polynomial time.
- Some examples of NP-complete problems are:

  - SAT: Given a Boolean formula in conjunctive normal form (CNF), is there an assignment of truth values to the variables that satisfies the formula?
  - 3-SAT: Given a Boolean formula in CNF where each clause has exactly three literals, is there an assignment of truth values to the variables that satisfies the formula?
  - Clique: Given a graph and a positive integer k, is there a subset of k vertices that are all adjacent to each other (a clique)?
  - Vertex Cover: Given a graph and a positive integer k, is there a subset of k vertices that covers all the edges (a vertex cover)?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits every vertex exactly once (a Hamiltonian cycle)?
  - Travelling Salesman Problem (TSP): Given a set of n cities and a distance matrix, is there a tour that visits every city exactly once and has a total length at most k?
  - Subset Sum: Given a set of n positive integers and a target sum t, is there a subset of the integers that adds up to t?
  - Graph Coloring: Given a graph and a positive integer k, is there a way of assigning k colors to the vertices such that no two adjacent vertices have the same color (a k-coloring)?

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions.
- Optimization problems can be either minimization problems, where the goal is to minimize an objective function, or maximization problems, where the goal is to maximize an objective function.
- An approximation algorithm is a polynomial time algorithm that produces a feasible solution that is close to the optimal solution in some measure.
- The measure of closeness is usually the approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution.
- For minimization problems, the approximation ratio is the value of the algorithm solution divided by the value of the optimal solution, and for maximization problems, it is the value of the optimal solution divided by the value of the algorithm solution.
- The approximation ratio is always at least 1, and the closer it is to 1, the better the approximation is.
- An approximation algorithm is called an α-approximation algorithm if it guarantees an approximation ratio of

