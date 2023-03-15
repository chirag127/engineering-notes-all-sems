# Locality of reference

- Locality of reference is the tendency of a computer program to access the same set of memory locations for a particular time period .
- Locality of reference is based on the observation that programs usually exhibit **temporal locality** and **spatial locality**  .
  - Temporal locality means that a memory location that is accessed once is likely to be accessed again soon in the future.
  - Spatial locality means that a memory location that is accessed once is likely to have nearby memory locations accessed soon in the future.
- Locality of reference is important for the design and performance of cache memory, which is a small and fast memory that stores frequently accessed data .
  - Cache memory exploits temporal locality by keeping recently accessed data in the cache for faster retrieval.
  - Cache memory exploits spatial locality by fetching blocks of data that contain the requested data and its neighboring data, assuming that they will be accessed soon.
- Locality of reference is also relevant for other memory management techniques, such as virtual memory, paging, and segmentation.
  - Virtual memory uses locality of reference to reduce the number of page faults, which occur when a requested page is not in the main memory.
  - Paging and segmentation use locality of reference to allocate and deallocate memory pages or segments efficiently and reduce external fragmentation.