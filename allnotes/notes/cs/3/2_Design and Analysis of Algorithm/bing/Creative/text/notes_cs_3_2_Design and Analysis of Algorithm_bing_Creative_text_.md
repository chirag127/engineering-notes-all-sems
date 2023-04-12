

## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An **algorithm** is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation.
- **Analyzing algorithms** is the process of determining the amount of resources (such as time and space) necessary to execute them.
- The **complexity of algorithms** is a measure of the amount of resources required by an algorithm to run as a function of the size of the input.
- The **growth of functions** is the study of how the running time or space requirements of an algorithm increase with the size of the input.
- **Performance measurements** are the methods and tools used to evaluate the efficiency and effectiveness of algorithms in terms of time, space, and other criteria.
- **Sorting** is the process of arranging a collection of items in a certain order, such as ascending or descending, according to some comparison rule.
- **Order statistics** are the values of the kth smallest or largest element in a collection of items, such as the minimum, maximum, median, or percentile.
- **Shell sort** is a sorting algorithm that repeatedly applies insertion sort to subarrays of the input, with decreasing gaps between the elements of each subarray, until the whole array is sorted.
- **Quick sort** is a sorting algorithm that partitions the input array into two subarrays based on a pivot element, such that all elements in the left subarray are less than or equal to the pivot and all elements in the right subarray are greater than or equal to the pivot, and then recursively sorts the subarrays.
- **Merge sort** is a sorting algorithm that divides the input array into two halves, recursively sorts each half, and then merges the two sorted halves into one sorted array.
- **Heap sort** is a sorting algorithm that builds a binary heap from the input array, and then repeatedly extracts the maximum element from the heap and places it at the end of the output array, until the heap is empty.
- **Comparison of sorting algorithms** is the evaluation of the advantages and disadvantages of different sorting algorithms in terms of their time complexity, space complexity, stability, adaptability, and other factors.
- **Sorting in linear time** is the possibility of sorting a collection of items in O(n) time, where n is the number of items, by using algorithms that do not rely on comparisons, such as counting sort, radix sort, or bucket sort. These algorithms are usually applicable only to certain types of inputs, such as integers in a fixed range.



### Algorithms for the notes of the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An algorithm is a finite sequence of well-defined instructions that solves a problem or performs a task.
- Analyzing algorithms is the process of determining the amount of resources (such as time and space) that an algorithm consumes when executed on a given input.
- Complexity of algorithms is the measure of how the resource consumption of an algorithm grows as the input size increases.
- Growth of functions is the mathematical notation that describes how a function behaves asymptotically, that is, when the input size approaches infinity.
- Performance measurements are the empirical methods of evaluating the efficiency and correctness of algorithms, such as running time, memory usage, and output quality.
- Sorting and order statistics are two related problems that deal with arranging a sequence of items in a certain order or finding the item that occupies a given position in the sorted sequence.
- Shell sort is a sorting algorithm that sorts the items by comparing and swapping elements that are far apart, and then reducing the gap between the compared elements until it reaches one.
- Quick sort is a sorting algorithm that sorts the items by choosing a pivot element and partitioning the sequence into two sub-sequences, such that all the elements in the left sub-sequence are smaller than the pivot and all the elements in the right sub-sequence are larger than the pivot, and then recursively sorting the sub-sequences.
- Merge sort is a sorting algorithm that sorts the items by dividing the sequence into two equal or nearly equal sub-sequences, recursively sorting the sub-sequences, and then merging the sorted sub-sequences into one sorted sequence.
- Heap sort is a sorting algorithm that sorts the items by using a data structure called a heap, which is a binary tree that satisfies the heap property, that is, the value of each node is greater than or equal to the value of its children. The algorithm repeatedly extracts the maximum element from the heap and places it at the end of the sequence, until the heap is empty.
- Comparison of sorting algorithms is the process of evaluating the advantages and disadvantages of different sorting algorithms based on various criteria, such as time complexity, space complexity, stability, adaptability, and simplicity.
- Sorting in linear time is the possibility of sorting a sequence of items in O(n) time, where n is the number of items, by using some special properties of the items, such as their range, distribution, or structure. Examples of such algorithms are counting sort, radix sort, and bucket sort.



### Analyzing Algorithms

- Analyzing algorithms is the process of finding the computational complexity of algorithms, which is the amount of time, storage, or other resources needed to execute them .
- The computational complexity of an algorithm is usually expressed as a function of the length of the input, denoted by n. For example, an algorithm that takes n steps to sort an array of n elements has a time complexity of O(n).
- The most common measures of computational complexity are time complexity and space complexity, which indicate how fast an algorithm runs and how much memory it uses, respectively.
- Analyzing algorithms is important for several reasons:
  - To predict the behavior of an algorithm without implementing it on a specific computer.
  - To compare the efficiency of different algorithms for the same problem.
  - To choose the best algorithm for a given problem and input size.
  - To understand the theoretical limits of computation and the inherent difficulty of some problems.
- There are different methods and techniques for analyzing algorithms, such as asymptotic analysis, amortized analysis, average-case analysis, worst-case analysis, best-case analysis, etc.
- Asymptotic analysis is the most widely used method, which focuses on the growth rate of the complexity function as the input size approaches infinity. It uses the notation of big O, big Omega, and big Theta to classify algorithms into different complexity classes.
- Amortized analysis is a method that averages the cost of a sequence of operations over the whole sequence, rather than considering the worst-case cost of each operation. It is useful for analyzing algorithms that have a variable cost per operation, such as dynamic data structures.
- Average-case analysis is a method that considers the expected cost of an algorithm over all possible inputs, rather than the worst-case or best-case cost. It is useful for analyzing algorithms that have a high variance in their performance, such as randomized algorithms.
- Worst-case analysis is a method that considers the maximum cost of an algorithm over all possible inputs, regardless of their probability. It is useful for analyzing algorithms that have a low variance in their performance, such as deterministic algorithms.
- Best-case analysis is a method that considers the minimum cost of an algorithm over all possible inputs, regardless of their probability. It is rarely useful for analyzing algorithms, as it does not reflect the typical or average behavior of an algorithm.



### Complexity of Algorithms

- Complexity of an algorithm is a measure of how long an algorithm would take to complete given an input of size n.
- Complexity is calculated asymptotically as n approaches infinity, to capture the behavior of the algorithm for large inputs.
- Complexity is about the algorithm itself, not the actual execution time or the hardware used.
- Complexity is expressed using the big O notation, which gives the upper bound of the number of operations executed by an algorithm as a function of n.
- For example, an algorithm that has a complexity of O(n) means that the number of operations grows linearly with the input size n.
- Complexity can be classified into two types: time complexity and space complexity.
- Time complexity is the amount of time required by the algorithm to solve the problem.
- Space complexity is the amount of memory required by the algorithm to solve the problem.
- Both time and space complexity depend on the choice of the algorithm, the input data, and the implementation details.
- Some common classes of complexity are:
  - Constant: O(1), the algorithm takes a constant amount of time or space regardless of the input size.
  - Logarithmic: O(log n), the algorithm takes a logarithmic amount of time or space with respect to the input size.
  - Linear: O(n), the algorithm takes a linear amount of time or space with respect to the input size.
  - Quadratic: O(n^2), the algorithm takes a quadratic amount of time or space with respect to the input size.
  - Cubic: O(n^3), the algorithm takes a cubic amount of time or space with respect to the input size.
  - Exponential: O(2^n), the algorithm takes an exponential amount of time or space with respect to the input size.
  - Factorial: O(n!), the algorithm takes a factorial amount of time or space with respect to the input size.
- The complexity of an algorithm can be analyzed by using the following steps:
  - Identify the basic operations that contribute to the running time or space usage of the algorithm, such as arithmetic operations, comparisons, assignments, etc.
  - Count the number of times each basic operation is executed as a function of the input size n.
  - Find the dominant term in the function, which has the highest growth rate as n increases.
  - Ignore the lower-order terms and the constant factors, and use the big O notation to express the complexity of the algorithm.
- For example, consider the following algorithm that computes the sum of the first n natural numbers:

```
Algorithm Sum(n)
  s = 0
  for i = 1 to n
    s = s + i
  return s
```

- The basic operations are the assignment s = 0, the comparison i <= n, the increment i = i + 1, the addition s = s + i, and the return s.
- The assignment s = 0 is executed once, so it contributes O(1) to the complexity.
- The comparison i <= n is executed n + 1 times, so it contributes O(n) to the complexity.
- The increment i = i + 1 is executed n times, so it contributes O(n) to the complexity.
- The addition s = s + i is executed n times, so it contributes O(n) to the complexity.
- The return s is executed once, so it contributes O(1) to the complexity.
- The total complexity of the algorithm is O(1) + O(n) + O(n) + O(n) + O(1) = O(3n + 2).
- The dominant term is 3n, which has the highest growth rate as n increases.
- The lower-order term 2 and the constant factor 3 can be ignored, and the complexity can be expressed as O(n) using the big O notation.
- Therefore, the complexity of the algorithm Sum(n) is O(n).



### Growth of Functions

- Growth of functions is a way of measuring the efficiency and performance of algorithms based on their input size and execution time.
- Growth of functions helps us to compare different algorithms and choose the most suitable one for a given problem.
- Growth of functions is expressed using asymptotic notation, which simplifies the function by ignoring the constants and lower order terms.
- Asymptotic notation includes three types: big-O, big-Ω, and big-Θ, which represent the upper bound, lower bound, and tight bound of the function respectively.
- The rate of growth of a function indicates how fast or slow the function increases or decreases as the input size grows.
- The rate of growth of a function can be classified into different categories, such as constant, linear, logarithmic, polynomial, exponential, etc.
- The lower the rate of growth of a function, the more efficient the algorithm is, and vice versa.
- For example, a linear search algorithm has a growth of function of Θ(n), which means it takes linear time to search an element in an array of size n.
- A binary search algorithm has a growth of function of Θ(log n), which means it takes logarithmic time to search an element in a sorted array of size n.
- A binary search algorithm is more efficient than a linear search algorithm, because log n < n for any n > 1.



### Performance Measurements

- Performance measurements are used to evaluate the efficiency and effectiveness of an algorithm or a program.
- Performance measurements can be based on various factors, such as time, space, network, power, etc.
- Time complexity is the measure of how much time the algorithm or the program takes to execute for a given input size.
- Space complexity is the measure of how much memory or space the algorithm or the program uses while it is executed for a given input size.
- Network complexity is the measure of how much data the algorithm or the program transfers over the network for a given input size.
- Power complexity is the measure of how much energy the algorithm or the program consumes while it is executed for a given input size.
- Performance measurements can be expressed using different notations, such as big O, big Ω, big Θ, etc.
- Big O notation is the most commonly used notation to describe the upper bound or the worst-case scenario of the performance of an algorithm or a program.
- Big Ω notation is used to describe the lower bound or the best-case scenario of the performance of an algorithm or a program.
- Big Θ notation is used to describe the tight bound or the average-case scenario of the performance of an algorithm or a program.
- Performance measurements can help compare different algorithms or programs and choose the most suitable one for a given problem or application.



