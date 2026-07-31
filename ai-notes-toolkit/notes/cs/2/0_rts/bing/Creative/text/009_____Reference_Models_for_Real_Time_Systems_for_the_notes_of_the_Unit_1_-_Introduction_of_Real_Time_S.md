### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .

- A workload model describes the applications supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, priority, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.)  .
- A resource model describes the resources available to the system, such as the CPU, memory, network, sensors, actuators, etc., their types (e.g., preemptive, non-preemptive, shared, exclusive, etc.), and their relations (e.g., hierarchy, contention, etc.) .
- A system model describes the policies and mechanisms used by the system to manage the workload and the resources, such as the scheduling algorithm, the synchronization protocol, the communication protocol, the fault tolerance strategy, etc. .

- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- The RCS architecture consists of a hierarchical structure of nodes, each of which performs a specific function, such as sensing, planning, controlling, or coordinating .
- The RCS architecture also defines the interfaces and protocols for communication and coordination among the nodes, as well as the methods for error detection and recovery .