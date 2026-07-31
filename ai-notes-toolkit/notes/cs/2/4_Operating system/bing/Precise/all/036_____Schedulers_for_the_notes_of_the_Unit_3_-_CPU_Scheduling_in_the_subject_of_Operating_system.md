# Schedulers for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- The main function of the CPU scheduling is to ensure that whenever the CPU remains idle, the OS has at least selected one of the processes available in the ready-to-use line.
- Whenever the CPU gets idle, the operating system (OS) has to select one of the processes in the ready queue for execution.
- The selection process is performed by the short-term scheduler (also known as CPU scheduler).
- The scheduler picks up a process from the processes in memory which are ready to be executed and allocate the CPU with that process.
- The challenge is to make the overall system as “efficient” and “fair” as possible, subject to varying and often dynamic conditions.
- “Efficient” and “fair” are somewhat subjective terms, often subject to shifting priority policies.
- The storage structure for the ready queue and the algorithm used to select the next process are not necessarily a FIFO queue.