### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes at that site.
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which update their global WFGs accordingly.
- A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site.
- A site detects a global deadlock by checking for cycles in its global WFG. If a cycle is found, the site sends a message to the initiator of the deadlock computation, which then selects a victim process to abort.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require probe messages to traverse the WFG.
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may generate false cycles due to inconsistent global WFGs.