 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Deadlock Prevention for Distributed System

1. Mutual Exclusion: Allow only one process at a time to access shared resources. Do not allow multiple processes to access the same resource simultaneously. This prevents deadlock.
2. Hold and Wait: A process can hold allocated resources but cannot request new resources until it releases the currently held resources. This avoids circular wait condition and prevents deadlock.
3. No Preemption: Once a process holds a resource, it cannot be taken away from the process forcibly unless the process releases it. This can lead to deadlock. To prevent, preemptive resource allocation can be used where a process can be preempted and resources can be taken back.
4. Resource Reclaiming: Deadlock can occur if a process holding some resources permanently does not release them even when they are no longer required. To avoid, allocate resources to processes only for a specific time period. If a process does not release resources after the expiry of allocation time, reclaim the resources forcefully.
5. Banker's Algorithm: It is used for resource allocation to processes. It keeps track of allocated and requested resources and only allocates resources if it is safe to do so, thus avoiding deadlock.

The above points cover key techniques to prevent deadlock in distributed systems. By following these techniques, resource allocation and process coordination can be handled efficiently without leading to deadlock situations.