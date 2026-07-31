### Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

#### Token based algorithms

- In token based algorithms, a unique token is shared among all the processes in the system. The token represents the permission to enter the critical section. Only the process that holds the token can access the shared resource.
- Token based algorithms are simple and efficient, as they require only one message (the token) to be exchanged per critical section entry. However, they have some drawbacks, such as:
  - The token may be lost or duplicated due to message failures or process crashes, leading to deadlock or violation of mutual exclusion.
  - The token may cause unnecessary delays if it is far away from the requesting process, leading to low system utilization.
  - The token may not reflect the current requests of the processes, leading to unfairness or starvation.
- Some examples of token based algorithms are:
  - The centralized algorithm, where one process acts as the token manager and grants the token to the processes in a fixed or dynamic order.
  - The ring algorithm, where the processes are arranged in a logical ring and pass the token along the ring in a clockwise or anticlockwise direction.
  - The Suzuki-Kasami algorithm, where the token contains a vector of requests from all the processes and is sent to the process with the highest request number.

#### Non token based algorithms

- In non token based algorithms, there is no token in the system. Instead, the processes communicate with each other using messages to request, grant, or release the permission to enter the critical section.
- Non token based algorithms are more robust and flexible, as they can tolerate message failures and process crashes, and can adapt to the changing requests of the processes. However, they have some drawbacks, such as:
  - They require more messages to be exchanged per critical section entry, leading to higher communication overhead and network congestion.
  - They may cause deadlock or livelock if the messages are delayed or lost, or if the processes do not follow the same protocol or order.
  - They may require global synchronization or knowledge of the system state, leading to scalability and privacy issues.
- Some examples of non token based algorithms are:
  - The Lamport's algorithm, where the processes use logical timestamps to order the requests and grant the permission to the process with the smallest timestamp.
  - The Ricart-Agrawala algorithm, where the processes use logical timestamps and multicast messages to request and reply the permission to enter the critical section.
  - The Maekawa's algorithm, where the processes form a voting set and request the permission from a majority of the voting set members .