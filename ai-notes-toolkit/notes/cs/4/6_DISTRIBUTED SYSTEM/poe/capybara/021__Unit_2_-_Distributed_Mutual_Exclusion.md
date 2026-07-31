## Unit 2 - Distributed Mutual Exclusion

Distributed Mutual Exclusion is a crucial topic in the field of distributed systems. It refers to the process of coordinating access to shared resources among multiple processes in a distributed system to prevent conflicts and ensure consistency. Here are some key points to understand about Distributed Mutual Exclusion:

- **What is Mutual Exclusion?** Mutual Exclusion is a property that ensures that only one process can access a shared resource at a time. It is essential to prevent conflicts and maintain consistency in a distributed system.

- **Why is Distributed Mutual Exclusion necessary?** In a distributed system, multiple processes may attempt to access a shared resource simultaneously. Without proper coordination, this can lead to conflicts and inconsistencies. Distributed Mutual Exclusion techniques are used to ensure that only one process can access the shared resource at a time, regardless of where the processes are located in the system.

- **What are the challenges of Distributed Mutual Exclusion?** Ensuring Mutual Exclusion in a distributed system can be challenging due to factors such as network delays, failures, and the lack of a centralized clock. Distributed Mutual Exclusion techniques must be designed to handle these challenges effectively.

- **What are the different approaches to Distributed Mutual Exclusion?** There are several approaches to implementing Distributed Mutual Exclusion, including:

  - **Centralized Approach:** In this approach, a central server is responsible for coordinating access to the shared resource. The processes communicate with the server to request access to the resource, and the server grants access to one process at a time.

  - **Distributed Approach:** In this approach, the processes themselves are responsible for coordinating access to the shared resource. The processes communicate with each other to determine which process should have access to the resource.

  - **Token-based Approach:** In this approach, a token is passed among the processes to determine which process has access to the resource. The process holding the token is allowed to access the resource, and when it is done, it passes the token to the next process in the queue.

- **What are the advantages and disadvantages of different approaches?** Each approach has its advantages and disadvantages. The centralized approach is simple to implement but can become a bottleneck if the server fails or if there are too many processes requesting access. The distributed approach is more robust but can be complex to implement. The token-based approach is efficient but requires additional communication overhead to pass the token.

- **What are some examples of Distributed Mutual Exclusion techniques?** Some examples of Distributed Mutual Exclusion techniques include Lamport's Distributed Mutual Exclusion Algorithm, Ricart-Agrawala Algorithm, and Maekawa's Algorithm.

Overall, Distributed Mutual Exclusion is a critical topic to understand in the field of distributed systems. By properly coordinating access to shared resources, it ensures consistency and prevents conflicts in a distributed system.