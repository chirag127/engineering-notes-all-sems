 Here is the content in markdown format without any emojis or external links, written in a formal tone:

### Protection schemes for the notes of the Unit 4 - Memory Management in the subject of Operating system.

1. Base and limit registers: The base register holds the smallest legal address for a process and the limit register specifies the size of the range. If the process makes an out-of-bounds memory reference, the OS aborts the instruction.
2. Segmentation: Divides memory into segments that can have different sizes and protection attributes. A process can have multiple segments. The OS checks that a memory reference is within the bounds of the appropriate segment and has proper access rights.
3. Paging: Divides memory into fixed-sized blocks called pages. Each process gets its own set of pages. The OS checks that a memory reference is within the bounds of the appropriate page and has proper access rights.
4. Capability-based addressing: Processes possess capabilities or tickets that identify the resources they are allowed to access. The OS verifies that a process has the proper capability for any memory access.
5. Memory-mapping techniques: Instead of having conventional addresses to refer to memory, processes specify the name of the memory object they wish to access. The OS verifies that the process has the proper access rights to the object.

The above points cover the key protection schemes for memory management to ensure secure and authorized access to memory by processes. The formal tone and formatting without emojis or external links as requested have been incorporated in the content. Please let me know if you would like me to modify or expand the response.