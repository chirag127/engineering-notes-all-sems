

## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- **Algorithms**: A sequence of steps or rules that can be followed to solve a problem or perform a task. An algorithm can be expressed in natural language, pseudocode, flowchart, or programming language.
- **Analyzing Algorithms**: The process of determining the efficiency and correctness of an algorithm, based on the resources it uses (such as time and space) and the output it produces (such as accuracy and reliability).
- **Complexity of Algorithms**: A measure of how the resource usage of an algorithm varies with the size of the input. Complexity can be expressed in terms of worst-case, average-case, or best-case scenarios. Complexity can also be classified into time complexity (how long the algorithm takes to run) and space complexity (how much memory the algorithm uses).
- **Growth of Functions**: A way of comparing the complexity of different algorithms by using mathematical notation and asymptotic analysis. Growth of functions can be expressed in terms of big O, big Omega, big Theta, or little o notation, which indicate the upper bound, lower bound, tight bound, or strict upper bound of the complexity, respectively.
- **Performance Measurements**: A way of evaluating the actual running time and space usage of an algorithm on a specific machine or platform, using empirical methods such as experiments, benchmarks, or simulations.
- **Sorting and Order Statistics**: Sorting is the process of arranging a collection of items (such as numbers, words, or records) in a certain order (such as ascending, descending, or alphabetical). Order statistics are the values that occupy certain positions in a sorted collection, such as the minimum, maximum, median, or kth smallest or largest element.
- **Shell Sort**: A sorting algorithm that is based on the insertion sort algorithm, but avoids large shifts by sorting elements that are far apart from each other first, and then reducing the gap between them until it becomes one. Shell sort uses a sequence of intervals (such as N/2, N/4, ...1) to determine which elements to compare and swap. Shell sort is an in-place and unstable algorithm, with a worst-case time complexity of O(N^2) and a best-case time complexity of O(N log N), depending on the choice of intervals.
- **Quick Sort**: A sorting algorithm that is based on the divide-and-conquer strategy, where the collection is partitioned into two subcollections around a pivot element, such that all the elements in the left subcollection are smaller than or equal to the pivot, and all the elements in the right subcollection are larger than or equal to the pivot. Then, the subcollections are recursively sorted until the base case of one or zero elements is reached. Quick sort is an in-place and unstable algorithm, with a worst-case time complexity of O(N^2) and an average-case and best-case time complexity of O(N log N), depending on the choice of pivot.
- **Merge Sort**: A sorting algorithm that is also based on the divide-and-conquer strategy, where the collection is divided into two equal or nearly equal subcollections, which are recursively sorted until the base case of one or zero elements is reached. Then, the subcollections are merged back together in a sorted order by comparing the first elements of each subcollection and taking the smaller one. Merge sort is a stable algorithm, but not an in-place algorithm, as it requires an auxiliary array to store the merged subcollections. Merge sort has a time complexity of O(N log N) in all cases, and a space complexity of O(N).
- **Heap Sort**: A sorting algorithm that is based on the heap data structure, which is a complete binary tree where each node is larger than or equal to its children (max-heap) or smaller than or equal to its children (min-heap). Heap sort first builds a max-heap or a min-heap from the collection, and then repeatedly swaps the root element with the last element in the heap, and reduces the size of the heap by one, until the heap is empty. Heap sort is an in-place and unstable algorithm, with a time complexity of O(N log N) in all cases, and a space complexity of O(1).
- **Comparison of Sorting Algorithms**: Different sorting algorithms have different advantages and disadvantages, depending on the characteristics of the collection to be sorted, such as the size, the range, the distribution, the order, and the type of the



### Algorithms for the notes of the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time.

- An algorithm is a finite sequence of well-defined instructions that solves a problem or performs a task.
- Analyzing algorithms is the process of determining the amount of resources (such as time and space) that an algorithm consumes when executed on a given input.
- Complexity of algorithms is the measure of how the resource consumption of an algorithm grows as the input size increases.
- Growth of functions is the mathematical notation that describes how a function behaves asymptotically, that is, when the input size approaches infinity.
- Performance measurements are the empirical methods of evaluating the efficiency and correctness of algorithms, such as running time, memory usage, and output quality.
- Sorting and order statistics are two related problems that deal with arranging a sequence of items in a particular order or finding the item that occupies a certain position in the sequence.
- Shell sort is a sorting algorithm that improves the performance of insertion sort by dividing the sequence into sub-sequences and sorting them using insertion sort, then combining the sorted sub-sequences.
- Quick sort is a sorting algorithm that uses the divide-and-conquer technique to partition the sequence into two sub-sequences based on a pivot element, then recursively sort the sub-sequences.
- Merge sort is a sorting algorithm that uses the divide-and-conquer technique to split the sequence into two sub-sequences, then recursively sort the sub-sequences and merge them into one sorted sequence.
- Heap sort is a sorting algorithm that uses a data structure called a heap to store the sequence and repeatedly extract the maximum or minimum element from the heap and place it at the end or the beginning of the sorted sequence.
- Comparison of sorting algorithms is the process of evaluating the advantages and disadvantages of different sorting algorithms based on various criteria, such as time complexity, space complexity, stability, adaptability, and simplicity.
- Sorting in linear time is the possibility of sorting a sequence of items in O(n) time, where n is the size of the input, by using algorithms that do not rely on comparisons, such as counting sort, radix sort, and bucket sort.



### Analyzing Algorithms

- Analyzing algorithms is the process of finding the **computational complexity** of algorithms, which is the amount of time, storage, or other resources needed to execute them .
- The computational complexity of an algorithm is usually expressed as a **function** of the length of its input, denoted by **n**. For example, an algorithm that takes **n** steps to sort an array of length **n** has a time complexity of **O(n)**, where **O** is the **big-O notation** that represents the upper bound of the function .
- Analyzing algorithms is important for several reasons:
  - To **predict** the behavior of an algorithm without implementing it on a specific computer.
  - To **compare** the efficiency of different algorithms for the same problem.
  - To **design** better algorithms that use fewer resources or solve more problems.
- Analyzing algorithms involves two steps:
  - **Modeling** the algorithm by identifying its basic operations and counting how many times they are executed for a given input size.
  - **Simplifying** the model by using asymptotic analysis, which focuses on the dominant term of the function and ignores lower-order terms and constant factors.
- Analyzing algorithms also requires **verifying** the correctness of the algorithm, which means proving that it always produces the correct output for any valid input. One way to verify an algorithm is by using a **proof by induction**, which is a technique that shows that the algorithm works for a base case and then for any larger case.



### Complexity of Algorithms

- Complexity of an algorithm is a measure of how long an algorithm would take to complete given an input of size n.
- Complexity is calculated asymptotically as n approaches infinity, to estimate the worst-case or average-case scenario.
- Complexity is about the algorithm itself, not the actual execution time or the hardware used.
- Complexity is expressed using the big O notation, which indicates the order of growth of an algorithm's running time or space requirement as a function of n .
- For example, an algorithm that has a complexity of O(n) means that its running time or space requirement increases linearly with the input size n.
- Complexity can be classified into two types: time complexity and space complexity.
  - Time complexity is the amount of time required by an algorithm to solve a problem, measured by counting the number of elementary operations performed by the algorithm .
  - Space complexity is the amount of memory or storage required by an algorithm to solve a problem, measured by counting the number of bits or bytes used by the algorithm .
- Complexity can also be analyzed in terms of the best case, worst case, and average case scenarios .
  - Best case is the scenario where the algorithm performs the minimum number of operations or uses the minimum amount of space for a given input .
  - Worst case is the scenario where the algorithm performs the maximum number of operations or uses the maximum amount of space for a given input .
  - Average case is the scenario where the algorithm performs an average number of operations or uses an average amount of space for a given input .
- Complexity of an algorithm is important for designing efficient and scalable algorithms that can solve problems within a reasonable time and space bound .
- Complexity of an algorithm can be determined by using mathematical analysis, empirical analysis, or simulation.
- Complexity of an algorithm can be compared with other algorithms that solve the same problem, to choose the best algorithm for a given situation .



### Growth of Functions

- Growth of functions is a concept that helps us to compare the efficiency of different algorithms based on their running time or space requirements as a function of the input size.
- Growth of functions is also useful for describing the asymptotic behavior of algorithms, that is, how they perform in the limit of large inputs.
- Growth of functions can be expressed using different notations, such as big O, big Omega, big Theta, little o, and little omega. These notations capture the order of magnitude, the lower bound, the tight bound, the upper bound, and the strict upper bound of a function, respectively.
- Growth of functions can be classified into different classes, such as constant, logarithmic, linear, polynomial, exponential, and factorial. These classes represent the common patterns of how the running time or space requirements of an algorithm grow with the input size.
- Growth of functions can be compared using some basic rules, such as:

  - If f(n) and g(n) are two functions, then f(n) + g(n) is O(max(f(n), g(n))).
  - If f(n) and g(n) are two functions, then f(n) * g(n) is O(f(n) * g(n)).
  - If f(n) is a function and c is a constant, then c * f(n) is O(f(n)).
  - If f(n) is a function and k is a positive integer, then f(n)^k is O(f(n)^k).
  - If f(n) and g(n) are two functions, then f(g(n)) is O(f(n)) if g(n) is O(n).

- Growth of functions can be analyzed using some common techniques, such as:

  - The loop rule: If a loop runs for n iterations and each iteration takes O(f(n)) time, then the loop takes O(n * f(n)) time.
  - The recursion rule: If a recursive function calls itself a times with input size n/b, and each call takes O(f(n)) time, then the recursive function takes O(f(n) + a * T(n/b)) time, where T(n) is the time complexity of the function.
  - The master theorem: If a recursive function calls itself a times with input size n/b, and each call takes O(f(n)) time, where f(n) is asymptotically positive, then the recursive function takes O(n^log_b(a) * f(n)) time if f(n) is O(n^log_b(a)), O(f(n)) time if f(n) is O(n^log_b(a) / log n), and O(n^log_b(a)) time if f(n) is O(n^log_b(a) / polylog n), where polylog n is any polynomial function of log n.



### Performance Measurements

- Performance measurements are used to evaluate the efficiency and effectiveness of an algorithm in solving a problem.
- Performance measurements can be based on various factors, such as time, space, network, power, etc. However, the most common factors are time and space complexity.
- Time complexity measures how much time an algorithm takes to execute for a given input size. It depends on the number of basic operations performed by the algorithm, such as arithmetic, comparisons, assignments, etc.
- Space complexity measures how much memory or space an algorithm uses while it is executed for a given input size. It depends on the amount of data and program space required by the algorithm, such as variables, arrays, stacks, etc.
- Performance measurements can be expressed using different notations, such as big O, big Omega, big Theta, etc. These notations capture the asymptotic behavior of an algorithm, that is, how the algorithm behaves as the input size grows indefinitely.
- Big O notation gives the upper bound of the time or space complexity of an algorithm, that is, the worst-case scenario. For example, O(n) means that the algorithm takes at most linear time or space in terms of the input size n.
- Big Omega notation gives the lower bound of the time or space complexity of an algorithm, that is, the best-case scenario. For example, Omega(n) means that the algorithm takes at least linear time or space in terms of the input size n.
- Big Theta notation gives the tight bound of the time or space complexity of an algorithm, that is, the average-case scenario. For example, Theta(n) means that the algorithm takes exactly linear time or space in terms of the input size n.
- Performance measurements can be used to compare different algorithms for the same problem and choose the most suitable one based on the trade-offs between time and space, or other factors. For example, sorting algorithms can be compared based on their time and space complexity, as well as their stability, adaptability, etc.



