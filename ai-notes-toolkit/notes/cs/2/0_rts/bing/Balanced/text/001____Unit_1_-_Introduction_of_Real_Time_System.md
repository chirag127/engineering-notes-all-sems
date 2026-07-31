## Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization).
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur. For example, flight control systems, airbag systems, etc. .
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. For example, video streaming, online gaming, etc..
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities.
- A real-time system can have different types of tasks: periodic, aperiodic, and sporadic.
- A periodic task is a task that has a fixed interval between successive executions. For example, sensor readings, heartbeat signals, etc..
- An aperiodic task is a task that has a variable interval between successive executions. For example, user inputs, network requests, etc..
- A sporadic task is a task that has a minimum interval between successive executions. For example, emergency signals, alarms, etc..
- A real-time system can have different types of scheduling algorithms: static, dynamic, preemptive, and non-preemptive.
- A static scheduling algorithm assigns priorities to tasks before execution. For example, rate-monotonic scheduling, deadline-monotonic scheduling, etc..
- A dynamic scheduling algorithm assigns priorities to tasks during execution. For example, earliest deadline first scheduling, least laxity first scheduling, etc..
- A preemptive scheduling algorithm allows a higher priority task to interrupt a lower priority task. For example, round-robin scheduling, shortest remaining time first scheduling, etc..
- A non-preemptive scheduling algorithm does not allow a higher priority task to interrupt a lower priority task. For example, first come first served scheduling, shortest job first scheduling, etc..