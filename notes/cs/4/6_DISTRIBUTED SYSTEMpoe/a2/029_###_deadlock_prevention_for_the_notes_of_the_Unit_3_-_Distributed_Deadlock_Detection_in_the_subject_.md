 Here is the content in markdown format for the topic - ### deadlock prevention for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM:

### Deadlock Prevention

- **Resource allocation graph:** Model the system as a graph with vertices representing processes and resources and edges representing requests/holdings. If a cycle exists, then a deadlock is possible. Break cycles to prevent deadlock.
- **Allocate resources in a safe state:** Track resources allocated to processes. Before allocating a new resource, ensure the new state is "safe" (no deadlocks). This requires tracking resource types and amounts.
- **Use resource hierarchy:** Impose a total ordering on resource types and require that resources be acquired in increasing order. This prevents circular wait conditions.
- **Limit the number of resources:** By limiting the number of resources of each type, we can bound the length of resource holding chains and thus ensure the system cannot deadlock. However, this approach can lead to resource starvation.
- **Preempt resources:** Allow resources to be forcibly removed from processes. By periodically preempting resources throughout the system, we can prevent circular wait conditions from persisting long enough to lead to deadlock. However, this can significantly increase complexity and degrade performance.

Some mnemonics/learning tricks for deadlock prevention:

- Think of resource allocation graph as a cycle. Break the cycle to prevent deadlock.
- Allocate resources in a sequence (resource hierarchy) to avoid circular waits.
- Limit resources to bound resource chains and avoid deadlock. But beware of starvation.
- Preempt resources to break circular waits. But beware of performance hits.

The content covers the key points to learn and remember for the topic of deadlock prevention for distributed deadlock detection. The mnemonics can help in easy recollection of the prevention techniques. Please let me know if you would like me to elaborate on any of the points or add more details/examples to the content.