### Sorting and Order Statistics - Shell Sort

- Shell sort is a sorting algorithm that is based on the idea of insertion sort, but improves its efficiency by using a gap sequence to compare and swap elements that are far apart.
- Shell sort works by dividing the input array into subarrays with a certain gap between the elements, and then applying insertion sort on each subarray. The gap is gradually reduced until it becomes one, and the array is fully sorted.
- The performance of shell sort depends on the choice of the gap sequence. A common gap sequence is to start with the largest gap that is smaller than the array size, and then divide it by a constant factor (usually 2) until it reaches one. For example, if the array size is 16, the gap sequence could be 8, 4, 2, 1.
- Shell sort has an average time complexity of O(n^(3/2)) for the gap sequence mentioned above, and can be improved to O(n^(4/3)) or O(n*log(n)) by using other gap sequences. However, the best gap sequence is still an open problem, and no one has proven a lower bound for the worst-case time complexity of shell sort.
- Shell sort is an in-place and unstable sorting algorithm, meaning that it does not require extra space and it does not preserve the relative order of equal elements.
- Shell sort is suitable for sorting arrays that are mostly sorted or have a small number of inversions, as it can take advantage of the existing order and reduce the number of comparisons and swaps. It is also easy to implement and has low overhead. However, it is not very efficient for large or random arrays, and it is difficult to analyze its performance theoretically.



### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle, and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The base case of the recursion is when the subarray has one or zero elements, in which case it is already sorted.
- The average-case time complexity of quick sort is **O(n log n)**, where n is the number of elements in the array.
- The worst-case time complexity of quick sort is **O(n^2)**, which occurs when the pivot element is always the smallest or the largest element in the subarray, resulting in unbalanced partitions.
- The space complexity of quick sort is **O(log n)**, which is the depth of the recursion tree.
- Quick sort is an **in-place** sorting algorithm, meaning it does not use any extra space to store the sorted elements, but modifies the original array.
- Quick sort is not a **stable** sorting algorithm, meaning it does not preserve the relative order of equal elements in the array.



### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  - If the array has zero or one element, it is already sorted and no further action is needed.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the sorted subarrays into a single sorted array by repeatedly taking the smallest element from either subarray and appending it to the output array.

- The merge operation can be implemented using a temporary array and two pointers, one for each subarray, that keep track of the current element to be compared.
- The merge operation takes linear time, O(n), where n is the total number of elements in the two subarrays.
- The merge sort algorithm has a recurrence relation for its running time, T(n), given by:

  - T(n) = O(1) if n <= 1
  - T(n) = 2T(n/2) + O(n) if n > 1

- Using the master theorem, we can solve this recurrence and obtain that T(n) = O(n log n) for all n.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is also a comparison-based sorting algorithm, meaning that it only uses comparisons between elements to determine their order.
- Merge sort has a space complexity of O(n), since it requires a temporary array of the same size as the input array to perform the merge operation.



### Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: building the heap and extracting the elements from the heap.
- Building the heap: the algorithm rearranges the elements of the array into a max-heap or a min-heap, depending on the desired sorting order. This can be done in linear time using a bottom-up approach that starts from the last non-leaf node and moves up to the root, applying a procedure called heapify to each node. Heapify ensures that the subtree rooted at a given node satisfies the heap property by swapping the node with its largest or smallest child, if necessary, and recursing on the affected subtree.
- Extracting the elements from the heap: the algorithm repeatedly removes the root element of the heap, which is the largest or smallest element in the array, and places it at the end of the sorted output. Then, it restores the heap property by applying heapify to the new root node. This process is repeated until the heap is empty, resulting in a sorted array. This phase takes O(n log n) time, where n is the number of elements in the array, since each extraction and heapify operation takes O(log n) time and there are n such operations.
- Heap sort has the following advantages and disadvantages:
  - Advantages:
    - It is an in-place sorting algorithm, meaning it does not require extra space to store the sorted output.
    - It has a guaranteed worst-case running time of O(n log n), which is better than some other comparison-based sorting algorithms, such as bubble sort or insertion sort, that have quadratic worst-case running times.
    - It can be easily parallelized or adapted to handle external sorting, where the data does not fit in the main memory and has to be stored on disks or tapes.
  - Disadvantages:
    - It is not a stable sorting algorithm, meaning it does not preserve the relative order of equal elements in the input array.
    - It is not adaptive, meaning it does not take advantage of the existing order or partial order in the input array, and performs the same number of comparisons regardless of the input distribution.
    - It has a relatively large hidden constant factor in its running time, meaning it is often slower than some other comparison-based sorting algorithms, such as quick sort or merge sort, on average or in practice.



### Comparison of Sorting Algorithms

- Sorting algorithms are methods of arranging a list of elements in a certain order, such as ascending or descending.
- Sorting algorithms can be classified into two categories: comparison-based and non-comparison-based.
- Comparison-based sorting algorithms compare elements of the list with each other using a comparison operator, such as less than, equal to, or greater than, to determine their relative order.
- Non-comparison-based sorting algorithms do not use comparisons, but rely on other techniques, such as counting, hashing, or radix conversion, to sort the elements.
- Comparison-based sorting algorithms have a lower bound of Ω(n log n) on their time complexity, where n is the number of elements in the list. This means that no comparison-based sorting algorithm can perform better than n log n comparisons in the worst case.
- Non-comparison-based sorting algorithms can achieve linear time complexity, O(n), in some cases, but they may have additional space or memory requirements, or they may be restricted to certain types of elements or keys.

Some of the most common comparison-based sorting algorithms are:

- Shell sort: This algorithm sorts the list by comparing elements that are far apart, and then reducing the gap between them until it reaches one. This way, it partially sorts the list and makes it easier for the final insertion sort to finish the sorting. Shell sort has an average time complexity of O(n^(3/2)), and a worst case time complexity of O(n^2). It is an unstable and in-place algorithm, meaning that it does not preserve the order of equal elements, and it does not use extra space.
- Quick sort: This algorithm sorts the list by choosing a pivot element, and partitioning the list into two sublists, one with elements smaller than the pivot, and one with elements larger than the pivot. Then, it recursively sorts the sublists until the list is sorted. Quick sort has an average time complexity of O(n log n), and a worst case time complexity of O(n^2), which occurs when the pivot is the smallest or the largest element. It is an unstable and in-place algorithm, meaning that it does not preserve the order of equal elements, and it does not use extra space.
- Merge sort: This algorithm sorts the list by dividing it into two equal halves, and recursively sorting each half. Then, it merges the two sorted halves into one sorted list. Merge sort has a time complexity of O(n log n) in all cases, and it is a stable and out-of-place algorithm, meaning that it preserves the order of equal elements, and it uses extra space proportional to the size of the list.
- Heap sort: This algorithm sorts the list by building a heap data structure from the list, and then repeatedly removing the largest element from the heap and placing it at the end of the list. Heap sort has a time complexity of O(n log n) in all cases, and it is an unstable and in-place algorithm, meaning that it does not preserve the order of equal elements, and it does not use extra space.

Some of the most common non-comparison-based sorting algorithms are:

- Counting sort: This algorithm sorts the list by counting the number of occurrences of each element in the list, and then using the counts to determine the position of each element in the sorted list. Counting sort has a time complexity of O(n + k), where k is the range of the elements in the list. It is a stable and out-of-place algorithm, meaning that it preserves the order of equal elements, and it uses extra space proportional to the size of the list and the range of the elements. Counting sort is only suitable for sorting elements that are integers or can be mapped to integers.
- Radix sort: This algorithm sorts the list by sorting the elements according to their digits, starting from the least significant digit to the most significant digit. Radix sort has a time complexity of O(d * (n + b)), where d is the number of digits, n is the number of elements, and b is the base of the digits. It is a stable and out-of-place algorithm, meaning that it preserves the order of equal elements, and it uses extra space proportional to the size of the list and the base of the digits. Radix sort is only suitable for sorting elements that have a fixed number of digits or can be represented as digits.
- Bucket sort: This algorithm sorts the list by distributing the elements into buckets, and then sorting each bucket using another sorting algorithm. Bucket sort has a time complexity of O(n + k), where k is the number of buckets, if the elements are uniformly distributed and the buckets



### Sorting in Linear Time

- Sorting in linear time means sorting an array or a list of elements in O(n) time, where n is the number of elements.
- Sorting in linear time is possible only for special cases of input, where some additional information or assumptions are given about the elements.
- Sorting in linear time usually involves using operations other than comparisons, such as counting, grouping, hashing, or digit extraction, to determine the sorted order.
- Some examples of sorting algorithms that run in linear time are:

  - **Counting sort**: This algorithm assumes that the input consists of integers in a small range [0, k]. It counts the number of occurrences of each integer in the input and then outputs the integers in sorted order according to their counts. It runs in O(n + k) time and O(n + k) space.
  - **Radix sort**: This algorithm assumes that the input consists of d-digit numbers in base b. It sorts the numbers by their digits, starting from the least significant digit to the most significant digit, using a stable sorting algorithm such as counting sort. It runs in O(d(n + b)) time and O(n + b) space.
  - **Bucket sort**: This algorithm assumes that the input is generated by a random process that distributes the elements uniformly over the interval [0, 1). It divides the interval into n equal-sized buckets and then distributes the elements into the buckets according to their values. Then, it sorts each bucket using another sorting algorithm and concatenates the buckets in order. It runs in O(n) time on average and O(n) space.



## Unit 2 - Advanced Data Structures: Red-Black Trees, B – Trees, Binomial Heaps, Fibonacci Heaps, Tries, Skip List

- Advanced data structures are data structures that provide more efficient ways to organize, store, and manipulate data than the basic data structures such as arrays, linked lists, stacks, queues, etc.
- Some of the advanced data structures are:

  - **Red-Black Trees**: A red-black tree is a type of self-balancing binary search tree, where each node has an extra bit that represents its color, either red or black. The tree maintains the following properties:
    - Every node is either red or black.
    - The root and the leaves (NIL) are black.
    - If a node is red, then both its children are black.
    - Every simple path from a node to a descendant leaf contains the same number of black nodes.
  - These properties ensure that the tree remains balanced, and the height of the tree is O(log n) where n is the number of nodes. The operations of insertion, deletion, and search can be performed in O(log n) time.

  - **B-Trees**: A B-tree is a type of multi-way search tree, where each node can have more than two children. The tree maintains the following properties:
    - All leaves are at the same level.
    - Each node, except the root and the leaves, has at least t children, where t is a fixed integer greater than 1.
    - Each node, except the root, has at most 2t children.
    - Each node, except the leaves, has one key more than the number of its children.
    - The keys in each node are sorted in increasing order.
  - B-trees are useful for storing large amounts of data that do not fit in main memory, and can be accessed efficiently by disk operations. The operations of insertion, deletion, and search can be performed in O(log n) time, where n is the number of keys.

  - **Binomial Heaps**: A binomial heap is a type of heap data structure, where the heap is composed of a collection of binomial trees. A binomial tree of order k is a recursive structure that has the following properties:
    - It has 2^k nodes.
    - It has k levels, numbered from 0 to k-1.
    - The root has degree k, and its children are the roots of binomial trees of order k-1, k-2, ..., 0, in this order.
    - Each node in the tree has a key that is greater than or equal to the key of its parent (min-heap property).
  - A binomial heap maintains the following properties:
    - Each binomial tree in the heap obeys the min-heap property.
    - There is at most one binomial tree of each order in the heap.
    - The binomial trees in the heap are linked in increasing order of their orders.
  - Binomial heaps are useful for implementing priority queues, as they support the operations of insert, delete-min, and merge in O(log n) time, where n is the number of nodes in the heap.

  - **Fibonacci Heaps**: A Fibonacci heap is a type of heap data structure, where the heap is composed of a collection of rooted trees that are not necessarily binomial. A Fibonacci heap maintains the following properties:
    - Each tree in the heap obeys the min-heap property.
    - There is a pointer to the tree with the minimum key in the heap.
    - Each node in the heap has a mark bit that indicates whether it has lost a child since the last time it was made the child of another node.
    - The degree of each node in the heap is bounded by O(log n), where n is the number of nodes in the heap.
  - Fibonacci heaps are useful for implementing priority queues, as they support the operations of insert, delete-min, and merge in O(1) amortized time, and the operations of decrease-key and delete in O(log n) amortized time, where n is the number of nodes in the heap.

  - **Tries**: A trie is a type of tree data structure, where each node represents a prefix of a string. The tree maintains the following properties:
    - The root represents an empty string.
    - Each edge is labeled with a character.
    - The children



### Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and have a **guaranteed time complexity of O(log n)** for basic operations like insertion, deletion, and search .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**.
  - The root of the tree is always **black**.
  - Every leaf (NIL) is **black**.
  - If a node is **red**, then both its children are **black**.
  - Every simple path from a node to a descendant leaf contains the **same number of black nodes**. This number is called the **black-height** of the node.
- Red-black trees maintain these properties by **rotating** and **recoloring** the nodes after insertion or deletion .
- Red-black trees are used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - **Java Collections Framework**: The TreeMap and TreeSet classes are implemented using red-black trees.
  - **Linux kernel**: The Completely Fair Scheduler and the Ext4 file system use red-black trees.
  - **C++ STL**: The map, multimap, set, and multiset containers are typically implemented using red-black trees.
- Red-black trees are a special case of **B-trees** with order 4 and minimum degree 2. B-trees are another type of self-balancing search tree that can have more than two children per node and store multiple keys per node. B-trees are useful for storing large amounts of data on disk.



### B – Trees

- A B-tree is a **self-balancing** tree data structure that maintains **sorted** data and allows **searches, sequential access, insertions, and deletions** in logarithmic time   .
- A B-tree generalizes the binary search tree, allowing for nodes with more than two children .
- A B-tree of order m has the following properties :
  - Each node can have at most m children and m-1 keys.
  - Each node, except the root and the leaves, must have at least ⌈m/2⌉ children and ⌈m/2⌉-1 keys.
  - The root must have at least two children if it is not a leaf node.
  - All the leaves must be at the same level, and they have no children.
  - The keys in each node are stored in ascending order, and they act as separators for the subtrees.
  - A key k in a node N means that all the keys in the left subtree of N are less than k, and all the keys in the right subtree of N are greater than or equal to k.
- The height of a B-tree with n keys and order m is bounded by log<sub>m/2</sub>(n+1) and log<sub>m</sub>(n+1) .
- The basic operations on a B-tree are search, insert, and delete .
  - Search: To search for a key k in a B-tree, we start from the root and compare k with the keys in the current node. If k is found, we return the node and the index of k. If k is not found, we recursively search in the appropriate child subtree, or return null if there is no such child.
  - Insert: To insert a key k in a B-tree, we first search for the leaf node where k should be inserted. If the leaf node has less than m-1 keys, we simply insert k in the correct position and update the node. If the leaf node is full, we split it into two nodes and insert the middle key in the parent node, repeating the process until we reach a node that is not full or the root.
  - Delete: To delete a key k from a B-tree, we first search for the node that contains k. If k is in a leaf node, we simply remove it from the node and update the node. If k is in an internal node, we replace it with either its predecessor or successor in the tree, and then delete that key from the leaf node. If the deletion causes any node to have less than the minimum number of keys, we either borrow a key from a sibling node or merge two sibling nodes and delete a key from the parent node, repeating the process until we reach a node that satisfies the property or the root.
- B-trees are useful for storing and retrieving large amounts of data efficiently, especially when the data is stored on external memory devices such as disks   .
- B-trees are widely used in database systems, file systems, and indexing structures   .



### Binomial Heaps

- A binomial heap is a data structure that acts as a priority queue but also allows pairs of heaps to be merged.
- A binomial heap is implemented as a set of binomial trees that satisfy the binomial heap properties:
  - Each binomial tree in a heap obeys the minimum-heap property: the key of a node is greater than or equal to the key of its parent.
  - There can be at most one binomial tree for each order, including zero order.
- A binomial tree of order 0 is a single node. A binomial tree of order k has a root node whose children are roots of binomial trees of orders k-1, k-2, ..., 2, 1, 0 (in this order).
- The number of nodes in a binomial tree of order k is 2^k. The height of a binomial tree of order k is k.
- The binomial heap operations are as follows:
  - **Create-Heap**: creates an empty binomial heap.
  - **Insert**: inserts a new key into the binomial heap by creating a new binomial tree of order 0 and merging it with the existing heap.
  - **Get-Min**: returns the minimum key in the binomial heap by scanning the roots of all the binomial trees.
  - **Extract-Min**: removes and returns the minimum key in the binomial heap by deleting the root of the binomial tree that contains the minimum key and merging its children with the remaining heap.
  - **Union**: merges two binomial heaps into one by combining the binomial trees of the same order and adjusting the heap property if needed.
  - **Decrease-Key**: decreases the key of a given node in the binomial heap by swapping it with its parent until the heap property is restored.
  - **Delete**: deletes a given node in the binomial heap by decreasing its key to negative infinity and then extracting the minimum key.



### Fibonacci Heaps

- A Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
- A heap-ordered tree is a tree that satisfies the minimum-heap property, that is, the key of a child is always greater than or equal to the key of the parent.
- The minimum key is always at the root of one of the trees.
- Fibonacci heaps are named after the Fibonacci numbers, which are used in their running time analysis.
- Fibonacci heaps have a better amortized running time than many other priority queue data structures including the binary heap and binomial heap .
- The find-minimum operation takes constant (O(1)) amortized time.
- The insert and decrease key operations also work in constant amortized time.
- The delete and delete-minimum operations work in O(log n) amortized time, where n is the number of nodes in the heap.
- The merge or union operation, which combines two Fibonacci heaps into one, works in constant time .
- Fibonacci heaps are used to implement the priority queue element in Dijkstra’s algorithm, giving the algorithm a very efficient running time.
- Fibonacci heaps are more flexible than binomial heaps, as they allow arbitrary degree for each node and do not require the trees to be ordered.
- Fibonacci heaps use a lazy approach to maintain the heap structure, postponing the work until it is needed .
- Fibonacci heaps use two techniques to improve the efficiency of the operations: potential function and cascading cut .
- A potential function is a function that assigns a numerical value to each heap state, reflecting the amount of work that can be done in the future.
- A cascading cut is a procedure that cuts a node from its parent if it loses more than one child, and recursively cuts its parent if it is also marked.
- Fibonacci heaps are more complicated to implement than other heap types, and have a larger constant factor in the running time .
- Fibonacci heaps are not widely used in practice, but they have theoretical importance as they can improve the asymptotic running time of some algorithms .



### Tries

- A trie is a tree-based data structure used for storing and retrieving collections of strings .
- The word trie comes from the word re**trie**val which means to find or get something back.
- A trie is also called a digital tree or a prefix tree.
- A trie is a type of k-ary search tree, where each node has k children, one for each character in the alphabet.
- A trie can store strings that have a common prefix in a shared subtree, which saves space and allows fast search operations .
- A trie can support the following operations:
  - Insert: To add a new string to the trie, we start from the root and follow the path of the characters in the string. If a node for a character does not exist, we create a new node and link it to the parent. We mark the last node as the end of the word.
  - Search: To search for a string in the trie, we start from the root and follow the path of the characters in the string. If we reach a node that is marked as the end of the word, we return true. If we reach a node that does not exist or is not marked as the end of the word, we return false.
  - Delete: To delete a string from the trie, we start from the root and follow the path of the characters in the string. If we reach a node that is marked as the end of the word, we unmark it. If the node has no children, we delete it and recursively delete its parent if it has no other children.
- A trie can be used for various applications, such as:
  - Autocomplete: A trie can store a dictionary of words and suggest possible completions for a given prefix.
  - Spell check: A trie can check if a given word is in the dictionary or suggest corrections for misspelled words.
  - Pattern matching: A trie can match a pattern with a set of strings and find all the occurrences of the pattern.
  - IP routing: A trie can store IP addresses and find the longest prefix match for a given address.
  - Word games: A trie can generate valid words from a given set of letters or find words that match a given pattern.



### Skip List

- A skip list is a **probabilistic data structure** that allows for efficient search, insertion and deletion of elements in a **sorted list** .
- A skip list consists of multiple **layers** of linked lists, with each layer having a smaller number of elements than the previous one .
- The lowest layer contains all the elements of the sorted list, and the highest layer contains only one element, the **head** .
- Each element in a skip list has a **key** and a **value**, and a variable number of **forward pointers** to the next elements in the same or higher layers .
- The number of forward pointers of each element is determined randomly by a **coin toss** or a **geometric distribution**, such that the expected number of elements in each layer is half of the previous one .
- To search for an element in a skip list, we start from the head in the highest layer, and follow the forward pointers until we find a key that is larger than or equal to the target key .
- Then, we move down to the next lower layer, and repeat the process until we reach the lowest layer .
- If we find the target key in the lowest layer, we return the corresponding value, otherwise we return null .
- The expected time complexity of search in a skip list is **O(log n)**, where n is the number of elements in the sorted list .
- To insert an element in a skip list, we first search for the position where the element should be inserted in the lowest layer, and then insert it there .
- Then, we toss a coin to decide whether to insert the element in the next higher layer as well .
- We repeat this process until the coin toss returns tails or we reach the highest layer .
- The expected time complexity of insertion in a skip list is also **O(log n)** .
- To delete an element from a skip list, we first search for the element in the lowest layer, and then delete it from there .
- Then, we move up to the next higher layer, and delete the element from there if it exists .
- We repeat this process until we reach the highest layer or the element does not exist in the current layer .
- The expected time complexity of deletion in a skip list is also **O(log n)** .
- Skip lists are a simple, fast and space-efficient alternative to balanced trees for implementing ordered sequences .
- Skip lists can also support concurrent operations by using **locks** or **atomic operations** on the forward pointers .
- Skip lists can also be extended to support **range queries**, **multidimensional data**, **approximate queries**, and other applications .

: Skip list - Wikipedia
: Skip List | Set 1 (Introduction) - GeeksforGeeks
: Skip List | Brilliant Math & Science Wiki
: The Skip List Data Structure | Baeldung on Computer Science



## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

