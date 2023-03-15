### Reentrant Kernels

- A reentrant kernel is the one which allows multiple processes to be executing in the kernel mode at any given point of time and that too without causing any consistency problems among the kernel data structures.
- In kernel mode, a reentrant kernel allows processes (or, more precisely, their corresponding kernel threads) to give up the CPU. They have no effect on other processes entering kernel mode.
- Multiple processor systems may be scheduled together in the case of single-processor systems.
- A kernel is called reentrant if more than one process can be executing kernel code at the same time.
- "At the same time" can mean either that two processes are actually executing kernel code concurrently (on a multiprocessor system) or that one process has been interrupted while it is executing kernel code (because it is waiting for hardware to respond).