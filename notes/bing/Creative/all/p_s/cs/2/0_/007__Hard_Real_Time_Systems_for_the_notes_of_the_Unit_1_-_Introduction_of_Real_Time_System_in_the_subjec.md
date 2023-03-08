### Hard Real Time Systems

- A hard real time system is a type of real time system that has strict deadlines for completing tasks and delivering results.
- A deadline is the maximum time allowed for a task to finish execution and produce the expected output.
- Missing a deadline in a hard real time system is considered a system failure and can have catastrophic consequences.
- A hard real time system must guarantee that all deadlines are met, regardless of the workload, system state, or external events.
- A hard real time system must also ensure time synchronization among different components and processes that operate in parallel or communicate with each other.
- Examples of hard real time systems are airplane sensor and autopilot systems, spacecrafts and planetary rovers, process control systems, and autonomous driving systems.
- Some characteristics of hard real time systems are:

  - They require high reliability, availability, and safety.
  - They have deterministic and predictable behavior and performance.
  - They have fixed and known worst-case execution times for tasks and operations.
  - They have preemptive and priority-based scheduling policies for tasks and resources.
  - They have minimal or no overhead for context switching, interrupt handling, and communication.
  - They have low tolerance for faults and errors, and must have mechanisms for fault detection, isolation, and recovery.

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between hard and soft real time systems, you can use the acronym HASS: Hard real time systems are Always Strict and Safe, while Soft real time systems are Sometimes Slack and Satisfactory.
- To remember the characteristics of hard real time systems, you can use the acronym FRED PIMP: Fixed and known worst-case execution times, Reliable, Efficient, Deterministic, Preemptive and priority-based scheduling, Isolated and minimal overhead, Minimal or no faults, Predictable.
- To remember some examples of hard real time systems, you can use the acronym PASS: Planes, Autonomous driving, Spacecrafts, and Sensors.