### Detection & Resolution

- Detection is the process of identifying the existence of a deadlock in a distributed system.
- Resolution is the process of breaking the deadlock by aborting or preempting some of the processes involved in the deadlock.
- Detection and resolution can be done either in a centralized or a distributed manner.
- Centralized detection and resolution involves a designated coordinator process that collects information from all other processes and detects and resolves deadlocks.
- Distributed detection and resolution involves each process participating in the detection and resolution of deadlocks without a coordinator.
- Detection and resolution can be based on either global or local wait-for graphs.
- A global wait-for graph is a directed graph that represents the waiting relationships among all processes in the system.
- A local wait-for graph is a directed graph that represents the waiting relationships among the processes in a single site or node.
- Detection and resolution can be done either periodically or on demand.
- Periodic detection and resolution involves running the detection and resolution algorithms at regular intervals of time.
- On demand detection and resolution involves running the detection and resolution algorithms only when a deadlock is suspected or requested.