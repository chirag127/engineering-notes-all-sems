# Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Preemption ceiling protocol (PCP) is a job task synchronization protocol in a real-time system that is better than priority inheritance protocol in many ways.
- PCP assigns a priority ceiling to each shared resource, which is the highest priority of any task that can access that resource .
- PCP prevents a task from accessing a resource if its priority is lower than the priority ceiling of any resource currently locked by another task .
- PCP avoids priority inversion, deadlock, and chained blocking by ensuring that a task can be preempted only by a higher priority task that does not need any of the resources locked by the preempted task  .
- PCP can be implemented in two ways: static PCP and dynamic PCP.
  - Static PCP assigns a fixed priority ceiling to each resource based on the worst-case scenario, which is the highest priority of any task that may request that resource.
  - Dynamic PCP assigns a variable priority ceiling to each resource based on the actual scenario, which is the priority of the task that currently holds the resource.
- PCP can be extended to support preemption threshold scheduling (PTS), which is a technique that allows a task to specify a lower priority level at which it can be preempted by other tasks.
  - PTS enables a scalable real-time system design by reducing the number of preemptions and context switches.
  - PTS requires a dual ceiling protocol (DCP), which combines the priority ceiling and the preemption threshold of each resource to determine the blocking and preemption conditions for each task.
  - DCP prevents long priority inversion and maintains consistent object states in object-oriented real-time systems.