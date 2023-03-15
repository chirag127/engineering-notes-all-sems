### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements :
  - A workload model: It specifies the application supported by the system, such as a set of tasks or jobs, their parameters (e.g., execution time, deadline, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.).
  - A resource model: It describes the resources (e.g., CPU, memory, network, etc.) available to the system, their types (e.g., preemptive, non-preemptive, shared, etc.), and their relations (e.g., hierarchy, contention, etc.).
  - A service model: It defines the policies and mechanisms used by the system to allocate resources to tasks, such as scheduling algorithms, synchronization protocols, admission control, etc.
- An example of a reference model is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- A reference model is not a system design specification, but a conceptual framework that can guide the design and analysis of real time systems .