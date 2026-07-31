# Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database.
- An index file is a separate file that contains references to some records or blocks of records in the main file, based on some key values or ranges.
- The index file is much smaller than the main file, and can be searched faster using binary search or interpolation search.
- Once the index file is searched, the corresponding record or block of records in the main file can be accessed directly or sequentially, depending on the type of index.
- There are two types of index files: primary index and secondary index.
  - A primary index is a sorted index file that has one entry for each block of records in the main file. The entry contains the key value of the first record in the block, and the address of the block. The main file is also sorted by the same key field.
  - A secondary index is a sorted index file that has one entry for each record in the main file. The entry contains the key value of the record, and the address of the record. The main file can be sorted or unsorted by the key field.
- The advantages of index sequential search are:
  - It reduces the number of comparisons and disk accesses required to find a record, compared to sequential search or binary search on the main file.
  - It allows multiple keys to be used for searching, by creating different index files for different key fields.
  - It supports both exact and range queries, by using the index file to locate the first or last record that satisfies the query condition, and then scanning the main file sequentially.
- The disadvantages of index sequential search are:
  - It requires extra space and time to create and maintain the index file, especially when the main file is updated frequently.
  - It may become inefficient if the index file becomes too large or too sparse, or if the distribution of the key values changes significantly over time.