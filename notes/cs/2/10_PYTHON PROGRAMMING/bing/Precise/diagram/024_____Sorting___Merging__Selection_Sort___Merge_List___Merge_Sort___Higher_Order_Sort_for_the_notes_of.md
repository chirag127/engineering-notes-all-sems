### Sorting & Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

#### Selection Sort:
- Selection sort is an in-place comparison sorting algorithm.
- It has an O(n^2) time complexity, which makes it inefficient on large lists.
- The algorithm divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted.
- The algorithm proceeds by finding the smallest element in the unsorted sublist, exchanging it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.

#### Merge List:
- Merge List is an algorithm to merge two sorted lists into a single sorted list.
- The algorithm compares the first elements of the two lists and appends the smaller element to the result list.
- The process is repeated until one of the lists is exhausted, at which point the remaining elements of the other list are appended to the result list.

#### Merge Sort:
- Merge Sort is a divide and conquer algorithm that was invented by John von Neumann in 1945.
- It has an O(n log n) time complexity, which makes it efficient for large lists.
- The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining, which is the sorted list.

#### Higher Order Sort:
- Higher Order Sort is a sorting algorithm that can sort elements based on multiple criteria.
- The algorithm works by sorting the elements based on the first criterion, and then sorting the elements with equal values based on the second criterion, and so on.
- This can be useful when sorting complex data structures, where multiple fields need to be taken into account when sorting the elements.

### Unit 5 - Iterators & Recursion: Recursive Fibonacci, Tower Of Hanoi

#### Recursive Fibonacci:
- The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding numbers.
- The sequence can be defined recursively, with the base case being F(0) = 0 and F(1) = 1.
- The recursive definition of the Fibonacci sequence is F(n) = F(n-1) + F(n-2) for n > 1.

#### Tower Of Hanoi:
- The Tower of Hanoi is a mathematical puzzle consisting of three pegs and a number of disks of different sizes, which can slide onto any peg.
- The puzzle starts with the disks in a neat stack in ascending order of size on one peg, the smallest at the top.
- The objective of the puzzle is to move the entire stack to another peg, obeying the following rules:
  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the pegs and sliding it onto another peg, on top of the other disks that may already be present on that peg.
  - No disk may be placed on top of a smaller disk.
- The puzzle can be solved recursively, by moving the top n-1 disks to an intermediate peg, then moving the largest disk to the destination peg, and finally moving the n-1 disks from the intermediate peg to the destination peg. This process is repeated until the entire stack is moved to the destination peg.