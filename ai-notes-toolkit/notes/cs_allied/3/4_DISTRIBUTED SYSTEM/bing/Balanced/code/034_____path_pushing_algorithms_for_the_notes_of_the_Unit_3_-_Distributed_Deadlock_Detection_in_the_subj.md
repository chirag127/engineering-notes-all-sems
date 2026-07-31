### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes and resources at that site .
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which then update their global WFGs accordingly .
- A site can initiate a deadlock computation either periodically or when it detects a potential deadlock situation, such as a request timeout or a resource contention.
- A site can detect a deadlock by checking if there is a cycle in its global WFG that involves one of its local processes .
- If a deadlock is detected, the site can either initiate a resolution action, such as aborting or preempting a process, or report the deadlock to a coordinator site that is responsible for resolving deadlocks.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection.
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFGs, and they may incur false deadlocks due to the inconsistency of the global WFGs.