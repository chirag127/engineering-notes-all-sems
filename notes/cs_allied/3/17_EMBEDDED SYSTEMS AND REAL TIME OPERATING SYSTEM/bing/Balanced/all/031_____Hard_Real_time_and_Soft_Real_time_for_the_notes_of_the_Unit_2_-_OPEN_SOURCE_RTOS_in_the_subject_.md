# Hard Real Time and Soft Real Time

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-world applications.
- A real-time system is one where the correctness of the system depends not only on the logical results of the computations, but also on the time at which the results are produced.
- A real-time system can be classified into two types: hard real-time and soft real-time, based on the consequences of missing a deadline.

## Hard Real Time

- A hard real-time system is one where the time taken is deterministic to an exact moment.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- A hard real-time system is highly restrictive and doesn’t tolerate any system failure.
- Examples of hard real-time systems are air traffic control systems, nuclear power plant control systems, missile guidance systems, etc.

## Soft Real Time

- A soft real-time system is one where the time taken is deterministic to a range of values.
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system continues to function but with undesirable lower quality of output.
- A soft real-time system is less strict and can stand the system failure.
- Examples of soft real-time systems are multimedia systems, online gaming systems, video conferencing systems, etc.

## Key Differences

- Hard real-time systems are deterministic in nature while soft real-time systems are probabilistic.
- Hard real-time systems have strict deadlines while soft real-time systems have flexible deadlines.
- Hard real-time systems have catastrophic consequences of missing a deadline while soft real-time systems have degraded performance of missing a deadline.
- Hard real-time systems require specialized hardware and software while soft real-time systems can use general-purpose hardware and software.