### Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database.
- An index file is a separate data structure that contains references to some of the records in the array or database, usually based on a primary key or a candidate key.
- Each reference in the index file points to a block of records in the array or database, or to another expanded index file.
- The index file is searched first using a binary search or another efficient search algorithm, and then the corresponding block of records is searched using a sequential search or another suitable search algorithm.
- The advantage of index sequential search is that it reduces the number of comparisons and disk accesses needed to find a record, compared to a simple sequential search or a binary search on the whole array or database.
- The disadvantage of index sequential search is that it requires extra space and time to create and maintain the index file, and it may become inefficient if the array or database is frequently updated or modified.

#### Example

- Suppose we have an array of 1000 student records, sorted by their roll numbers. Each record contains the student's name, roll number, marks, and address.
- We want to search for the record of the student with roll number 345.
- We create an index file that contains 10 references, each pointing to a block of 100 records in the array. The index file looks like this:

| Index | Roll number | Block pointer |
| ----- | ----------- | ------------- |
| 1     | 1           | 0             |
| 2     | 101         | 100           |
| 3     | 201         | 200           |
| 4     | 301         | 300           |
| 5     | 401         | 400           |
| 6     | 501         | 500           |
| 7     | 601         | 600           |
| 8     | 701         | 700           |
| 9     | 801         | 800           |
| 10    | 901         | 900           |

- We search the index file using a binary search to find the reference with the largest roll number that is less than or equal to 345. This is the reference with index 4, which has the roll number 301 and the block pointer 300.
- We then search the block of records starting from the index 300 using a sequential search to find the record with the roll number 345. This is the record with the index 344, which has the student's name, marks, and address.
- The total number of comparisons needed to find the record is 4 (for the binary search on the index file) + 45 (for the sequential search on the block of records) = 49. This is much less than the number of comparisons needed for a sequential search on the whole array (345) or a binary search on the whole array (10).