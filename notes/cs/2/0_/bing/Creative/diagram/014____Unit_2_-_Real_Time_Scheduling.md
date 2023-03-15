## Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints. Real time scheduling aims to ensure that tasks meet their deadlines, avoid resource conflicts, and optimize system performance. Real time scheduling is used in applications such as embedded systems, robotics, multimedia, and industrial control.

Some of the topics covered in this unit are:

- **Real time system**: A system that must respond to events within a specified time interval. A real time system can be classified as hard, soft, or firm, depending on the consequences of missing a deadline.
- **Real time task**: A task that has a timing requirement, such as a deadline, a period, or a release time. A real time task can be periodic, aperiodic, or sporadic, depending on the pattern of its arrival.
- **Real time scheduler**: A component of a real time system that decides which task to execute at any given time. A real time scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not.
- **Real time scheduling algorithm**: A rule or a method that a real time scheduler follows to assign priorities and allocate resources to tasks. A real time scheduling algorithm can be static or dynamic, depending on whether it assigns priorities at design time or run time.
- **Real time scheduling analysis**: A technique to evaluate the feasibility and performance of a real time scheduling algorithm. Real time scheduling analysis can be based on utilization, response time, or deadline, depending on the metric of interest.

Some of the examples of real time scheduling algorithms are:

- **Rate monotonic scheduling (RMS)**: A static, preemptive algorithm that assigns priorities to periodic tasks based on their periods. The shorter the period, the higher the priority. RMS is optimal for a set of independent, periodic tasks on a single processor.
- **Earliest deadline first scheduling (EDF)**: A dynamic, preemptive algorithm that assigns priorities to tasks based on their deadlines. The closer the deadline, the higher the priority. EDF is optimal for a set of independent, periodic or aperiodic tasks on a single processor.
- **Least laxity first scheduling (LLF)**: A dynamic, preemptive algorithm that assigns priorities to tasks based on their laxity. The laxity of a task is the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority. LLF is optimal for a set of independent, periodic or aperiodic tasks on a single processor.
- **Fixed priority scheduling (FPS)**: A static, preemptive algorithm that assigns fixed priorities to tasks based on some criteria, such as criticality, importance, or user preference. FPS is widely used in real time systems, but it is not optimal in general.
- **Round robin scheduling (RR)**: A static, non-preemptive algorithm that assigns equal priorities to tasks and executes them in a circular order. RR is simple and fair, but it does not consider the timing requirements of tasks.