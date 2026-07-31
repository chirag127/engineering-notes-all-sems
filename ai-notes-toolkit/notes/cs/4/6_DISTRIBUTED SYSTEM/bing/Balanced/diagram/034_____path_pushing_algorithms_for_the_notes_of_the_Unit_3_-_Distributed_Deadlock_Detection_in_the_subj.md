Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on path pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM.

### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The WFG is a directed graph that represents the dependencies among the processes that are waiting for resources. A cycle in the WFG indicates a deadlock.
- The basic idea is to build a global WFG for each site by sending the local WFG to all the neighboring sites whenever a deadlock computation is performed .
- The neighboring sites are the sites that have processes that are either waiting for or holding resources from the local site.
- The global WFG is updated whenever a process requests, releases, or is granted a resource, or when a local WFG is received from another site.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require probe messages or diffusing computations .
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may generate false cycles due to the inconsistency of the global WFG .