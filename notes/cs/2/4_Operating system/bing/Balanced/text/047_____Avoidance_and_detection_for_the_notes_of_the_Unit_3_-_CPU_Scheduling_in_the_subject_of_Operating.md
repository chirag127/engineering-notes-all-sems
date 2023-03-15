### Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- Avoidance and detection are two strategies to deal with the problem of deadlock in operating systems.
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Avoidance is a proactive approach that prevents deadlock from occurring by ensuring that the system is always in a safe state.
- Detection is a reactive approach that detects deadlock after it has occurred and then takes some action to recover from it.
- Some of the points to remember about avoidance and detection are:

  - Avoidance requires prior knowledge of the maximum resource requirements of each process, whereas detection does not.
  - Avoidance uses the concept of a safe state, which is a state where there is at least one sequence of resource allocation that does not lead to deadlock. Detection uses the concept of a wait-for graph, which is a graph that shows the dependencies among the processes and the resources they are holding or requesting.
  - Avoidance uses algorithms such as the banker's algorithm, which simulates the allocation and request of resources and checks if the system remains in a safe state. Detection uses algorithms such as the resource allocation graph algorithm, which checks for cycles in the wait-for graph and identifies the processes involved in the deadlock.
  - Avoidance may incur more overhead and reduce system utilization, as it may deny some requests that are actually safe. Detection may incur more delay and waste of resources, as it may allow some requests that are actually unsafe.
  - Avoidance is more suitable for systems where the resource requirements are known in advance and the number of processes and resources is fixed. Detection is more suitable for systems where the resource requirements are dynamic and unpredictable and the number of processes and resources is variable.