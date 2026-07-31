### Deadlock

Deadlock is a situation in which two or more processes are unable to continue executing because they are waiting for each other to release resources. This can result in a system-wide deadlock, where no further progress can be made until the deadlock is resolved.

#### Conditions for Deadlock

There are four necessary conditions for deadlock to occur:

1. Mutual Exclusion: At least one resource must be held in a non-shareable mode, meaning that only one process can use the resource at a time.

2. Hold and Wait: A process must be holding at least one resource and waiting for additional resources that are currently being held by other processes.

3. No Preemption: Resources cannot be taken away from a process unless the process voluntarily releases them.

4. Circular Wait: There must be a circular chain of two or more processes, where each process is waiting for a resource held by the next process in the chain.

#### Prevention and Avoidance of Deadlock

There are two general approaches to dealing with deadlock: prevention and avoidance.

##### Deadlock Prevention

Deadlock prevention involves designing the system in such a way that at least one of the necessary conditions for deadlock cannot occur. This can be achieved through:

1. Mutual Exclusion: Use of shareable resources instead of non-shareable resources.

2. Hold and Wait: Require processes to request all necessary resources before starting execution.

3. No Preemption: Allow resources to be preempted from processes, either temporarily or permanently.

4. Circular Wait: Implement a total ordering of resources and require processes to request resources in a specific order.

##### Deadlock Avoidance

Deadlock avoidance involves dynamically detecting and preventing potential deadlocks before they occur. This can be achieved through:

1. Resource allocation graphs: A graph is constructed to represent the allocation of resources to processes. If a cycle exists in the graph, then a deadlock is possible.

2. Banker's Algorithm: A resource allocation and request algorithm that ensures that the system will not enter an unsafe state where deadlock is possible.

#### Deadlock Recovery

If a deadlock does occur, there are three general approaches to resolving it:

1. Process Termination: Terminate one or more processes involved in the deadlock to free up the resources they are holding.

2. Resource Preemption: Temporarily preempt resources from one or more processes involved in the deadlock to break the circular wait.

3. Rollback: Roll back the progress of one or more processes involved in the deadlock to a previous state where deadlock was not possible.