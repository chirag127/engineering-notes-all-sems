## Unit 2 - Real Time Scheduling

Real-time scheduling is an essential concept in computer science that ensures the timely execution of tasks in time-sensitive systems. In this unit, we will learn about real-time scheduling and its different approaches. 

Here are the key points to keep in mind:

- Real-time scheduling is a technique that ensures the timely execution of tasks in time-sensitive systems.
- There are two types of real-time systems: hard real-time systems and soft real-time systems.
- Hard real-time systems have strict timing requirements, and missing a deadline can result in catastrophic consequences.
- Soft real-time systems have looser timing requirements, and missing a deadline may not cause any significant harm.
- Real-time scheduling algorithms can be classified into two categories: static and dynamic.
- Static algorithms schedule tasks before the system starts executing, while dynamic algorithms schedule tasks during runtime.
- Some common static scheduling algorithms include Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF).
- RMS is a priority-based algorithm where tasks with shorter periods have higher priorities.
- EDF is another priority-based algorithm that schedules tasks based on their deadlines.
- Some common dynamic scheduling algorithms include Round Robin Scheduling and Priority Inheritance Protocol.
- Round Robin Scheduling assigns a fixed time quantum to each task and schedules them in a circular order.
- Priority Inheritance Protocol is used to prevent priority inversion, where a low-priority task holds a shared resource needed by a high-priority task.

In conclusion, real-time scheduling is a crucial concept in computer science, and it is essential to understand the different approaches to ensure efficient and timely execution of tasks in time-sensitive systems.