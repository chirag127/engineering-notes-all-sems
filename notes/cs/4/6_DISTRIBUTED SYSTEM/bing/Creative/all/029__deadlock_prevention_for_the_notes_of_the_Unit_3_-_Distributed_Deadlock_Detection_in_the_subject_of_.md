### Deadlock prevention for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for a resource that is held by some other process.
- There are four necessary conditions for a deadlock to occur, which are: mutual exclusion, hold and wait, no preemption, and circular wait .
- Deadlock prevention is a method of avoiding deadlock by ensuring that at least one of the four conditions is not satisfied.
- There are two ways to prevent deadlock in a distributed system: ordered request and collective request.

#### Ordered request
- In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy.
- For each resource, a global level number is assigned to impose ordering of all resource types. While requesting for a resource, a process has to make sure that it does not request for a resource whose level order is lower than the highest-level order resource it currently holds. It can only request resources higher than the highest level resources, held by the process.
- This method prevents the circular wait condition by breaking the cycle of resource requests .
- For example, suppose there are 10 resources from level 1 to 10, and 10 is the highest level order resource. If a process currently has resources 5 and 8, it cannot request a resource below 8, it can only request resources 9 and 10. Like, the process cannot make a request for resource 7, while holding resource 8. This method does not mean that requests should be made in increasing order of sequence. Before sending a request for resource 7, it has to release the held resource 8. After releasing 8, it can acquire 7. It is allowed because currently, it does not hold a resource higher than 7.
- Disadvantages:
  - A process that has resource request orders in increasing order levels with respect to resource allocation policy, will utilize all the resources and will waste the resources. For example, if a process has a resource request order from 1 to 10. It will acquire all resources and this degrades resource utilization.
  - The assignment of global level numbers to resources may be difficult and arbitrary in a distributed system, where resources are heterogeneous and dynamic.

#### Collective request
- This method prevents the hold and wait condition by using any of the following resource allocation policies:
  - All-or-nothing: This policy ensures that a process requests for all the required resources before the execution of the process. This way, the process does not hold any resource while waiting for another .
  - All-or-one: This policy ensures that a process requests for all the required resources at the same time. If the request is granted, the process acquires all the resources. If the request is denied, the process acquires only one resource and releases all the other resources it holds.
  - All-or-min: This policy ensures that a process requests for all the required resources at the same time. If the request is granted, the process acquires all the resources. If the request is denied, the process acquires the minimum number of resources needed to make progress and releases all the other resources it holds.
- Disadvantages:
  - These policies may lead to low resource utilization and throughput, as a process may have to wait for a long time to acquire all the required resources or release the resources it holds .
  - These policies may also lead to starvation, as a process may never get all the required resources due to contention or priority .

#### Mnemonics and learning tricks
- To remember the four necessary conditions for deadlock, use the acronym **M**utual exclusion, **H**old and wait, **N**o preemption, and **C**ircular wait, or **MHNC**.
- To remember the two ways to prevent deadlock in a distributed system, use the acronym **O**rdered request and **C**ollective request, or **OC**.
- To remember the three resource allocation policies for collective request, use the acronym **A**ll-or-nothing, **A**ll-or-one, and