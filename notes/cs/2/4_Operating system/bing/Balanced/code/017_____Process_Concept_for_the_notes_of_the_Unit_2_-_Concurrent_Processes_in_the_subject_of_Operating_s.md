### Process Concept

- A process is a program in execution which then forms the basis of all computation.
- A process is more than the program code as it includes the program counter, process stack, registers, program code etc.
- A process is defined as an entity which represents the basic unit of work to be implemented in the system.
- A process can be in one of the following states: new, ready, running, waiting, terminated.
- The operating system keeps its processes separate and allocates the resources they need, so that they are less likely to interfere with each other and cause system failures.
- The operating system may also provide mechanisms for inter-process communication to enable processes to interact in safe and predictable ways.
- The operating system is responsible for creating, managing, scheduling, and terminating processes.
- The operating system maintains a data structure called a process control block (PCB) for each process, which contains information such as process ID, priority, state, CPU registers, memory pointers, I/O status, etc.
- The operating system uses a process scheduler to select the next process to run based on some criteria, such as CPU utilization, throughput, response time, etc.
- The operating system may use different scheduling algorithms, such as first-come first-served (FCFS), shortest job first (SJF), priority, round robin, etc.
- The operating system may also support multiprogramming, multiprocessing, and multithreading, which allow multiple processes to share the CPU and memory resources .