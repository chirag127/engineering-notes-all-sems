### Unit 3 - Distributed Deadlock Detection

#### Resource Deadlocks vs Communication Deadlocks

- **Resource Deadlocks** occur when processes are waiting for resources that are held by other processes. This can happen in a distributed system when multiple processes are competing for a limited number of resources.

- **Communication Deadlocks** occur when processes are waiting for messages from other processes that are also waiting for messages. This can happen in a distributed system when processes are waiting for responses from other processes that are also waiting for responses.

- Both types of deadlocks can cause a system to become unresponsive and can be difficult to detect and resolve.

- Distributed deadlock detection algorithms can be used to detect and resolve deadlocks in a distributed system. These algorithms can be classified into two categories: centralized and distributed.

- Centralized algorithms rely on a single coordinator to detect and resolve deadlocks, while distributed algorithms rely on cooperation between multiple processes to detect and resolve deadlocks.

- Both types of algorithms have their advantages and disadvantages, and the choice of algorithm will depend on the specific requirements of the system.