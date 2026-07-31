# Sorting & Merging

## Selection Sort
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part. The algorithm maintains two sub-lists in a given input list:
1. The sub-list which is already sorted.
2. The remaining sub-list which is unsorted.

In every iteration of selection sort, the minimum element from the unsorted sub-list is picked and moved to the sorted sub-list.

## Merge List
Merging two lists involves combining the elements of the two lists into a single, sorted list. This can be done by comparing the first elements of each list and appending the smaller element to the result list, then repeating the process with the remaining elements of the lists until one of the lists is exhausted. The remaining elements of the non-exhausted list are then appended to the result list.

## Merge Sort
Merge sort is a divide-and-conquer algorithm that works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining, which will be the sorted list. The key process in the merge sort algorithm is the merging of two sorted sub-lists into a single sorted sub-list.

## Higher Order Sort
Higher-order sort refers to sorting algorithms that can sort elements based on a custom comparison function, rather than the default comparison of the elements' values. This allows for more flexible and complex sorting, as the comparison function can be tailored to the specific needs of the data being sorted.

# Unit 5 - Iterators & Recursion

## Recursive Fibonacci
The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding numbers, with the first two numbers being 0 and 1. A recursive function to generate the nth Fibonacci number can be defined as follows:
- If n is 0, return 0.
- If n is 1, return 1.
- Otherwise, return the sum of the (n-1)th and (n-2)th Fibonacci numbers.

## Tower Of Hanoi
The Tower of Hanoi is a mathematical puzzle that consists of three pegs and a number of disks of different sizes, which can slide onto any peg. The puzzle starts with the disks in a neat stack in ascending order of size on one peg, the smallest at the top. The objective of the puzzle is to move the entire stack to another peg, obeying the following rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the pegs and sliding it onto another peg, on top of the other disks that may already be present on that peg.
3. No disk may be placed on top of a smaller disk.

A recursive solution to the Tower of Hanoi puzzle can be defined as follows:
- Move n-1 disks from the start peg to the auxiliary peg, using the end peg as the auxiliary peg.
- Move the nth disk from the start peg to the end peg.
- Move the n-1 disks from the auxiliary peg to the end peg, using the start peg as the auxiliary peg.