### Sorting and Order Statistics - Shell Sort

- Shell sort is a generalization of insertion sort that allows the exchange of items that are far apart.
- The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list.
- Such a list is said to be h-sorted. It can also be thought of as h interleaved lists, each individually sorted.
- By performing insertion sort on each of the h sublists, the total number of exchanges required by insertion sort can be reduced.
- The final step of shell sort is a plain insertion sort, but by then, the list of elements is guaranteed to be almost sorted.
- The running time of shell sort depends on the choice of the increment sequence, which is a series of values for h that ends in 1.
- One common choice is h_k = 2^k, for k = floor(log_2 n), k-1, ..., 1, 0. This gives a worst-case running time of O(n^(3/2)).
- Another common choice is h_k = 3^k - 1 / 2, for k such that h_k < n / 3. This gives a worst-case running time of O(n^(3/2)) as well, but performs better in practice.
- The best known worst-case running time for shell sort with a specific increment sequence is O(n log^2 n), but the best increment sequence is not known.



### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The base case of the recursion is when the subarray has one or zero elements, which are trivially sorted.
- The average-case time complexity of quick sort is **O(n log n)**, where n is the number of elements in the array.
- The worst-case time complexity of quick sort is **O(n^2)**, which occurs when the pivot element is always the smallest or the largest element in the subarray, resulting in unbalanced partitions.
- The space complexity of quick sort is **O(log n)**, which is the depth of the recursion tree.
- Quick sort is an **in-place** sorting algorithm, meaning it does not require additional memory to store the sorted array.
- Quick sort is also an **unstable** sorting algorithm, meaning it does not preserve the relative order of equal elements in the array.

#### Pseudocode of quick sort

```
QUICK-SORT(A, p, r)
// A is the array to be sorted
// p and r are the indices of the first and last elements of the subarray
// initially, p = 0 and r = n - 1, where n is the size of the array
if p < r
    q = PARTITION(A, p, r) // q is the index of the pivot element after partitioning
    QUICK-SORT(A, p, q - 1) // recursively sort the left subarray
    QUICK-SORT(A, q + 1, r) // recursively sort the right subarray

PARTITION(A, p, r)
x = A[r] // choose the last element as the pivot
i = p - 1 // i is the index of the last element in the left subarray
for j = p to r - 1 // loop through the subarray, excluding the pivot
    if A[j] <= x // if the current element is less than or equal to the pivot
        i = i + 1 // increment i
        exchange A[i] with A[j] // swap the current element with the element at i
exchange A[i + 1] with A[r] // place the pivot element in its correct position
return i + 1 // return the index of the pivot element
```



### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The main idea of merge sort is to divide the problem of sorting an array of n elements into two subproblems of sorting two subarrays of n/2 elements each, and then combine the solutions of the subproblems by merging the two sorted subarrays.
- The algorithm can be described as follows:

  - **Base case:** If the array has zero or one element, it is already sorted and no further action is needed.
  - **Divide:** If the array has more than one element, split it into two subarrays of equal or nearly equal size.
  - **Conquer:** Recursively sort the two subarrays using merge sort.
  - **Combine:** Merge the two sorted subarrays into a single sorted array.

- The merge operation takes two sorted subarrays and merges them into a single sorted array. It uses an auxiliary array to store the merged elements, and two pointers to keep track of the current position in each subarray. It compares the elements at the current positions of the two subarrays, and copies the smaller one to the auxiliary array, advancing the corresponding pointer. It repeats this process until one of the subarrays is exhausted, and then copies the remaining elements of the other subarray to the auxiliary array. Finally, it copies the auxiliary array back to the original array.
- The pseudocode for the merge operation is as follows:

  ```
  MERGE(A, p, q, r)
  // A is an array, p, q, and r are indices such that p <= q < r
  // A[p..q] and A[q+1..r] are sorted subarrays
  // Merges the two subarrays into a single sorted subarray A[p..r]

  n1 = q - p + 1 // the length of the first subarray
  n2 = r - q // the length of the second subarray
  create arrays L[1..n1+1] and R[1..n2+1] // auxiliary arrays
  for i = 1 to n1
      L[i] = A[p + i - 1] // copy the first subarray to L
  for j = 1 to n2
      R[j] = A[q + j] // copy the second subarray to R
  L[n1 + 1] = infinity // a sentinel value to mark the end of L
  R[n2 + 1] = infinity // a sentinel value to mark the end of R
  i = 1 // the current position in L
  j = 1 // the current position in R
  for k = p to r
      if L[i] <= R[j]
          A[k] = L[i] // copy the smaller element to A
          i = i + 1 // advance the pointer in L
      else
          A[k] = R[j] // copy the smaller element to A
          j = j + 1 // advance the pointer in R
  ```

