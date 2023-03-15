## Unit 3 - CPU Scheduling

CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU . The aim of CPU scheduling is to make the system efficient, fast, and fair.

Some of the main objectives of CPU scheduling are:

- Maximize CPU utilization
- Minimize waiting time
- Minimize turnaround time
- Minimize response time
- Minimize overhead
- Achieve throughput
- Balance system load
- Enforce process priorities
- Avoid starvation
- Avoid deadlock

There are two types of CPU scheduling:

- Preemptive scheduling: In this type, the CPU can be taken away from a process if a higher priority process arrives or a certain time quantum expires . This type of scheduling is suitable for interactive and real-time systems, where responsiveness is important. Some examples of preemptive scheduling algorithms are:

  - Round robin: Each process gets a fixed amount of CPU time (called quantum) and then it is preempted and moved to the end of the ready queue . This algorithm is fair and simple, but it may cause high context switching overhead and poor performance for I/O bound processes.
  - Shortest remaining time first: The process with the smallest amount of time remaining until completion is selected to run next . This algorithm is optimal in terms of minimizing the average waiting time, but it is difficult to implement and may cause starvation for long processes.
  - Priority scheduling: Each process is assigned a priority and the process with the highest priority is selected to run next . This algorithm can be either preemptive or non-preemptive, depending on whether the priority can change during the execution of a process. This algorithm can achieve the desired goals of the system, but it may cause starvation for low priority processes.

- Non-preemptive scheduling: In this type, the CPU cannot be taken away from a process until it completes or voluntarily relinquishes the CPU . This type of scheduling is suitable for batch and background systems, where throughput is important. Some examples of non-preemptive scheduling algorithms are:

  - First come first serve: The process that requests the CPU first is allocated the CPU first . This algorithm is simple and easy to implement, but it may cause long waiting time and low CPU utilization for short processes that arrive later.
  - Shortest job first: The process with the smallest amount of CPU time required to complete is selected to run next . This algorithm is optimal in terms of minimizing the average waiting time, but it is difficult to implement and may cause starvation for long processes.
  - Last come first serve: The process that requests the CPU last is allocated the CPU first. This algorithm is rarely used, as it may cause indefinite postponement and low CPU utilization for processes that arrive earlier.

There are also some other factors that affect the CPU scheduling, such as:

- Process arrival time: The time when a process enters the ready queue.
- Process burst time: The amount of CPU time required by a process to complete its execution.
- Process deadline: The time by which a process must finish its execution.
- Process size: The amount of memory required by a process to run.
- Process I/O requirements: The frequency and duration of I/O operations performed by a process.
- Process synchronization: The need for a process to coordinate with other processes for sharing resources or data.

CPU scheduling is a complex and dynamic problem that requires trade-offs and compromises among various criteria and goals. There is no single best algorithm that can suit all types of systems and processes. Therefore, the choice of a CPU scheduling algorithm depends on the characteristics and requirements of the system and the processes.