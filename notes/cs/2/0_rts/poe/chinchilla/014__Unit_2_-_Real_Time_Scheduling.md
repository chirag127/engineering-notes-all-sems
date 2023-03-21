## Unit 2 - Real Time Scheduling

Real-time scheduling is a crucial aspect of operating systems, particularly in scenarios where time-sensitive tasks need to be executed. Here are some important points to keep in mind when studying real-time scheduling:

1. **Definition of Real-Time Scheduling:** Real-time scheduling is a process of scheduling tasks in a system such that they meet their timing constraints, i.e., complete their execution within the allotted time frame.

2. **Types of Real-Time Scheduling:** There are two types of real-time scheduling: hard real-time scheduling and soft real-time scheduling. Hard real-time scheduling involves ensuring that tasks meet their deadlines exactly, whereas soft real-time scheduling allows for some degree of deadline misses.

3. **Real-Time Scheduling Algorithms:** There are several real-time scheduling algorithms, including Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), and Deadline Monotonic Scheduling (DMS).

4. **Rate Monotonic Scheduling (RMS):** RMS is a real-time scheduling algorithm that assigns priorities to processes based on their periods, i.e., the time between successive instances of a task. Processes with shorter periods are given higher priority.

5. **Earliest Deadline First (EDF):** EDF is another real-time scheduling algorithm that assigns priorities to processes based on their deadlines, i.e., the time by which a task must be completed. Processes with earlier deadlines are given higher priority.

6. **Deadline Monotonic Scheduling (DMS):** DMS is a real-time scheduling algorithm that assigns priorities to processes based on their deadlines and execution times. Processes with shorter deadlines and execution times are given higher priority.

7. **Real-Time Scheduling in Linux:** Linux provides several real-time scheduling policies, including SCHED_FIFO, SCHED_RR, and SCHED_DEADLINE. These policies allow for real-time scheduling of processes in a Linux system.

8. **Challenges in Real-Time Scheduling:** Real-time scheduling can be challenging due to various factors, including the complexity of the system, the variability of task execution times, and the need to balance real-time and non-real-time tasks.

9. **Real-Time Scheduling Applications:** Real-time scheduling has numerous applications, including in industrial automation, robotics, aerospace, and multimedia systems.

In conclusion, real-time scheduling is a crucial aspect of operating systems, particularly in scenarios where time-sensitive tasks need to be executed. Understanding the different types of real-time scheduling algorithms, policies, and challenges is essential for developing effective real-time scheduling solutions.