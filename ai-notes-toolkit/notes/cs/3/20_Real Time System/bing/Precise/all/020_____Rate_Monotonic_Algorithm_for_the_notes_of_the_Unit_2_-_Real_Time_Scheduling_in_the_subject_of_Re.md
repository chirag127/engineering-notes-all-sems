# Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems (RTOS) with a static-priority scheduling class.
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority.
- It is a procedure for assigning fixed priorities to tasks to maximize their “schedulability”.
- A task set is considered schedulable if all tasks meet all deadlines all the time.
- The algorithm is simple: Assign the priority of each task according to its period, so that the shorter the period the higher the priority.
- It is preemptive in nature.
- If the process has a small job duration, then it has the highest priority.