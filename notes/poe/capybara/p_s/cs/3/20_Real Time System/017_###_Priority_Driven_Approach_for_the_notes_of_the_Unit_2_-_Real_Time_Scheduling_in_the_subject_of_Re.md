### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Real-time scheduling is a process of scheduling tasks or processes that have strict time requirements with respect to their completion. Priority-driven approach is one of the most commonly used scheduling techniques in real-time systems. In this approach, each process or task is assigned a priority value based on its importance and its deadline.

Here are some key points to understand the priority-driven approach for real-time scheduling:

1. Priority-driven approach is a preemptive scheduling technique, which means that the highest priority task is executed first and can interrupt a lower priority task if necessary.

2. Priority values are assigned to each task based on their importance and their deadline. The task with the highest priority value is executed first.

3. There are two types of priority-driven scheduling: static and dynamic. In static priority-driven scheduling, the priority value of each task is fixed and does not change during runtime. In dynamic priority-driven scheduling, the priority value of a task can change based on its behavior or external events.

4. There are several algorithms used for priority-driven scheduling, such as Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), etc. These algorithms differ in how they calculate the priority value and how they schedule tasks.

5. One of the advantages of priority-driven scheduling is that it ensures that critical tasks are executed on time. However, it can also lead to priority inversion, where a low priority task holds a resource needed by a high priority task.

6. Priority-driven scheduling can be applied in various real-time systems, such as aerospace, automotive, medical devices, etc. For example, in a medical device, the monitoring of a patient's vital signs may have a higher priority than other non-critical tasks.

In conclusion, the priority-driven approach is a widely used scheduling technique in real-time systems. It ensures that critical tasks are executed on time and can be applied in various domains. However, it is important to choose the right algorithm and be aware of its limitations, such as the possibility of priority inversion.