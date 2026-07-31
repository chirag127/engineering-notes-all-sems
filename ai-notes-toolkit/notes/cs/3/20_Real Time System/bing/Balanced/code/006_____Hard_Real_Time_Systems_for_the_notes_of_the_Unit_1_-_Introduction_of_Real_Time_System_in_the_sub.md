### Hard Real Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline, otherwise it will cause a system failure or a catastrophic consequence  .
- A hard real-time system has absolute deadlines, meaning that missing even a single deadline is unacceptable and intolerable .
- A hard real-time system is usually interacting at a low level with physical hardware, such as sensors, actuators, or embedded systems.
- Examples of hard real-time systems are flight control systems, nuclear power plant control systems, pacemakers, airbag systems, etc .
- A hard real-time system requires a real-time operating system (RTOS) that can provide deterministic scheduling, preemptive multitasking, priority-based interrupt handling, and time synchronization .
- A hard real-time system must be designed with careful analysis of the worst-case execution time (WCET) of each task, the deadline of each task, the priority of each task, and the possible interference of each task.
- A hard real-time system must be tested and verified rigorously to ensure its correctness, reliability, and safety.