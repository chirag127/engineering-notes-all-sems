 Here are the notes in formal Markdown format without emojis or external links:

### Parallel for the notes of the Unit 1 - EMBEDDED OS INTERNALS

1. Embedded Systems: Systems that are dedicated to specific tasks, like appliances, vehicles, medical devices, etc. They typically have software embedded in ROM or flash memory.
2. Real-Time Systems: Systems where correct functional operation depends on the correct sequencing and timing of inputs and outputs. Missing a deadline can lead to system failure. Hard real-time systems have firm deadlines. Soft real-time systems have flexible deadlines.
3. Multitasking: Performing multiple tasks simultaneously. Implemented via task switching, where the OS switches between tasks, giving the appearance of simultaneous execution.
4. Multi-Processing: Having multiple CPU cores executing tasks in parallel. Symmetric multiprocessing systems have multiple identical cores, while asymmetric systems have cores of different capabilities.
5. Co-operative Multitasking: Each task is responsible for voluntarily giving up the CPU to allow other tasks to run. Problems occur if a task does not yield.
6. Preemptive Multitasking: The OS can forcibly remove tasks from the CPU, allowing other tasks to run and implementing task scheduling. More reliable but requires more overhead.
7. Memory Management: The OS is responsible for allocating and de-allocating memory to tasks and managing virtual memory. Memory may be segmented or paged, with page replacement algorithms used when memory is full.
8. Synchronization: Coordinating access to shared resources. Critical sections of code can be protected using mechanisms such as semaphores, monitors, message passing, etc. Deadlock and livelock are hazards to avoid.
9. Input/Output: The OS is responsible for abstracting the hardware interfaces for storage, displays, networks, etc. and providing standard interfaces to applications. I/O can be via polling or interrupts.

Does this look okay? Let me know if you would like me to modify or expand on anything.