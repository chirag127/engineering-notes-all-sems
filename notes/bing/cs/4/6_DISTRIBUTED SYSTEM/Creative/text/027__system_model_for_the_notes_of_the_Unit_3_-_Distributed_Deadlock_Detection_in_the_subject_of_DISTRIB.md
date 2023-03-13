### System Model

- A distributed system consists of a set of **sites** connected by a communication network.
- Each site has one or more **processes** that can communicate with processes at other sites by sending and receiving **messages**.
- A process can request access to a **resource** (such as a file, a device, or a lock) by sending a request message to the site that controls the resource.
- The resource controller grants or denies the request according to some **resource allocation policy** (such as FIFO, priority, or random).
- A process may hold one or more resources while requesting another resource, thus creating a possibility of a **deadlock**.
- A deadlock occurs when a set of processes are waiting for each other in a circular fashion, and none of them can proceed until some other process in the set releases a resource.
- A distributed deadlock detection algorithm aims to detect such deadlocks and resolve them by aborting or preempting some processes in the deadlock cycle.