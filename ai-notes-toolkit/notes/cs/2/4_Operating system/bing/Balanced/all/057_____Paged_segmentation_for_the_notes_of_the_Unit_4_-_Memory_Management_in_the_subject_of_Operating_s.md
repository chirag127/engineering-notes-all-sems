# Paged Segmentation

- Paged segmentation is a memory management technique that combines the advantages of paging and segmentation.
- In paged segmentation, the logical address space of a process is divided into variable-sized segments, and each segment is further divided into fixed-sized pages.
- The segment table contains the base address and the limit of each segment, and the page table contains the frame number and the offset of each page within a segment.
- The physical address is computed by using the segment number, the page number, and the offset within the page.
- Paged segmentation allows for a flexible and efficient allocation of memory, as each segment can have a different size and protection, and each page can be mapped to any frame in the physical memory.
- Paged segmentation also reduces the external fragmentation and the size of the segment table, as the segments are divided into pages of equal size.
- However, paged segmentation also introduces some disadvantages, such as the increased overhead of maintaining two levels of tables, the internal fragmentation within the pages, and the complexity of the address translation process.