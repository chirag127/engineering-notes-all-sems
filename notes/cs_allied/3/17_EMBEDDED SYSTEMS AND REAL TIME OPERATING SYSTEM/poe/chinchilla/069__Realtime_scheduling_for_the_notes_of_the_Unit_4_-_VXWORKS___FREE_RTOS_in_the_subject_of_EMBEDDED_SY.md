### Realtime Scheduling Notes for Unit 4 - VXWORKS / FREE RTOS in the Subject of Embedded Systems and Real Time Operating System

Realtime scheduling is a critical component of embedded systems and real-time operating systems. In this unit, we will cover the concepts and techniques used for realtime scheduling on the VXWORKS and FREE RTOS platforms.

#### Realtime Scheduling Basics

1. Realtime scheduling is the process of allocating system resources to tasks in a way that meets their timing requirements.

2. Realtime scheduling is crucial in embedded systems and real-time operating systems, where tasks must be executed within strict time bounds.

3. Realtime scheduling involves the use of scheduling algorithms to determine how to allocate system resources to tasks.

4. The two primary types of scheduling algorithms are preemptive and non-preemptive.

5. Preemptive scheduling algorithms allow higher priority tasks to interrupt lower priority tasks.

6. Non-preemptive scheduling algorithms do not allow higher priority tasks to interrupt lower priority tasks.

#### VXWORKS Realtime Scheduling

1. VXWORKS is a real-time operating system that uses a preemptive priority-based scheduling algorithm.

2. The priority of a task in VXWORKS is determined by its priority level, with the highest priority task being assigned a priority level of 0.

3. VXWORKS also supports round-robin scheduling, which allows tasks with the same priority level to share the CPU equally.

4. The scheduling algorithm in VXWORKS is configurable, allowing developers to customize the scheduling behavior to meet their application's specific requirements.

#### FREE RTOS Realtime Scheduling

1. FREE RTOS is a real-time operating system that uses a preemptive priority-based scheduling algorithm.

2. The priority of a task in FREE RTOS is determined by its priority level, with the highest priority task being assigned a priority level of 0.

3. FREE RTOS also supports round-robin scheduling, which allows tasks with the same priority level to share the CPU equally.

4. The scheduling algorithm in FREE RTOS is configurable, allowing developers to customize the scheduling behavior to meet their application's specific requirements.

#### Realtime Scheduling Techniques

1. Rate Monotonic Scheduling (RMS) is a common scheduling technique used in real-time operating systems.

2. RMS assigns priorities to tasks based on their period, with tasks having shorter periods being assigned higher priorities.

3. Another commonly used scheduling technique is Earliest Deadline First (EDF), which assigns priorities based on the tasks' deadlines.

4. EDF ensures that tasks with the earliest deadlines are executed first, ensuring that all tasks meet their timing requirements.

5. Both RMS and EDF are supported by VXWORKS and FREE RTOS, making them powerful tools for developers working on real-time systems.

In conclusion, realtime scheduling is a critical component of embedded systems and real-time operating systems. By understanding the concepts and techniques used in realtime scheduling, developers can ensure that their applications meet their timing requirements and perform optimally in real-world scenarios. VXWORKS and FREE RTOS provide powerful tools for realtime scheduling, making them popular choices among developers working on real-time systems.