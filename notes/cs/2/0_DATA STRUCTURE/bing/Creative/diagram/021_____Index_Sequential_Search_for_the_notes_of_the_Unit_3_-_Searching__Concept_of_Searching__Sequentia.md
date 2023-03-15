### Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database.
- An index file is a separate file that contains references to some records or blocks of records in the main file.
- Each reference in the index file consists of a search key and a pointer to the corresponding record or block in the main file.
- The index file is much smaller than the main file and can be searched faster using binary search or interpolation search.
- Once the index file is searched, the pointer is used to locate the record or block in the main file and then a sequential search is performed within the record or block to find the desired element.
- The advantage of index sequential search is that it reduces the number of comparisons and disk accesses compared to a simple sequential search.
- The disadvantage of index sequential search is that it requires extra space and time to create and maintain the index file, and it may become inefficient if the main file is frequently updated or modified.