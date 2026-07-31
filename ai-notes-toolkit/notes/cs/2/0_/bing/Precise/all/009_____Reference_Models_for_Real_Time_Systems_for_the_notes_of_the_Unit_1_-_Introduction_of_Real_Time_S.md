# Reference Models for Real Time Systems

Real-time systems are computer systems that monitor, respond to, or control an external environment. This environment is connected to the computer system through sensors, actuators, and other input-output interfaces. The system must respond to events within a specified time frame, otherwise, the system's performance will degrade or fail.

There are several reference models for real-time systems, including:

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-based scheduling algorithm for real-time systems. It assigns priorities to tasks based on their rate of execution, with the highest rate tasks being assigned the highest priority.

2. **Earliest Deadline First (EDF)**: This is another priority-based scheduling algorithm for real-time systems. It assigns priorities to tasks based on their deadlines, with the earliest deadline tasks being assigned the highest priority.

3. **Sporadic Server**: This is a scheduling algorithm that is used to handle aperiodic tasks in real-time systems. It assigns a server task to handle the execution of aperiodic tasks, and the server task is scheduled using one of the other scheduling algorithms (such as RMS or EDF).

4. **Constant Bandwidth Server (CBS)**: This is a scheduling algorithm that is used to handle tasks with variable execution times in real-time systems. It assigns a server task to handle the execution of these tasks, and the server task is scheduled using one of the other scheduling algorithms (such as RMS or EDF).

These are some of the reference models used in real-time systems. Each model has its own advantages and disadvantages, and the choice of model depends on the specific requirements of the system being designed.