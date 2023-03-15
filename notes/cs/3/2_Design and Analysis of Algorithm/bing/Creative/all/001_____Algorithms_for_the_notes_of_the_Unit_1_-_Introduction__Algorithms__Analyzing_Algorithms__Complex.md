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