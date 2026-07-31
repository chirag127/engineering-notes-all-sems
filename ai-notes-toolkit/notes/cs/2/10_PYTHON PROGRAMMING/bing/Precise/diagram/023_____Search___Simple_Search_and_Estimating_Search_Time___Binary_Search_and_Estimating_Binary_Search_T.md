### Unit 5 - Iterators & Recursion: Recursive Fibonacci, Tower Of Hanoi

#### Search: Simple Search and Estimating Search Time

- Simple search, also known as linear search, is a method of finding a target value within a list.
- It sequentially checks each element of the list until a match is found or the whole list has been searched.
- The time complexity of simple search is O(n), where n is the number of elements in the list.
- This means that in the worst case scenario, the algorithm will have to check every element in the list before finding the target value or determining that it is not in the list.
- The average case performance is also O(n), as on average, the algorithm will have to check half of the elements in the list.

#### Binary Search and Estimating Binary Search Time

- Binary search is a search algorithm that finds the position of a target value within a sorted list.
- It works by repeatedly dividing the search interval in half and comparing the middle element of the interval with the target value.
- If the middle element is equal to the target value, the search is successful.
- If the middle element is less than the target value, the search continues in the right half of the interval.
- If the middle element is greater than the target value, the search continues in the left half of the interval.
- The time complexity of binary search is O(log n), where n is the number of elements in the list.
- This means that in the worst case scenario, the algorithm will have to perform log2(n) comparisons before finding the target value or determining that it is not in the list.
- The average case performance is also O(log n), as on average, the algorithm will have to perform log2(n)/2 comparisons.