### Binary Search

- Binary search is an efficient algorithm for finding an element within a sorted array. 
- It works by repeatedly dividing in half the portion of the list that could contain the element, until you've narrowed down the possible locations to just one. 
- Binary search compares the element to the middle element of the array or subarray. 
- If the element is equal to the middle element, then the search is successful and the position of the element is returned. 
- If the element is less than the middle element, then the search continues in the left half of the array. 
- If the element is greater than the middle element, then the search continues in the right half of the array. 
- This process is repeated until the element is found or the array is exhausted. 
- The time complexity of binary search is O(log n), where n is the number of elements in the array. 
- The space complexity of binary search is O(1), as it only requires a constant amount of auxiliary space. 
- One of the main drawbacks of binary search is that the array must be sorted before applying the algorithm. 
- Sorting the array can take additional time and space, depending on the sorting algorithm used. 
- Binary search is useful for building more complex algorithms in computer science, such as interpolation search, exponential search, and binary search trees. 
- Binary search can also be implemented iteratively or recursively, depending on the preference of the programmer. 
- Binary search is also known as half-interval search, logarithmic search, or binary chop.   

: Binary search algorithm - Wikipedia
: Binary search (article) | Algorithms | Khan Academy
: Binary Search - GeeksforGeeks