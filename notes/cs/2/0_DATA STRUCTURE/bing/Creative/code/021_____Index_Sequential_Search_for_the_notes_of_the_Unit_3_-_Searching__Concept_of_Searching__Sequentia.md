### Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database .
- An index file is a data structure that contains references to a group of records or blocks in the array or database, based on some key values .
- The index file is searched first using a suitable algorithm, such as binary search, to find the index that points to the block or group that contains the desired record .
- Then, the block or group is searched sequentially to locate the record within it .
- Index sequential search reduces the number of comparisons and disk accesses needed to find a record, compared to a simple sequential search .
- However, index sequential search requires extra space and time to create and maintain the index file, and may become inefficient if the array or database is frequently updated .

#### Example

- Suppose we have an array of 1000 records, sorted by name, and we want to search for the record with name "Zara".
- We can create an index file that contains 10 entries, each pointing to a block of 100 records in the array, based on the first letter of the name.
- The index file may look like this:

| Index | First letter | Pointer |
| ----- | ------------ | ------- |
| 1     | A            | 0       |
| 2     | C            | 100     |
| 3     | E            | 200     |
| 4     | G            | 300     |
| 5     | J            | 400     |
| 6     | L            | 500     |
| 7     | N            | 600     |
| 8     | R            | 700     |
| 9     | T            | 800     |
| 10    | W            | 900     |

- To search for "Zara", we can use binary search on the index file to find the index that has the first letter "Z", which is 10.
- Then, we can access the block of records starting from the pointer 900, and search sequentially for the record with name "Zara" within that block.
- This way, we only need to perform log(10) + 100 comparisons, instead of 1000 comparisons if we use a simple sequential search on the whole array.