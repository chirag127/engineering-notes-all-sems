### Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the search continues in the lower half. Otherwise, it continues in the upper half. Repeatedly check until the value is found or the interval is empty.

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).

#### Algorithm:
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right half subarray after the mid element. So we recur for the right half.
4. Else (x is smaller) recur for the left half.

#### Example:
Suppose we have a sorted array [1, 3, 4, 6, 8, 9, 11] and we want to search for the number 6.

1. We start by comparing 6 with the middle element, 6.
2. Since 6 is equal to the middle element, we have found the number and return the index of the middle element, which is 3.

#### Complexity:
The time complexity of binary search is O(log n) since we divide the search interval in half each time. The space complexity is O(1) since we only need to keep track of the start and end indices of the search interval.

#### Advantages:
- Binary search is faster than linear search for large data sets.
- It is easy to implement and understand.

#### Disadvantages:
- The data set must be sorted.
- It is not efficient for small data sets.
- It may not work for data sets with duplicate values.

#### Applications:
- Binary search is commonly used in computer science, for example in searching algorithms and databases.
- It is also used in mathematical algorithms, such as finding the square root of a number or solving equations.