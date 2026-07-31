## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion refers to the coordination of processes in a distributed system to ensure that only one process can access a shared resource at a time. This is necessary to prevent conflicts and ensure data consistency in the system.

There are several algorithms that can be used to achieve distributed mutual exclusion, including:

1. **Centralized Algorithm**: In this approach, a central coordinator is responsible for granting access to the shared resource. Processes send requests to the coordinator, which grants access to one process at a time.

2. **Distributed Algorithm**: In this approach, there is no central coordinator. Instead, processes communicate with each other to coordinate access to the shared resource. Examples of distributed algorithms include Ricart-Agrawala and Maekawa's algorithms.

3. **Token-based Algorithm**: In this approach, a token is passed between processes in the system. The process holding the token has the right to access the shared resource. Examples of token-based algorithms include Suzuki-Kasami and Raymond's algorithms.

Each of these algorithms has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system. It is important to carefully evaluate the trade-offs between performance, scalability, and fault tolerance when selecting an algorithm for distributed mutual exclusion.