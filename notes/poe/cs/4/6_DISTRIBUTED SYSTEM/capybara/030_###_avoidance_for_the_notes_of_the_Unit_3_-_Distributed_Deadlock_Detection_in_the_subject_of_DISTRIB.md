### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

In distributed systems, deadlocks can occur when multiple processes or threads wait for each other to release resources. To prevent these deadlocks, we can use the avoidance technique. The avoidance technique involves preventing the system from entering a state that could lead to a deadlock. Here are some important points to remember about the avoidance technique:

1. Resource allocation: In the avoidance technique, resources are allocated to processes only if the allocation will not result in a deadlock. The system keeps track of the resources allocated to each process and the resources needed by each process.

2. Resource request: When a process requests a resource, the system checks if the allocation of the resource will lead to a deadlock. If the allocation will lead to a deadlock, the request is denied.

3. Safe state: To ensure that the system is in a safe state, the system must maintain a record of the resources that are available and the resources that are currently being used by processes.

4. Resource allocation graph: The resource allocation graph is a tool used to determine if the system is in a safe state. It consists of nodes that represent processes and resources, and edges that represent requests and allocations. If the graph contains no cycles, the system is in a safe state.

5. Banker's algorithm: The banker's algorithm is a popular algorithm used for the avoidance technique. It is a resource allocation and deadlock avoidance algorithm that tests for safety before allocating any resources to processes. The algorithm is used to determine if the system is in a safe state by simulating the allocation of resources to processes.

6. Advantages: The avoidance technique ensures that the system remains in a safe state and prevents deadlocks from occurring. It also ensures that resources are allocated efficiently and fairly.

7. Disadvantages: The avoidance technique can be complex and difficult to implement. It may also lead to inefficiencies in resource allocation and may require significant computational resources.

Overall, the avoidance technique is an important technique for preventing deadlocks in distributed systems. It ensures that the system remains in a safe state and resources are allocated efficiently. The banker's algorithm is a popular algorithm used for the avoidance technique and is recommended for further study.