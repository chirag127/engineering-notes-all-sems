### Locality of reference for the notes of the Unit 4 - Memory Management in the subject of Operating system

- Locality of reference is the tendency of a computer program to access the same set of memory locations repetitively over a short period of time.
- Locality of reference is based on the observation that programs usually exhibit two types of locality: temporal and spatial.
- Temporal locality means that a memory location that is accessed once is likely to be accessed again soon. For example, a loop variable or a frequently used function.
- Spatial locality means that a memory location that is accessed once is likely to have nearby memory locations accessed soon. For example, an array or a sequential code.
- Locality of reference is important for memory management because it can improve the performance and efficiency of the system by reducing the number of page faults and cache misses .
- Page faults occur when a program tries to access a page that is not present in the main memory and has to be brought from the secondary memory. Cache misses occur when a program tries to access a data that is not present in the cache memory and has to be fetched from the main memory or the secondary memory.
- By exploiting the locality of reference, the system can use techniques such as caching, prefetching, buffering, and paging to keep the frequently and recently accessed pages and data in the faster memory levels and reduce the access time and the memory bandwidth .