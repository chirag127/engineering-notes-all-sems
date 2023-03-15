### Locality of reference

- Locality of reference is the tendency of a computer program to access the same set of memory locations for a particular time period .
- Locality of reference is based on the observation that programs usually exhibit **temporal locality** and **spatial locality**  .
  - Temporal locality means that a memory location that is accessed once is likely to be accessed again soon.
  - Spatial locality means that a memory location that is accessed once is likely to have nearby memory locations accessed soon.
- Locality of reference is important for the performance of cache memory, which is a small and fast memory that stores frequently accessed data .
  - Cache memory exploits temporal locality by keeping recently accessed data in cache for faster retrieval.
  - Cache memory exploits spatial locality by fetching blocks of data that contain the requested data and its neighboring data.
- Locality of reference can be improved by using techniques such as loop unrolling, blocking, prefetching, and data structure reorganization .
  - Loop unrolling reduces the number of loop control instructions and increases the number of data access instructions in a loop, which improves spatial locality.
  - Blocking divides a large matrix or array into smaller submatrices or subarrays that fit in cache, which improves temporal locality.
  - Prefetching anticipates the future data access patterns and brings the data into cache before it is needed, which reduces cache misses.
  - Data structure reorganization changes the layout of data in memory to make it more cache-friendly, such as using arrays instead of linked lists, or using structures of arrays instead of arrays of structures.