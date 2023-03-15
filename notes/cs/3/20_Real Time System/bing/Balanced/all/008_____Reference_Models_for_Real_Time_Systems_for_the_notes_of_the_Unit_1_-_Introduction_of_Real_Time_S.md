# Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps us to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .

## Workload Model

- The workload model specifies the applications supported by the system, such as tasks, jobs, processes, etc  .
- The workload model describes the parameters of each application, such as execution time, deadline, period, priority, resource dependencies, etc  .
- The workload model can also represent the precedence and communication relations among the applications, such as task graphs, data flow graphs, etc .

## Resource Model

- The resource model describes the resources available in the system, such as processors, memory, network, sensors, actuators, etc  .
- The resource model specifies the types and properties of each resource, such as speed, capacity, bandwidth, latency, etc  .
- The resource model can also represent the relations and constraints among the resources, such as shared access, mutual exclusion, contention, etc .

## System Model

- The system model defines the policies and mechanisms that govern the allocation and execution of the applications on the resources .
- The system model includes the scheduling algorithms, the synchronization protocols, the communication protocols, the fault tolerance techniques, etc .
- The system model determines the quality of service and the performance guarantees of the system, such as timeliness, reliability, availability, etc .