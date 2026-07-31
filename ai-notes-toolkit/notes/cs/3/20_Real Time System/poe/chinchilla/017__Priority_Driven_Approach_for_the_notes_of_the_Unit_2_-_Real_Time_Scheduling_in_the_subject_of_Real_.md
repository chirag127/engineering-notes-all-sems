### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Real-time systems require scheduling algorithms that can guarantee timely execution of tasks. One such scheduling approach is the Priority Driven Approach. In this approach, tasks are assigned priorities based on their deadlines and criticality. 

Following are the key points related to the Priority Driven Approach:

- The Priority Driven Approach assigns priorities to tasks based on their criticality and deadlines. The tasks with the earliest deadlines or the highest criticality are assigned higher priorities.
- The Priority Driven Approach uses a preemptive scheduling algorithm, where a higher priority task can preempt a lower priority task if it becomes ready to execute.
- The Priority Driven Approach can be implemented using a fixed-priority or dynamic-priority scheduling algorithm. In the fixed-priority approach, priorities are assigned statically, while in the dynamic-priority approach, priorities can be changed dynamically based on the system state.
- The Priority Driven Approach can be used in both hard real-time and soft real-time systems. In hard real-time systems, the deadlines are strict and must be met, while in soft real-time systems, deadlines can be missed occasionally without causing catastrophic failures.
- The Priority Driven Approach can lead to priority inversion issues if not implemented carefully. Priority inversion occurs when a low-priority task holds a resource that is required by a high-priority task, causing the high-priority task to be blocked.

To summarize, the Priority Driven Approach is a popular scheduling algorithm for real-time systems. It assigns priorities to tasks based on their criticality and deadlines and can be implemented using fixed-priority or dynamic-priority scheduling algorithms. It can be used in both hard real-time and soft real-time systems, but care must be taken to avoid priority inversion issues.