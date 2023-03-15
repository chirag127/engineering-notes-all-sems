 Here is the content in markdown format:

### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

**1. Resource Allocation Graph (RAG):**
- A directed graph used to represent resource allocation relationships between processes in a distributed system.
- Each vertex represents a resource (R) or a process (P).
- Each edge is directed from a process vertex to a resource vertex if the process requests that resource.
- A cyclic chain of edges indicates a possibility of deadlock.
- By analyzing the RAG, deadlock avoidance algorithms can detect and prevent deadlock.

**2. Banker's Algorithm:**
- A deadlock avoidance algorithm for resource allocation.
- It keeps track of the maximum and allocated number of instances of each resource type.
- Before allocating a resource to a process, it checks if the process can complete execution after allocation. If not, the request is postponed.
- It is applicable to systems where the maximum resource need of each process is known a priori.

**3. Mnemonics:**
- RAG: Circular chain -> Deadlock
- Banker: Available - Allocation >= Need; Allocate else Wait

**Advantages:** Prevents rather than detects and recovers from deadlocks.
**Disadvantages:** May lead to low resource utilization as safe states may be overly conservative.
**Applications:** Resource allocation in operating systems, transaction management in databases.

The content summarizes the key points about Resource Allocation Graph and Banker's Algorithm which are distributed deadlock avoidance techniques. Mnemonics are included wherever applicable to aid learning. Diagrams and examples can also be added if required. Please let me know if you would like me to modify or expand the content.