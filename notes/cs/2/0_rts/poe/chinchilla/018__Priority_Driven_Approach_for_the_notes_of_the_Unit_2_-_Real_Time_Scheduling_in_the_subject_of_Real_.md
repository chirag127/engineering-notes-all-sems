### Priority Driven Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Real-time systems require scheduling algorithms that can guarantee timely execution of tasks. In this unit, we will discuss the priority-driven approach for real-time scheduling. The priority-driven approach assigns priorities to tasks based on their criticality and urgency. The tasks with higher priorities are executed before tasks with lower priorities. 

Here are some important points to remember about the priority-driven approach for real-time scheduling:

- Priority-driven scheduling algorithms are based on the concept of priority. Each task is assigned a priority based on its requirements and importance.
- The priority of a task determines its position in the scheduling queue. Tasks with higher priorities are executed first.
- In priority-driven scheduling, each task must be assigned a priority value before it can be scheduled. The priority can be based on factors such as deadline, importance, criticality, or any other relevant criteria.
- Priority-driven scheduling algorithms can be preemptive or non-preemptive. In preemptive scheduling, a higher priority task can interrupt a lower priority task in the middle of its execution. In non-preemptive scheduling, a task must complete its execution before another task can be scheduled.
- Priority inheritance is a technique used in priority-driven scheduling to prevent priority inversion. In priority inversion, a low-priority task holds a resource that a high-priority task needs, causing the high-priority task to wait. Priority inheritance ensures that the priority of a task holding a resource is temporarily elevated to the priority of the highest-priority task waiting for that resource.
- Priority-driven scheduling can be implemented using various algorithms such as Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), and Deadline Monotonic Scheduling (DMS).

Understanding the priority-driven approach for real-time scheduling is crucial for designing efficient and reliable real-time systems. By assigning priorities to tasks, we can ensure that critical tasks are executed first, and the system meets its timing requirements. Various scheduling algorithms based on the priority-driven approach can be used depending on the system requirements and design constraints.