### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .

- A workload model describes the applications supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, priority, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.)  .
- A resource model describes the resources available to the system, such as the CPU, memory, network, sensors, actuators, etc., their types (e.g., preemptive, non-preemptive, shared, dedicated, etc.), and their relations (e.g., contention, communication, etc.) .
- A system model describes the system behavior, such as the scheduling policy, the synchronization mechanism, the fault tolerance technique, the performance metric, etc., that determine how the workload is mapped to the resources .

- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .