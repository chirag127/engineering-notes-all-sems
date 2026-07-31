# Avoidance and Detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating System

- **Avoidance**: Avoidance is a technique used to prevent the occurrence of deadlocks in the system. It involves the use of algorithms that ensure that the system will never enter into a deadlock state. Some of the commonly used avoidance algorithms are Banker's algorithm and Resource allocation graph algorithm.

- **Detection**: Detection is a technique used to identify the occurrence of deadlocks in the system. It involves the use of algorithms that periodically check the system for the presence of deadlocks. If a deadlock is detected, the system can take appropriate actions to recover from it. Some of the commonly used detection algorithms are Wait-for graph algorithm and Cycle detection algorithm.

- **Banker's Algorithm**: Banker's algorithm is an avoidance algorithm that is used to prevent the occurrence of deadlocks in the system. It is based on the concept of a safe state. A state is considered safe if there exists a sequence of resource allocation to processes such that each process can complete its execution without causing a deadlock.

- **Resource Allocation Graph Algorithm**: Resource allocation graph algorithm is another avoidance algorithm that is used to prevent the occurrence of deadlocks in the system. It involves the use of a directed graph to represent the allocation of resources to processes. The algorithm checks for the presence of cycles in the graph to determine if the system is in a safe state.

- **Wait-for Graph Algorithm**: Wait-for graph algorithm is a detection algorithm that is used to identify the occurrence of deadlocks in the system. It involves the use of a directed graph to represent the waiting relationships between processes. The algorithm checks for the presence of cycles in the graph to determine if a deadlock has occurred.

- **Cycle Detection Algorithm**: Cycle detection algorithm is another detection algorithm that is used to identify the occurrence of deadlocks in the system. It involves the use of algorithms that can detect the presence of cycles in a directed graph. If a cycle is detected, it indicates that a deadlock has occurred in the system.
