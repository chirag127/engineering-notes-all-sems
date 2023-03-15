### Segmentation

- Segmentation is an operating system memory management technique of division of a computer's primary memory into segments or sections.
- Segments are logical units of memory that correspond to the user's view of the program, such as code, data, stack, etc.
- Segments can be of variable size and noncontiguous in physical memory.
- Segments are identified by a segment number and an offset within the segment.
- Segments are mapped to physical memory by a segment table, which contains the base address and the limit of each segment.
- Segmentation provides the following advantages :
  - Protection: Segments can have different access rights and privileges, such as read-only, execute-only, etc. This prevents unauthorized or illegal access to memory.
  - Sharing: Segments can be shared among different processes, such as libraries, code, etc. This reduces the memory requirement and improves performance.
  - Flexibility: Segmentation provides a higher degree of flexibility than paging. Segments can be of variable size, and processes can be designed to have multiple segments, allowing for more fine-grained memory allocation.
- Segmentation also has some disadvantages :
  - External fragmentation: Segments of different sizes may leave holes in the memory, which cannot be used by other segments. This wastes memory and reduces the available space for allocation.
  - Overhead: Segmentation requires a segment table for each process, which consumes memory and CPU time. The segment table also needs to be updated whenever a segment is created, deleted, or resized.
  - Complexity: Segmentation adds complexity to the memory management system, as it requires more hardware and software support. Segmentation also makes it harder to implement virtual memory and swapping.