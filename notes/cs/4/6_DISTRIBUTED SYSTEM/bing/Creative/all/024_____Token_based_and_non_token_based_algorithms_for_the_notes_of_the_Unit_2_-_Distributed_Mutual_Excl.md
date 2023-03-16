# Token based and non token based algorithms for distributed mutual exclusion

Distributed mutual exclusion (DME) is the problem of ensuring that only one process at a time can access a shared resource in a distributed system. There are two main types of algorithms for DME: token based and non token based.

## Token based algorithms

- In token based algorithms, a unique token is shared among all the sites in the distributed system. The token represents the permission to enter the critical section. Only the site that holds the token can access the shared resource.
- Token based algorithms guarantee mutual exclusion and freedom from deadlock, but they may suffer from starvation and high message complexity.
- Examples of token based algorithms are:
  - **Suzuki-Kasami algorithm**: This is a modification of Ricart-Agrawala algorithm, a permission based (non token based) algorithm that uses REQUEST and REPLY messages to ensure mutual exclusion. In Suzuki-Kasami algorithm, the token is a vector that records the number of requests made by each site. The token is passed to the site with the highest request number that has not yet received the token. This algorithm reduces the number of messages from O(n^2) to O(n) per critical section execution, where n is the number of sites.
  - **Raymond's algorithm**: This is a tree-based algorithm that organizes the sites into a logical tree. The token is initially held by the root of the tree. A site that wants to enter the critical section sends a REQUEST message to its parent in the tree. The parent forwards the request to its parent, and so on, until it reaches the token holder. The token holder then sends the token along the reverse path to the requester. A site that receives the token becomes the new root of the tree. This algorithm reduces the number of messages to O(log n) per critical section execution, but it may cause starvation and high delay.

## Non token based algorithms

- In non token based algorithms, also known as permission based algorithms, a site communicates with a set of other sites to determine who should execute the critical section next. A site that wants to enter the critical section sends a REQUEST message to the other sites and waits for their REPLY messages. The REPLY messages indicate the permission or denial of the request. A site can enter the critical section only if it receives permission from all the other sites.
- Non token based algorithms do not require a unique token, but they may cause deadlock, starvation, and high message complexity.
- Examples of non token based algorithms are:
  - **Lamport's algorithm**: This is a timestamp based algorithm that uses logical clocks to order the requests for the critical section. A site that wants to enter the critical section sends a REQUEST message with its timestamp to all the other sites. A site that receives a REQUEST message replies with a REPLY message if it is not interested in the critical section or if its timestamp is larger than the requester's timestamp. Otherwise, it defers the reply until it exits the critical section. A site can enter the critical section only if it receives REPLY messages from all the other sites and its timestamp is the smallest among all the requests. This algorithm ensures mutual exclusion and freedom from starvation, but it requires O(n^2) messages per critical section execution, where n is the number of sites.
  - **Ricart-Agrawala algorithm**: This is an optimization of Lamport's algorithm that reduces the number of messages to O(n) per critical section execution. A site that wants to enter the critical section sends a REQUEST message with its timestamp to all the other sites. A site that receives a REQUEST message replies with a REPLY message if it is not interested in the critical section or if it has already sent a REPLY message to a site with a smaller timestamp. Otherwise, it defers the reply until it exits the critical section. A site can enter the critical section only if it receives REPLY messages from all the other sites.

: https://www.geeksforgeeks.org/suzuki-kasami-algorithm-for-mutual-exclusion-in-distributed-system/
: https://www.geeksforgeeks.org/raymonds-algorithm-for-mutual-exclusion-in-distributed-system/
: https://www.geeksforgeeks.org/lamports-algorithm-for-mutual-exclusion-in-distributed-system/
: https://www.geeksforgeeks.org/ricart-agrawala-algorithm-for-mutual-exclusion-in-distributed-system/
: https://