- The pseudocode for the merge sort algorithm is as follows:

  ```
  MERGE-SORT(A, p, r)
  // A is an array, p and r are indices such that p <= r
  // Sorts the subarray A[p..r] using merge sort

  if p < r // the base case is when p >= r, meaning the subarray has zero or one element
      q = floor((p + r) / 2) // find the middle point of the subarray
      MERGE-SORT(A, p, q) // recursively sort the left subarray
      MERGE-SORT(A, q + 1, r) // recursively sort the right subarray
      MERGE(A, p, q, r) // merge the two sorted subarrays
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge operation takes O(n) time to merge the two subarrays. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm uses an auxiliary array of size n to store the merged elements at each level of recursion. Therefore, the total space is O(n).
-



### Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the value of its children (for a max heap) or less than or equal to the value of its children (for a min heap).
- The heap sort algorithm can be divided into two steps: heapify and extract.
- Heapify is the process of building a heap from an unsorted list. It can be done in linear time by starting from the last non-leaf node and sifting it down until it satisfies the heap property, and then repeating the same for all the preceding non-leaf nodes.
- Extract is the process of removing the root element of the heap (which is the maximum or minimum element depending on the type of heap) and replacing it with the last element of the heap, and then sifting it down until it satisfies the heap property. This is repeated until the heap is empty, and the extracted elements form a sorted list.
- Heap sort is an in-place algorithm, meaning it does not require extra space to sort the list. However, it is not a stable algorithm, meaning it does not preserve the relative order of equal elements.
- The time complexity of heap sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the list. This is because heapify takes O(n) time and extract takes O(log n) time for each element.
- The space complexity of heap sort is O(1), as it only requires a constant amount of extra space to store the heap.
- Heap sort is typically 2-3 times slower than well-implemented quick sort, due to the lack of locality of reference and the overhead of maintaining the heap structure.
- Heap sort is suitable for sorting large data sets that do not fit in memory, as it can be easily implemented using external storage devices. It is also useful for finding the k largest or smallest elements in a list, as it can be done in O(n + k log n) time by using a heap of size k.



### Comparison of Sorting Algorithms

Sorting algorithms are methods of arranging a list of elements in a certain order, such as ascending or descending. There are many different sorting algorithms, each with different advantages and disadvantages. Some of the factors that can be used to compare sorting algorithms are:

- Time complexity: how the running time of the algorithm grows as the input size increases.
- Space complexity: how much extra memory the algorithm requires to sort the list.
- Stability: whether the algorithm preserves the relative order of elements with equal keys.
- Comparison-based or not: whether the algorithm only compares elements with a comparison operator, or uses other information such as the range or distribution of the keys.

Some of the most commonly used sorting algorithms are:

- Shell sort: an improvement of insertion sort that uses gaps between elements to reduce the number of comparisons and shifts. It has an average time complexity of O(n^1.5), a worst-case time complexity of O(n^2), and a space complexity of O(1). It is unstable and comparison-based.
- Quick sort: a divide-and-conquer algorithm that partitions the list around a pivot element and recursively sorts the sublists. It has an average and best-case time complexity of O(n log n), a worst-case time complexity of O(n^2), and a space complexity of O(log n) for the recursive calls. It is unstable and comparison-based, but can be made stable with extra space.
- Merge sort: another divide-and-conquer algorithm that splits the list into two halves, recursively sorts them, and merges them back together. It has a time complexity of O(n log n) in all cases, and a space complexity of O(n) for the auxiliary array. It is stable and comparison-based.
- Heap sort: an algorithm that builds a heap data structure from the list, and repeatedly extracts the maximum element and places it at the end of the list. It has a time complexity of O(n log n) in all cases, and a space complexity of O(1). It is unstable and comparison-based.
- Counting sort: a non-comparison-based algorithm that counts the number of occurrences of each key in the list, and uses them to determine the position of each element in the output list. It has a time complexity of O(n + k), where k is the range of the keys, and a space complexity of O(n + k). It is stable and non-comparison-based, but only works for integer keys.
- Bucket sort: another non-comparison-based algorithm that distributes the elements into buckets based on their keys, and sorts each bucket using another sorting algorithm. It has an average time complexity of O(n + k), where k is the number of buckets, and a worst-case time complexity of O(n^2) if the buckets are not evenly distributed. It has a space complexity of O(n + k). It is stable and non-comparison-based, but depends on the choice of the bucket function and the sorting algorithm for each bucket.

The following table summarizes the comparison of sorting algorithms based on the factors mentioned above:

| Algorithm | Time complexity (average) | Time complexity (worst) | Space complexity | Stability | Comparison-based |
|-----------|---------------------------|-------------------------|------------------|-----------|------------------|
| Shell sort | O(n^1.5) | O(n^2) | O(1) | No | Yes |
| Quick sort | O(n log n) | O(n^2) | O(log n) | No | Yes |
| Merge sort | O(n log n) | O(n log n) | O(n) | Yes | Yes |
| Heap sort | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting sort | O(n + k) | O(n + k) | O(n + k) | Yes | No |
| Bucket sort | O(n + k) | O(n^2) | O(n + k) | Yes | No |



### Sorting in Linear Time

- Sorting in linear time means arranging a sequence of elements in a specific order in O(n) time, where n is the number of elements.
- Sorting in linear time is possible only when some special assumptions are made about the input sequence, such as the range of values, the distribution of elements, or the representation of data.
- Some examples of sorting algorithms that run in linear time are counting sort, radix sort, and bucket sort. These algorithms are not based on comparisons, but on other operations such as counting, grouping, or hashing.
- Counting sort assumes that the input consists of integers in a small range  . It counts the number of occurrences of each integer and then outputs the sorted sequence by placing each integer according to its count.
- Radix sort assumes that the input consists of integers or strings that can be represented in a fixed number of digits or characters  . It sorts the input by grouping the elements based on each digit or character, starting from the least significant one to the most significant one.
- Bucket sort assumes that the input is generated by a random process that distributes elements uniformly over an interval  . It divides the interval into equal-sized buckets and then sorts each bucket using another sorting algorithm. It then concatenates the sorted buckets to obtain the sorted sequence.
- Sorting in linear time has some advantages and disadvantages. Some advantages are that it can be faster than comparison-based sorting algorithms, which have a lower bound of O(n log n) time, and that it can be useful for sorting large data sets with certain properties. Some disadvantages are that it requires extra space, that it may not be stable, and that it may not be applicable for arbitrary input sequences.



## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

- Advanced data structures are data structures that provide more efficient ways to organize, store, and manipulate data than the basic data structures such as arrays, linked lists, stacks, queues, etc.
- Some of the advanced data structures are:

  - **Red-Black Trees**: A red-black tree is a type of self-balancing binary search tree, where each node has an extra bit that represents its color, either red or black. The tree maintains the following properties:
    - Every node is either red or black.
    - The root and the leaves (NIL) are black.
    - If a node is red, then both its children are black.
    - Every simple path from a node to a descendant leaf contains the same number of black nodes.
  - These properties ensure that the tree remains balanced, and the height of the tree is O(log n), where n is the number of nodes. The operations of insertion, deletion, and search can be performed in O(log n) time.

  - **B-Trees**: A B-tree is a type of multi-way search tree, where each node can have more than two children. The tree maintains the following properties:
    - All the leaves are at the same level.
    - Each node, except the root and the leaves, has at least t children, where t is a fixed integer greater than 1.
    - Each node, except the root, has at most 2t children.
    - Each node, except the leaves, has one key less than the number of its children, and the keys are stored in sorted order.
  - B-trees are useful for storing large amounts of data that do not fit in main memory, and can be accessed efficiently by disk operations. The operations of insertion, deletion, and search can be performed in O(log n) time, where n is the number of keys.

  - **Binomial Heaps**: A binomial heap is a type of heap data structure, where the heap is represented as a collection of binomial trees. A binomial tree of order k is a recursive structure that has the following properties:
    - It has 2^k nodes.
    - It has k levels, numbered from 0 to k-1.
    - The root has the smallest key among all the nodes in the tree, and the key of any node is greater than or equal to the key of its parent.
    - The root has k children, and the i-th child is a binomial tree of order k-i-1, for i = 0, 1, ..., k-1.
  - A binomial heap maintains the following properties:
    - Each binomial tree in the heap obeys the min-heap property, that is, the key of any node is greater than or equal to the key of its parent.
    - There can be at most one binomial tree of any order in the heap.
  - Binomial heaps are useful for implementing priority queues, as they support the operations of insert, delete-min, merge, and decrease-key in O(log n) time, where n is the number of nodes in the heap.

  - **Fibonacci Heaps**: A Fibonacci heap is a type of heap data structure, where the heap is represented as a collection of rooted trees that are not necessarily binomial. A Fibonacci heap maintains the following properties:
    - Each tree in the heap obeys the min-heap property, that is, the key of any node is greater than or equal to the key of its parent.
    - There is a pointer to the tree with the minimum key in the heap, called the min-pointer.
    - Each node has a degree, which is the number of its children, and a mark, which is a boolean value that indicates whether the node has lost a child since it became a child of another node.
    - The degree of any node is bounded by O(log n), where n is the number of nodes in the heap.
  - Fibonacci heaps are useful for implementing priority queues, as they support the operations of insert, delete-min, merge, and decrease-key in O(1) amortized time, and the operation of delete in O(log n) amortized time.

  - **Tries**: A trie is a type of tree data structure, where each node represents a prefix of a string



### Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and **efficient** for storing and retrieving ordered data .
- Red-black trees have the following **properties** :
  - Each node is either **red** or **black**.
  - The root of the tree is always **black**.
  - Every leaf node (NIL) is **black**.
  - If a node is **red**, then both its children are **black**.
  - Every simple path from a node to a descendant leaf node has the same number of **black** nodes. This number is called the **black height** of the node.
- Red-black trees maintain these properties by performing **rotations** and **recoloring** operations after insertion or deletion of nodes .
- Red-black trees have a **guaranteed time complexity** of O(log n) for basic operations like insertion, deletion, and search .
- Red-black trees can be used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - Implementing **associative arrays** and **multisets**.
  - Implementing **priority queues** and **scheduling algorithms**.
  - Implementing **interval trees** and **augmented trees**.
  - Implementing **concurrent data structures** and **lock-free algorithms**.



### B-Trees

- A B-tree is a **self-balancing** tree data structure that maintains **sorted data** and allows **searches, sequential access, insertions, and deletions** in **logarithmic time** .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children. Each node can have up to **m** children and **m-1** keys, where **m** is the **order** of the tree.
- Each node must have at least **⌈m/2⌉** children (except the root) to keep the tree balanced. The root must have at least two children if it is not a leaf.
- All the leaves are at the same level, and no node can have more than one parent.
- The keys in each node are stored in **ascending order**, and the keys in the subtree of a node are **greater than** the key to its left and **less than or equal to** the key to its right .
- The height of a B-tree with **n** keys and order **m** is bounded by **logm/2(n+1)**.
- The main advantage of a B-tree is that it can handle **massive amounts of data** with ease, as it reduces the number of disk accesses by storing multiple keys in each node.
- The main operations on a B-tree are **search, insert, and delete**. Each operation takes **O(logn)** time, where **n** is the number of keys in the tree .
- To search for a key in a B-tree, we start from the root and compare the key with the keys in the node. If the key is found, we return the node. If the key is smaller than the smallest key, we recursively search in the leftmost child. If the key is larger than the largest key, we recursively search in the rightmost child. If the key is in between two keys, we recursively search in the child corresponding to the interval .
- To insert a key in a B-tree, we first search for the leaf node where the key should be inserted. If the leaf node has space, we simply insert the key in the correct position. If the leaf node is full, we split it into two nodes and insert the middle key in the parent node. This may cause the parent node to overflow, in which case we repeat the splitting process until we reach a node that has space or the root. If the root is split, we create a new root with the middle key and two children .
- To delete a key from a B-tree, we first search for the node that contains the key. If the key is in a leaf node, we simply remove it from the node. If the key is in an internal node, we replace it with its predecessor or successor in the leaf level and delete that key. This may cause the node to underflow, in which case we borrow a key from a sibling or merge with a sibling and delete a key from the parent node. This may cause the parent node to underflow, in which case we repeat the borrowing or merging process until we reach a node that has enough keys or the root. If the root has only one key and two children, we delete the root and make one of the children the new root .



### Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node.
- A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- A binomial tree of order k has 2^k nodes.
- A binomial heap with n nodes has at most log(n) + 1 binomial trees.
- The operations supported by a binomial heap are:
  - Create-heap: creates an empty binomial heap.
  - Insert: inserts a new node into the binomial heap.
  - Get-min: returns the node with the minimum key in the binomial heap.
  - Extract-min: removes and returns the node with the minimum key in the binomial heap.
  - Union: merges two binomial heaps into one.
  - Decrease-key: decreases the key of a given node in the binomial heap.
  - Delete: deletes a given node from the binomial heap.
- The time complexities of the operations are:
  - Create-heap: O(1)
  - Insert: O(log n)
  - Get-min: O(log n)
  - Extract-min: O(log n)
  - Union: O(log n)
  - Decrease-key: O(log n)
  - Delete: O(log n)



### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees  .
- A Fibonacci heap is a collection of trees satisfying the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent. This implies that the minimum key is always at the root of one of the trees.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- For the Fibonacci heap, the find-minimum operation takes constant (O(1)) amortized time. The insert and decrease key operations also work in constant amortized time  .
- The delete and delete-minimum operations work in O(log n) amortized time, where n is the number of nodes in the heap  .
- The merge or union operation, which combines two Fibonacci heaps into one, works in constant amortized time  .
- The key advantage of a Fibonacci heap over other heap data structures is its fast amortized running time for operations such as insert, decrease key, and merge, which are useful in many algorithms such as Dijkstra's algorithm and Prim's algorithm  .
- The structure of a Fibonacci heap is more flexible than that of a binary heap or a binomial heap, as it allows arbitrary degree of nodes and arbitrary shape of trees.
- A Fibonacci heap maintains a pointer to the minimum node and a circular, doubly linked list of roots of the trees. Each node stores a pointer to its parent, a pointer to one of its children, and pointers to its left and right siblings. Each node also stores its degree (the number of children) and a mark bit (indicating whether it has lost a child since the last time it was made a child of another node) .
- A Fibonacci heap supports the following operations:

  - **make-heap**: creates and returns a new, empty Fibonacci heap.
  - **insert**: inserts a new node with a given key into the heap.
  - **find-min**: returns a pointer to the node with the minimum key in the heap.
  - **union**: merges two Fibonacci heaps into one and returns the resulting heap.
  - **extract-min**: deletes the node with the minimum key from the heap and returns its key.
  - **decrease-key**: decreases the key of a given node in the heap to a new value, which must be no greater than the current key.
  - **delete**: deletes a given node from the heap.



### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings over an alphabet .
- The word trie comes from the word re**trie**val, which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has at most k children, and the links between nodes are defined by individual characters of the keys.
- A trie can store a large amount of strings efficiently, and perform pattern matching and prefix search operations.
- A trie has the following properties:
  - The root node does not contain any character, and represents an empty string.
  - Each node, except the root, contains one character of a key.
  - Each node may have a boolean flag to indicate whether it marks the end of a key or not.
  - A node is a leaf node if it has no children.
  - A node is an internal node if it has at least one child.
  - A key is stored in the trie by following the path from the root to a leaf node, or to a node marked as the end of a key.
  - A key is present in the trie if there is a path from the root to a node marked as the end of the key, and the characters along the path match the key.
  - A key is a prefix of another key if there is a path from the root to a node that contains the key, and the node is not marked as the end of the key.
  - A node can have multiple prefixes and suffixes, depending on the keys stored in the trie.
- A trie can be implemented using an array of pointers, a hash map, or a dynamic array to store the children of each node.
- A trie can be traversed using depth-first search or breadth-first search algorithms.
- A trie can be used for various applications, such as:
  - Autocomplete and spell check features in text editors and search engines.
  - IP routing and longest prefix matching in computer networks.
  - Text compression and encoding schemes.
  - Dictionary and word games.



### Skip List

- A skip list is a probabilistic data structure that allows for efficient search, insertion and deletion of elements in a sorted list .
- A skip list consists of multiple layers of linked lists, with each layer having a smaller number of elements than the previous one .
- The lowest layer contains all the elements of the list in sorted order, and the highest layer contains only a few elements that act as shortcuts for faster traversal .
- Each element in a skip list has a random level, which determines how many layers it belongs to. The level of an element is chosen randomly with a geometric distribution, such that the probability of an element having level k is p^(k-1) * (1-p), where p is a fixed parameter between 0 and 1 .
- The expected number of elements in a layer is proportional to p^(k), where k is the layer number. The expected height of a skip list is O(log n), where n is the number of elements in the list .
- To search for an element in a skip list, we start from the highest layer and move forward until we find an element that is larger than or equal to the target element. Then we move down to the next layer and repeat the process until we reach the lowest layer. If we find the target element, we return it. Otherwise, we return null  .
- The expected time complexity of search in a skip list is O(log n), where n is the number of elements in the list. This is because we expect to visit O(log n) elements in each layer, and there are O(log n) layers in the skip list  .
- To insert an element in a skip list, we first search for the position where the element should be inserted in the lowest layer. Then we generate a random level for the element, and insert it into all the layers up to that level. We update the pointers of the previous and next elements in each layer accordingly  .
- The expected time complexity of insertion in a skip list is O(log n), where n is the number of elements in the list. This is because we expect to visit O(log n) elements in each layer, and there are O(log n) layers in the skip list. The space complexity of insertion is O(1), since we only need to allocate a new node for the element  .
- To delete an element from a skip list, we first search for the element in the skip list. If we find it, we remove it from all the layers it belongs to, and update the pointers of the previous and next elements in each layer accordingly. If we do not find it, we do nothing  .
- The expected time complexity of deletion in a skip list is O(log n), where n is the number of elements in the list. This is because we expect to visit O(log n) elements in each layer, and there are O(log n) layers in the skip list. The space complexity of deletion is O(1), since we only need to deallocate the node of the element  .
- Skip lists are a simple, fast and space-efficient data structure that can replace balanced trees in many applications. They are easy to implement and parallelize, and can support dynamic operations efficiently  .



## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

- Divide and conquer is a technique of breaking a problem into smaller subproblems, solving them recursively, and combining their solutions to obtain the solution of the original problem.
- Some examples of divide and conquer algorithms are:
  - Sorting: Merge sort, quick sort, and heap sort are examples of sorting algorithms that use divide and conquer. They divide the input array into smaller subarrays, sort them recursively, and merge or rearrange them to obtain the sorted array.
  - Matrix multiplication: Strassen's algorithm is an example of matrix multiplication algorithm that uses divide and conquer. It divides the input matrices into smaller submatrices, performs some multiplications and additions on them recursively, and combines them to obtain the product matrix.
  - Convex hull: Graham scan and quick hull are examples of convex hull algorithms that use divide and conquer. They divide the input set of points into smaller subsets, find the convex hull of each subset recursively, and merge them to obtain the convex hull of the whole set.
  - Searching: Binary search and interpolation search are examples of searching algorithms that use divide and conquer. They divide the input sorted array into smaller subarrays, compare the target element with the middle or a suitable element of each subarray, and recursively search in the subarray that may contain the target element.

- Greedy method is a technique of making a locally optimal choice at each stage of a problem, hoping that it will lead to a globally optimal solution.
- Some examples of greedy algorithms are:
  - Optimal reliability allocation: This is a problem of allocating a given budget to increase the reliability of different components of a system, such that the overall system reliability is maximized. A greedy algorithm for this problem is to allocate the budget to the component that has the highest ratio of reliability improvement per unit cost at each stage, until the budget is exhausted or all components are fully reliable.
  - Knapsack: This is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized. A greedy algorithm for this problem is to sort the items by their value per unit weight in decreasing order, and pack them into the knapsack in that order, until the knapsack is full or all items are packed.
  - Minimum spanning tree: This is a problem of finding a subset of edges of a weighted undirected graph that connects all the vertices with the minimum total weight. A greedy algorithm for this problem is to sort the edges by their weight in increasing order, and add them to the spanning tree in that order, as long as they do not create a cycle, until all vertices are connected.
  - Single source shortest paths: This is a problem of finding the shortest paths from a given source vertex to all other vertices in a weighted directed graph. A greedy algorithm for this problem is to maintain a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined, ordered by their distance from the source. At each stage, the algorithm extracts the vertex with the minimum distance from the queue, adds it to the set, and updates the distances of its adjacent vertices in the queue, until the queue is empty or the destination vertex is extracted. Dijkstra's algorithm and Bellman Ford algorithm are two variants of this greedy algorithm, differing in how they handle negative edge weights.



### Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer  .
- Divide and conquer algorithms have three main steps: divide, conquer, and combine .
  - Divide: This step involves splitting the problem into smaller and simpler subproblems of the same type.
  - Conquer: This step involves solving the subproblems by calling the same algorithm recursively until they reach a base case, which can be solved directly.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure and properties .
- Some examples of divide and conquer algorithms are:
  - Sorting: Sorting algorithms like merge sort and quicksort use divide and conquer to sort an array of elements. They divide the array into two or more subarrays, sort them recursively, and then merge or partition them to get the sorted array .
  - Matrix multiplication: Matrix multiplication algorithms like Strassen's algorithm use divide and conquer to multiply two matrices. They divide the matrices into four submatrices, multiply them recursively using fewer operations than the naive method, and then combine them to get the product matrix .
  - Convex hull: Convex hull algorithms like Graham scan and quickhull use divide and conquer to find the convex hull of a set of points. They divide the points into two subsets, find the convex hull of each subset recursively, and then merge them to get the convex hull of the whole set.
  - Searching: Searching algorithms like binary search and interpolation search use divide and conquer to find an element in a sorted array. They divide the array into two halves, compare the element with the middle element, and then search in the appropriate half recursively until they find the element or conclude that it is not present .



### Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer technique again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure and properties.
- Some examples of divide and conquer algorithms are:
  - Binary search: This algorithm searches for a target value in a sorted array by repeatedly dividing the array into two halves and discarding the half that does not contain the target value.
  - Merge sort: This algorithm sorts an array by recursively dividing it into two halves, sorting each half, and merging the sorted halves.
  - Quick sort: This algorithm sorts an array by recursively choosing a pivot element, partitioning the array around the pivot, and sorting the two subarrays on either side of the pivot.
  - Strassen's algorithm: This algorithm multiplies two matrices by recursively dividing them into four submatrices each, computing seven products of submatrices, and combining them to get the final product.
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by recursively dividing the sequence into two halves, computing the transform of each half, and combining them using the butterfly operation.



### Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by recursively breaking it into smaller subproblems of the same type, until they become simple enough to be solved directly.
- The solutions of the subproblems are then combined to give a solution to the original problem.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
- Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same size and structure as the original problem.
- Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
- Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the problem size exponentially and exploit the structure of the problem.
- Some examples of divide and conquer algorithms are:

  - Merge sort: This algorithm sorts an array by dividing it into two halves, sorting each half recursively, and then merging the two sorted halves.
  - Quick sort: This algorithm sorts an array by choosing a pivot element, partitioning the array around the pivot, and then sorting the two subarrays recursively.
  - Binary search: This algorithm searches for a target value in a sorted array by comparing it with the middle element, and then recursively searching in the left or right subarray depending on the comparison result.
  - Strassen's algorithm: This algorithm multiplies two matrices by dividing them into four submatrices each, computing seven products of submatrices recursively, and then combining them to obtain the final product.
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by dividing it into two sequences of even and odd indices, computing their transforms recursively, and then combining them using the butterfly operation.
  - Convex hull: This algorithm finds the smallest convex polygon that contains a set of points in the plane by dividing the set into two halves, finding the hulls of each half recursively, and then merging the two hulls using the upper and lower tangent algorithm.



### Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a paradigm for designing algorithms that solve a problem by recursively breaking it into smaller subproblems, solving them, and combining their solutions .
- Divide and conquer algorithms have three steps:
  - Divide: Split the problem into smaller subproblems of the same type.
  - Conquer: Solve the subproblems recursively or directly if they are simple enough.
  - Combine: Merge the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, and can achieve lower time complexities than brute-force or iterative methods.
- Some examples of divide and conquer algorithms are:
  - Sorting: Merge sort and quicksort are two sorting algorithms that use divide and conquer. Merge sort divides the array into two halves, sorts them recursively, and then merges them in linear time. Quicksort partitions the array around a pivot element, sorts the two subarrays recursively, and then concatenates them .
  - Matrix multiplication: Strassen's algorithm is an efficient algorithm to multiply two matrices. A naive method to multiply two matrices needs three nested loops and is O(n^3). Strassen's algorithm divides each matrix into four submatrices, performs seven multiplications and some additions on them, and then combines them to get the final product. Strassen's algorithm reduces the time complexity to O(n^2.8974) .
  - Convex hull: The convex hull of a set of points is the smallest convex polygon that contains all the points. A divide and conquer algorithm to find the convex hull works as follows: Split the points into two halves by a vertical line, find the convex hull of each half recursively, and then merge the two hulls by finding the upper and lower tangents.
  - Searching: Binary search is a classic example of a divide and conquer algorithm. If we have a sorted array of data, we can find any element in the array using a divide and conquer process. We compare the element with the middle element of the array, and if they are equal, we return the index. If the element is smaller, we search in the left half of the array, and if it is larger, we search in the right half. We repeat this process until we find the element or the array is empty. Binary search reduces the time complexity from O(n) to O(log n) .



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods are simple, fast, and easy to implement, but they do not always guarantee the best possible solution. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that the optimal solution to a problem can be obtained by combining the optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be reached by making the locally optimal choice at each step.

Some examples of greedy methods are:

- Optimal reliability allocation: This problem involves allocating a given budget to improve the reliability of different components of a system, such that the overall system reliability is maximized. A greedy method for this problem is to allocate the budget to the component that has the highest marginal increase in reliability per unit cost at each step, until the budget is exhausted or all components are improved to the maximum possible level.
- Knapsack problem: This problem involves packing a knapsack with a given capacity with items that have different weights and values, such that the total value of the items in the knapsack is maximized. A greedy method for this problem is to sort the items by their value-to-weight ratio, and then pack the knapsack with the items in descending order of this ratio, until the knapsack is full or no more items are left.
- Minimum spanning tree: This problem involves finding a subset of edges in a weighted undirected graph that connects all the vertices with the minimum possible total edge weight. A greedy method for this problem is to start with an empty set of edges, and then add the edge with the smallest weight that does not form a cycle with the existing edges, until all the vertices are connected. This method is known as Prim's algorithm. Another greedy method for this problem is to sort the edges by their weights, and then add the edges in ascending order of their weights, as long as they do not form a cycle with the existing edges. This method is known as Kruskal's algorithm.
- Single source shortest path: This problem involves finding the shortest path from a given source vertex to every other vertex in a weighted directed graph. A greedy method for this problem is to maintain a set of vertices whose shortest distance from the source is known, and then select the vertex with the smallest distance from this set, and update the distances of its adjacent vertices based on the edge weights. This method is repeated until all the vertices are visited. This method is known as Dijkstra's algorithm. Another greedy method for this problem is to relax all the edges in the graph for a certain number of times, and then check if there are any negative cycles in the graph. This method is known as Bellman-Ford algorithm.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step, without considering the future consequences.

Some examples of greedy methods are:

- **Fractional Knapsack Problem**: Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, find the maximum value that can be obtained by filling the knapsack with fractions of items. The greedy choice is to pick the item with the highest value-to-weight ratio first, and then the next highest, and so on, until the knapsack is full or no more items are left.
- **Optimal Reliability Allocation Problem**: Given a system with n components, each with a reliability and a cost, and a budget B, find the optimal way to allocate the budget among the components to maximize the overall reliability of the system. The greedy choice is to allocate the budget to the component with the highest marginal reliability per unit cost first, and then the next highest, and so on, until the budget is exhausted or no more components are left.
- **Minimum Spanning Tree Problem**: Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. The greedy choice is to pick the edge with the lowest weight that does not form a cycle with the already selected edges, and then repeat until all the vertices are connected.
- **Single Source Shortest Path Problem**: Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex in the graph. The greedy choice is to pick the vertex with the lowest distance from the source that has not been visited yet, and then update the distances of its adjacent vertices, and then repeat until all the vertices are visited.
- **Activity Selection Problem**: Given a set of activities, each with a start and finish time, find the maximum number of activities that can be performed by a single person, assuming that a person can only work on one activity at a time. The greedy choice is to pick the activity with the earliest finish time first, and then the next earliest, and so on, as long as they do not overlap with the already selected activities.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step, without considering the future consequences.

Some examples of greedy methods are:

- Minimum spanning tree: A minimum spanning tree (MST) of a weighted undirected graph is a subset of edges that connects all the vertices with the minimum total weight. There are two well-known greedy algorithms to find the MST of a graph: Prim's algorithm and Kruskal's algorithm.

  - Prim's algorithm starts with an arbitrary vertex and grows the MST by adding the edge with the minimum weight that connects a vertex in the MST to a vertex outside the MST, until all the vertices are included.
  - Kruskal's algorithm starts with an empty set of edges and adds the edge with the minimum weight that does not create a cycle, until all the vertices are connected.

- Knapsack problem: The knapsack problem is to find the maximum value of items that can be packed into a knapsack with a given capacity. There are two variants of the knapsack problem: the 0-1 knapsack problem and the fractional knapsack problem.

  - The 0-1 knapsack problem assumes that each item can be either taken or left, and the goal is to maximize the total value of the taken items without exceeding the capacity of the knapsack. A greedy algorithm for this problem is to sort the items by their value-to-weight ratio and take the items with the highest ratio until the knapsack is full or no more items can be taken. This algorithm does not always give the optimal solution, but it gives a good approximation.
  - The fractional knapsack problem assumes that each item can be divided into smaller parts, and the goal is to maximize the total value of the items in the knapsack without exceeding the capacity. A greedy algorithm for this problem is to sort the items by their value-to-weight ratio and take as much as possible of the item with the highest ratio, then move to the next item with the next highest ratio, and so on, until the knapsack is full or no more items are available. This algorithm always gives the optimal solution.

- Single source shortest path: The single source shortest path problem is to find the shortest path from a given source vertex to every other vertex in a weighted directed graph. There are two well-known greedy algorithms to solve this problem: Dijkstra's algorithm and Bellman-Ford algorithm.

  - Dijkstra's algorithm maintains a set of vertices whose shortest distance from the source is known, and a priority queue of vertices whose shortest distance is tentative. It repeatedly extracts the vertex with the minimum tentative distance from the queue, updates the tentative distance of its adjacent vertices, and adds them to the queue, until the queue is empty or the destination is reached. This algorithm works only for graphs with non-negative edge weights.
  - Bellman-Ford algorithm iterates over all the edges of the graph and relaxes them, that is, updates the tentative distance of the destination vertex if it can be improved by using the edge. It repeats this process for |V| - 1 times, where |V| is the number of vertices in the graph. This algorithm works for graphs with negative edge weights, but not for graphs with negative cycles.



### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast and easy to implement, but they may not always guarantee the best solution.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: The optimal solution to the problem can be obtained by combining the optimal solutions to its subproblems.
  - Greedy choice property: A globally optimal solution can be reached by making a locally optimal (greedy) choice at each step, without considering the future consequences.
- Some examples of greedy methods are:

#### Single Source Shortest Paths - Dijkstra’s Algorithm
- This algorithm finds the shortest path from a given source vertex to all other vertices in a weighted graph, where the weights are non-negative.
- The algorithm maintains a set of visited vertices, and a set of unvisited vertices with their tentative distances from the source.
- The algorithm repeatedly selects the unvisited vertex with the smallest tentative distance, marks it as visited, and updates the tentative distances of its adjacent vertices by adding the weight of the edge.
- The algorithm terminates when all vertices are visited or when the smallest tentative distance among the unvisited vertices is infinity, indicating that there is no path to the remaining vertices.
- The algorithm can be implemented using a priority queue to store the unvisited vertices and their tentative distances, which allows selecting the minimum in O(log n) time, where n is the number of vertices.
- The time complexity of the algorithm is O((n + m) log n), where m is the number of edges, assuming a binary heap is used as the priority queue.

#### Single Source Shortest Paths - Bellman Ford Algorithm
- This algorithm also finds the shortest path from a given source vertex to all other vertices in a weighted graph, but it can handle negative weights, as long as there are no negative cycles (a cycle whose total weight is negative).
- The algorithm relaxes all the edges of the graph n - 1 times, where n is the number of vertices, by updating the tentative distance of the destination vertex if it can be improved by going through the source vertex and the edge weight.
- The algorithm can also detect negative cycles by performing one more relaxation and checking if any distance can be improved further. If so, then there is a negative cycle and the shortest path is not well-defined.
- The time complexity of the algorithm is O(nm), where n is the number of vertices and m is the number of edges.



## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure properties. It works by breaking down the problem into smaller subproblems, solving them once and storing their solutions, and then combining the solutions to obtain the optimal solution for the original problem.
- Knapsack problem is an example of a dynamic programming problem. It is a problem of packing a set of items, each with a weight and a value, into a knapsack with a limited capacity. The goal is to maximize the total value of the items in the knapsack without exceeding the capacity. The knapsack problem can be solved by using a two-dimensional array to store the optimal value for each subproblem of choosing a subset of items and a subcapacity of the knapsack. The optimal value for the original problem can be obtained by filling the array from bottom to top and right to left, using the recurrence relation:

  - `V[i][w] = max(V[i-1][w], V[i-1][w-wi] + vi)` if `wi <= w`
  - `V[i][w] = V[i-1][w]` otherwise

  where `V[i][w]` is the optimal value for choosing from the first `i` items and a knapsack capacity of `w`, `wi` and `vi` are the weight and value of the `i`-th item, respectively  .

- All pair shortest paths problem is another example of a dynamic programming problem. It is a problem of finding the shortest paths between every pair of vertices in a weighted graph. The problem can be solved by using a three-dimensional array to store the shortest distance for each subproblem of choosing a pair of vertices and an intermediate vertex. The shortest distance for the original problem can be obtained by filling the array from front to back and bottom to top, using the recurrence relation:

  - `D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j])`

  where `D[k][i][j]` is the shortest distance between vertices `i` and `j` using only the first `k` vertices as intermediate vertices  .

- Resource allocation problem is a problem of allocating a limited amount of resources to a number of independent activities in order to maximize the total profit or minimize the total cost. The problem can be solved by using a functional equation technique of dynamic programming. The idea is to define a function that represents the optimal value for each subproblem of allocating a certain amount of resources to a certain number of activities. The optimal value for the original problem can be obtained by solving the functional equation recursively or iteratively, using the principle of optimality   .

- Backtracking is a technique for solving problems that involve searching for a solution among a large number of possibilities. It works by exploring the solution space incrementally, making a choice at each step, and backtracking if the choice leads to a dead end or a suboptimal solution. Backtracking can be used to solve problems that have a goal test, a set of constraints, and a set of choices at each step.
- Travelling salesman problem is an example of a problem that can be solved by backtracking. It is a problem of finding the shortest tour that visits every city in a given set of cities exactly once and returns to the starting city. The problem can be solved by using a one-dimensional array to store the current tour, a variable to store the current length, and a variable to store the minimum length. The solution can be obtained by starting from an arbitrary city, choosing the next city to visit from the unvisited ones, updating the current tour and length, checking if the current tour is a complete tour or if the current length is already greater than the minimum length, and backtracking if necessary.

- Branch and bound is a technique for solving optimization problems that involve searching for a solution among a large number of possibilities. It works by exploring the solution space incrementally, making a choice at each step



### Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be formulated as recurrence relations, which express the solution of a problem in terms of the solutions of smaller instances of the same problem.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the intermediate results in a table or an array.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which can be stated as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given capacity and the total value is as large as possible.
  - The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, but not partially.
  - The 0/1 knapsack problem can be solved using dynamic programming by defining a function `f(i, w)` that returns the maximum value that can be obtained by using items from `1` to `i` with a weight limit of `w`.
  - The recurrence relation for `f(i, w)` is:

    - `f(i, w) = 0` if `i = 0` or `w = 0`
    - `f(i, w) = f(i - 1, w)` if `w < wi`
    - `f(i, w) = max(f(i - 1, w), f(i - 1, w - wi) + vi)` if `w >= wi`
  - Where `wi` and `vi` are the weight and value of the `i`-th item, respectively.
  - The base case of the recurrence is when there are no items or no weight limit, in which case the maximum value is zero.
  - The optimal solution of the problem is `f(n, W)`, where `n` is the number of items and `W` is the capacity of the knapsack.
  - The dynamic programming algorithm for the 0/1 knapsack problem can be implemented as follows:

    - Initialize a two-dimensional array `dp[n + 1][W + 1]` to store the values of `f(i, w)`.
    - For `i` from `0` to `n`, and for `w` from `0` to `W`, compute `dp[i][w]` according to the recurrence relation.
    - Return `dp[n][W]` as the optimal solution.
  - The time complexity of the dynamic programming algorithm is `O(nW)`, where `n` is the number of items and `W` is the capacity of the knapsack. The space complexity is also `O(nW)`, as we need to store the values of `f(i, w)` in a two-dimensional array.
  - An example of the 0/1 knapsack problem is:

    - Number of items `n = 4`, knapsack capacity `W = 5`, weights `(w1, w2, w3, w4) = (2, 3, 4, 5)` and values `(v1, v2, v3, v4) = (3, 4, 5, 6)`.
    - The dynamic programming table `dp` is:

      | i\w | 0 | 1 | 2 | 3 | 4 | 5 |
      | --- | - | - | - | - | - | - |
      | 0   | 0 | 0 | 0 | 0 | 0 | 0 |
      | 1   | 0 | 0 | 3 | 3 | 3 | 3 |
      | 2   | 0 | 0 | 3 | 4 | 4 | 7 |
      | 3   | 0 | 0 | 3 | 4 | 5 | 7 |
      | 4   | 0 | 0 | 3 | 4 | 5 | 7



Hello, I am Sydney, your AI assistant. I can help you with your topic of dynamic programming with examples such as all pair shortest paths, Warshal's and Floyd's algorithms, resource allocation problem, etc. Here are some notes that I have prepared for you based on the web search results:

### Dynamic Programming

- Dynamic programming is a technique of solving complex problems by breaking them down into smaller subproblems, and reusing the solutions of the subproblems to avoid repeated computations  .
- Dynamic programming can be applied to problems that have two main characteristics: optimal substructure and overlapping subproblems.
  - Optimal substructure means that the optimal solution of the original problem can be obtained by combining the optimal solutions of the subproblems.
  - Overlapping subproblems means that the same subproblems are encountered multiple times during the problem-solving process, and their solutions can be stored and reused to save time and space.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up .
  - Top-down approach starts with the original problem and recursively divides it into smaller subproblems until the base cases are reached. Then, the solutions of the subproblems are combined to obtain the solution of the original problem .
  - Bottom-up approach starts with the base cases and iteratively builds up the solutions of larger subproblems until the solution of the original problem is obtained. This approach usually uses a table or an array to store the solutions of the subproblems .
- Dynamic programming can be used to solve various types of problems, such as optimization, counting, decision making, etc. Some common examples of dynamic programming problems are:
  - Knapsack problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a knapsack so that the total weight is less than or equal to a given limit and the total value is as large as possible.
  - Coin change problem: Given an array of coin values and a target amount, find the minimum number of coins needed to make the change, or return -1 if it is not possible.
  - Longest common subsequence problem: Given two sequences, find the length of the longest subsequence that is common to both of them.
  - Matrix chain multiplication problem: Given a sequence of matrices, find the most efficient way to multiply them together. The cost of multiplying two matrices is equal to the number of scalar multiplications required.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- All pair shortest paths problem is to find the shortest distance between every pair of vertices in a weighted graph.
- Warshal's algorithm is a dynamic programming algorithm that can be used to find the transitive closure of a directed graph. The transitive closure of a graph is a graph that contains an edge from u to v if there is a path from u to v in the original graph.
- Warshal's algorithm works by iteratively adding intermediate vertices to the path between any two vertices, and updating the distance matrix accordingly. The algorithm runs in O(n^3) time, where n is the number of vertices in the graph.
- Floyd's algorithm is a dynamic programming algorithm that can be used to find the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively considering each vertex as an intermediate vertex, and updating the distance matrix accordingly. The algorithm runs in O(n^3) time, where n is the number of vertices in the graph.
- The pseudocode of Warshal's algorithm is:

```
function Warshal(G):
  // G is an n x n adjacency matrix of a directed graph
  // D is an n x n distance matrix, initialized to G
  D = G
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        // if there is a path from i to j through k, update D[i][j] to 1
        D[i][j] = D[i][j] or (D[i][k] and D[k][j])
  return D
