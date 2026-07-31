### Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed computing systems. It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner. In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.

There are three basic approaches for implementing distributed mutual exclusion :

1. **Token-based approach**: A unique token (also known as the PRIVILEGE message) is shared among the sites. A site is allowed to enter its critical section if it possesses the token. Mutual exclusion is ensured because the token is unique .
2. **Non-token-based approach**: This approach does not use a token for mutual exclusion.
3. **Quorum-based approach**: This approach uses a quorum of sites to implement mutual exclusion.

These are the prime classifications of distributed mutual exclusion algorithms.