- Divide and conquer is a technique of breaking a problem into smaller subproblems, solving them recursively, and combining the solutions to obtain the final answer.
- Some examples of divide and conquer algorithms are:
  - Sorting: Merge sort, quick sort, and heap sort are based on dividing the array into smaller parts, sorting them, and merging or rearranging them.
  - Matrix multiplication: Strassen's algorithm is based on dividing the matrices into smaller submatrices, multiplying them recursively, and adding or subtracting the results to obtain the final product.
  - Convex hull: The convex hull of a set of points is the smallest convex polygon that contains all the points. Graham scan and quick hull are algorithms that use divide and conquer to find the convex hull of a set of points.
  - Searching: Binary search and interpolation search are based on dividing the search space into smaller intervals, and finding the target element by comparing it with the middle or a suitable point.

- Greedy methods are a technique of making the best local choice at each step, hoping that it will lead to the optimal global solution.
- Some examples of greedy algorithms are:
  - Optimal reliability allocation: Given a system with n components, each having a reliability and a cost, and a budget B, the problem is to allocate the reliability to each component such that the overall system reliability is maximized. A greedy algorithm is to sort the components by their cost-reliability ratios, and allocate the reliability to the components with the lowest ratios until the budget is exhausted.
  - Knapsack: Given a set of items, each having a weight and a value, and a capacity C, the problem is to select a subset of items such that the total weight does not exceed C and the total value is maximized. A greedy algorithm is to sort the items by their value-weight ratios, and select the items with the highest ratios until the capacity is reached or no more items can be added.
  - Minimum spanning trees: Given a connected, undirected, weighted graph, the problem is to find a subset of edges that connects all the vertices and has the minimum total weight. Prim's algorithm and Kruskal's algorithm are greedy algorithms that find the minimum spanning tree by adding the edges with the lowest weights that do not create cycles.
  - Single source shortest paths: Given a weighted graph and a source vertex, the problem is to find the shortest paths from the source to all other vertices. Dijkstra's algorithm and Bellman Ford algorithm are greedy algorithms that find the shortest paths by relaxing the edges in a certain order and updating the distances of the vertices.



### Divide and Conquer with Examples Such as Sorting for the notes of the Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms. in the subject of Design and Analysis of Algorithm

- Divide and conquer is a technique that breaks a problem into smaller subproblems, solves them recursively, and combines their solutions to obtain the solution for the original problem.
- Divide and conquer can be applied to various problems such as sorting, matrix multiplication, convex hull, and searching.
- Sorting is the process of arranging a sequence of elements in a certain order, such as ascending or descending. Some examples of divide and conquer sorting algorithms are:
  - Merge sort: This algorithm divides the sequence into two halves, sorts each half recursively, and merges the two sorted halves into one sorted sequence.
  - Quick sort: This algorithm chooses a pivot element, partitions the sequence around the pivot such that all elements smaller than the pivot are on the left and all elements larger than the pivot are on the right, and sorts each partition recursively.
  - Heap sort: This algorithm builds a heap data structure from the sequence, repeatedly extracts the maximum element from the heap and places it at the end of the sorted sequence, and reduces the size of the heap by one until the heap is empty.
- Matrix multiplication is the operation of multiplying two matrices to obtain a third matrix. A naive algorithm for matrix multiplication takes O(n^3) time, where n is the size of the matrices. A divide and conquer algorithm for matrix multiplication is:
  - Strassen's algorithm: This algorithm divides each matrix into four submatrices of size n/2 x n/2, computes seven products of submatrices using recursive calls, and combines the products to obtain the final matrix. This algorithm takes O(n^2.81) time, which is asymptotically faster than the naive algorithm.
- Convex hull is the smallest convex polygon that contains a set of points in the plane. A convex polygon is a polygon whose interior angles are all less than 180 degrees. A divide and conquer algorithm for convex hull is:
  - Graham scan: This algorithm sorts the points by their polar angle with respect to the lowest point, pushes the points onto a stack in the sorted order, and pops the points from the stack if they make a clockwise turn with the previous two points on the stack. The remaining points on the stack form the convex hull. This algorithm takes O(n log n) time, where n is the number of points.
- Searching is the process of finding a target element in a collection of elements. Some examples of divide and conquer searching algorithms are:
  - Binary search: This algorithm assumes that the collection is sorted, and compares the target element with the middle element of the collection. If they are equal, the search is successful. If the target element is smaller than the middle element, the search continues in the left half of the collection. If the target element is larger than the middle element, the search continues in the right half of the collection. This algorithm takes O(log n) time, where n is the size of the collection.
  - Interpolation search: This algorithm also assumes that the collection is sorted, and estimates the position of the target element based on the first and last elements of the collection and the target value. If the estimated position matches the target element, the search is successful. If the target element is smaller than the estimated position, the search continues in the left subcollection. If the target element is larger than the estimated position, the search continues in the right subcollection. This algorithm takes O(log log n) time on average, but O(n) time in the worst case, where n is the size of the collection.

- Greedy methods are techniques that make a locally optimal choice at each step, hoping to obtain a globally optimal solution. Greedy methods can be applied to various problems such as optimal reliability allocation, knapsack, minimum spanning trees, and single source shortest paths.
- Optimal reliability allocation is the problem of allocating a given budget to improve the reliability of a system composed of n components, such that the overall reliability of the system is maximized. A greedy algorithm for optimal reliability allocation is:
  - Incremental improvement algorithm: This algorithm starts with an initial allocation of the budget, and iteratively improves the allocation by transferring a small amount of budget from the component with the lowest marginal return to the component with the highest marginal return, until no further improvement is possible. The marginal return of a component is the increase in the system reliability per



### Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure and properties.
- Some examples of divide and conquer algorithms are:
  - Binary search: This algorithm searches for a target value in a sorted array by repeatedly dividing the array into two halves and discarding the half that does not contain the target value.
  - Merge sort: This algorithm sorts an array by recursively dividing it into two halves, sorting each half, and merging the sorted halves.
  - Quick sort: This algorithm sorts an array by recursively choosing a pivot element, partitioning the array around the pivot, and sorting the two subarrays on either side of the pivot.
  - Strassen's algorithm: This algorithm multiplies two matrices by recursively dividing them into four submatrices each, computing seven products of submatrices, and combining them to get the final product.
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by recursively dividing the sequence into two halves, computing the Fourier transform of each half, and combining them using the butterfly operation.



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
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by dividing it into two sequences of even and odd indices, computing their transforms recursively, and then combining them using the butterfly operation.
  - Convex hull: This algorithm finds the smallest convex polygon that contains a set of points in the plane by dividing the set into two subsets, finding their convex hulls recursively, and then merging them using the upper and lower tangent algorithm.



### Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer  .
- Divide and conquer algorithms often have a logarithmic complexity, as they reduce the problem size by a constant factor at each recursive step  .
- Some examples of divide and conquer algorithms are:

  - Sorting: Merge sort and quicksort are two sorting algorithms that use divide and conquer. Merge sort divides the array into two halves, sorts them recursively, and then merges them in linear time. Quicksort partitions the array around a pivot element, such that all elements smaller than the pivot are on the left and all elements larger than the pivot are on the right, and then sorts the two subarrays recursively .
  - Matrix multiplication: Strassen's algorithm is an efficient algorithm to multiply two matrices. A simple method to multiply two matrices needs 3 nested loops and is O(n^3). Strassen's algorithm divides each matrix into four submatrices, performs seven multiplications and some additions on them, and then combines them to get the final product. Strassen's algorithm reduces the time complexity to O(n^2.8974) .
  - Convex hull: The convex hull of a set of points is the smallest convex polygon that contains all the points. A divide and conquer algorithm for finding the convex hull works as follows: Sort the points by their x-coordinates, split them into two halves, find the convex hull of each half recursively, and then merge the two hulls using a linear algorithm.
  - Searching: Binary search is a classic example of a divide and conquer algorithm. If we have a list of data that has already been sorted, we can easily find any item in the list using a divide and conquer process. For example, let’s say we want to find the value 19 in that list. We start by comparing 19 with the middle element of the list, which is 14. Since 19 is larger than 14, we can eliminate the left half of the list and focus on the right half. We repeat this process until we find 19 or conclude that it is not in the list.

### Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

- Greedy methods are a paradigm for designing algorithms that make a locally optimal choice at each step, hoping to find a globally optimal solution .
- Greedy methods are often simple and fast, but they may not always guarantee the optimal solution .
- Some examples of greedy methods are:

  - Optimal reliability allocation: Given a system with n components, each having a reliability r_i and a cost c_i, and a budget B, the problem is to allocate the reliabilities to the components such that the overall system reliability is maximized. A greedy method for this problem works as follows: Sort the components by their cost-effectiveness ratio c_i/r_i in ascending order, and assign the highest possible reliability to each component until the budget is exhausted.
  - Knapsack: Given a set of items, each having a weight w_i and a value v_i, and a capacity W, the problem is to select a subset of items such that the total weight does not exceed W and the total value is maximized. A greedy method for this problem works as follows: Sort the items by their value-to-weight ratio v_i/w_i in descending order, and pick the items in that order until the capacity is reached or no more items can be added .
  - Minimum spanning trees: Given a connected, undirected, weighted graph, the problem is to find a subset of edges that connects all the vertices and has the minimum total weight. A greedy method for this problem works as follows: Start with an empty set of edges, and at each step, add the edge with the smallest weight that does not create a cycle. This method is known as Kruskal's algorithm. Another greedy method for this problem works as follows: Start with any vertex and mark it as visited,



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Design and Analysis of Algorithm. Here is the content for the topic of Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

### Greedy Methods with Examples

- Greedy methods are a class of algorithms that make a series of locally optimal choices to find a globally optimal solution.
- Greedy methods do not always guarantee the optimal solution, but they are often efficient and easy to implement.
- Greedy methods can be applied to various problems, such as optimal reliability allocation, knapsack, minimum spanning trees, and single source shortest paths.

#### Optimal Reliability Allocation

- Optimal reliability allocation is a problem of allocating a given budget to improve the reliability of a system composed of n components.
- The objective is to maximize the overall system reliability, which is the probability that all components function properly.
- A greedy method for this problem is to allocate the budget to the component with the lowest reliability-cost ratio, where the reliability-cost ratio is the ratio of the increase in reliability to the cost of improvement for a component.
- The algorithm repeats this process until the budget is exhausted or all components have reached their maximum reliability.
- This greedy method is optimal if the reliability-cost ratio is a non-increasing function of the reliability for each component.

#### Knapsack

- Knapsack is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity.
- The objective is to maximize the total value of the items in the knapsack, without exceeding the capacity.
- A greedy method for this problem is to sort the items by their value-weight ratio, and then pack the items in the decreasing order of this ratio, until the knapsack is full or no more items can be packed.
- This greedy method is optimal if the items can be fractionally divided, meaning that a fraction of an item can be packed with the same value-weight ratio as the whole item.
- If the items cannot be fractionally divided, this greedy method is not optimal, but it can be used as a heuristic to find an approximate solution.

#### Minimum Spanning Trees

- Minimum spanning tree is a problem of finding a subset of edges in a weighted undirected graph that connects all the vertices and has the minimum total weight.
- The objective is to minimize the cost of building a network that connects all the nodes in the graph.
- A greedy method for this problem is Prim's algorithm, which starts with an arbitrary vertex and adds the edge with the minimum weight that connects a vertex in the current tree to a vertex outside the tree, until all the vertices are in the tree.
- Another greedy method for this problem is Kruskal's algorithm, which sorts the edges by their weights and adds the edge with the minimum weight that does not create a cycle in the current forest, until all the vertices are in the same tree.
- Both Prim's and Kruskal's algorithms are optimal and find the same minimum spanning tree for any given graph.

