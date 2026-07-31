 Here is the content in markdown format without any emojis or external links, being formal and not showing any feeling or friendliness:

### Multiprogramming with variable partitions

- In this memory management technique, the memory is divided into a number of variable sized partitions.
- The processes are allocated partitions according to their memory requirements.
- The main advantage is that there is no internal fragmentation as the partitions are of variable sizes and allocated according to the process memory requirements.
- However, there is still external fragmentation as the total available memory space is not utilized fully if the total available memory space is not sufficient to accommodate the next partition required by a process.
- To overcome this, compaction is used. It involves shifting the processes so that all the occupied partitions are rearranged and the free memory space is accumulated in between.
- The main limitation is that as the partitions are of variable sizes, it is difficult to keep track of free memory and allocate it to the processes.
- This technique is useful for batch operating systems where the memory requirements are known in advance.

This content is written inside the header for the topic **Multiprogramming with variable partitions** for the notes of the Unit 4 - Memory Management in the subject of Operating system to learn and read from like study material for exams. The points are written in a formal tone without any emojis or external links.