```

- The pseudocode of Floyd's algorithm is:

```
function Floyd(G):
  // G is an n x n adjacency matrix of a weighted graph
  // D

```




### Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, and can be implemented using either a top-down (memoization) or a bottom-up (tabulation) approach.
- One example of a dynamic programming problem is the resource allocation problem, where a limited amount of resources (such as time, money, or materials) needs to be allocated to a number of activities (such as projects, tasks, or locations) in order to maximize the total return (such as profit, utility, or satisfaction).
- The resource allocation problem can be formulated as follows:

  - Let N be the number of activities, and let X be the total amount of resources available.
  - Let x_k be the amount of resources allocated to activity k, and let r_k(x_k) be the return function of activity k, which gives the return from allocating x_k resources to activity k.
  - The objective is to find the optimal allocation x* = (x*_1, x*_2, ..., x*_N) that maximizes the total return R(x) = sum_{k=1}^N r_k(x_k), subject to the constraint sum_{k=1}^N x_k <= X and x_k >= 0 for all k.

- The resource allocation problem can be solved using dynamic programming by defining a subproblem as follows:

  - Let R_k(x) be the maximum return that can be obtained by allocating x resources to the first k activities, and let x*_k be the optimal amount of resources allocated to activity k in this subproblem.
  - The base case is R_0(x) = 0 for all x, which means that no return can be obtained by allocating resources to zero activities.
  - The recursive relation is R_k(x) = max_{0 <= x_k <= x} {R_{k-1}(x - x_k) + r_k(x_k)} for k = 1, 2, ..., N, which means that the optimal return for allocating x resources to the first k activities is obtained by choosing the optimal amount of resources x_k to allocate to activity k, and adding it to the optimal return for allocating the remaining x - x_k resources to the first k - 1 activities.
  - The optimal solution is R_N(X), which gives the maximum return for allocating X resources to all N activities, and the optimal allocation x* can be obtained by tracing back the values of x*_k from the subproblems.

- An example of a resource allocation problem is the following:

  - Suppose there are three activities, A, B, and C, and 10 units of resources available.
  - The return functions of the activities are r_A(x) = 10x - x^2, r_B(x) = 12x - x^2, and r_C(x) = 15x - x^2, which are concave and have a maximum at x = 5, 6, and 7.5, respectively.
  - The optimal allocation can be found by using dynamic programming as follows:

    - R_0(x) = 0 for all x
    - R_1(x) = max_{0 <= x_1 <= x} {R_0(x - x_1) + r_A(x_1)} = max_{0 <= x_1 <= x} {10x_1 - x_1^2}
    - R_2(x) = max_{0 <= x_2 <= x} {R_1(x - x_2) + r_B(x_2)} = max_{0 <= x_2 <= x} {max_{0 <= x_1 <= x - x_2} {10x_1 - x_1^2} + 12x_2 - x_2^2}
    - R_3(x) = max_{0 <= x_3 <= x} {R_2(x - x_3) + r_C(x_3)} = max_{0 <= x_3 <= x} {max_{0 <= x_2 <= x - x_3} {max_{0 <= x_1 <= x - x_2 - x_3} {10x_1 - x_1^2



### Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization problems, such as finding the shortest path, the minimum cost, the maximum profit, etc. They both use a tree structure to represent the possible solutions and explore them in a systematic way. However, they differ in how they prune the tree and select the next node to visit.

#### Backtracking

- Backtracking is a technique that tries to find all possible solutions to a problem by building a partial solution and then extending it step by step.
- If the partial solution is found to be invalid or unsatisfactory, the algorithm backtracks to the previous step and tries a different option.
- Backtracking can be used to solve problems that have a finite number of solutions, such as the n-queen problem, the graph coloring problem, the Hamiltonian cycle problem, etc.
- Backtracking can be implemented using recursion or a stack data structure.
- The main advantage of backtracking is that it can find all possible solutions to a problem, and it can also find the optimal solution if there is one.
- The main disadvantage of backtracking is that it can be very time-consuming and memory-intensive, as it may explore a large number of nodes in the tree.

#### Branch and Bound

- Branch and bound is a technique that tries to find the optimal solution to a problem by building a partial solution and then bounding its value using some heuristic function.
- If the partial solution is found to be worse than the best known solution so far, the algorithm discards it and does not explore its children nodes.
- If the partial solution is found to be promising, the algorithm branches into its children nodes and repeats the process.
- Branch and bound can be used to solve problems that have a single optimal solution, such as the travelling salesman problem, the knapsack problem, the sum of subsets problem, etc.
- Branch and bound can be implemented using a priority queue data structure, where the nodes are ordered by their bound values.
- The main advantage of branch and bound is that it can find the optimal solution to a problem, and it can also reduce the search space by pruning the nodes that are guaranteed to be worse than the optimal solution.
- The main disadvantage of branch and bound is that it can be very sensitive to the choice of the bounding function, as a poor bound may lead to exploring many unnecessary nodes.

#### Examples

##### Travelling Salesman Problem

- The travelling salesman problem (TSP) is a problem of finding the shortest possible tour that visits each city exactly once and returns to the starting point.
- The TSP is an NP-hard problem, meaning that there is no known polynomial-time algorithm that can solve it optimally.
- One way to solve the TSP using backtracking is to generate all possible permutations of the cities and calculate their tour lengths, and then choose the shortest one.
- One way to solve the TSP using branch and bound is to use a lower bound function that estimates the minimum possible tour length from a given partial solution, and then discard the nodes that have a higher bound than the best known solution so far.

##### Graph Coloring Problem

- The graph coloring problem (GCP) is a problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color, and using the minimum number of colors possible.
- The GCP is an NP-hard problem, meaning that there is no known polynomial-time algorithm that can solve it optimally.
- One way to solve the GCP using backtracking is to assign colors to the vertices one by one, and check if the color is valid for each vertex. If the color is invalid, the algorithm backtracks and tries a different color. If the color is valid, the algorithm moves to the next vertex and repeats the process.
- One way to solve the GCP using branch and bound is to use an upper bound function that estimates the maximum number of colors needed from a given partial solution, and then discard the nodes that have a higher bound than the best known solution so far.



### Backtracking, Branch and Bound with Examples Such as Graph Coloring

- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large number of possibilities. It works by trying out different choices and undoing them if they lead to a dead end or an infeasible solution. Backtracking can be applied to problems that can be formulated as finding a path in a state space tree, where each node represents a partial solution and each edge represents a choice or a decision .
- Branch and bound is a technique to solve optimization problems, where the goal is to find the best solution among a large number of possibilities. It works by exploring the state space tree in a systematic way, using bounds or estimates to prune branches that cannot lead to a better solution than the current best one. Branch and bound can be applied to problems that can be formulated as finding a path in a state space tree, where each node represents a partial solution and each edge represents a choice or a decision.
- Graph coloring is a problem of assigning colors to the vertices of a graph, such that no two adjacent vertices have the same color. Graph coloring can be used to model various real-world problems, such as scheduling, map coloring, register allocation, etc. Graph coloring can be solved using both backtracking and branch and bound techniques  .

#### Example of Graph Coloring using Backtracking

- Given a graph G and a number of colors m, the problem is to find a way to color the vertices of G using at most m colors, such that no two adjacent vertices have the same color.
- A possible algorithm using backtracking is as follows:

```
# Input: A graph G, a number of colors m, an array color of size n (number of vertices in G)
# Output: A boolean value indicating whether a valid coloring exists or not, and the color array with the assigned colors

