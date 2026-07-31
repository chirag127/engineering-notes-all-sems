 Here is the content in markdown format without any emojis or external links and in formal tone:

### Performance of demand paging for the notes of the Unit 4 - Memory Management in the subject of Operating system.

1. Less memory wastage: In demand paging, only those pages are loaded into the memory which are actually referenced by the process. This results in less memory wastage as compared to other memory allocation techniques like pure segmentation or swapping where the allocated memory may not be fully utilized.

2. Thrashing: As the space in the memory is limited, it may lead to a situation where the pages in the memory are constantly being replaced leading to a severe performance degradation. This situation is known as thrashing. Thrashing can be avoided by properly tuning the operating system parameters to allocate memory judiciously.

3. More page faults: Whenever a page is not found in the memory, a page fault occurs which results in the page being loaded from the secondary storage. This leads to more page faults and increases the time required for the process execution. The performance can be increased by efficiently managing the memory to reduce page faults.

4. More overhead: The operating system has to constantly keep track of the pages in the memory, replace the pages if required and handle the page faults. This leads to more overhead on the operating system resulting in slightly lower performance as compared to other memory management techniques. However, this overhead is not very high and the other benefits of demand paging outweigh this minor overhead.

The above points discuss the major pros and cons of demand paging in terms of performance. By properly tuning the parameters and efficiently managing the memory, the performance of demand paging can be increased and the disadvantages can be minimized. Demand paging is a very useful memory management technique which forms the basis of virtual memory in operating systems.