#### Single Source Shortest Paths

- Single source shortest path is a problem of finding the shortest paths from a given source vertex to all other vertices in a weighted directed graph.
- The objective is to minimize the time or distance of traveling from the source to any other node in the graph.
- A greedy method for this problem is Dijkstra's algorithm, which maintains a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined.
- The algorithm repeatedly extracts the vertex with the minimum distance from the source from the priority queue, and updates the distances of its adjacent vertices in the queue, until the queue is empty or the destination is reached.
- Dijkstra's algorithm is optimal and finds the shortest paths from the source to all other vertices in the graph, if the edge weights are non-negative.
- If the edge weights can be negative, Dijkstra's algorithm may not work correctly, and a different greedy method is needed, such as Bellman-Ford algorithm.
- Bellman-Ford algorithm relaxes all the edges in the graph for n-1 times, where n is the number of vertices, and updates the distances of the vertices accordingly.
- Bellman-Ford algorithm is optimal and finds the shortest paths from the source to all other vertices in the graph, if there are no negative cycles in the graph, meaning that there is no cycle whose total weight is negative.
- If there are negative cycles in the graph, Bellman-Ford algorithm can detect them and report that the shortest paths do not exist.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step, without considering the future consequences.

Some examples of greedy methods are:

- Fractional knapsack problem: Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, find the maximum value that can be obtained by filling the knapsack with fractions of items. The greedy method is to sort the items by their value-to-weight ratio, and then take the items with the highest ratio until the knapsack is full or no more items are left.
- Prim's algorithm: Given a connected, undirected, weighted graph, find a minimum spanning tree (MST), which is a subset of edges that connects all the vertices with the minimum total weight. The greedy method is to start from an arbitrary vertex, and then repeatedly add the edge with the minimum weight that connects a vertex in the MST to a vertex outside the MST, until all the vertices are included.
- Dijkstra's algorithm: Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex. The greedy method is to maintain a set of visited vertices and a priority queue of unvisited vertices, and then repeatedly extract the vertex with the minimum distance from the source from the queue, mark it as visited, and update the distances of its adjacent vertices in the queue, until the queue is empty or the destination is reached.
- Activity selection problem: Given a set of activities, each with a start and finish time, find the maximum number of activities that can be performed by a single person or resource, assuming that only one activity can be performed at a time. The greedy method is to sort the activities by their finish time, and then select the first activity, and then repeatedly select the next activity that starts after the finish of the previous activity, until no more activities can be selected.



### Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast and easy to implement, but they may not always yield the best solution.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: An optimal solution to the problem contains optimal solutions to the subproblems.
  - Greedy choice property: A locally optimal choice is also globally optimal, and can be made without considering the subproblems.
- Some examples of problems that can be solved by greedy methods are:
  - Minimum spanning tree: A spanning tree of a connected, undirected and weighted graph is a subgraph that connects all the vertices and has the minimum total weight. A minimum spanning tree can be found by two greedy algorithms: Prim's and Kruskal's.
    - Prim's algorithm: Start with an arbitrary vertex and add the edge with the minimum weight that connects it to another vertex in the graph. Repeat this process until all the vertices are included in the tree.
    - Kruskal's algorithm: Sort all the edges in the graph by their weights in ascending order. Pick the edge with the lowest weight and add it to the tree if it does not create a cycle. Repeat this process until the tree has n-1 edges, where n is the number of vertices in the graph.
  - Optimal reliability allocation: Given a system with n components, each with a reliability ri and a cost ci, find the optimal allocation of a budget B to improve the reliability of the components, such that the overall reliability of the system is maximized. A possible greedy algorithm is:
    - Initialize the allocation vector x = [0, 0, ..., 0].
    - Calculate the marginal reliability gain per unit cost for each component i as gi = (1 - ri) / ci.
    - Sort the components by their gi values in descending order.
    - For each component i in the sorted order, allocate as much budget as possible to it, such that xi <= B and ri + xi <= 1. Update B = B - xi and ri = ri + xi.
    - Return the allocation vector x and the overall reliability R = prod(ri) for i = 1 to n.
  - Knapsack problem: Given a set of n items, each with a weight wi and a value vi, and a knapsack with a capacity W, find the maximum value that can be obtained by putting some or all of the items in the knapsack, without exceeding the capacity. A possible greedy algorithm is:
    - Calculate the value per unit weight for each item i as pi = vi / wi.
    - Sort the items by their pi values in descending order.
    - Initialize the value V = 0 and the weight W = 0.
    - For each item i in the sorted order, if W + wi <= W, then add the item to the knapsack, update V = V + vi and W = W + wi.
    - Return the value V and the subset of items in the knapsack.
  - Single source shortest paths: Given a weighted, directed graph G = (V, E) and a source vertex s, find the shortest path from s to every other vertex in the graph. Two greedy algorithms that can solve this problem are:
    - Dijkstra's algorithm: Maintain a set S of vertices whose shortest distance from s is known, and a priority queue Q of vertices whose distance is to be determined, ordered by their distance estimates. Initially, S is empty and Q contains all the vertices, with d(s) = 0 and d(v) = infinity for all v != s. At each step, extract the vertex u with the minimum distance estimate from Q, add it to S, and relax all the edges (u, v) in E, i.e., update d(v) = min(d(v), d(u) + w(u, v)) and Q accordingly. Repeat this process until Q is empty or the destination vertex is reached.
    - Bellman-Ford algorithm: Initialize the distance vector d = [0, infinity, ..., infinity], where d(v) is the distance estimate from s to v. Repeat the following for n-1 times, where n is the number of vertices in the graph: for each edge (u, v) in E, relax the edge, i.e., update d(v) = min(d(v), d(u) + w(u, v)). Optionally, check for negative cycles by relaxing the edges one more time and reporting if any distance estimate decreases.



### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold. Optimal substructure means that an optimal solution to the problem contains optimal solutions to its subproblems. Greedy choice property means that a globally optimal solution can be obtained by making a locally optimal choice at each step, without considering the future consequences.

Some examples of greedy methods are:

- **Single source shortest paths - Dijkstra’s and Bellman Ford algorithms**: These algorithms find the shortest path from a given source node to all other nodes in a weighted graph. They use a priority queue to select the node with the minimum distance from the source at each step, and update the distances of its adjacent nodes. Dijkstra’s algorithm works for graphs with non-negative edge weights, while Bellman Ford algorithm can handle negative edge weights as long as there are no negative cycles.
- **Optimal reliability allocation**: This problem involves allocating a fixed budget to improve the reliability of a system composed of several components. Each component has a cost and a reliability function, which gives the probability of the component functioning properly. The goal is to maximize the overall reliability of the system. A greedy method for this problem is to select the component that has the highest marginal increase in reliability per unit cost at each step, until the budget is exhausted.
- **Knapsack problem**: This problem involves packing a set of items with different weights and values into a knapsack with a limited capacity. The goal is to maximize the total value of the items in the knapsack. A greedy method for this problem is to sort the items by their value-to-weight ratio, and select the items with the highest ratio until the knapsack is full or no more items can be added.
- **Minimum spanning trees - Prim’s and Kruskal’s algorithms**: These algorithms find a subset of edges in a weighted undirected graph that connects all the nodes with the minimum total weight. They use a greedy strategy to select the edges with the lowest weight at each step, without creating cycles. Prim’s algorithm starts from an arbitrary node and grows the tree by adding the edge with the lowest weight that connects a node in the tree to a node outside the tree. Kruskal’s algorithm starts with an empty set of edges and adds the edge with the lowest weight that does not create a cycle, until all the nodes are connected.



## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure. It works by breaking down the problem into smaller subproblems, solving them once and storing their solutions in a table, and then using the table to construct the optimal solution for the original problem.
- Knapsack problem is an example of dynamic programming. It is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the items in the knapsack is maximized. The optimal solution can be found by using a two-dimensional table, where each cell represents the maximum value that can be obtained by packing items up to a certain weight and index. The table can be filled by using the following recurrence relation:

  - If `w[i] > W`, then `V[i][W] = V[i-1][W]`, where `w[i]` is the weight of the `i`-th item, `W` is the capacity of the knapsack, and `V[i][W]` is the maximum value that can be obtained by packing items up to `i` and weight `W`.
  - If `w[i] <= W`, then `V[i][W] = max(V[i-1][W], v[i] + V[i-1][W-w[i]])`, where `v[i]` is the value of the `i`-th item, and the second term represents the value of packing the `i`-th item and the optimal solution for the remaining capacity and items.
  - The optimal value is given by `V[n][W]`, where `n` is the number of items, and the optimal subset can be traced back by checking which items were included in each cell.

- All pair shortest paths problem is another example of dynamic programming. It is a problem of finding the shortest distance between every pair of vertices in a weighted graph. There are two algorithms that can solve this problem using dynamic programming: Warshal's algorithm and Floyd's algorithm. Both algorithms use a three-dimensional table, where each cell represents the shortest distance between two vertices using intermediate vertices up to a certain index. The table can be filled by using the following recurrence relations:

  - Warshal's algorithm: `D[k][i][j] = D[k-1][i][j] or (D[k-1][i][k] and D[k-1][k][j])`, where `D[k][i][j]` is the shortest distance between vertices `i` and `j` using vertices up to `k` as intermediates, and `or` and `and` are logical operations that return 1 if either or both of the operands are 1, and 0 otherwise. The algorithm works for graphs with binary weights (0 or 1), and the final solution is given by `D[n][i][j]`, where `n` is the number of vertices.
  - Floyd's algorithm: `D[k][i][j] = min(D[k-1][i][j], D[k-1][i][k] + D[k-1][k][j])`, where `D[k][i][j]` is the shortest distance between vertices `i` and `j` using vertices up to `k` as intermediates, and `min` is the minimum function that returns the smaller of the two operands. The algorithm works for graphs with any weights, and the final solution is given by `D[n][i][j]`, where `n` is the number of vertices.

- Resource allocation problem is a problem of allocating a limited amount of resources among a number of activities, such that the total profit or benefit is maximized. It can be solved by using dynamic programming, by using a table where each cell represents the maximum profit that can be obtained by allocating resources up to a certain amount and activity. The table can be filled by using the following recurrence relation:

  - `P[i][r] = max(P[i-1][r], p[i] + P[i-1][r-r[i]])`, where `P[i][r]` is the maximum profit that can be obtained by allocating resources up to `r` and activity `i`, `p[i]` is the profit of activity `i`, and `r[i]` is the amount of resources



### Dynamic Programming with Examples Such as Knapsack

- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be used to solve problems that can be formulated as recurrence relations, which express the solution of a problem in terms of the solutions of smaller instances of the same problem.
- Dynamic programming can reduce the time complexity of solving a problem from exponential to polynomial, by avoiding recomputation of subproblems and storing the results in a table or an array.
- One of the classic examples of dynamic programming is the 0/1 knapsack problem, which can be stated as follows:

  - Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight does not exceed a given limit and the total value is as large as possible.
  - The 0/1 knapsack problem is called so because each item can be either included (1) or excluded (0) from the collection, but not partially.
  - The 0/1 knapsack problem can be solved using dynamic programming by defining a two-dimensional array `K[n+1][W+1]`, where `n` is the number of items and `W` is the weight limit of the knapsack.
  - The array `K[i][j]` stores the maximum value that can be obtained by using items from `1` to `i` and having a total weight of at most `j`.
  - The array can be filled up using the following recurrence relation:

    - `K[0][j] = 0` for all `j`, because no items can be included if there are none.
    - `K[i][0] = 0` for all `i`, because no value can be obtained if the weight limit is zero.
    - `K[i][j] = K[i-1][j]` if `w[i] > j`, because the `i`th item cannot be included if its weight exceeds the current weight limit.
    - `K[i][j] = max(K[i-1][j], v[i] + K[i-1][j-w[i]])` if `w[i] <= j`, because the `i`th item can be either included or excluded, and the maximum value is the maximum of these two options.
  - The optimal value of the problem is `K[n][W]`, and the optimal subset of items can be obtained by tracing back the array from this cell and checking which items were included or excluded at each step.
  - The time complexity of this algorithm is `O(nW)`, and the space complexity is also `O(nW)`.



### Dynamic Programming with Examples

Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure. It involves breaking down a complex problem into smaller and simpler subproblems, solving them once and storing their solutions in a table or an array, and then using these solutions to construct the solution for the original problem. Dynamic programming can reduce the time and space complexity of recursive algorithms by avoiding repeated computations.

Some examples of problems that can be solved using dynamic programming are:

- **Knapsack problem**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- **Coin change problem**: Given a set of coin denominations and a target amount, find the minimum number of coins needed to make the change or determine if it is impossible.
- **Longest common subsequence problem**: Given two sequences, find the length of the longest subsequence that is common to both of them.
- **Matrix chain multiplication problem**: Given a sequence of matrices, find the most efficient way to multiply them together. The cost of multiplying two matrices is equal to the number of scalar multiplications required.
- **All pair shortest paths problem**: Given a weighted graph, find the shortest distance between every pair of vertices in the graph. There are two algorithms for solving this problem using dynamic programming: Warshall's algorithm and Floyd's algorithm.

#### Warshall's Algorithm

Warshall's algorithm is a dynamic programming algorithm that computes the transitive closure of a directed graph. The transitive closure of a graph is a new graph that contains an edge from u to v if there is a path from u to v in the original graph. The algorithm works as follows:

- Initialize a matrix W of size n x n, where n is the number of vertices in the graph, such that W[i][j] = 1 if there is an edge from i to j, and W[i][j] = 0 otherwise.
- For k = 1 to n, do the following:
  - For i = 1 to n, do the following:
    - For j = 1 to n, do the following:
      - W[i][j] = W[i][j] or (W[i][k] and W[k][j])
- Return W as the transitive closure of the graph.

The time complexity of Warshall's algorithm is O(n^3), where n is the number of vertices in the graph. The space complexity is O(n^2), since we need to store the matrix W.

#### Floyd's Algorithm

Floyd's algorithm is a dynamic programming algorithm that computes the shortest distances between every pair of vertices in a weighted graph. The algorithm works as follows:

- Initialize a matrix D of size n x n, where n is the number of vertices in the graph, such that D[i][j] = w(i, j) if there is an edge from i to j with weight w(i, j), and D[i][j] = infinity otherwise. Also, set D[i][i] = 0 for all i.
- For k = 1 to n, do the following:
  - For i = 1 to n, do the following:
    - For j = 1 to n, do the following:
      - D[i][j] = min(D[i][j], D[i][k] + D[k][j])
- Return D as the matrix of shortest distances between every pair of vertices.

The time complexity of Floyd's algorithm is O(n^3), where n is the number of vertices in the graph. The space complexity is O(n^2), since we need to store the matrix D.



### Dynamic Programming with Examples Such as Resource Allocation Problem

- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming can be applied to both discrete and continuous problems, where the state space can be finite or infinite, and the time horizon can be finite or infinite.
- Dynamic programming can reduce the time complexity of solving a problem by storing and reusing the solutions of subproblems, instead of recomputing them.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up. Top-down approach starts from the original problem and breaks it down into smaller subproblems, and solves them recursively. Bottom-up approach starts from the smallest subproblems and builds up the solution of the original problem by combining the solutions of subproblems.
- Resource allocation problem is an example of a dynamic programming problem, where a limited amount of resources (such as money, time, or materials) need to be allocated to a number of activities (such as projects, tasks, or locations) in order to maximize the total return (such as profit, utility, or satisfaction).
- Resource allocation problem can be formulated as follows: given N activities, each with a return function r_k(x_k) that depends on the amount of resource x_k allocated to it, and a total amount of resource X, find the optimal allocation x* = (x*_1, x*_2, ..., x*_N) that maximizes the total return R(x) = sum(r_k(x_k)) subject to the constraint sum(x_k) <= X.
- Resource allocation problem can be solved using dynamic programming by defining the state as the remaining amount of resource and the stage as the activity index. The state transition equation is x_k = x_k-1 - x_k, and the return function is r_k(x_k). The optimal value function is V_k(x_k) = max(r_k(x_k) + V_k+1(x_k-1 - x_k)), where V_N+1(x_N) = 0. The optimal allocation can be obtained by tracing back the optimal decisions at each stage.
- Resource allocation problem can be generalized to multiple types of resources, multiple constraints, and nonlinear return functions. In such cases, the state space, the state transition equation, and the return function may become more complex, and the optimal value function may not have a closed-form solution. Numerical methods, such as linear programming, nonlinear programming, or gradient descent, may be needed to solve the problem.



### Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

- Backtracking is an algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Branch and bound is an algorithm for discrete and combinatorial optimization problems and mathematical optimization, where the problem is to minimize or maximize a linear function of several variables, possibly subject to some constraints. The algorithm explores a tree of possible solutions, using bounds to avoid exploring suboptimal branches.
- Both backtracking and branch and bound use the depth-first search method to traverse the state-space tree of possible solutions, but they differ in how they prune the branches that are unlikely to lead to optimal solutions. Backtracking uses a bounding function that checks whether the current partial solution satisfies the constraints, while branch and bound uses a bounding function that compares the current partial solution with the best known solution so far.
- Some examples of problems that can be solved by backtracking and branch and bound are:

  - Travelling salesman problem: Given a set of cities and distances between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point. This problem can be solved by backtracking, by generating all possible permutations of cities and checking the total distance of each route, or by branch and bound, by using a lower bound on the length of any route that starts with a given partial route.
  - Graph coloring: Given an undirected graph and a number of colors, the problem is to assign a color to each vertex of the graph such that no two adjacent vertices have the same color, and the number of colors used is minimized. This problem can be solved by backtracking, by assigning colors to vertices one by one and checking for conflicts, or by branch and bound, by using an upper bound on the number of colors needed for any partial coloring.
  - n-Queen problem: Given a chessboard of size n x n, the problem is to place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem can be solved by backtracking, by placing queens on different rows and columns and checking for attacks, or by branch and bound, by using a lower bound on the number of queens that can be placed on the remaining rows and columns.
  - Hamiltonian cycle: Given an undirected graph, the problem is to find a simple cycle that visits every vertex exactly once and returns to the starting vertex. This problem can be solved by backtracking, by generating all possible paths that start and end at a given vertex and checking for cycles, or by branch and bound, by using a lower bound on the length of any cycle that starts with a given partial path.
  - Sum of subsets: Given a set of positive integers and a target sum, the problem is to find all subsets of the given set whose elements add up to the target sum. This problem can be solved by backtracking, by generating all possible subsets and checking their sums, or by branch and bound, by using an upper bound on the sum of any subset that contains a given partial subset.



### Backtracking, Branch and Bound with Examples Such as Graph Coloring

- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large number of possibilities.
- Backtracking works by exploring the solution space incrementally, building a partial solution at each step, and then backtracking (undoing) the last step if it leads to a dead end (an infeasible or suboptimal solution).
- Backtracking can be applied to problems that have the following characteristics:
  - The problem can be decomposed into a sequence of decisions or choices.
  - Each choice has a finite number of alternatives or candidates.
  - The goal is to find a complete solution that satisfies some constraints or optimality criteria.
- Backtracking can be implemented using recursion or iteration, with the help of a data structure (such as a stack) to store the partial solutions and the candidates for the next choice.
- Backtracking can be classified into two types: chronological backtracking and intelligent backtracking.
  - Chronological backtracking always undoes the most recent choice when a dead end is encountered, and tries the next alternative for that choice.
  - Intelligent backtracking can undo more than one choice at a time, by using some information (such as a bound or a heuristic) to prune the search space and avoid exploring unpromising branches.
- Branch and bound is a technique to solve optimization problems that involve finding the best (minimum or maximum) solution among a large number of possibilities.
- Branch and bound works by dividing the solution space into smaller and smaller subspaces (branches), and then bounding (estimating) the quality of the best solution in each subspace.
- Branch and bound can be applied to problems that have the following characteristics:
  - The problem can be formulated as a mathematical optimization problem, such as a linear programming or an integer programming problem.
  - The objective function and the constraints are linear or can be linearized.
  - The solution space is discrete or can be discretized.
- Branch and bound can be implemented using recursion or iteration, with the help of a data structure (such as a queue or a priority queue) to store the subspaces and their bounds.
- Branch and bound can be classified into two types: best-first branch and bound and depth-first branch and bound.
  - Best-first branch and bound always selects the subspace with the best (lowest or highest) bound for further exploration, and maintains a global upper or lower bound for the optimal solution.
  - Depth-first branch and bound explores the subspaces in a depth-first order, and updates a local upper or lower bound for the optimal solution at each node.

- Graph coloring is an example of a problem that can be solved by backtracking or branch and bound.
- Graph coloring is the problem of assigning colors to the vertices of a graph, such that no two adjacent vertices have the same color, and the number of colors used is minimized.
- Graph coloring can be modeled as a backtracking problem, by considering the following choices and candidates:
  - The choices are the vertices of the graph, ordered by some criterion (such as the degree or the index).
  - The candidates for each vertex are the colors that have not been used by its neighbors.
  - The goal is to color all the vertices with the minimum number of colors.
- Graph coloring can be modeled as a branch and bound problem, by considering the following formulation and bounds:
  - The formulation is an integer programming problem, where the variables are binary indicators of whether a vertex is colored with a certain color, and the objective is to minimize the sum of the variables, subject to the constraints that each vertex is colored with exactly one color, and no two adjacent vertices are colored with the same color.
  - The bounds can be computed by relaxing the integer constraints and solving the linear programming problem, or by using some heuristics (such as the greedy algorithm or the Welsh-Powell algorithm) to obtain an upper bound for the minimum number of colors, and a lower bound based on the chromatic number or the chromatic index of the graph.



### Backtracking with Examples Such as n-Queen Problem

Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve an optimization problem. Backtracking is also known as depth-first search or branch and bound. Backtracking works in an incremental way and is an optimization over the naive approach.

Backtracking can be applied to solve problems that involve finding all (or some) solutions to a problem that satisfy a given set of constraints. Some examples of such problems are:

- n-Queen problem: Place n queens on an n×n chessboard such that no two queens attack each other.
- Graph coloring problem: Assign colors to the vertices of a graph such that no two adjacent vertices have the same color.
- Hamiltonian cycle problem: Find a cycle that visits every vertex of a graph exactly once.
- Sum of subsets problem: Find all subsets of a given set of integers that sum up to a given value.

