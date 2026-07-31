### Index Sequential Search

Index Sequential Search is a searching algorithm that improves the performance of Sequential search by reducing the number of comparisons required to find the desired element in the list. It is also known as the Indexed search or Indexed Sequential Access Method (ISAM).

#### Concept of Index Sequential Search

- Index Sequential Search is based on the principle of creating an index for a list of elements that serves as a guide for searching the elements efficiently.
- The index is created by dividing the list into blocks of fixed size and selecting a representative key value for each block.
- The key values are then stored in an index table along with the block number that contains the elements with the corresponding key value.
- The index table is sorted in ascending order based on the key values.
- During the search operation, the index table is used to locate the block that contains the desired element, and then a sequential search is performed within that block.
- If the desired element is not found in the current block, the next block is accessed based on the index table until the element is found or the end of the list is reached.

#### Advantages of Index Sequential Search

- Index Sequential Search reduces the number of comparisons required to find the desired element compared to sequential search.
- It is efficient for large lists with a fixed block size.
- It can handle both sorted and unsorted lists.

#### Disadvantages of Index Sequential Search

- Index Sequential Search requires additional space to store the index table.
- If the block size is too small, the index table becomes too large, and if the block size is too large, the search time within a block increases.
- The index table needs to be updated whenever new elements are added or deleted from the list, which can be time-consuming.

#### Example

Suppose we have a list of 1000 elements and a block size of 100. The index table would have 10 entries, each representing a block of 100 elements with a representative key value. If we want to search for an element with a key value of 450, we would first search the index table to locate the block containing elements with key values between 401 and 500. Once we locate the block, we would perform a sequential search within that block to find the desired element.

#### Conclusion

Index Sequential Search is a useful searching algorithm for large lists with a fixed block size. It reduces the number of comparisons required to find the desired element compared to sequential search, making it more efficient. However, it requires additional space to store the index table and needs to be updated whenever new elements are added or deleted from the list.