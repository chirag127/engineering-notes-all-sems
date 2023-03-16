### Priority Driven Approach

Priority driven approach is a scheduling method used in real-time systems. In this approach, tasks are assigned priorities based on their importance and urgency. The scheduler then selects the highest priority task for execution. Here are some key points to note about priority driven approach:

1. **Fixed Priority Scheduling**: In fixed priority scheduling, the priorities of tasks are assigned at design time and do not change during runtime. The most common fixed priority scheduling algorithm is Rate Monotonic Scheduling (RMS).

2. **Dynamic Priority Scheduling**: In dynamic priority scheduling, the priorities of tasks can change during runtime. The most common dynamic priority scheduling algorithm is Earliest Deadline First (EDF).

3. **Preemptive and Non-Preemptive Scheduling**: Priority driven approach can be implemented as either preemptive or non-preemptive scheduling. In preemptive scheduling, a higher priority task can interrupt a lower priority task that is currently executing. In non-preemptive scheduling, a lower priority task will continue to execute until completion, even if a higher priority task becomes available.

4. **Priority Inversion**: Priority inversion is a problem that can occur in priority driven scheduling. It happens when a low priority task holds a resource that is needed by a higher priority task. The higher priority task is blocked and cannot execute until the lower priority task releases the resource. This can result in missed deadlines and reduced system performance.

5. **Priority Inheritance Protocol**: Priority inheritance protocol is a solution to the priority inversion problem. It works by temporarily raising the priority of the low priority task that is holding the resource needed by the higher priority task. This allows the low priority task to complete and release the resource, unblocking the higher priority task.

These are some of the key points to note about priority driven approach in real-time scheduling. It is an important concept in the study of real-time systems and is covered in Unit 2 - Real Time Scheduling of the subject Real Time System.