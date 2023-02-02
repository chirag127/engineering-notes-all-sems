### detection & resolution for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM
Distributed deadlocks occur when multiple processes in a distributed system are waiting for resources held by each other. Detection and resolution of distributed deadlocks are critical for ensuring the system's stability and performance.

Detection:
1. Centralized Detection: A coordinator process is used to keep track of all the resources and processes in the system. When a deadlock is detected, the coordinator process resolves it.
2. Distributed Detection: Each process in the system maintains information about the resources it holds and the resources it is waiting for. When a process detects that it is involved in a deadlock, it informs other processes to resolve the deadlock.

Resolution:
1. Prevention: Deadlocks can be prevented by using resource allocation algorithms such as the Banker's algorithm.
2. Avoidance: Deadlocks can be avoided by ensuring that the system's resource allocation policies are such that deadlocks cannot occur.
3. Detection and Recovery: When a deadlock is detected, it can be resolved by releasing one or more resources to break the deadlock.
4. Timeout: A timeout mechanism can be used to periodically check for deadlocks and resolve them if they occur.
