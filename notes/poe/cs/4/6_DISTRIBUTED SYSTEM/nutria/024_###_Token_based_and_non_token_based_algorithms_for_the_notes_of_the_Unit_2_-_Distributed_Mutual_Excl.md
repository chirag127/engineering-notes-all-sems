
### Token based and non token based algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM

* Token-based algorithms: These algorithms use a token or a lock to manage access to shared resources. The token is passed from process to process in a circular manner. The token is used to grant access to the shared resource.

* Non-token-based algorithms: These algorithms do not use a token or a lock to manage access to shared resources. Instead, they rely on the cooperation of all processes involved. A process may request access to a shared resource and then wait for the other processes to grant it.

* Advantages of token-based algorithms: 
  * They provide a simple and efficient way to manage access to shared resources.
  * They are easy to implement and maintain.

* Disadvantages of token-based algorithms: 
  * They are prone to deadlocks if the token is not passed in a timely manner.
  * They require a large amount of communication between processes.

* Advantages of non-token-based algorithms: 
  * They are more flexible than token-based algorithms.
  * They are less prone to deadlocks.

* Disadvantages of non-token-based algorithms: 
  * They require more complex implementations.
  * They require more communication between processes.

* Examples of token-based algorithms: Ricart-Agrawala algorithm, Lamport's bakery algorithm.

* Examples of non-token-based algorithms: Chandy-Misra-Haas algorithm, Maekawa's algorithm.

* Applications of token-based algorithms: Distributed mutual exclusion, distributed deadlock detection.

* Applications of non-token-based algorithms: Distributed deadlock prevention, distributed resource allocation.