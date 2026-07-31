# Segmentation in Operating System

- Segmentation is an operating system memory management technique of division of a computer's primary memory into segments or sections.
- Segments are uneven-sized blocks of memory that contain logical units of a program, such as functions, data structures, or modules .
- Segmentation allows the programmer to view the memory as a collection of variable-sized segments, rather than a linear array of bytes or words.
- Segmentation also enables the protection and sharing of memory among different processes or users.
- Segmentation can be implemented in two ways: simple segmentation and virtual memory segmentation.
  - Simple segmentation: Each process is divided into a number of segments, all of which are loaded into memory at run time. The segments are allocated in contiguous memory locations. The segments of different processes may be swapped in and out of memory as needed.
  - Virtual memory segmentation: Each process is divided into a number of segments, not all of which are resident in memory at any time. The segments are allocated in non-contiguous memory locations. The segments of different processes may be paged in and out of memory as needed.
- Segmentation has some advantages and disadvantages over other memory management techniques, such as paging .
  - Advantages:
    - Segmentation is closer to the programmer's view of physical memories, as it allows the separation of code, data, and stack segments.
    - Segmentation prevents internal fragmentation, as each segment occupies only the required amount of memory.
    - Segmentation reduces CPU overhead, as it contains an entire module at once, rather than splitting it into pages.
    - Segmentation facilitates the protection and sharing of memory, as each segment can have its own access rights and permissions.
  - Disadvantages:
    - Segmentation causes external fragmentation, as the segments of different sizes and shapes may leave gaps in memory.
    - Segmentation requires more complex hardware and software support, as it involves two levels of address translation: segment number and segment offset.
    - Segmentation may increase the memory requirement, as each segment needs a segment table entry and a base register.