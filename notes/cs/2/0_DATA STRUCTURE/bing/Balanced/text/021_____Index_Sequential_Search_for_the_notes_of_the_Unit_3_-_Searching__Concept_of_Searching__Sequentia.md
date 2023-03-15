### Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database .
- An index file is a data structure that contains references to a group of records or blocks in the array or database, based on some key values .
- The index file is searched first using a suitable algorithm, such as binary search, to find the index that points to the block that contains the desired record .
- Then, the block is searched sequentially to locate the record within the block .
- Index sequential search reduces the number of comparisons and disk accesses required to find a record, compared to a simple sequential search .
- However, index sequential search also has some drawbacks, such as the extra space and time required to create and maintain the index file, and the possibility of index overflow if the index file grows too large .

### Example of Index Sequential Search

- Suppose we have an array of 100 records, sorted by a numeric key, and we want to search for the record with the key 75.
- We can create an index file that contains 10 entries, each pointing to a block of 10 records in the array, as shown below:

| Index | Key | Block |
| ----- | --- | ----- |
| 1     | 10  | 1-10  |
| 2     | 20  | 11-20 |
| 3     | 30  | 21-30 |
| 4     | 40  | 31-40 |
| 5     | 50  | 41-50 |
| 6     | 60  | 51-60 |
| 7     | 70  | 61-70 |
| 8     | 80  | 71-80 |
| 9     | 90  | 81-90 |
| 10    | 100 | 91-100|

- We can use binary search to find the index that contains the key 75, which is index 8 with the key 80.
- Then, we can search the block 71-80 sequentially to find the record with the key 75, which is the fifth record in the block.
- The total number of comparisons required for this search is log2(10) + 5 = 8, which is much less than the 75 comparisons required for a simple sequential search.