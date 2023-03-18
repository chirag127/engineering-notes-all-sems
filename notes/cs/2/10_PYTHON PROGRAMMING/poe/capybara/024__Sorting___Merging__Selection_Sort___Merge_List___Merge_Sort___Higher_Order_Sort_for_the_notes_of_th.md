### Sorting & Merging: Selection Sort , Merge List , Merge Sort , Higher Order Sort

Sorting and merging are important operations in computer programming. In this section, we will discuss different types of sorting algorithms and merging techniques.

#### Selection Sort

Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. This process is repeated until the entire array is sorted.

- Selection sort has a time complexity of O(n^2).
- It is not suitable for large datasets.
- Selection sort is an in-place sorting algorithm.

#### Merge List

Merging two sorted lists into a single sorted list is a common operation in computer programming.

- Merge list algorithm works by comparing the first element of both lists and selecting the smaller one.
- The selected element is added to the new list, and the process is repeated until both lists are empty.
- Merge list has a time complexity of O(n).

#### Merge Sort

Merge sort is a divide-and-conquer algorithm that works by dividing the list into two halves, sorting them separately and then merging them.

- Merge sort has a time complexity of O(n log n).
- It is a stable sorting algorithm.
- Merge sort requires additional memory for the merge step.

#### Higher Order Sort

Higher order sort is a technique for sorting objects based on a key function that extracts a value from the object.

- Key functions can be used to extract complex data types like strings, lists, and dictionaries.
- Higher order sort can sort objects in ascending or descending order.
- Higher order sort has a time complexity of O(n log n).

### Unit 5 - Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

Iterators and recursion are important concepts in Python programming. In this section, we will discuss two problems that can be solved using recursion.

#### Recursive Fibonacci

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The first two numbers in the sequence are 0 and 1.

- Recursive Fibonacci is a function that calculates the nth number in the Fibonacci sequence using recursion.
- Recursive Fibonacci has a time complexity of O(2^n).

#### Tower Of Hanoi

The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod.

- The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
- A disk cannot be placed on top of a smaller disk.
- Tower of Hanoi can be solved using recursion.

In conclusion, sorting and merging are important operations in computer programming. Selection sort, merge list, merge sort, and higher order sort are some of the common sorting and merging techniques. Recursion is an important concept in Python programming, and it can be used to solve problems like recursive Fibonacci and Tower of Hanoi.