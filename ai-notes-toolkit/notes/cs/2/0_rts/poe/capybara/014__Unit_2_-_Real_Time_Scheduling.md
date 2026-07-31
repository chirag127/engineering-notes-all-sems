## Unit 2 - Real Time Scheduling

Real-time scheduling is an important concept in computer science that deals with scheduling tasks in a manner that meets strict timing requirements. In this unit, we will learn about the different types of real-time scheduling, their characteristics, and how they are implemented.

### Types of Real-Time Scheduling

There are two types of real-time scheduling, namely:

1. Hard Real-Time Scheduling
    - In this type of scheduling, tasks must be completed within a strict deadline.
    - Failure to meet the deadline can result in catastrophic consequences.
    - Examples of hard real-time systems include air traffic control systems and medical equipment.

2. Soft Real-Time Scheduling
    - In this type of scheduling, tasks have a deadline, but missing the deadline does not have catastrophic consequences.
    - Examples of soft real-time systems include multimedia applications and online gaming.

### Characteristics of Real-Time Scheduling

The following are some of the characteristics of real-time scheduling:

1. Determinism
    - Real-time scheduling must be deterministic, i.e., the time required to complete a task must be known in advance.
    - This is necessary to ensure that tasks are completed within their respective deadlines.

2. Pre-emption
    - Real-time scheduling must support pre-emption, i.e., tasks with higher priority must be allowed to interrupt tasks with lower priority.
    - This is necessary to ensure that tasks with strict deadlines are completed on time.

3. Schedulability
    - Real-time scheduling must be schedulable, i.e., it must be possible to determine whether a set of tasks can be completed within their respective deadlines.
    - This is necessary to ensure that the system as a whole is predictable and reliable.

### Real-Time Scheduling Algorithms

The following are some of the real-time scheduling algorithms:

1. Rate Monotonic Scheduling (RMS)
    - This algorithm assigns priorities to tasks based on their periods, i.e., tasks with shorter periods have higher priorities.
    - RMS is optimal for scheduling periodic tasks.

2. Earliest Deadline First (EDF) Scheduling
    - This algorithm assigns priorities to tasks based on their deadlines, i.e., tasks with earlier deadlines have higher priorities.
    - EDF is optimal for scheduling aperiodic tasks.

3. Deadline Monotonic Scheduling (DMS)
    - This algorithm assigns priorities to tasks based on their deadlines, i.e., tasks with shorter deadlines have higher priorities.
    - DMS is optimal for scheduling periodic tasks.

### Conclusion

Real-time scheduling is an important concept in computer science, especially for systems that require strict timing requirements. In this unit, we have learned about the different types of real-time scheduling, their characteristics, and how they are implemented. We have also discussed some of the real-time scheduling algorithms.