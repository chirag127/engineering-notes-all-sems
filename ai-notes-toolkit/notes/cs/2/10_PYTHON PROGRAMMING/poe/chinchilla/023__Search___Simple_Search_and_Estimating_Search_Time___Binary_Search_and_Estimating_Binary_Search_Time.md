### Search: Simple Search and Estimating Search Time, Binary Search and Estimating Binary Search Time for the notes of the Unit 5 - Iterators & Recursion: Recursive Fibonacci, Tower Of Hanoi in the subject of PYTHON PROGRAMMING.

In the world of programming, searching is a fundamental operation. It is the process of finding a specific element or value from a given set of data. In this unit, we will learn about two types of searching techniques: Simple Search and Binary Search.

#### Simple Search

Simple Search is also known as Linear Search. It is a straightforward and easy-to-understand searching algorithm. It works by comparing each element of the given set of data with the target value until it is found.

Steps to perform Simple Search:
1. Start searching from the first element of the data set.
2. Compare the target value with the current element.
3. If the target value is found, return the index of the element.
4. If the target value is not found, move to the next element and repeat steps 2-3.
5. If the target value is not found in the entire data set, return -1.

Estimating Search Time for Simple Search:
The average time complexity of Simple Search is O(n), where n is the number of elements in the data set. Therefore, the time required to search for an element increases linearly with the increase in the size of the data set.

#### Binary Search

Binary Search, also known as Half-Interval Search or Logarithmic Search, is a more efficient searching algorithm than Simple Search. It works by dividing the data set into halves and searching for the target value in the appropriate half.

Steps to perform Binary Search:
1. Sort the data set in ascending or descending order.
2. Divide the data set into two halves.
3. Compare the target value with the middle element.
4. If the target value is equal to the middle element, return the index of the element.
5. If the target value is less than the middle element, repeat steps 2-4 on the left half of the data set.
6. If the target value is greater than the middle element, repeat steps 2-4 on the right half of the data set.
7. If the target value is not found in the entire data set, return -1.

Estimating Search Time for Binary Search:
The average time complexity of Binary Search is O(log n), where n is the number of elements in the data set. Therefore, the time required to search for an element increases logarithmically with the increase in the size of the data set.

In conclusion, both Simple Search and Binary Search are essential searching algorithms in programming. Simple Search is easy to understand and implement, but it is not very efficient for large data sets. On the other hand, Binary Search is more efficient, but it requires the data set to be sorted. So, depending on the size and nature of the data set, either Simple Search or Binary Search can be used.