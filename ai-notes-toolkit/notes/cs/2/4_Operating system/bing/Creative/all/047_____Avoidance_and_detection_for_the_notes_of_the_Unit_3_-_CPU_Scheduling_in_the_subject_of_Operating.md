# Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- **Avoidance** is a method used by the operating system to prevent deadlocks from occurring by ensuring that the system is always in a **safe state** .
- A safe state is one where there exists a **safe sequence** of processes that can be allocated resources without causing a deadlock.
- To use avoidance, the operating system needs to know the **maximum number of resources** that each process may request in advance .
- One of the algorithms used for avoidance is the **Banker's algorithm**, which simulates the allocation and request of resources and checks if the system remains in a safe state .
- **Detection** is a method used by the operating system to detect deadlocks after they have occurred by examining the **resource allocation graph** or the **resource allocation matrix**.
- A resource allocation graph is a directed graph that shows the processes and resources in the system and the requests and assignments between them.
- A resource allocation matrix is a table that shows the current allocation, request, and availability of resources for each process in the system.
- One of the algorithms used for detection is the **deadlock detection algorithm**, which checks if there is a **cycle** in the resource allocation graph or if the system can satisfy the requests of all processes using the resource allocation matrix.
- If a deadlock is detected, the operating system needs to apply a **recovery** method, such as **preemption**, **rollback**, **killing processes**, or **restarting the system**.
- The choice of avoidance or detection depends on the **specific requirements** of the system and the **trade-offs** between performance, complexity, and accuracy .