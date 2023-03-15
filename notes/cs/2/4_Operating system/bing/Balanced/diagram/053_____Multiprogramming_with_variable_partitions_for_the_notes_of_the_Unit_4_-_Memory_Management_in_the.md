### Multiprogramming with variable partitions

- Multiprogramming with variable partitions is a contiguous memory management technique in which the main memory is not divided into fixed-sized partitions, but rather into variable-sized chunks of free memory that can fit the processes as they arrive  .
- The advantage of this technique is that it can accommodate more processes in the main memory and reduce the internal fragmentation, which is the wasted space within a partition that is not used by the process  .
- The disadvantage of this technique is that it can cause external fragmentation, which is the wasted space between the partitions that is not used by any process. External fragmentation occurs when the processes are allocated and deallocated from the main memory, leaving behind small gaps of free memory that are too small to fit any process  .
- To overcome external fragmentation, a technique called compaction can be used, which involves moving the processes in the main memory to make them contiguous and create a large block of free memory. However, compaction is costly in terms of time and CPU overhead, as it requires updating the addresses of the processes and interrupting their execution  .
- Another technique to reduce external fragmentation is to use a suitable allocation algorithm that can efficiently allocate the free memory to the processes. Some of the common allocation algorithms are:
  - First fit: It allocates the first chunk of free memory that is large enough to fit the process. It is fast but can leave behind small gaps of free memory  .
  - Best fit: It allocates the smallest chunk of free memory that is large enough to fit the process. It can minimize the wasted space but can also create many small gaps of free memory that are difficult to reuse  .
  - Worst fit: It allocates the largest chunk of free memory that is available. It can reduce the number of gaps of free memory but can also create large gaps of free memory that are wasted  .
  - Next fit: It allocates the next chunk of free memory that is large enough to fit the process, starting from the last allocated chunk. It is similar to first fit but can reduce the search time  .

- A diagram to illustrate the multiprogramming with variable partitions is shown below:

```
|-----------------|    |-----------------|    |-----------------|
| Process A (10K) |    | Process A (10K) |    | Process A (10K) |
|-----------------|    |-----------------|    |-----------------|
| Free (20K)      |    | Free (10K)      |    | Free (10K)      |
|-----------------|    |-----------------|    |-----------------|
| Process B (15K) |    | Process B (15K) |    | Process B (15K) |
|-----------------|    |-----------------|    |-----------------|
| Free (10K)      |    | Free (10K)      |    | Process C (10K) |
|-----------------|    |-----------------|    |-----------------|
| Process C (10K) |    | Process C (10K) |    | Free (10K)      |
|-----------------|    |-----------------|    |-----------------|
| Free (5K)       |    | Process D (15K) |    | Process D (15K) |
|-----------------|    |-----------------|    |-----------------|
| Process D (15K) |    | Free (5K)       |    | Free (5K)       |
|-----------------|    |-----------------|    |-----------------|
| Free (5K)       |    | Free (5K)       |    | Free (5K)       |
|-----------------|    |-----------------|    |-----------------|

Initial state    After allocating Process E (10K) using first fit    After deallocating Process E (10K)
```