### Types of Scheduling for the Notes of the Unit 1 - Embedded OS Internals in the Subject of Embedded Systems and Real Time Operating System

- Scheduling is the process of allocating CPU time to different tasks or processes in an embedded system.
- Scheduling can be classified into two main categories: non-preemptive and preemptive scheduling.
- Non-preemptive scheduling means that once a task is assigned to the CPU, it cannot be interrupted by another task until it finishes or voluntarily relinquishes the CPU.
- Preemptive scheduling means that a task can be interrupted by another task with higher priority or urgency, and resume later when the CPU is available.
- There are different types of scheduling algorithms that can be used in embedded systems, depending on the system requirements and constraints. Some of the common types are:

  - Round-robin scheduling: This is a simple and fair algorithm that assigns equal time slices to each task in a circular order. It is suitable for systems with equal priority tasks and low response time requirements.
  - Time slice scheduling: This is a variation of round-robin scheduling that allows different time slices for different tasks, depending on their priority or complexity. It is suitable for systems with variable priority tasks and moderate response time requirements.
  - Priority scheduling: This is a more complex algorithm that assigns tasks to the CPU based on their priority levels, which can be static or dynamic. It is suitable for systems with high priority tasks and strict response time requirements.
  - Composite scheduling: This is a combination of different scheduling algorithms that can be applied to different groups of tasks or different situations. It is suitable for systems with heterogeneous tasks and diverse response time requirements.

- Some embedded systems also need to consider real-time constraints, which means that the system must complete certain tasks within specified deadlines or else face serious consequences. Real-time systems can be classified into two types:

  - Hard real-time systems: These are systems that must meet all the deadlines without any exception, otherwise the system may fail or cause damage. Examples of hard real-time systems are airbag controllers, pacemakers, and missile guidance systems.
  - Soft real-time systems: These are systems that can tolerate some deadline misses or delays, but with a degradation in performance or quality. Examples of soft real-time systems are video streaming, voice recognition, and online gaming.