The general idea of backtracking is to try different possibilities (branches) until a solution is found, or all possibilities are exhausted. A branch can be rejected (pruned) if it does not satisfy some constraint, or if it leads to a dead end (a partial solution that cannot be extended further).

The pseudocode for backtracking is:

```
backtrack(current_state):
  if current_state is a solution:
    report or store the solution
  else:
    for each possible choice from current_state:
      if the choice is valid:
        make the choice and update current_state
        backtrack(current_state)
        undo the choice and restore current_state
```

The n-Queen problem can be solved using backtracking as follows:

- The current_state is an array of size n that stores the column index of the queen in each row. For example, current_state = [2, 4, 1, 3] means that there is a queen at (0, 2), (1, 4), (2, 1), and (3, 3).
- A solution is found when the current_state has n elements, meaning that n queens have been placed.
- The possible choices are the column indices from 0 to n-1 for the next row.
- The choice is valid if it does not conflict with any of the queens already placed. This can be checked by comparing the row, column, and diagonal distances of the new queen with the existing queens.
- The choice is made by appending the column index to the current_state array.
- The choice is undone by removing the last element from the current_state array.

The pseudocode for n-Queen problem using backtracking is:

```
nQueen(n):
  backtrack([]) # start with an empty state

backtrack(current_state):
  if current_state has n elements:
    report or store current_state as a solution
  else:
    row = current_state.length # the next row to place a queen
    for col from 0 to n-1:
      if col is a valid choice for row:
        current_state.append(col) # make the choice
        backtrack(current_state) # explore further
        current_state.pop() # undo the choice
```

The validity check for col can be implemented as:

```
isValid(current_state, col):
  row = current_state.length
  for i from 0 to row-1:
    if current_state[i] == col: # same column
      return false
    if abs(current_state[i] - col) == abs(i - row): # same diagonal
      return false
  return true
```



### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve an optimization problem.
- Backtracking is often implemented recursively by trying to extend a partial solution obtained so far and backtrack (go back) if the extension is not valid or does not lead to a desired solution.
- Backtracking can be applied to problems that require finding all (or some) solutions, such as enumerating permutations, combinations, subsets, or satisfying assignments.
- Backtracking can also be applied to problems that require finding a single solution that satisfies some constraints, such as puzzles, games, or combinatorial optimization problems.
- Backtracking is based on the idea of depth-first search (DFS), where the nodes of a search tree are explored in a LIFO (last-in first-out) order.
- Backtracking differs from DFS in that it abandons a branch of the search tree when it determines that the branch cannot possibly lead to a valid solution. This can save a lot of time and space, especially when the search space is large and the constraints are tight.
- Backtracking can be implemented using a stack to store the nodes of the search tree, or using recursion, which implicitly uses the call stack.
- Backtracking can be optimized by using heuristics, pruning, and memoization to reduce the size of the search space and avoid repeated work.

#### Example: Hamiltonian Cycles

- A Hamiltonian cycle is a cycle in an undirected graph that visits every vertex exactly once and returns to the starting vertex.
- Finding a Hamiltonian cycle in a graph is an NP-complete problem, which means that there is no known polynomial-time algorithm to solve it for all graphs.
- However, backtracking can be used to find a Hamiltonian cycle (if it exists) or determine that none exists in a given graph.
- The idea is to start from any vertex and try to extend a partial path by adding adjacent vertices that are not already in the path, until either a cycle is formed or all vertices are exhausted.
- If a cycle is formed, check if it is a Hamiltonian cycle (i.e., it contains all vertices). If yes, return the cycle as a solution. If no, backtrack and try another extension.
- If all vertices are exhausted, backtrack and try another extension.
- If all possible extensions have been tried and no Hamiltonian cycle is found, return that none exists.

##### Algorithm

- Input: A graph G = (V, E) with n vertices and m edges
- Output: A Hamiltonian cycle in G or a message that none exists

- Choose a starting vertex v and initialize a path P = [v]
- Define a recursive function backtrack(P) that takes a path P as input and returns a Hamiltonian cycle or None
  - If P contains n vertices, check if the last vertex in P is adjacent to the first vertex in P
    - If yes, return P as a Hamiltonian cycle
    - If no, return None
  - For each vertex u that is adjacent to the last vertex in P and not already in P
    - Append u to P and call backtrack(P)
    - If backtrack(P) returns a Hamiltonian cycle, return it
    - Otherwise, remove u from P and continue the loop
  - If the loop ends without returning a Hamiltonian cycle, return None
- Call backtrack(P) and return its result



### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve a computational problem.
- Backtracking is often implemented using recursion, which makes the code compact and elegant.
- Backtracking can be used to solve problems that involve finding all possible arrangements or permutations of a given set of elements, such as the n-queens problem, the sudoku problem, the crossword puzzle, etc.
- Backtracking can also be used to solve optimization problems, such as the knapsack problem, the traveling salesman problem, the graph coloring problem, etc.
- The basic idea of backtracking is to start from an empty solution vector and one by one add items (candidates) to the solution vector. For each item, we check if it is feasible to add it to the solution vector. If it is, we recursively explore further by adding more items. If it is not, we backtrack and remove the item from the solution vector and try a different item.
- The key to backtracking is to define the following components:
  - The solution vector: a data structure that holds the partial or complete solution to the problem.
  - The candidates: a set of possible items that can be added to the solution vector.
  - The feasibility function: a function that checks if a candidate can be added to the solution vector without violating any constraints.
  - The goal function: a function that checks if the solution vector is complete and satisfies the problem statement.
- One example of a problem that can be solved using backtracking is the sum of subsets problem. The problem is to find all subsets of a given set of positive integers that sum up to a given target value. For example, given the set {10, 7, 5, 18, 12, 20, 15} and the target value 35, the subsets are {10, 7, 18}, {10, 5, 20}, {10, 12, 13}, {7, 5, 12, 15}, {18, 17}, {20, 15}.
- To solve the sum of subsets problem using backtracking, we can define the following components:
  - The solution vector: an array of boolean values that indicate whether an element of the given set is included in the subset or not. For example, [true, false, true, false, false, false, false] means that the subset contains the first and the third element of the set, i.e., {10, 5}.
  - The candidates: the remaining elements of the given set that have not been considered yet. For example, if the solution vector is [true, false, true, false, false, false, false], the candidates are {18, 12, 20, 15}.
  - The feasibility function: a function that checks if adding a candidate to the solution vector will not exceed the target value. For example, if the solution vector is [true, false, true, false, false, false, false], the target value is 35, and the candidate is 18, the feasibility function will return false, because 10 + 5 + 18 > 35.
  - The goal function: a function that checks if the sum of the elements in the solution vector is equal to the target value. For example, if the solution vector is [true, false, true, false, false, false, false], the target value is 35, and the sum of the elements in the solution vector is 15, the goal function will return false, because 15 != 35.
- The pseudocode for the backtracking algorithm for the sum of subsets problem is as follows:

```
// n is the size of the given set, s is the array of the given set elements, t is the target value, x is the solution vector, and sum is the current sum of the elements in the solution vector
backtrack(n, s, t, x, sum) {
  // if the goal function is true, print the solution vector
  if (sum == t) {
    print(x)
    return
  }
  // if there are no more candidates, return
  if (n == 0) {
    return
  }
  // for each candidate
  for i from 0 to 1 {
    // set the ith element of the solution vector to true or false
    x[n-1] = i
    // if the feasibility function is true, recursively explore further
    if (sum + i *

```




## Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, meaning that given a solution, we can check if it is correct in a number of steps that is proportional to some power of the input size. A problem is NP-complete if it is NP and also every other NP problem can be reduced to it in polynomial time, meaning that we can transform any instance of any NP problem into an instance of the NP-complete problem such that the answer is the same. NP-complete problems are believed to be the hardest problems in NP, and no polynomial time algorithm is known for any of them. If a polynomial time algorithm is found for any NP-complete problem, then it would imply that P = NP, which is one of the most famous open questions in computer science.

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones according to some objective function. For example, finding the shortest path between two nodes in a graph, or finding the maximum number of clauses that can be satisfied in a boolean formula. Approximation algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal one in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the approximation. For some NP-complete optimization problems, there are approximation algorithms that achieve a constant or a logarithmic approximation ratio, meaning that the solution found by the algorithm is within a constant or a logarithmic factor of the optimal one. For some other NP-complete optimization problems, there are no approximation algorithms that achieve a polynomial approximation ratio, unless P = NP    .

- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting city. The TSP is NP-complete even if the distances satisfy the triangle inequality, meaning that the distance between any two cities is no more than the sum of the distances between them and a third city. There is no approximation algorithm for the TSP that achieves a constant approximation ratio, unless P = NP. However, there is a 2-approximation algorithm for the TSP with triangle inequality, which is based on finding a minimum spanning tree of the cities and then traversing it in a depth-first order .

  - Graph Coloring: Given an undirected graph and a positive integer k, assign a color to each node of the graph such that no two adjacent nodes have the same color, and use at most k colors. The Graph Coloring problem is NP-complete for any fixed k greater than 2. There is no approximation algorithm for the Graph Coloring problem that achieves a polynomial approximation ratio, unless P = NP. However, there is a simple greedy algorithm that uses at most ∆ + 1 colors, where ∆ is the maximum degree of the graph, which is a logarithmic approximation ratio .

  - n-Queen Problem: Given a positive integer n, place n queens on an n x n chessboard such that no two queens attack each other, meaning that no two queens share the same row, column, or diagonal. The n-Queen problem is NP-complete for any n greater than 3. There is no approximation algorithm for the n-Queen problem, since it is a decision problem and not an optimization problem. However, there are some heuristic algorithms that can find a solution for the n-Queen problem in polynomial time for most values of n, such as the backtracking algorithm or the hill-climbing algorithm .

  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each node exactly once and returns to the starting node. The Hamiltonian Cycle problem is NP-complete for any graph. There is no approximation algorithm for the Hamiltonian Cycle problem that achieves a constant approximation ratio, unless P = NP



### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, given a certificate or a witness for the answer. A problem is NP-complete if it is NP and every other NP problem can be reduced to it in polynomial time, using a transformation that preserves the answer. NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm for them.
- Approximation Algorithms are a way of coping with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function. An approximation algorithm does not guarantee the best solution, but it tries to come as close as possible to the optimal solution in polynomial time, by giving a performance guarantee or an approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution  .
- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better approximation ratio than 3/2, unless P=NP. A simple 2-approximation algorithm is to find a minimum spanning tree of the cities, and then traverse it in a depth-first order, skipping the visited cities. This algorithm produces a tour that is at most twice as long as the optimal one .
  - Graph Coloring: Given an undirected graph and a number k, assign a color to each vertex such that no two adjacent vertices have the same color, and use at most k colors. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better approximation ratio than n^(1-1/k), unless P=NP. A simple k-approximation algorithm is to order the vertices arbitrarily, and then assign the smallest available color to each vertex in that order. This algorithm uses at most k colors, and produces a coloring that is at most n^(1-1/k) times worse than the optimal one .
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better approximation ratio than n^(1/2), unless P=NP. A simple n-approximation algorithm is to place a queen on each row, and then move it to the column that minimizes the number of conflicts with other queens. This algorithm places n queens on the board, and produces a solution that is at most n times worse than the optimal one .
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting point. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better approximation ratio than 2, unless P=NP. A simple 2-approximation algorithm is to find a minimum spanning tree of the graph, and then traverse it in a depth-first order, skipping the visited vertices. This algorithm produces a cycle that is at most twice as long as the optimal one .
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the set that sums up to the target, or report that no such subset exists. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better approximation ratio than 2, unless P=NP. A simple 2-approximation algorithm is to sort the set in decreasing order, and then add the elements to the subset one by one, as long as the sum does not exceed the target. This algorithm produces a subset that is at most twice as large as the optimal one .



### NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP-complete if it is both NP and NP-hard. NP means that any given solution can be verified in polynomial time, and NP-hard means that any other NP problem can be reduced to it in polynomial time. NP-complete problems are believed to be the hardest problems in NP, and no polynomial time algorithm is known to solve them. Examples of NP-complete problems are the Travelling Salesman Problem, the Graph Coloring Problem, the n-Queen Problem, the Hamiltonian Cycle Problem, and the Sum of Subsets Problem.

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. An approximation algorithm does not guarantee the optimal solution, but rather a solution that is close to the optimal one in terms of some measure of quality, such as the ratio of the cost or value of the solution to the optimal one. The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, which is at most the time required to solve any NP problem. Examples of approximation algorithms are the 2-approximation algorithm for the Vertex Cover Problem, the 7/8-approximation algorithm for the Max 3-SAT Problem, and the Christofides algorithm for the Metric Travelling Salesman Problem    .

- Graph Coloring is an NP-complete problem that asks for the minimum number of colors needed to color the vertices of a graph such that no two adjacent vertices have the same color. An approximation algorithm for this problem is to use a greedy strategy that assigns colors to the vertices in some order, and always chooses the smallest available color that does not conflict with any of the previously colored neighbors. This algorithm can use at most one more color than the optimal solution, and thus has an approximation ratio of 2.

- Travelling Salesman Problem is an NP-complete problem that asks for the shortest tour that visits every vertex of a graph exactly once and returns to the starting point. A metric version of this problem assumes that the graph satisfies the triangle inequality, which means that the distance between any two vertices is no more than the sum of the distances along any other path between them. An approximation algorithm for the metric version of this problem is the Christofides algorithm, which first finds a minimum spanning tree of the graph, then adds the minimum number of edges to make it Eulerian, and then follows the Eulerian circuit while skipping repeated vertices. This algorithm can guarantee a tour that is at most 1.5 times longer than the optimal one, and thus has an approximation ratio of 1.5.

- n-Queen Problem is an NP-complete problem that asks for the number of ways to place n queens on an n x n chessboard such that no two queens attack each other. An approximation algorithm for this problem is to use a backtracking strategy that tries to place a queen in each row, and checks for conflicts with the previous queens. If a conflict is found, the algorithm backtracks and tries a different column. This algorithm can find a solution in polynomial time if one exists, but it cannot guarantee that it will find all the solutions or the optimal one.

- Hamiltonian Cycle Problem is an NP-complete problem that asks for a cycle that visits every vertex of a graph exactly once and returns to the starting point. An approximation algorithm for this problem is to use a heuristic that starts from a random vertex, and repeatedly adds the nearest unvisited vertex to the cycle, until all the vertices are visited. This algorithm can find a cycle in polynomial time, but it cannot guarantee that it will find the shortest one or that one exists at all.

- Sum of Subsets Problem is an NP-complete problem that asks for a subset of a given set of positive integers that sums up to a given target value. An approximation algorithm for this problem is to use a greedy strategy that sorts the integers in descending order, and then adds the largest one that does not exceed the remaining target value, until the target value is reached or no more integers can be added. This algorithm can find a subset in polynomial time, but it cannot guarantee that it will find the optimal one or that one exists at all.



### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP-complete if it is both NP and NP-hard. NP means that any instance of the problem can be verified in polynomial time, given a certificate or a witness for the answer. NP-hard means that any problem in NP can be reduced to this problem in polynomial time, meaning that this problem is at least as hard as any problem in NP.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions. An approximation algorithm does not guarantee the best solution, but it aims to come as close as possible to the optimal solution in polynomial time. An approximation algorithm has an approximation ratio, which is the ratio between the value of the solution obtained by the algorithm and the value of the optimal solution  .
- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting city. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better than 3/2 approximation ratio, unless P=NP. A simple approximation algorithm is to find a minimum spanning tree of the cities, and then traverse the tree in a depth-first order, skipping any visited city. This algorithm has a 2-approximation ratio .
  - Graph Coloring: Given an undirected graph, assign a color to each vertex such that no two adjacent vertices have the same color, and minimize the number of colors used. This problem is NP-complete, and there is no polynomial time algorithm that can achieve a better than n/2 approximation ratio, where n is the number of vertices, unless P=NP. A simple approximation algorithm is to order the vertices arbitrarily, and then assign the smallest available color to each vertex in that order. This algorithm has a n-approximation ratio .
  - n-Queen Problem: Given a n x n chessboard, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem is NP-complete, and there is no polynomial time algorithm that can find a solution for any n, unless P=NP. A simple approximation algorithm is to place a queen on the first column of each row, and then move each queen to the right until it is not attacked by any other queen. This algorithm may not find a solution, but if it does, it has a 1-approximation ratio.
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting vertex. This problem is NP-complete, and there is no polynomial time algorithm that can find a solution for any graph, unless P=NP. A simple approximation algorithm is to find a minimum spanning tree of the graph, and then traverse the tree in a depth-first order, skipping any visited vertex. This algorithm may not find a solution, but if it does, it has a 2-approximation ratio.
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the integers that adds up to the target sum, or report that no such subset exists. This problem is NP-complete, and there is no polynomial time algorithm that can find a solution for any instance, unless P=NP. A simple approximation algorithm is to sort the integers in decreasing order, and then add the largest integer that does not exceed the remaining target sum, until the target sum is reached or no more integers can be added. This algorithm may not find a solution, but if it does, it has a 1-approximation ratio.



### NP-Completeness and Approximation Algorithms with Examples Such as Hamiltonian Cycles

- NP-Completeness is a concept that deals with the complexity of decision problems, i.e., problems that have a yes or no answer. A problem is NP-complete if it is both NP and NP-hard. NP means that the problem can be solved in polynomial time by a non-deterministic algorithm, i.e., an algorithm that can guess the correct solution among many possibilities. NP-hard means that the problem is at least as hard as any other NP problem, i.e., any NP problem can be reduced to it in polynomial time. 
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, i.e., problems that have a numerical objective function to be maximized or minimized. These algorithms do not guarantee the optimal solution, but they aim to come as close as possible to it in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution obtained by the algorithm and the value of the optimal solution.   
- Some examples of NP-complete optimization problems are:
  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point. The approximation ratio of the best known polynomial time algorithm for TSP is 1.5. 
  - Graph Coloring: Given an undirected graph, assign a color to each vertex such that no two adjacent vertices have the same color. The objective is to minimize the number of colors used. The approximation ratio of the best known polynomial time algorithm for graph coloring is O(log n), where n is the number of vertices. 
  - n-Queen Problem: Given an n x n chessboard, place n queens on it such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. The objective is to maximize the number of queens placed. The approximation ratio of the best known polynomial time algorithm for n-queen problem is 0.75. 
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting point. The objective is to minimize the length of the cycle. The approximation ratio of the best known polynomial time algorithm for Hamiltonian cycle is 2. 
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the set that sums up to the target. The objective is to maximize the number of elements in the subset. The approximation ratio of the best known polynomial time algorithm for sum of subsets is 0.5.



### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that relates to the difficulty of solving certain problems in polynomial time. A problem is NP-complete if it belongs to the class NP (nondeterministic polynomial time) and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for every problem in NP.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. Optimization problems are those that seek to find the best solution among a set of feasible solutions, according to some objective function. For example, finding the shortest path between two nodes in a graph, or finding the maximum number of clauses that can be satisfied in a Boolean formula. Approximation algorithms do not guarantee the best solution, but they aim to come as close as possible to the optimal solution in polynomial time  .
- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point. This problem is NP-complete, and there is no polynomial time algorithm that can guarantee a solution within any constant factor of the optimal length. However, there are approximation algorithms that can achieve a solution within a logarithmic factor of the optimal length, such as the Christofides algorithm.
  - Graph Coloring: Given an undirected graph, assign a color to each node such that no two adjacent nodes have the same color, and minimize the number of colors used. This problem is NP-complete, and there is no polynomial time algorithm that can guarantee a solution within any constant factor of the optimal number of colors. However, there are approximation algorithms that can achieve a solution within a logarithmic factor of the optimal number of colors, such as the greedy algorithm.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem is NP-complete, and there is no polynomial time algorithm that can guarantee a solution for any n. However, there are approximation algorithms that can find a solution for most values of n, such as the backtracking algorithm.
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each node exactly once and returns to the starting point. This problem is NP-complete, and there is no polynomial time algorithm that can guarantee a solution for any graph. However, there are approximation algorithms that can find a solution for some classes of graphs, such as the Dirac's theorem for graphs with minimum degree at least n/2.
  - Sum of Subsets: Given a set of positive integers and a target value, find a subset of the set that sums up to the target value. This problem is NP-complete, and there is no polynomial time algorithm that can guarantee a solution for any set and target. However, there are approximation algorithms that can find a solution for some cases, such as the dynamic programming algorithm for sets with small integers.



### NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer. A problem is NP if it can be verified in polynomial time, given a certificate or a witness for the answer. A problem is NP-complete if it is NP and every other NP problem can be reduced to it in polynomial time. NP-complete problems are believed to be the hardest problems in NP, and no efficient algorithm is known to solve them in the worst case.
- Approximation Algorithms are a way of coping with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones. An approximation algorithm does not guarantee the optimal solution, but it tries to come as close as possible to it in polynomial time. The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution obtained by the algorithm and the value of the optimal solution  .
- Some examples of NP-complete optimization problems and their approximation algorithms are:

  - Travelling Salesman Problem (TSP): Given a set of cities and the distances between them, find the shortest tour that visits each city exactly once and returns to the starting point. This problem is NP-complete, and the best known approximation algorithm has a ratio of 1.5, which means that the tour found by the algorithm is at most 1.5 times longer than the optimal tour.
  - Graph Coloring: Given an undirected graph, assign a color to each vertex such that no two adjacent vertices have the same color, and use the minimum number of colors possible. This problem is NP-complete, and the best known approximation algorithm has a ratio of O(log n), where n is the number of vertices in the graph.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal. This problem is NP-complete, and the best known approximation algorithm has a ratio of O(n^(1/3)), which means that the algorithm can place at least n^(1/3) queens on the board without any attacks.
  - Hamiltonian Cycle: Given an undirected graph, find a cycle that visits each vertex exactly once and returns to the starting point. This problem is NP-complete, and the best known approximation algorithm has a ratio of 2, which means that the cycle found by the algorithm is at most twice as long as the optimal cycle.
  - Sum of Subsets: Given a set of positive integers and a target sum, find a subset of the set that adds up to the target sum, or report that no such subset exists. This problem is NP-complete, and the best known approximation algorithm has a ratio of 2, which means that the sum of the subset found by the algorithm is at most twice the target sum.

