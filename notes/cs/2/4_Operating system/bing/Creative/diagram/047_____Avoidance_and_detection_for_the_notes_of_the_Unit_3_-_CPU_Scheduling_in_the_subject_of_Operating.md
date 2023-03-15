### Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- CPU scheduling aims to optimize the utilization of CPU and to avoid the possibility of deadlock in the system.
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock avoidance is a method used by the operating system to check whether the system is in a safe state or in an unsafe state and to prevent the occurrence of deadlocks.
- Deadlock detection is a method used by the operating system to identify the existence of deadlocks in the system and to recover from them.

#### Deadlock Avoidance
- Deadlock avoidance requires the operating system to have prior knowledge of the maximum number of resources a process can request in order to complete its execution.
- Deadlock avoidance can be done with Banker's Algorithm, which tests all the requests made by processes for resources, and checks for the safe state, if after granting request system remains in the safe state it allows the request otherwise it delays the request.
- A safe state is one in which there is at least one sequence of resource allocation to processes that does not result in a deadlock.
- An unsafe state is one in which there is no such sequence of resource allocation to processes that does not result in a deadlock.
- An unsafe state does not imply that a deadlock has occurred, but it means that a deadlock may occur in the future.

#### Deadlock Detection
- Deadlock detection requires the operating system to periodically check the system for the presence of deadlocks and to take appropriate actions to resolve them.
- Deadlock detection can be done with various algorithms, such as Wait-For Graph, Resource Allocation Graph, or Matrix-based methods.
- Wait-For Graph is a graphical representation of the system's processes and resources. A directed edge is created from a process to a resource if the process is waiting for that resource. A cycle in the graph indicates a deadlock.
- Resource Allocation Graph is a graphical representation of the system's processes and resources. A directed edge is created from a resource to a process if the resource is allocated to the process. A directed edge is created from a process to a resource if the process is requesting the resource. A cycle in the graph indicates a deadlock.
- Matrix-based methods use two matrices to represent the system's processes and resources. The allocation matrix shows the number of resources of each type currently allocated to each process. The request matrix shows the number of resources of each type currently requested by each process. A deadlock exists if there is no process that can be allocated resources and finish its execution.
- Deadlock recovery can be done by either aborting one or more processes involved in the deadlock, or preempting some resources from the processes and allocating them to other processes.