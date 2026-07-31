### Sequential search

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
- The advantages of sequential search are that it is simple, easy to implement, and does not require any sorting or ordering of the list.
- The disadvantages of sequential search are that it is slow, inefficient, and requires more comparisons than other searching methods.

### Index sequential search

- Index sequential search is a searching method that uses an index file to speed up the search process. An index file contains some specific group or division of required records.
- Index sequential search is also known as indexed search or index search.
- Index sequential search can be applied to data structures that are sorted and have random access, such as arrays or files.
- The algorithm for index sequential search is as follows:

```
Step 1: First, read the search element (Target element) in the array or file.
Step 2: In the second step, locate the index file that contains the target element's group or division.
Step 3: If the index file is found, search the target element within the group or division using sequential search or binary search.
Step 4: If the target element is found, display “Target element is found” and terminate the Index Sequential Search function.
Step 5: If the target element is not found, display “Target element is not found” and terminate the Index Sequential Search function.
Step 6: If the index file is not found, display “Target element is not found” and terminate the Index Sequential Search function.
```

- The time complexity of index sequential search is O(log n + k), where n is the number of elements in the list, and k is the number of elements in the group or division.
- The advantages of index sequential search are that it is faster, more efficient, and requires less comparisons than sequential search.
- The disadvantages of index sequential search are that it requires extra space for the index file, and it depends on the distribution and size of the groups or divisions.