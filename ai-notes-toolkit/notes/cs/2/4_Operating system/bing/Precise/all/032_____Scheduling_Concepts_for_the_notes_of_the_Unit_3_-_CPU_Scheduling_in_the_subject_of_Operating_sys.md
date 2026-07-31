# Scheduling Concepts

CPU scheduling is a process that allows one process to use the CPU while the execution of another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU. The aim of CPU scheduling is to make the system efficient, fast and fair.

Some of the important concepts in CPU scheduling are:

1. **CPU Burst:** The time required by a process to execute on the CPU is known as CPU burst time. It is the time during which the process is actually executing on the CPU.

2. **I/O Burst:** The time required by a process to perform I/O operations is known as I/O burst time. It is the time during which the process is waiting for I/O operations to complete.

3. **Dispatcher:** The dispatcher is the module that gives control of the CPU to the process selected by the short-term scheduler. It involves switching context, switching to user mode, and jumping to the proper location in the user program to restart that program.

4. **Context Switch:** A context switch is the mechanism to store and restore the state or context of a CPU in Process Control block so that a process execution can be resumed from the same point at a later time.

5. **Preemption:** Preemption is the act of temporarily interrupting a task being carried out by a computer system, without requiring its cooperation, and with the intention of resuming the task at a later time.

6. **Throughput:** Throughput is the number of processes that complete their execution per time unit.

7. **Turnaround Time:** Turnaround time is the total time taken between the submission of a process and its completion.

8. **Waiting Time:** Waiting time is the amount of time a process has been waiting in the ready queue.

9. **Response Time:** Response time is the amount of time it takes from when a request was submitted until the first response is produced.

These are some of the important concepts in CPU scheduling. Understanding these concepts is essential for understanding the various scheduling algorithms and their performance.