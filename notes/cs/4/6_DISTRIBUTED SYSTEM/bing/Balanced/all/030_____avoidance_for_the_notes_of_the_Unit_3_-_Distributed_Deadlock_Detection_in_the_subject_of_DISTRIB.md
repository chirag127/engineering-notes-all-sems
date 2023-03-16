# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance can be implemented using either static or dynamic methods.
- Static methods involve pre-allocating resources to processes before they start execution, based on some criteria such as priority, resource requirements, etc.
- Dynamic methods involve granting or denying resource requests at run-time, based on the current state of the system and the potential impact of the request on the system's safety.
- However, avoidance is impractical in distributed systems due to several problems, such as:
  - The lack of global information and synchronization among processes and resources.
  - The uncertainty and unpredictability of resource requests and releases in a dynamic and heterogeneous environment.
  - The high overhead and complexity of maintaining and checking the system's safety.
  - The possibility of starvation and unfairness for some processes that may be denied resources indefinitely.
- Therefore, deadlock detection is preferred over avoidance in distributed systems, as it allows more flexibility and concurrency for processes and resources.