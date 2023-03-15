### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor nonpreemptively  .
- A critical section is a segment of code that accesses a shared resource and must be executed atomically, i.e., without interruption or interference from other tasks or interrupts.
- Non-preemptive means that once a task enters a critical section, it cannot be preempted (interrupted or suspended) by any other task or interrupt until it exits the critical section.
- The main advantage of NPCS is that it prevents deadlock, which is a situation where two or more tasks are waiting for each other to release a resource and none of them can proceed.
- The main disadvantage of NPCS is that it may cause priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a resource and cannot be preempted.
- To avoid priority inversion, NPCS uses a priority ceiling protocol, which assigns a priority ceiling to each resource and elevates the priority of a task that acquires a resource to the highest priority ceiling of all the resources it holds  .
- The priority ceiling protocol ensures that a task can only be blocked by tasks that have higher original priority than itself, and that no circular waiting can occur among tasks that request resources.
- NPCS is suitable for hard real-time systems, where missing deadlines can have catastrophic consequences, and where the critical sections are short and bounded.