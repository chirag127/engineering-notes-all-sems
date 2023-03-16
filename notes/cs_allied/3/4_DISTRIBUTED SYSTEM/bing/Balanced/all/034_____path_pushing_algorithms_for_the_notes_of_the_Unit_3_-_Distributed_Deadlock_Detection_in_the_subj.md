# Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by merging the local WFGs of each site, which represent the waiting relationships among the processes at that site .
- Whenever a site performs a deadlock computation, it sends its local WFG to all its neighboring sites, which then update their global WFGs accordingly .
- A site can initiate a deadlock computation either periodically or when a new edge is added to its local WFG .
- A site can detect a deadlock by finding a cycle in its global WFG that involves one of its local processes .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and that they do not require any special messages to be exchanged among the sites .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and update the global WFGs, and that they may generate false positives if the global WFGs are not consistent .