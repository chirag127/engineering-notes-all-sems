 Here is the content in markdown format without any emojis or external links:

### System Model for Distributed Deadlock Detection

1. The system consists of a finite number of processes that share resources.
2. Each process follows a resource allocation policy that may result in deadlock.
3. The resources are partitioned into several resource types.
4. Each resource has a quantifiable capacity (e.g., units of processor time, memory space, devices).
5. The system has a global deadlock detection mechanism that can detect and resolve deadlocks.
6. The global deadlock detection mechanism consists of a set of resource manager processes, one for each resource type.
7. The resource manager processes communicate with each other and with the processes that request and release resources.
8. The resource manager for each resource type keeps track of:
   - The current allocation of resources of that type.
   - The maximum capacity of resources of that type.

The above points cover the basic system model for Distributed Deadlock Detection. The resource managers keep track of resource allocations and capacities to detect and resolve deadlocks that may occur due to distributed resource sharing.