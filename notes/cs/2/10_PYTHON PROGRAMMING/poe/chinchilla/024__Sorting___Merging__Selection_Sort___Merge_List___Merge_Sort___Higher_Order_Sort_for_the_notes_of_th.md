### Sorting & Merging: Selection Sort , Merge List , Merge Sort , Higher Order Sort

Sorting and merging are essential operations in computer programming that help organize and manipulate data efficiently. In Python programming, there are various sorting and merging algorithms that one can use to sort and merge data. Below are some of the most commonly used sorting and merging algorithms:

#### Selection Sort
- Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the data and moving it to the beginning of the sorted part.
- The algorithm maintains two subarrays: the sorted subarray and the unsorted subarray. Initially, the sorted subarray is empty, and the unsorted subarray is the entire data.
- The algorithm then finds the minimum element from the unsorted subarray and swaps it with the first element of the unsorted subarray. This process is repeated until the unsorted subarray becomes empty.
- Selection sort has a time complexity of O(n^2), which makes it inefficient for large data sets.

#### Merge List
- Merging two lists is an operation that combines two sorted lists into a single sorted list.
- The merge list algorithm works by comparing the first elements of the two lists and selecting the smaller one to be the first element of the new list. The algorithm then repeats this process for the remaining elements of the two lists until one of the lists becomes empty.
- The remaining elements of the non-empty list are then appended to the end of the new list.
- Merge list has a time complexity of O(n), which makes it efficient for merging large data sets.

#### Merge Sort
- Merge sort is a divide and conquer algorithm that works by dividing the data into two halves, sorting each half recursively, and then merging the two sorted halves into a single sorted list.
- The algorithm first divides the data into two halves and sorts each half recursively using the merge sort algorithm.
- The sorted halves are then merged using the merge list algorithm to produce the final sorted list.
- Merge sort has a time complexity of O(nlogn), which makes it efficient for sorting large data sets.

#### Higher Order Sort
- Higher order sort is a sorting algorithm that uses a comparison function to determine the order of the elements in the data.
- The comparison function is a function that takes two elements as input and returns a value indicating their order.
- The higher order sort algorithm works by repeatedly applying the comparison function to pairs of elements in the data and swapping them if necessary.
- Higher order sort has a time complexity of O(nlogn), which makes it efficient for sorting large data sets.

### Iterators & Recursion: Recursive Fibonacci , Tower Of Hanoi

#### Recursive Fibonacci
- The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1.
- Recursive Fibonacci is a function that calculates the nth number in the Fibonacci sequence recursively.
- The function works by calling itself recursively with the two preceding numbers until it reaches the base case, which is when the input number is 0 or 1.
- Recursive Fibonacci has a time complexity of O(2^n), which makes it inefficient for calculating large Fibonacci numbers.

#### Tower Of Hanoi
- The Tower of Hanoi is a mathematical puzzle in which a tower of discs of different sizes is moved from one peg to another, one disc at a time, while obeying certain rules.
- The Tower of Hanoi problem can be solved recursively.
- The recursive algorithm works by moving the top n-1 discs from the source peg to the auxiliary peg, then moving the nth disc from the source peg to the target peg, and finally moving the n-1 discs from the auxiliary peg to the target peg.
- Tower of Hanoi has a time complexity of O(2^n), which makes it inefficient for solving large Tower of Hanoi problems.