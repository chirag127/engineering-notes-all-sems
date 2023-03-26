 Here is the formal content in markdown format without any emojis or external links on the topic of memory requirements and control for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

### Memory Requirements and Control

* Memory is a limited resource in embedded systems. The real-time kernel must manage memory efficiently.
* The kernel requires memory for its code and data as well as for task control blocks, stacks, and message queues.
* Partitions are fixed-size blocks of memory allocated for tasks. Tasks are assigned memory from partitions.
* If all partitions are full, incoming tasks may be rejected or existing tasks may be suspended to free up memory.
* Dynamic memory allocation enables more flexible memory usage but requires more complex memory management in the kernel. External fragmentation can occur, leaving scattered blocks of unused memory between allocated blocks.
* Memory can be shared between tasks through shared partitions or explicit sharing mechanisms. Access to shared memory must be controlled to avoid corruption. Semaphores or other synchronization mechanisms are typically used.
* Swapping or virtual memory techniques can be used to handle more tasks than can fit in physical memory, at the cost of performance. These techniques are less common in real-time systems.
* Garbage collection can reclaim unused memory, but the non-deterministic nature of garbage collection makes it problematic for real-time systems. Manual memory deallocation is more common.

The points are written in a formal tone without any feelings or friendliness as emojis or external links are avoided. The content is written in markdown format as a study material to learn the topic. Please let me know if you would like me to modify or expand the answer.