def graphColoring(G, m, color, v):
  # Base case: If all vertices are colored, return true
  if v == n:
    return true
  
  # Try different colors for the current vertex
  for c in range(1, m+1):
    # Check if the color c is safe for the current vertex
    if isSafe(G, color, v, c):
      # Assign the color c to the current vertex
      color[v] = c
      # Recursively try to color the next vertex
      if graphColoring(G, m, color, v+1):
        return true
      # If coloring the next vertex fails, backtrack and undo the color assignment
      color[v] = 0
  
  # If no color can be assigned to the current vertex, return false
  return false

def isSafe(G, color, v, c):
  # Check if any adjacent vertex of v has the same color c
  for u in range(n):
    if G[v][u] == 1 and color[u] == c:
      return false
  # If no adjacent vertex has the same color, return true
  return true
```

- The algorithm starts from the first vertex and tries to assign a color from 1 to m. If the color is safe, meaning it does not conflict with any adjacent vertex, it moves to the next vertex and repeats the process. If the color is not safe, it tries another color. If no color is safe, it backtracks to the previous vertex and tries a different color. The algorithm terminates when either all vertices are colored or no valid coloring exists.
- The time complexity of the algorithm is O(m^n), where n is the number of vertices and m is the number of colors. The space complexity is O(n), where n is the number of vertices.



### Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- Backtracking can be applied to problems that can be formulated as a state space tree, where each node represents a partial solution and each edge represents a possible extension of the solution. 
- The backtracking algorithm traverses the state space tree in a depth-first manner, exploring one branch of the tree until it reaches a dead end or a solution, and then backtracks to the previous node and tries another branch. 
- The backtracking algorithm can be generalized by the following pseudocode: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate, reject(P, c) is a function that returns true if c is not a valid partial solution, accept(P, c) is a function that returns true if c is a complete and valid solution, output(P, c) is a function that prints or stores the solution, first(P, c) is a function that returns the first extension of c, and next(P, c) is a function that returns the next extension of c after s. 
- The functions reject, accept, first, and next depend on the specific problem and the representation of the candidates. They can be implemented using various techniques, such as pruning, bounding, heuristics, or symmetry breaking. 
- One example of a problem that can be solved by backtracking is the n-queen problem, where the goal is to place n queens on an n×n chessboard such that no two queens attack each other. 
- A possible representation of a candidate is a one-dimensional array of size n, where each element denotes the column number of the queen in the corresponding row. For example, [2, 4, 1, 3] represents a solution for n = 4, where the queens are placed at (1, 2), (2, 4), (3, 1), and (4, 3). 
- The function reject can check if the current candidate violates the constraint of no two queens attacking each other by comparing the column and diagonal values of the last queen with the previous ones. The function accept can check if the current candidate is a complete solution by verifying if the array is filled with n values. The function first can return the first possible column value for the next row, which is 1. The function next can return the next possible column value for the same row, which is the previous value plus 1, until it reaches n. 
- The following is a possible implementation of the backtracking algorithm for the n-queen problem in Python: 

```python
def backtrack(n, c):
    if reject(n, c):
        return
    if accept(n, c):
        output(n, c)
    s = first(n, c)
    while s != None:
        backtrack(n, s)
        s = next(n, s)

