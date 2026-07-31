# Time and Space Complexity

## Introduction

- Time and space complexity are two measures of the efficiency of an algorithm.
- Time complexity refers to the amount of time required by an algorithm to execute for a given input size.
- Space complexity refers to the amount of memory (or storage) required by an algorithm to execute for a given input size.
- Both time and space complexity depend on the input size, the algorithm design, and the implementation details.

## Basic Terminology

- Input size: The number of elements or the size of the data that the algorithm operates on. For example, the input size for sorting an array of n numbers is n, and the input size for searching a key in a binary tree of n nodes is n.
- Algorithm: A finite set of well-defined steps or instructions to solve a problem or perform a task. For example, the algorithm for sorting an array of numbers can be described as follows:

  - Step 1: Compare the first two elements of the array and swap them if they are out of order.
  - Step 2: Repeat step 1 for the next pair of elements until the end of the array is reached.
  - Step 3: Repeat steps 1 and 2 until no swaps are made in a pass through the array.

- Efficiency of an algorithm: The measure of how well an algorithm performs in terms of time and space. For example, the efficiency of the sorting algorithm above can be improved by using a different algorithm, such as merge sort or quick sort, that can sort the array in fewer comparisons and swaps.

## Time Complexity

- Time complexity is the measure of how long an algorithm takes to execute for a given input size. It is usually expressed as a function of the input size, denoted by n.
- For example, the time complexity of the sorting algorithm above can be expressed as T(n) = O(n^2), where T(n) is the time function and O(n^2) is the asymptotic notation for the upper bound of the time function.
- Asymptotic notation is a way of describing the growth rate of a function as the input size approaches infinity. It ignores the constant factors and lower-order terms that do not affect the long-term behavior of the function. There are three common asymptotic notations:

  - Big Oh notation: O(f(n)) represents the upper bound of a function, meaning that the function is always less than or equal to some constant multiple of f(n) for sufficiently large n. For example, O(n^2) means that the function is always less than or equal to c*n^2 for some constant c and for all n > n0, where n0 is some threshold value.
  - Big Theta notation: Θ(f(n)) represents the tight bound of a function, meaning that the function is always between some constant multiples of f(n) for sufficiently large n. For example, Θ(n^2) means that the function is always between c1*n^2 and c2*n^2 for some constants c1 and c2 and for all n > n0, where n0 is some threshold value.
  - Big Omega notation: Ω(f(n)) represents the lower bound of a function, meaning that the function is always greater than or equal to some constant multiple of f(n) for sufficiently large n. For example, Ω(n^2) means that the function is always greater than or equal to c*n^2 for some constant c and for all n > n0, where n0 is some threshold value.

- The asymptotic notation helps to compare the efficiency of different algorithms by focusing on the dominant term of the time function. For example, O(n^2) is more efficient than O(n^3), but less efficient than O(n) or O(log n).
- The time complexity of an algorithm can be analyzed by counting the number of basic operations or steps performed by the algorithm for a given input size. For example, the sorting algorithm above performs n-1 comparisons and swaps in the first pass, n-2 in the second pass, and so on, until 1 in the last pass. Therefore, the total number of comparisons and swaps is (n-1) + (n-2) + ... + 1 = n*(n-1)/2, which is O(n^2).

## Space Complexity

- Space complexity is the measure of how much memory (or storage) an algorithm requires to execute for a given input size. It is usually expressed as a function of the input size, denoted by n.
- For example, the space complexity of the sorting algorithm above can be expressed as S(n) = O(n), where S(n) is the space function and O(n) is the asymptotic notation