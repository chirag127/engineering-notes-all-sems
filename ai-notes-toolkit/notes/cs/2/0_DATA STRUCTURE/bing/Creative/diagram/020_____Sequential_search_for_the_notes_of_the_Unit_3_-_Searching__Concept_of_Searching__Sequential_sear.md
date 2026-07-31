### Sequential Search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found.
- Sequential search is also known as linear search or serial search.
- Sequential search can be applied to any data structure, such as arrays, linked lists, or binary trees.
- The algorithm for sequential search is as follows:

```
Step 1: First, read the search element (Target element) in the array.
Step 2: In the second step compare the search element with the first element in the array.
Step 3: If both are matched, display “Target element is found” and terminate the Linear Search function.
Step 4: If both are not matched, compare the search element with the next element in the array.
Step 5: Repeat steps 3 and 4 until the search element is found or the end of the array is reached.
Step 6: If the end of the array is reached, display “Target element is not found” and terminate the Linear Search function.
```

- The time complexity of sequential search is O(n), where n is the number of elements in the list.
- The advantages of sequential search are that it is simple, easy to implement, and does not require any sorting or ordering of the data.
- The disadvantages of sequential search are that it is slow, inefficient, and impractical for large or unsorted data sets.
- Sequential search can be improved by using indexing, which is a technique of creating an index file that contains some specific group or division of required records. This reduces the search time by locating the target element in a specified group.