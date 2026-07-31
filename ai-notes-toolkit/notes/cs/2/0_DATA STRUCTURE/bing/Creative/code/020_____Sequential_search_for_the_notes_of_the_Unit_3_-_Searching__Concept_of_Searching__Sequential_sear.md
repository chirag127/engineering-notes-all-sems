### Sequential search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found .
- Sequential search is also known as linear search or brute-force search .
- Sequential search can be applied to any data structure, such as arrays, linked lists, trees, etc.
- Sequential search has a time complexity of O(n), where n is the number of elements in the list .
- Sequential search is simple and easy to implement, but it is inefficient for large lists or sorted lists .

### Index sequential search

- Index sequential search is a searching method that uses an index file to speed up the search process.
- Index sequential search is also known as indexed search or index search.
- Index sequential search is suitable for sorted lists or files that are accessed frequently.
- Index sequential search creates an index file that contains some specific group or division of required records. The index file is sorted by some key value that is used to locate the records.
- Index sequential search has two steps: first, it searches the index file to find the group or division that contains the target record; second, it performs a sequential search within that group or division to find the exact record.
- Index sequential search has a time complexity of O(log n + k), where n is the number of groups or divisions in the index file, and k is the number of records in each group or division.
- Index sequential search is faster and more efficient than sequential search, but it requires extra space and maintenance for the index file.