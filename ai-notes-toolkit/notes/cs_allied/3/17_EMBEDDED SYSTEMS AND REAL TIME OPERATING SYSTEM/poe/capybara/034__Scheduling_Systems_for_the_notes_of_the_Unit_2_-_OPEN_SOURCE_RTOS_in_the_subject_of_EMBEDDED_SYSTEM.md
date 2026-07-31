### Scheduling Systems

Scheduling systems are a fundamental aspect of real-time operating systems (RTOS). They determine the execution order and timing of tasks in the system. In this unit, we will discuss the different scheduling systems used in open-source RTOS.

Here are the key points to remember:

1. **Preemptive Scheduling:** In preemptive scheduling, the RTOS interrupts a task and switches to another task based on priority. This ensures that higher-priority tasks are executed first. Preemptive scheduling is the most common scheduling system used in RTOS.

2. **Cooperative Scheduling:** In cooperative scheduling, tasks voluntarily yield control to the RTOS. This means that tasks with higher priority will execute only when tasks with lower priority have finished. Cooperative scheduling is not as effective as preemptive scheduling since it can lead to lower system performance.

3. **Round-Robin Scheduling:** Round-robin scheduling is a type of preemptive scheduling where tasks are executed in a circular order. Each task is allocated a specific time slice, and the RTOS switches to the next task once the time slice has expired. This ensures that all tasks get an equal amount of CPU time.

4. **Priority Inheritance:** Priority inheritance is a technique used to prevent priority inversions in RTOS. In a priority inversion, a lower-priority task holds a resource required by a higher-priority task. In priority inheritance, the priority of the lower-priority task is temporarily elevated to that of the higher-priority task until the resource is released.

5. **Priority Ceiling:** Priority ceiling is another technique used to prevent priority inversions in RTOS. In priority ceiling, each resource is assigned a priority ceiling – the highest priority of any task that can use the resource. When a task requests a resource, its priority is temporarily elevated to the ceiling of the resource. This ensures that no lower-priority task can hold the resource.

In conclusion, scheduling systems are a critical aspect of real-time operating systems. Understanding the different types of scheduling systems and their advantages can help developers design efficient and reliable embedded systems.