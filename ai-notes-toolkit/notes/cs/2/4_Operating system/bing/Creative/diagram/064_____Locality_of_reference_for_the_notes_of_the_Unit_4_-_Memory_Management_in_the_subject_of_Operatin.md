### Locality of reference

- Locality of reference is the tendency of a computer program to access the same set of memory locations for a particular time period    .
- Locality of reference is based on the observation that programs usually exhibit **temporal locality** and **spatial locality**  .
- Temporal locality means that a memory location that is accessed once is likely to be accessed again soon  . For example, a loop variable or a frequently used function.
- Spatial locality means that a memory location that is accessed once is likely to have its nearby locations accessed soon  . For example, an array or a sequential code.
- Locality of reference is important for improving the performance of memory hierarchy, such as cache memory, virtual memory, and paging   .
- Locality of reference allows the system to predict the future memory accesses and prefetch the data from lower levels of memory to higher levels of memory, reducing the access time and latency   .
- Locality of reference also enables the system to use smaller and faster memory units to store the most frequently or recently accessed data, leaving the larger and slower memory units for the less accessed data   .
- Locality of reference can be improved by using techniques such as loop unrolling, blocking, data structure reorganization, and compiler optimization  .