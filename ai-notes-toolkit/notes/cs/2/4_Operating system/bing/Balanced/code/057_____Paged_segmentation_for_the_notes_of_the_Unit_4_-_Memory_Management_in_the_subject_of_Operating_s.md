### Paged segmentation

- Paged segmentation is a memory management technique that combines the advantages of paging and segmentation.
- Paging is a technique that divides the logical address space of a process into fixed-size pages, and maps them to physical frames in the main memory.
- Segmentation is a technique that divides the logical address space of a process into variable-size segments, and maps them to physical regions in the main memory.
- Paged segmentation divides the logical address space of a process into segments, and then divides each segment into pages.
- This allows for a flexible allocation of memory, where each segment can have a different size, and each page can have a different size within a segment.
- Paged segmentation also reduces the external fragmentation caused by segmentation, as the pages can be allocated to any available frames in the main memory.
- Paged segmentation requires two levels of mapping to translate a logical address to a physical address.
- The logical address consists of a segment number, a page number, and an offset within the page.
- The segment number is used to index a segment table, which contains the base address and the limit of each segment.
- The base address of the segment is added to the page number to form the address of the page table for that segment.
- The page table contains the frame number and the valid bit for each page in the segment.
- The frame number is concatenated with the offset to form the physical address of the memory location.
- Paged segmentation can be illustrated by the following diagram:

```
Logical address: | Segment number | Page number | Offset |
                 |----------------|-------------|--------|
                 | 8 bits         | 8 bits      | 8 bits |

Segment table:   | Segment number | Base address | Limit  |
                 |----------------|--------------|--------|
                 | 0              | 1000         | 200    |
                 | 1              | 1500         | 100    |
                 | 2              | 2000         | 300    |
                 | ...            | ...          | ...    |

Page table for segment 0: | Page number | Frame number | Valid bit |
                          |-------------|--------------|-----------|
                          | 0           | 10           | 1         |
                          | 1           | 12           | 1         |
                          | 2           | 15           | 0         |
                          | ...         | ...          | ...       |

Page table for segment 1: | Page number | Frame number | Valid bit |
                          |-------------|--------------|-----------|
                          | 0           | 11           | 1         |
                          | 1           | 13           | 1         |
                          | 2           | 16           | 0         |
                          | ...         | ...          | ...       |

Page table for segment 2: | Page number | Frame number | Valid bit |
                          |-------------|--------------|-----------|
                          | 0           | 14           | 1         |
                          | 1           | 17           | 1         |
                          | 2           | 18           | 1         |
                          | ...         | ...          | ...       |

Main memory:    | Frame number | Content |
                |--------------|---------|
                | 0            | ...     |
                | 1            | ...     |
                | 2            | ...     |
                | ...          | ...     |
                | 10           | Page 0 of segment 0 |
                | 11           | Page 0 of segment 1 |
                | 12           | Page 1 of segment 0 |
                | 13           | Page 1 of segment 1 |
                | 14           | Page 0 of segment 2 |
                | 15           | ...     |
                | 16           | ...     |
                | 17           | Page 1 of segment 2 |
                | 18           | Page 2 of segment 2 |
                | ...          | ...     |
```

- For example, to translate the logical address 01000011, we use the following steps:
  - The segment number is 01, which corresponds to segment 1 in the segment table.
  - The base address of segment 1 is 1500, and the limit is 100.
  - The page number is 00, which corresponds to page 0 in the page table for segment 1.
  - The frame number of page 0 is 11, and the valid bit is 1, which means the page is present in the main