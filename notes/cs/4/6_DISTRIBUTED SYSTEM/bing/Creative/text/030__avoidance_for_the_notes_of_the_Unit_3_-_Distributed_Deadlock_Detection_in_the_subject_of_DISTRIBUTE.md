### Avoidance

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by avoiding unsafe states.
- Avoidance requires some knowledge of the resource requirements and availability in the system, and some control over the allocation of resources to processes.
- Avoidance can be classified into two categories: static and dynamic.
- Static avoidance is based on the assumption that the resource requirements of each process are known in advance, before the process starts execution. This allows the system to check if granting a resource request will lead to a safe state or not, and deny the request if it will lead to an unsafe state. An example of static avoidance is the Banker's algorithm.
- Dynamic avoidance is based on the assumption that the resource requirements of each process are not known in advance, but can be estimated or predicted during the execution. This allows the system to monitor the resource utilization and availability, and adjust the allocation of resources to processes accordingly. An example of dynamic avoidance is the Wait-Die and Wound-Wait schemes.