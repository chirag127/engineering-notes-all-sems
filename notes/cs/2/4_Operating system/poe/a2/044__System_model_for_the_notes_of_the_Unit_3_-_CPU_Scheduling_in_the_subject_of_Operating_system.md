 Here is the content in markdown format without any emojis or external links:

### System model for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. CPU: The Central Processing Unit(CPU) is the brain of the computer which executes program instructions. It spends its time executing processes and performing Tasks.
2. Memory: The memory is used to hold the instructions and data of the processes that are being executed. The CPU fetches instructions from memory, executes them and stores results back in memory.
3. Ready queue: The processes which are residing in the memory and are ready to execute are kept in the ready queue. The processes from the ready queue get the CPU depending on the CPU scheduling algorithm used.
4. Device queues: The I/O devices also have their device queues where the processes waiting for Input Output get queued. Once a process completes its I/O operation, it moves back to the ready queue.

The above system model components interact with each other in the following manner:
1. When a process enters the system, it is placed in the ready queue.
2. The CPU scheduling algorithm picks a process from the ready queue and allocates the CPU to it.
3. The process executes for a while and if it needs some Input Output, it gets placed in the I/O device queue.
4. Once the I/O is complete, the process moves back to the ready queue.
5. This cycle continues until the process terminates.

The notes cover the system model to give an overview of how the CPU scheduling works. The key components like CPU, Memory and Queues along with their interactions are described in a formal manner as requested without the use of emojis or external links. The points are written in a way to serve as study material for exams on the topic of CPU Scheduling.