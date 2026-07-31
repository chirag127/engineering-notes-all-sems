## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning CPU time to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines while maximizing system performance. Here are some key points to consider when studying real-time scheduling:

1. **Hard real-time systems** have strict deadlines that must be met, while **soft real-time systems** have more flexible deadlines.
2. **Scheduling algorithms** are used to determine the order in which tasks are executed. Common real-time scheduling algorithms include **Rate Monotonic Scheduling (RMS)** and **Earliest Deadline First (EDF)**.
3. **Priority inversion** can occur when a low-priority task holds a resource needed by a high-priority task. This can be addressed using techniques such as **priority inheritance** or **priority ceiling**.
4. **Jitter** refers to the variation in the time between when a task is released and when it is executed. Jitter can be minimized using techniques such as **time-triggered scheduling**.
5. **Overload** occurs when there are more tasks to be executed than can be completed within their deadlines. This can be addressed using techniques such as **admission control** or **load shedding**.

These are some of the key concepts to consider when studying real-time scheduling. It is important to understand the different types of real-time systems, the scheduling algorithms used, and the techniques for addressing common challenges such as priority inversion, jitter, and overload.