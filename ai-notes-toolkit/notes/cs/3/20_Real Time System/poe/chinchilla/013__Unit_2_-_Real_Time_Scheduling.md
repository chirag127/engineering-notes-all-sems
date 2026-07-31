## Unit 2 - Real Time Scheduling

Real-time scheduling is a crucial aspect of operating systems that deal with real-time applications. It is the process of managing and scheduling tasks in a real-time system to ensure that they meet their deadlines. In this unit, we will explore the various real-time scheduling algorithms and their implementation in operating systems.

### Real-Time Systems

Real-time systems are those where the correctness of the system depends not only on the logical correctness but also on the timeliness of the results. These systems must respond to events within a specific time frame to ensure that the system meets its requirements. Real-time systems can be classified into soft and hard real-time systems.

- Soft real-time systems: In soft real-time systems, the deadline is not critical, and missing a deadline may result in a degraded performance of the system, but it does not cause a system failure.
- Hard real-time systems: In hard real-time systems, missing a deadline can result in a system failure, which can have catastrophic consequences.

### Real-Time Scheduling Algorithms

Real-time scheduling algorithms are used to schedule tasks in real-time systems to ensure that they meet their deadlines. The following are the commonly used scheduling algorithms:

- Rate Monotonic Scheduling (RMS): RMS is a preemptive priority-based scheduling algorithm where the task with the shortest period has the highest priority. This algorithm is optimal when the utilization of the system is less than 69%.
- Earliest Deadline First (EDF): EDF is a preemptive priority-based scheduling algorithm where the task with the earliest deadline has the highest priority. This algorithm is optimal when the utilization of the system is greater than 69%.
- Fixed-Priority Scheduling (FPS): FPS is a preemptive or non-preemptive priority-based scheduling algorithm where priorities are assigned to tasks based on their importance. This algorithm is simple to implement and is used in many real-time systems.

### Real-Time Scheduling in Operating Systems

Real-time scheduling in operating systems involves implementing real-time scheduling algorithms to schedule tasks in a real-time system. The following are the commonly used real-time scheduling algorithms in operating systems:

- Linux Scheduler: The Linux scheduler uses the Completely Fair Scheduler (CFS) for non-real-time tasks and the Round Robin (RR) scheduler for real-time tasks.
- Windows Scheduler: The Windows scheduler uses the Earliest Deadline First (EDF) algorithm for real-time tasks and the Round Robin (RR) algorithm for non-real-time tasks.
- Real-Time Operating System (RTOS): An RTOS is a specialized operating system designed for real-time applications. It provides deterministic scheduling and fast context switching, which is essential for real-time applications.

### Conclusion

Real-time scheduling is a critical aspect of operating systems that deal with real-time applications. Real-time scheduling algorithms ensure that tasks in a real-time system meet their deadlines, which is essential for the proper functioning of the system. Operating systems use different real-time scheduling algorithms to schedule tasks, depending on the requirements of the system. Understanding real-time scheduling and its implementation in operating systems is crucial for developing real-time applications.