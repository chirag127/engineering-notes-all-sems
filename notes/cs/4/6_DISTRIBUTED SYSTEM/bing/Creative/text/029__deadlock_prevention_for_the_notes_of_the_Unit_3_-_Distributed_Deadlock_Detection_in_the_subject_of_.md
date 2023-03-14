### Deadlock Prevention in Distributed Systems

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for a resource that is held by some other process. There are four necessary conditions for a deadlock to occur, which are:

- Mutual Exclusion: There is at least one resource that is non-sharable and can be used by only one process at a time.
- Hold and Wait: A process is holding at least one resource and waiting for another.
- No Preemption: A resource cannot be taken from a process until it releases the resource.
- Circular Wait: At least two processes should form a circular chain by holding a resource and waiting for a resource that is held by the next process in the chain.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four conditions is not satisfied. There are two main ways to prevent deadlock in a distributed system:

- Ordered Request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the Resource Allocation policy. For each resource, a global level number is assigned to impose ordering of all resource types. While requesting for a resource, a process has to make sure that it does not request for a resource whose level order is lower than the highest-level order resource it currently holds. It can only request resources higher than the highest level resources, held by the process. This method prevents the circular wait condition by breaking the cycle of resource requests.
- Collective Request: In this method, a process requests for all the required resources before the start of its execution, or releases all the resources before making a new request. This prevents the hold and wait condition by avoiding partial allocation of resources. This method may lead to low resource utilization and starvation.