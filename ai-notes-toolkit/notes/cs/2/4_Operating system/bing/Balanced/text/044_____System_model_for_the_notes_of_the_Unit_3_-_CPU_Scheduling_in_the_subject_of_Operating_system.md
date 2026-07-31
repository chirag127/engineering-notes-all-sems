### System model for CPU scheduling

- CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it for execution .
- CPU scheduling aims to maximize the utilization of the CPU, the throughput of the system, and the fairness among the processes .
- CPU scheduling can be classified into two types: preemptive and non-preemptive.
  - Preemptive scheduling allows the CPU to be taken away from a running process when a higher priority process arrives or a time quantum expires.
  - Non-preemptive scheduling does not interrupt a running process until it finishes or requests I/O.
- CPU scheduling can also be classified into four levels: long-term, medium-term, short-term, and dispatcher.
  - Long-term scheduling decides which processes are admitted to the system for execution.
  - Medium-term scheduling decides which processes are swapped in or out of the main memory.
  - Short-term scheduling decides which process is selected from the ready queue for the CPU.
  - Dispatcher is the module that switches the context from the current process to the next process.
- CPU scheduling can be performed on different types of resources, such as single processor, multiple processors, or multiple cores .
  - Single processor scheduling assigns one process to the CPU at a time.
  - Multiple processor scheduling assigns processes to more than one CPU simultaneously.
  - Multiple core scheduling assigns processes to different cores within a single CPU.