### Segmentation

- Segmentation is an operating system memory management technique of division of a computer's primary memory into segments or sections.
- Segments are logical units of memory that correspond to the user's view of the program, such as code, data, stack, etc.
- Segments can be of variable size and can grow or shrink dynamically.
- Segments are identified by a segment number and an offset within the segment.
- Segments are mapped to physical memory by a segment table, which contains the base address and the limit of each segment.
- Segmentation provides the following advantages :
  - It allows the user to access memory in a logical way, rather than a physical way.
  - It supports the protection and sharing of memory among processes, by assigning different access rights to different segments.
  - It reduces the external fragmentation and compaction problems of paging, by allowing noncontiguous allocation of memory.
  - It provides a higher degree of flexibility and modularity than paging, by allowing processes to have multiple segments of different sizes and types.
- Segmentation also has some disadvantages :
  - It introduces the problem of internal fragmentation, as segments may not fully utilize the allocated memory blocks.
  - It requires more complex hardware and software to implement and manage the segment table and the segment mapping.
  - It may cause more overhead and latency in memory access, as the segment number and the offset need to be translated to a physical address.