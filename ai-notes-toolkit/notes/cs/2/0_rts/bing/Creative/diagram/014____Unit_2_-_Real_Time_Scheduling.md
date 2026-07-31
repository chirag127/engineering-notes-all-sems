## Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints. Real time scheduling aims to ensure that tasks meet their deadlines, avoid interference from other tasks, and optimize the system performance. Real time scheduling is essential for applications that require high reliability, responsiveness, and predictability, such as industrial control, robotics, multimedia, and avionics.

Some of the topics covered in this unit are:

- **Real time system**: A system that must respond to events within a specified time interval. A real time system can be classified as hard, soft, or firm, depending on the consequences of missing a deadline.
- **Real time task**: A task that has a timing requirement, such as a period, a deadline, and an execution time. A real time task can be periodic, aperiodic, or sporadic, depending on the pattern of its arrival.
- **Real time scheduler**: A component of a real time system that decides which task to execute at any given time. A real time scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not.
- **Real time scheduling algorithm**: A rule or a method that a real time scheduler follows to assign priorities and allocate resources to tasks. A real time scheduling algorithm can be static or dynamic, depending on whether it assigns priorities at design time or run time.
- **Real time scheduling analysis**: A technique to evaluate the feasibility and performance of a real time scheduling algorithm. A real time scheduling analysis can use analytical methods, simulation, or testing to determine the schedulability, response time, utilization, and jitter of tasks.

Some of the examples of real time scheduling algorithms are:

- **Rate monotonic scheduling (RMS)**: A static, preemptive algorithm that assigns priorities to tasks based on their periods. The shorter the period, the higher the priority. RMS is optimal for periodic tasks with implicit deadlines (equal to their periods).
- **Earliest deadline first scheduling (EDF)**: A dynamic, preemptive algorithm that assigns priorities to tasks based on their deadlines. The closer the deadline, the higher the priority. EDF is optimal for periodic and aperiodic tasks with arbitrary deadlines.
- **Least laxity first scheduling (LLF)**: A dynamic, preemptive algorithm that assigns priorities to tasks based on their laxity. The laxity of a task is the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority. LLF is optimal for periodic and aperiodic tasks with arbitrary deadlines.
- **Fixed priority scheduling (FPS)**: A static, preemptive algorithm that assigns fixed priorities to tasks at design time. The priorities can be based on any criteria, such as importance, criticality, or user preference. FPS is not optimal, but it is widely used in practice due to its simplicity and flexibility.
- **Round robin scheduling (RR)**: A static, non-preemptive algorithm that assigns equal priorities to tasks and executes them in a circular order. Each task gets a fixed time slice to run, and then it is moved to the end of the queue. RR is fair and simple, but it does not consider the timing requirements of tasks.