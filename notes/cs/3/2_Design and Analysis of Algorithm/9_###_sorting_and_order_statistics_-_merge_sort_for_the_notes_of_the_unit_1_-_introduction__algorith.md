### Sorting and Order Statistics - Merge Sort for the notes of the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time. in the subject of Design and Analysis of Algorithm

Merge Sort is a sorting algorithm that works by dividing the input into smaller sub-arrays, sorting these sub-arrays, and then merging them back together in sorted order. It is a divide-and-conquer algorithm that has a time complexity of O(n log n) in the average and worst-case scenarios.

The algorithm works as follows:

1. Divide: The input array is divided into two halves.

2. Recursively sort: The two halves are sorted recursively using the same algorithm.

3. Merge: The two sorted halves are merged back together in sorted order.

The merge step involves comparing the first elements of the two sub-arrays and adding the smaller element to the result. This process is repeated until one of the sub-arrays is empty, at which point, the remaining elements of the other sub-array are added to the result.

Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input. It is also an efficient sorting algorithm for large arrays, as its time complexity is O(n log n), which is the best possible time complexity for a comparison-based sorting algorithm.

In the context of the subject of Design and Analysis of Algorithm, Merge Sort is one of several sorting algorithms covered in Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time. The unit covers the basics of sorting algorithms, including their time and space complexity, as well as their strengths and weaknesses.
