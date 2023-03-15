# Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

## Simple Search
- A simple search algorithm is one that checks every element in a data structure until it finds the target value or exhausts the search space.
- The most common example of a simple search algorithm is **linear search**, which iterates over an array or a list and compares each element with the target value.
- The time complexity of linear search is **O(n)**, where **n** is the number of elements in the data structure. This means that the worst-case scenario is that the algorithm has to check every element before finding the target or concluding that it is not present.
- The space complexity of linear search is **O(1)**, since it does not require any extra memory to perform the search.

## Binary Search
- A binary search algorithm is one that exploits the **sorted** order of a data structure to reduce the search space by half at each step.
- The most common example of a binary search algorithm is **binary search**, which works on a sorted array or a list. The algorithm starts by comparing the target value with the middle element of the array. If they are equal, the search is over. If the target is smaller, the algorithm discards the right half of the array. If the target is larger, the algorithm discards the left half of the array. The algorithm repeats this process until it finds the target or the array becomes empty.
- The time complexity of binary search is **O(log n)**, where **n** is the number of elements in the data structure. This means that the worst-case scenario is that the algorithm has to perform **log n** comparisons before finding the target or concluding that it is not present.
- The space complexity of binary search is **O(1)** for the iterative implementation, and **O(log n)** for the recursive implementation, since it requires **log n** stack frames to perform the search.