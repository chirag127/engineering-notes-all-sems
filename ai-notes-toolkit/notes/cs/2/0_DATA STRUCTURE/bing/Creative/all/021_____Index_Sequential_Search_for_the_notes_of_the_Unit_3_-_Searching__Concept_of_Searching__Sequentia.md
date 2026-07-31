# Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database .
- An index file is a data structure that contains references to a group of records or blocks in the array or database, based on some key values .
- The index file is searched first using a suitable algorithm, such as binary search, to find the index entry that matches or precedes the search key .
- The index entry points to the block or record where the search key is likely to be found, or to another expanded index that further narrows down the search range .
- The block or record is then searched sequentially to locate the exact position of the search key, or to determine that the key is not present .
- Index sequential search reduces the number of comparisons and disk accesses needed to find a key, compared to a simple sequential search .
- However, index sequential search also requires extra space and time to create and maintain the index file, and to update it whenever the array or database is modified .
- Index sequential search is suitable for applications where the array or database is relatively static and the search frequency is high .