def reject(n, c):
    # check if the last queen conflicts with any previous one
    k = len(c) - 1
    for i in range(k):
        if c[i] == c[k] or abs(c[i] - c[k]) == k - i:
            return True
    return False

def accept(n, c):
    # check if the array is complete
    return len(c) == n

def output(n, c):
    # print the solution
    print(c)

def first(n, c):
    # return the first column value for the next row
    return [1]

def next(n, s):
    # return the next column value for the

```




### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm reduces the problem to the call `backtrack(root(P))`, where `backtrack` is the following recursive procedure: 

```python
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- The procedure `backtrack` takes two arguments: a problem instance `P` and a partial candidate `c`. The procedure `reject` tests whether the partial candidate is worth completing, and returns `true` if it is not. The procedure `accept` tests whether the partial candidate is a solution, and returns `true` if it is. The procedure `output` prints or stores the solution. The procedure `first` generates the first extension of the partial candidate, and `next` generates the next extension after a given one. If there are no more extensions, `next` returns `NULL`.
- Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems. 
- A Hamiltonian cycle (or Hamiltonian circuit) is a cycle in an undirected graph that visits each vertex exactly once and also returns to the starting vertex. Finding a Hamiltonian cycle in a given graph is an NP-complete problem. 
- One way to find a Hamiltonian cycle in a graph is to use backtracking. The idea is to start from any vertex and keep adding adjacent vertices to the current path until either all vertices are visited or there is no more adjacent vertex to extend the path. If all vertices are visited, then check if there is an edge from the last vertex to the first vertex to complete the cycle. If there is no such edge, then backtrack and remove the last vertex from the path and try another adjacent vertex. If there is no more adjacent vertex to extend the path, then backtrack and remove the last vertex from the path and try another adjacent vertex. Repeat this process until either a Hamiltonian cycle is found or all possible paths are exhausted. 
- The following is a pseudocode for finding a Hamiltonian cycle using backtracking: 

