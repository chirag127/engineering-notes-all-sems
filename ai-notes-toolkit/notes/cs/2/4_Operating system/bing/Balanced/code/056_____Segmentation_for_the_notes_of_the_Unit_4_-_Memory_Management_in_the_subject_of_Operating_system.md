### Segmentation

- Segmentation is an operating system memory management technique of division of a computer's primary memory into segments or sections.
- Segments are logical units of memory that correspond to the user's view of the program, such as code, data, stack, etc.
- Segments can be of variable size and noncontiguous in physical memory.
- Segments are identified by a segment number and an offset within the segment.
- Segments are mapped to physical memory by a segment table, which contains the base address and the limit of each segment.
- Segmentation provides the following advantages :
  - It allows the user to access memory in a logical way, rather than a physical way.
  - It supports the sharing and protection of segments among processes.
  - It supports the dynamic growth and shrinking of segments, as well as dynamic loading and linking of segments.
  - It reduces the external fragmentation and compaction problems of paging.
- Segmentation also has some disadvantages :
  - It may cause internal fragmentation within segments, as segments are allocated in fixed units of memory.
  - It may cause segmentation fault, which occurs when a process tries to access a memory location outside its segment limit.
  - It may require more memory for storing the segment table and more time for accessing the segment table.