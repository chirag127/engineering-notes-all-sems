### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems can be classified into two types: hard real-time and soft real-time .
- The difference between hard and soft real-time communication systems is the consequences of missing the deadlines .
- A deadline is the maximum time allowed for a task to complete its execution.
- Hard real-time communication systems are deterministic and require that all tasks meet their deadlines without any exception .
- If a hard real-time communication system misses a deadline, it may cause catastrophic failure or unacceptable damage .
- Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and pacemakers .
- Soft real-time communication systems are probabilistic and allow some tasks to miss their deadlines occasionally with low probability .
- If a soft real-time communication system misses a deadline, it may cause degraded performance or reduced quality of service .
- Examples of soft real-time communication systems are multimedia streaming, video conferencing, and online gaming .
- The following diagram illustrates the difference between hard and soft real-time communication systems:

```markdown
|-----------------|-----------------|-----------------|
|                 | Hard Real-Time  | Soft Real-Time  |
|-----------------|-----------------|-----------------|
| Deadline        | Strict          | Flexible        |
|-----------------|-----------------|-----------------|
| Consequence     | Catastrophic    | Degraded        |
|-----------------|-----------------|-----------------|
| Determinism     | Yes             | No              |
|-----------------|-----------------|-----------------|
| Example         | Air Traffic     | Video Streaming |
|                 | Control         |                 |
|-----------------|-----------------|-----------------|
```