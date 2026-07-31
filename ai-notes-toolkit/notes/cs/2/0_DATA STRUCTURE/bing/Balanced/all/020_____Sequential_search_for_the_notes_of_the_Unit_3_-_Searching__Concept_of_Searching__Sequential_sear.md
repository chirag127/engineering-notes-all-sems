# Sequential Search

- Sequential search is the most natural searching method. In this method, the searching begins with searching every element of the list till the required record is found.
- Sequential search is also known as linear search, as it scans the list or array linearly from the first element to the last element .
- The average number of comparisons in a sequential search is (N+1)/2 where N is the size of the list or array.
- The best case of sequential search is when the target element is the first element, and the worst case is when the target element is the last element or not present in the list or array.
- The time complexity of sequential search is O(N) in the worst case and O(1) in the best case.
- Sequential search is simple and easy to implement, but it is inefficient for large or unsorted lists or arrays.
- Sequential search can be performed on any type of list or array, whether it is sorted or unsorted, sequential or linked.

# Index Sequential Search

- Index sequential search is a searching method that uses an index file to speed up the search process.
- An index file is a file that contains some specific group or division of required records, such as the first letter of the name, the range of values, or the category of items.
- The index file is sorted according to the key field of the records, and each index entry points to the first record of the corresponding group or division in the main file.
- To perform an index sequential search, first the index file is searched using binary search or interpolation search to find the index entry that matches or precedes the target key.
- Then, the main file is searched sequentially from the record pointed by the index entry until the target record is found or the end of the group or division is reached.
- The advantage of index sequential search is that it reduces the number of comparisons and disk accesses compared to sequential search, especially for large or sorted files.
- The disadvantage of index sequential search is that it requires extra space and time to create and maintain the index file, and it may become outdated if the main file is updated frequently.
- The time complexity of index sequential search is O(log I + S) where I is the size of the index file and S is the average size of the group or division in the main file.