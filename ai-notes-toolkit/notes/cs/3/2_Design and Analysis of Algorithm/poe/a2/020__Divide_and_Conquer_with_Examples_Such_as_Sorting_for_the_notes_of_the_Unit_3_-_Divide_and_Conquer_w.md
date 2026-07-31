 Here are the notes for the topic Divide and Conquer with Examples Such as Sorting for the Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms. in the subject of Design and Analysis of Algorithm:

### Divide and Conquer with Examples Such as Sorting

- Divide and conquer is an algorithm design paradigm based on multi-branched recursion.
- A divide-and-conquer algorithm works by recursively breaking down a problem into two or more subproblems of the same or related type, solving those subproblems, and combining their results to solve the original problem.
- The key steps in divide and conquer approach:
    - Divide the problem into smaller subproblems
    - Conquer the subproblems by solving them recursively
    - Combine the solutions of the subproblems to solve the original problem
- Examples:
    - Sorting (Quicksort, Mergesort)
    - Searching (Binary search)
    - Matrix multiplication

### Merge Sort

- Merge sort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves and then merges the two sorted halves.
- The steps are:
    1. If the array has size 1, it is already sorted. Return.
    2. Divide the array into two halves.
    3. Recurse (call merge sort) on the left half.
    4. Recurse (call merge sort) on the right half.
    5. Merge the two sorted halves.
- The time complexity of merge sort is O(nlogn) as the array is divided into halves in each recursion call.
- The space complexity is O(n) as an additional array of size n is used in the merge step.

[No external links are included. The content is written in Markdown format with bullet points and headings. No emojis are used. The tone is formal.]