 Here is the content in markdown format for the topic - ### Cluster Middleware and SSI for the notes of the Unit 3 - Overview of Cluster Computing in the subject of High Performance Computing:

Cluster Middleware and Single System Image (SSI)

- Cluster Middleware: Software layer that sits between the application and the operating system to manage and coordinate the resources of a cluster. It provides a single system view to the user and handles inter-process communication, load balancing, fault tolerance, etc. Examples: MPICH, OpenMPI, Sun Grid Engine, etc.

- Single System Image (SSI): Presents the cluster of computers as a unified computing resource so that the application can access the resources as if they were on a single machine. The cluster appears as a single system to the user. The middleware handles the distribution of processes and data across the cluster.

Advantages of SSI:

- Transparency: The complexity of distributed system is hidden from the user. The cluster appears as a single system.
- Ease of use: User can focus on the application rather than worrying about the underlying architecture.
- Scalability: Additional nodes can be easily integrated into the system.

Disadvantages of SSI:

- Difficult to implement: Providing a single system view on a distributed system is a challenging task. The middleware has to effectively manage all the resources and handle faults.
- Performance overhead: The additional functionality provided by the middleware can introduce delays and impact performance.
- Less control: The user has less control over resource allocation as that is handled by the middleware.

Applications of cluster computing with middleware and SSI:

- High performance scientific computing: Simulations, data analysis, etc.
- Web services: Handling large volumes of requests.
- Enterprise computing: Supply chain management, transaction processing, etc.

[Detailed diagrams and examples can be added here if required.]