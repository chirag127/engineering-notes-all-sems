### System model for CPU scheduling

- CPU scheduling is a process that allows one process to use the CPU while the execution of another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU.
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling is performed by the operating system using various scheduling algorithms.
- A system model for CPU scheduling consists of the following components:
  - A set of processes that are ready to execute on the CPU.
  - A ready queue that holds the processes waiting for the CPU.
  - A CPU that can execute one process at a time.
  - A scheduler that selects the next process from the ready queue to run on the CPU.
  - A dispatcher that switches the context of the CPU from the current process to the selected process.
- CPU scheduling can be classified into two types based on the time of scheduling:
  - Non-preemptive scheduling: The CPU is allocated to a process until it completes or requests I/O. The process cannot be interrupted by the scheduler.
  - Preemptive scheduling: The CPU is allocated to a process for a fixed time slice or quantum. The process can be interrupted by the scheduler if it exceeds the quantum or a higher priority process arrives.
- CPU scheduling can also be classified into two types based on the number of processors in the system:
  - Single processor scheduling: The system has only one CPU that can execute one process at a time. The scheduler selects the next process from the ready queue based on some criteria.
  - Multiple processor scheduling: The system has more than one CPU that can execute multiple processes concurrently. The scheduler has to decide how to distribute the processes among the CPUs. There are two approaches to multiple processor scheduling:
    - Symmetric multiprocessing: Each processor is self-scheduling. All processes may be in a common ready queue, or each processor may have its private queue for ready processes.
    - Asymmetric multiprocessing: One processor is designated as the master processor. It is responsible for scheduling the processes on the other processors. The other processors execute the processes assigned by the master processor.