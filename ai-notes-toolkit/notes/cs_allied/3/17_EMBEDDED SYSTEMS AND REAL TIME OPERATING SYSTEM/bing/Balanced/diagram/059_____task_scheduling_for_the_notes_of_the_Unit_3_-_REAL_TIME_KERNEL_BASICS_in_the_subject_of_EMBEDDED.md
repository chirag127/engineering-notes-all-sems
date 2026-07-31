### Task scheduling for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Task scheduling is the process of allocating CPU time to different tasks or processes in a real time operating system (RTOS).
- Task scheduling can be classified into two types: non-preemptive and preemptive.
- Non-preemptive scheduling means that a task runs until it completes, blocks, or yields the CPU voluntarily. No other task can interrupt it. Examples of non-preemptive scheduling algorithms are run to completion (RTC) and round robin (RR).
- Preemptive scheduling means that a task can be interrupted by a higher priority task at any time. The interrupted task is suspended and resumed later when the higher priority task finishes or blocks. Examples of preemptive scheduling algorithms are time slice (TS), time slice with background task (TSBG), and priority (PRI).
- The choice of task scheduling algorithm depends on the requirements and characteristics of the real time system, such as the number of tasks, the deadlines, the criticality, the periodicity, the synchronization, and the resource utilization.
- Some advantages of preemptive scheduling over non-preemptive scheduling are:
  - It can handle tasks with hard deadlines more effectively, as it ensures that the highest priority task always gets the CPU when it is ready.
  - It can improve the responsiveness of the system, as it reduces the worst-case waiting time for any task.
  - It can avoid the problem of priority inversion, where a low priority task blocks a high priority task indirectly by holding a shared resource.
- Some disadvantages of preemptive scheduling over non-preemptive scheduling are:
  - It can introduce more overhead and complexity, as it requires context switching, interrupt handling, and priority management.
  - It can cause the problem of starvation, where a low priority task never gets the CPU because of the continuous arrival of higher priority tasks.
  - It can affect the predictability and stability of the system, as it can introduce timing anomalies, jitter, and interference.