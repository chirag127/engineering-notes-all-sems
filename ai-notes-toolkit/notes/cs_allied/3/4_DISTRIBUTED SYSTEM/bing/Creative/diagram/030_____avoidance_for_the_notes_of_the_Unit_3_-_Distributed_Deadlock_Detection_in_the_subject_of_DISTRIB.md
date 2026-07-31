Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection

- Avoidance is a technique that prevents deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- A system is in an unsafe state if there is no such sequence of resource allocations.
- Avoidance requires the system to have some knowledge of the current and future resource requests of the processes, which may not be feasible or accurate in a distributed system.
- Avoidance also requires the system to make decisions about granting or denying resource requests based on the global state of the system, which may be difficult or costly to obtain in a distributed system.
- Therefore, avoidance is impractical in distributed systems, and deadlock detection is preferred as a technique to handle deadlocks in distributed systems.
- Some examples of avoidance algorithms are Banker's algorithm and Resource ordering algorithm.