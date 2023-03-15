### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT) .
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- Hard real-time systems are deterministic in nature, meaning that they guarantee to meet the deadlines for all tasks .
- Soft real-time systems are probabilistic in nature, meaning that they may occasionally miss the deadlines for some tasks, but with a very low probability .
- Examples of hard real-time systems are nuclear power plant control, missile guidance, pacemaker, etc. .
- Examples of soft real-time systems are video conferencing, multimedia streaming, online gaming, etc. .
- Hard real-time systems require strict timing constraints and high reliability, while soft real-time systems can tolerate some degree of latency and jitter .
- Hard real-time systems often use preemptive scheduling and priority-based algorithms, while soft real-time systems may use non-preemptive scheduling and best-effort algorithms .
- Hard real-time systems will cease to function if a deadline is missed, which can result in dangerous consequences, while soft real-time systems will continue to function even if a deadline is missed, but with degraded performance .