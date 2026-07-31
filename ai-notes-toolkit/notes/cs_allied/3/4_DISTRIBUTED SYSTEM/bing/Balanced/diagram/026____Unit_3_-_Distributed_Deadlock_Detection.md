## Unit 3 - Distributed Deadlock Detection

- A **deadlock** is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed until some of the resources are released.
- A **distributed deadlock** can occur when distributed transactions or concurrency control are utilized in distributed systems.
- **Deadlock detection** is a strategy to deal with deadlocks by examining the status of the process-resource interactions for the presence of a cyclic wait .
- **Deadlock detection** in distributed systems can be done by either a **centralized** or a **distributed** technique.
- A **centralized** technique involves a designated **deadlock detector** that collects information from all the sites and constructs a global **wait-for graph (WFG)** to detect cycles .
- A **distributed** technique involves each site maintaining a local **wait-for graph (WFG)** and exchanging messages with other sites to detect cycles .
- Some examples of distributed techniques are **edge chasing**, **path pushing**, and **diffusing computation**.
- **Edge chasing** is a technique where each site sends a **probe** message along the edges of its local WFG and waits for an **echo** message to return. If a site receives a probe message that originated from itself, it detects a cycle.
- **Path pushing** is a technique where each site sends the **path** of its local WFG along the edges and updates the path at each site. If a site receives a path that contains itself, it detects a cycle.
- **Diffusing computation** is a technique where each site initiates a **diffusing computation** when it requests a resource and waits for a reply. A diffusing computation consists of a **query** phase and a **reply** phase. In the query phase, the initiator sends a query message to all its neighbors and waits for their replies. In the reply phase, each site sends a reply message to the initiator after receiving replies from all its neighbors. If the initiator receives a reply message that indicates a cycle, it detects a deadlock.
- **Deadlock resolution** is the process of breaking the deadlock by aborting one or more of the deadlocked processes .
- **Deadlock resolution** can be done by either a **centralized** or a **distributed** technique.
- A **centralized** technique involves a designated **deadlock resolver** that decides which processes to abort based on some criteria, such as priority, age, or number of resources held.
- A **distributed** technique involves each site participating in the decision of which processes to abort based on some criteria, such as global or local timestamps, or random numbers.