## Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics

### Algorithms
- An algorithm is a step-by-step procedure for solving a problem or achieving a specific task.
- It is a finite sequence of well-defined, computer-implementable instructions.
- Algorithms can be expressed in many ways, including natural language, pseudocode, flowcharts, and programming languages.

### Analyzing Algorithms
- Analyzing an algorithm involves determining the amount of resources (such as time and storage) necessary to execute it.
- The goal is to predict the performance of different algorithms in order to guide design decisions.
- The analysis of algorithms typically focuses on the worst-case and average-case scenarios.

### Complexity of Algorithms
- The complexity of an algorithm is a measure of the amount of resources (such as time and storage) required to execute it as a function of the size of the input.
- The time complexity of an algorithm is the number of basic operations (such as additions or comparisons) performed as a function of the size of the input.
- The space complexity of an algorithm is the amount of memory required to execute it as a function of the size of the input.

### Growth of Functions
- The growth of a function is a measure of how quickly its values increase as the size of the input increases.
- Commonly used notations for expressing the growth of functions include big O, big Omega, and big Theta.
- These notations provide upper, lower, and tight bounds on the growth of a function, respectively.

### Performance Measurements
- Performance measurements involve collecting data on the actual execution of an algorithm in order to evaluate its efficiency.
- Common performance metrics include execution time, memory usage, and power consumption.
- Performance measurements can be used to compare different algorithms or to optimize the performance of a single algorithm.

### Sorting and Order Statistics
- Sorting involves arranging a set of items in a specific order, such as ascending or descending order.
- Order statistics are specific items in a set, such as the minimum, maximum, or median.
- Common sorting algorithms include Shell Sort, Quick Sort, Merge Sort, Heap Sort, and others.

#### Shell Sort
- Shell Sort is an in-place comparison sort algorithm.
- It is a generalization of insertion sort that allows the exchange of items that are far apart.
- The algorithm works by comparing elements separated by a gap of a certain size and swapping them if they are in the wrong order.

#### Quick Sort
- Quick Sort is an efficient, in-place sorting algorithm.
- It works by selecting a pivot element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
- The pivot is then placed in its final position and the process is repeated on the two sub-arrays.

#### Merge Sort
- Merge Sort is an efficient, comparison-based sorting algorithm.
- It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.
- Merge Sort has a time complexity of O(n log n) in the worst case.

#### Heap Sort
- Heap Sort is a comparison-based sorting algorithm.
- It works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region.
- Heap Sort has a time complexity of O(n log n) in the worst case.

#### Comparison of Sorting Algorithms
- Different sorting algorithms have different time and space complexities, and their performance can vary depending on the size and nature of the input.
- For example, Quick Sort has a time complexity of O(n^2) in the worst case, but it is generally faster than other sorting algorithms for large inputs.
- Sorting algorithms can also be compared based on their stability, adaptivity, and other factors.

#### Sorting in Linear Time
- Some sorting algorithms, such as Counting Sort and Radix Sort, can sort n integers in the range [1, k] in linear time, where k is a constant.
- These algorithms are not comparison-based and rely on the specific properties of the input to achieve linear time complexity.
- However, they are not suitable for all types of inputs and may have large space requirements.