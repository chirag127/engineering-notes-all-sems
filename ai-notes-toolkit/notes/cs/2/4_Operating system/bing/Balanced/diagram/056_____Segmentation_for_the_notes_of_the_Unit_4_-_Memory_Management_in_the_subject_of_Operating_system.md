### Segmentation

- Segmentation is an operating system memory management technique of division of a computer's primary memory into segments or sections.
- Segments are logical units of a program, such as code, data, stack, heap, etc.
- Segments can be of variable size and noncontiguous in physical memory.
- Segments are identified by a segment number and an offset within the segment.
- Segmentation provides the user's view of the memory, as opposed to paging which provides the system's view of the memory.
- Segmentation has the following advantages:
  - Protection: Segments can have different access rights, such as read-only, execute-only, etc. This prevents unauthorized or illegal access to memory locations.
  - Sharing: Segments can be shared among different processes, such as libraries, code, etc. This reduces the memory requirement and improves performance.
  - Relocation: Segments can be relocated in physical memory without affecting the logical address. This facilitates dynamic loading and linking of segments.
  - Segmentation has the following disadvantages:
  - External fragmentation: Segments of different sizes may leave holes in the memory, which cannot be used by other segments. This wastes memory space and reduces efficiency.
  - Overhead: Segmentation requires additional hardware support, such as segment table, segment registers, etc. This increases the complexity and cost of the system.
  - Segmentation can be combined with paging to overcome some of the drawbacks of both techniques. This is called segmentation with paging or paged segmentation.