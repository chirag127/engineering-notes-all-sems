### Paged segmentation

- Paged segmentation is a memory management technique that combines the advantages of paging and segmentation.
- In paged segmentation, the logical address space of a process is divided into variable-sized segments, and each segment is further divided into fixed-sized pages .
- The segment table contains the base address and the size of each segment, and the page table contains the frame number and the offset of each page within a segment.
- The physical address is computed by using the segment number, the page number, and the offset from the logical address.
- Paged segmentation allows for a flexible and efficient allocation of memory, where each segment can have a different size and meaning, and each page can have a different protection and sharing attributes .
- Paged segmentation reduces the external fragmentation caused by segmentation, and the internal fragmentation caused by paging.
- Paged segmentation also reduces the size of the segment table, by dividing it into pages and storing it in the main memory.
- Paged segmentation is used in some operating systems, such as Multics and Intel 80386.