```python
# Assume that the graph is represented by an adjacency matrix adj
# Assume that n is the number of vertices in the graph
# Assume that path is an array of size n to store the current path
# Assume that pos is the current position in the path array
# Assume that v is the current vertex to be added to the path

procedure hamiltonian(v, pos) is
    # Base case: all vertices are visited
    if pos == n then
        # Check if there is an edge from the last vertex to the first vertex
        if adj[v][path[0]] == 1 then
            # A Hamiltonian cycle is found
            output(path)
            return true
        else
            # No Hamiltonian cycle is possible
            return false
    # Recursive case: try all possible extensions of the current path
    for u in range(n) do
        # Check if u is adjacent to v and not already in the path
        if adj[v][u] == 1 and u not in path[0..pos-1] then
            # Add u to the path
            path[pos] = u
            # Recursively extend the path from u
            if hamiltonian(u, pos+1) then
                return true
            # Backtrack and remove u from the path
            path[pos] = -1
    # No extension is possible
    return false

# Start from any vertex as the first vertex in the path

```




### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be visualized as a state space tree, where each node represents a partial solution, and the root node represents an empty solution. The algorithm explores the tree by visiting the nodes in a depth-first manner, and prunes the branches that cannot lead to a valid solution.
- A backtracking algorithm consists of the following steps :
  - Define a procedure `backtrack(P, c)` that takes a problem `P` and a candidate solution `c` as inputs.
  - If `c` is a reject, then return without any further action.
  - If `c` is an accept, then output `c` as a solution and return.
  - Let `s` be the first extension of `c` for `P`.
  - While `s` is not null, do the following:
    - Call `backtrack(P, s)` recursively.
    - Let `s` be the next extension of `c` for `P`.
- An example of a backtracking problem is the sum of subsets problem, where we are given a set of positive integers `S` and a target sum `T`, and we want to find all the subsets of `S` that add up to `T`.
- A possible solution to the sum of subsets problem using backtracking is as follows:
  - Define a problem `P` that consists of the set `S`, the target sum `T`, and a current sum `C`.
  - Define a candidate solution `c` that consists of a subset of `S` and a boolean array `A` that indicates which elements of `S` are included in the subset.
  - Define a reject condition as `C > T`, which means that the current sum exceeds the target sum.
  - Define an accept condition as `C == T`, which means that the current sum equals the target sum.
  - Define a first extension of `c` as adding the next element of `S` to the subset, and updating `C` and `A` accordingly.
  - Define a next extension of `c` as removing the last element of `S` from the subset, and updating `C` and `A` accordingly.
  - Call `backtrack(P, c)` with an empty subset and a zero current sum as the initial candidate solution.



## Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A decision problem is NP-complete if it satisfies two conditions:
  - It is in NP, which means that there is a polynomial-time algorithm that can verify a given solution to the problem.
  - It is NP-hard, which means that any other problem in NP can be reduced to it in polynomial time, using a transformation that preserves the yes or no answer.
- NP-complete problems are believed to be very hard to solve, as no polynomial-time algorithm is known for any of them, and it is widely conjectured that none exists. If one NP-complete problem can be solved in polynomial time, then all NP problems can be solved in polynomial time, which would imply that P = NP, a major open question in computer science.
- Some examples of NP-complete problems are:
  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine whether the vertices of the graph can be assigned k different colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
  - Hamiltonian Cycle: Given a graph, determine whether there is a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target sum, determine whether there is a subset of the set that adds up to the target sum.

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function. An approximation algorithm does not guarantee the optimal solution, but rather a solution that is close to the optimal one, within some factor or bound  .
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, by sacrificing some accuracy for efficiency. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution obtained by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm.
- Some examples of approximation algorithms are:
  - TSP: A 2-approximation algorithm is to find a minimum spanning tree of the given graph, and then traverse the tree in a depth-first order, skipping any visited vertices. This produces a tour that is at most twice as long as the optimal one.
  - Graph Coloring: A simple approximation algorithm is to assign colors to the vertices in any order, using the smallest available color for each vertex. This produces a coloring that uses at most one more color than the optimal one.
  - n-Queen Problem: A heuristic approximation algorithm is to place queens on the main diagonal of the board, and then try to move them to different positions that do not cause conflicts, using a local search technique. This may produce a feasible solution, but it is not guaranteed to do so.
  - Hamiltonian Cycle: A 2-approximation algorithm is to find a minimum spanning tree of the given graph, and then double each edge of the tree. This produces a cycle that visits each vertex exactly twice, and has a length that is at most twice as long as the optimal one.
  - Sum of Subsets: A greedy approximation algorithm is to sort the given set in decreasing order, and then select the elements one by one, as long as the partial sum does not exceed the target sum. This produces a subset that is as close as possible to the target sum, but it may not be the optimal one.



### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the difficulty of solving certain problems in polynomial time. A problem is said to be NP-complete if it belongs to the class NP (meaning that a solution can be verified in polynomial time) and every other problem in NP can be reduced to it in polynomial time (meaning that a solution to the other problem can be transformed into a solution to the NP-complete problem in polynomial time) .
- NP-complete problems are believed to be intractable, meaning that there is no efficient algorithm that can solve them in polynomial time. Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets .
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. Optimization problems are those that seek to find the best solution among a set of feasible solutions, according to some objective function. For example, the Travelling Salesman Problem is to find the shortest tour that visits every city in a given set exactly once .
- Approximation Algorithms do not guarantee the best solution, but they aim to come as close as possible to the optimal solution in polynomial time. They usually provide a performance guarantee, which is a ratio between the value of the solution obtained by the algorithm and the value of the optimal solution. For example, a 2-approximation algorithm for the Travelling Salesman Problem guarantees that the length of the tour found by the algorithm is at most twice the length of the optimal tour .
- Approximation Algorithms are some of the most clever and sophisticated algorithms around, and they are useful for many practical applications where finding the optimal solution is too costly or impossible. Some examples of approximation algorithms for NP-complete problems are: a 2-approximation algorithm for the Vertex Cover problem , a 7/8-approximation algorithm for the Max 3-SAT problem , a 2-approximation algorithm for the Graph Coloring problem , a 2-approximation algorithm for the n-Queen Problem , a 2-approximation algorithm for the Hamiltonian Cycle problem , and a 1/2-approximation algorithm for the Sum of Subsets problem .



### NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, given a certificate or a witness for the answer. A problem is NP-complete if it is NP and every other NP problem can be reduced to it in polynomial time. NP-complete problems are believed to be the hardest problems in NP, and no efficient algorithm is known to solve them in the worst case.
- Approximation Algorithms are a way of coping with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. An approximation algorithm does not guarantee the optimal solution, but it tries to come as close as possible to it in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution obtained by the algorithm and the value of the optimal solution  .
- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point. This problem is NP-complete, and the best known approximation algorithm has a ratio of 1.5, which means that the tour found by the algorithm is at most 1.5 times longer than the optimal tour.
  - Graph Coloring: Given an undirected graph, assign a color to each vertex such that no two adjacent vertices have the same color, and use the minimum number of colors possible. This problem is NP-complete, and the best known approximation algorithm has a ratio of O(log n), where n is the number of vertices in the graph. This means that the number of colors used by the algorithm is at most O(log n) times larger than the optimal number of colors.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem is NP-complete, and the best known approximation algorithm has a ratio of 2, which means that the number of queens placed by the algorithm is at most twice the optimal number of queens.
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting point. This problem is NP-complete, and the best known approximation algorithm has a ratio of 2, which means that the length of the cycle found by the algorithm is at most twice the length of the optimal cycle.
  - Sum of Subsets: Given a set of positive integers and a target value, find a subset of the set that sums up to the target value, or report that no such subset exists. This problem is NP-complete, and the best known approximation algorithm has a ratio of 2, which means that the sum of the subset found by the algorithm is at most twice the target value.



### NP-Completeness and Approximation Algorithms with Examples Such as n-Queen Problem for the notes of the Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, given a certificate or a witness for the answer. A problem is NP-complete if it is NP and every other NP problem can be reduced to it in polynomial time.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. An approximation algorithm does not guarantee the best solution, but it tries to come as close as possible to the optimal solution in polynomial time  .
- Examples of NP-complete optimization problems are Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. These problems have no known polynomial time algorithms to find the optimal solution, but they have approximation algorithms that can find near-optimal solutions in polynomial time.
- Travelling Salesman Problem (TSP) is the problem of finding the shortest tour that visits every city in a given set of cities and returns to the starting city. An approximation algorithm for TSP is the nearest neighbor algorithm, which starts from a random city and always visits the nearest unvisited city until all cities are visited. This algorithm has a performance ratio of 2, which means that the length of the tour found by the algorithm is at most twice the length of the optimal tour.
- Graph Coloring is the problem of assigning colors to the vertices of a graph such that no two adjacent vertices have the same color. The goal is to use the minimum number of colors. An approximation algorithm for graph coloring is the greedy algorithm, which assigns colors to the vertices in any order, using the smallest available color that does not conflict with any of the previously colored neighbors. This algorithm has a performance ratio of ∆ + 1, where ∆ is the maximum degree of the graph.
- n-Queen Problem is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. The goal is to find any valid placement. An approximation algorithm for n-Queen Problem is the backtracking algorithm, which tries to place a queen in each row, starting from the first row. If a conflict occurs, it backtracks to the previous row and tries a different column. This algorithm can find a solution in polynomial time if one exists.
- Hamiltonian Cycle is the problem of finding a cycle that visits every vertex of a graph exactly once and returns to the starting vertex. The goal is to find any such cycle. An approximation algorithm for Hamiltonian Cycle is the Christofides algorithm, which works for graphs that are complete and have non-negative edge weights. The algorithm first finds a minimum spanning tree of the graph, then adds the minimum number of edges to make the tree Eulerian, and then follows the Eulerian tour to get a Hamiltonian cycle. This algorithm has a performance ratio of 3/2, which means that the length of the cycle found by the algorithm is at most 3/2 times the length of the optimal cycle.
- Sum of Subsets is the problem of finding a subset of a given set of positive integers that sums up to a given target value. The goal is to find any such subset. An approximation algorithm for Sum of Subsets is the greedy algorithm, which sorts the integers in descending order and adds them to the subset until the sum is equal to or exceeds the target value. This algorithm can find a solution in polynomial time if one exists.



### NP-Completeness and Approximation Algorithms with Examples Such as Hamiltonian Cycles

- NP-Completeness is a concept that relates to the difficulty of solving certain problems in polynomial time. A problem is said to be NP-complete if it belongs to the class NP (meaning that a solution can be verified in polynomial time) and every other problem in NP can be reduced to it in polynomial time (meaning that a solution to the other problem can be transformed into a solution to the NP-complete problem in polynomial time).
- NP-complete problems are believed to be intractable, meaning that there is no efficient algorithm that can solve them in polynomial time. Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. Optimization problems are those that seek to find the best solution among a set of feasible solutions, according to some objective function. For example, the Travelling Salesman Problem seeks to find the shortest tour that visits every city in a given set of cities exactly once.
- Approximation Algorithms do not guarantee the best solution, but they aim to come as close as possible to the optimal solution in polynomial time. They usually provide a performance guarantee, which is a ratio between the value of the solution obtained by the algorithm and the value of the optimal solution. For example, a 2-approximation algorithm for the Vertex Cover problem guarantees that the size of the vertex cover found by the algorithm is at most twice the size of the minimum vertex cover.
- Some examples of Approximation Algorithms for NP-complete problems are:

  - Travelling Salesman Problem: A simple approximation algorithm for this problem is to find a minimum spanning tree of the given graph, and then traverse it in a depth-first order, skipping any visited vertices. This algorithm produces a tour that is at most twice the length of the optimal tour.
  - Graph Coloring: A simple approximation algorithm for this problem is to order the vertices of the graph arbitrarily, and then assign each vertex the smallest available color that does not conflict with any of its previously colored neighbors. This algorithm produces a coloring that uses at most one more color than the minimum number of colors needed to color the graph.
  - n-Queen Problem: A simple approximation algorithm for this problem is to place the queens on the main diagonal of the n x n chessboard, starting from the top-left corner. This algorithm produces a placement that has at most n - 1 conflicts, where a conflict occurs when two queens attack each other.
  - Hamiltonian Cycles: A simple approximation algorithm for this problem is to find a minimum spanning tree of the given graph, and then find an Eulerian circuit of the tree, which is a cycle that visits every edge exactly once. This algorithm produces a cycle that visits every vertex at least once, and has the same length as the minimum spanning tree.
  - Sum of Subsets: A simple approximation algorithm for this problem is to sort the given set of positive integers in decreasing order, and then select the elements one by one, as long as the sum of the selected elements does not exceed the given target value. This algorithm produces a subset that has the largest possible sum that does not exceed the target value.



### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, meaning that given a solution, we can check if it is correct in a number of steps that is proportional to some power of the input size. A problem is NP-complete if it is NP and also every other NP problem can be reduced to it in polynomial time, meaning that we can transform any instance of any NP problem into an instance of the NP-complete problem such that the answer is the same. NP-complete problems are believed to be the hardest problems in NP, and no polynomial time algorithm is known for any of them. Examples of NP-complete problems are Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets .

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones according to some objective function. An approximation algorithm does not guarantee the best solution, but rather a solution that is close to the optimal one in some sense. The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, which is at most proportional to some power of the input size. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm. Examples of approximation algorithms are the 2-approximation algorithm for Vertex Cover, the 7/8-approximation algorithm for Max 3-SAT, and the Christofides algorithm for Travelling Salesman Problem   .

- Travelling Salesman Problem (TSP) is an optimization problem that asks to find the shortest tour that visits a given set of cities and returns to the starting point. The tour must visit each city exactly once. TSP is NP-complete, meaning that no polynomial time algorithm is known to solve it exactly. However, there are approximation algorithms that can find near-optimal tours in polynomial time. One such algorithm is the Christofides algorithm, which works as follows:

  - Find a minimum spanning tree of the given graph, which is a tree that connects all the vertices with the minimum total edge weight.
  - Find a minimum weight perfect matching of the odd-degree vertices in the tree, which is a set of edges that pairs up the vertices with odd degree such that the total edge weight is minimized.
  - Combine the tree and the matching to form an Eulerian graph, which is a graph that has an Eulerian circuit, which is a cycle that visits every edge exactly once.
  - Find an Eulerian circuit of the Eulerian graph, and shortcut it to obtain a Hamiltonian cycle, which is a cycle that visits every vertex exactly once.
  - Return the Hamiltonian cycle as the tour.

  The Christofides algorithm has an approximation ratio of 3/2, meaning that the tour found by the algorithm is at most 3/2 times longer than the optimal tour.

- Graph Coloring is an optimization problem that asks to assign colors to the vertices of a given graph such that no two adjacent vertices have the same color, and the number of colors used is minimized. Graph Coloring is NP-complete, meaning that no polynomial time algorithm is known to find the minimum number of colors needed for any graph. However, there are approximation algorithms that can find near-optimal colorings in polynomial time. One such algorithm is the greedy algorithm, which works as follows:

  - Order the vertices of the graph in some arbitrary way.
  - For each vertex in the order, assign it the smallest available color that does not conflict with any of its neighbors.
  - Return the coloring obtained.

  The greedy algorithm has an approximation ratio of O(log n), meaning that the number of colors used by the algorithm is at most proportional to the logarithm of the number of vertices in the graph.

- n-Queen Problem is a decision problem that asks if it is possible to place n queens on an n x n chessboard such that no two queens attack each other, meaning that no two queens share the same row, column, or diagonal.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

### NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science.
- Some examples of NP-complete problems are: SAT (satisfiability of boolean formulas), 3-SAT (satisfiability of boolean formulas in conjunctive normal form with at most three literals per clause), CLIQUE (finding a complete subgraph of a given size in a graph), VERTEX COVER (finding a minimum set of vertices that cover all the edges in a graph), HAMILTONIAN CYCLE (finding a cycle that visits every vertex exactly once in a graph), TRAVELLING SALESMAN PROBLEM (finding a minimum cost tour that visits every city exactly once in a graph), SUBSET SUM (finding a subset of numbers that add up to a given target), KNAPSACK (finding a subset of items that maximize the total value without exceeding the total weight), GRAPH COLORING (assigning colors to the vertices of a graph such that no two adjacent vertices have the same color), N-QUEEN (placing n queens on an n x n chessboard such that no two queens attack each other).

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function.
- An approximation algorithm is a polynomial time algorithm that produces a solution that is close to the optimal one, within some guaranteed factor or bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, without necessarily finding it.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution. For minimization problems, the approximation ratio is the maximum ratio over all instances, and for maximization problems, it is the minimum ratio over all instances.
- An approximation algorithm is called a r-approximation algorithm if its approximation ratio is at most r for minimization problems, or at least r for maximization problems. For example, a 2-approximation algorithm for the VERTEX COVER problem is an algorithm that finds a vertex cover that is at most twice as large as the minimum vertex cover.
- Some examples of approximation algorithms are: a 2-approximation algorithm for the VERTEX COVER problem, which selects a vertex cover by repeatedly choosing an arbitrary edge and adding both its endpoints to the cover, until no edges remain; a 7/8-approximation algorithm for the MAX 3-SAT problem, which assigns a random truth value to each variable and satisfies at least 7/8 of the clauses in expectation; a 2-approximation algorithm for the TRAVELLING SALESMAN PROBLEM, which finds a minimum spanning tree of the graph and doubles its edges to form a tour; a (1 + 1/k)-approximation algorithm for the KNAPSACK problem, which rounds down the weights and values of the items to the nearest multiple of W/k, where W is the knapsack capacity and k is a parameter, and then solves the modified problem exactly using dynamic programming; a (2 - 2/(k + 1))-approximation algorithm for the GRAPH COLORING problem,

