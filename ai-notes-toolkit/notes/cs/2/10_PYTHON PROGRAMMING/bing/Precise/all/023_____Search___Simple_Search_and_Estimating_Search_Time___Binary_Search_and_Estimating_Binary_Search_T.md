# Unit 5 - Iterators & Recursion: Recursive Fibonacci, Tower Of Hanoi

## Search: Simple Search and Estimating Search Time

- Simple search, also known as linear search, is a method for finding an element within a list.
- It sequentially checks each element of the list until a match is found or the whole list has been searched.
- The time complexity of simple search is O(n), where n is the number of elements in the list.
- This means that in the worst case, the algorithm will have to search through all n elements to find the target element.
- The average case is also O(n), as on average, the target element will be found halfway through the list.

## Binary Search and Estimating Binary Search Time

- Binary search is a search algorithm that finds the position of a target value within a sorted array.
- It works by repeatedly dividing the search interval in half and comparing the middle element to the target value.
- If the middle element is equal to the target value, the search is successful.
- If the middle element is greater than the target value, the search continues in the lower half of the array.
- If the middle element is less than the target value, the search continues in the upper half of the array.
- The time complexity of binary search is O(log n), where n is the number of elements in the array.
- This means that in the worst case, the algorithm will have to perform log n comparisons to find the target element.
- The average case is also O(log n), as on average, the target element will be found after log n comparisons.