### Semaphores

Semaphores are a synchronization tool used to control access to shared resources in concurrent processes. They are used to solve the critical section problem, where multiple processes compete for access to a shared resource.

- A semaphore is an integer variable that can be accessed through two standard atomic operations: `wait()` and `signal()`.
- The `wait()` operation decrements the semaphore value, and if the result is negative, the process is blocked until the semaphore value becomes positive again.
- The `signal()` operation increments the semaphore value, and if there are any processes blocked on the semaphore, one of them is unblocked.
- Semaphores can be used to implement mutual exclusion, where only one process can access a shared resource at a time, as well as to implement synchronization, where multiple processes must wait for each other to reach a certain point before proceeding.
- There are two types of semaphores: counting semaphores and binary semaphores. Counting semaphores can take on any non-negative integer value, while binary semaphores can only take on the values 0 and 1.
- Semaphores were introduced by Edsger Dijkstra in 1965.
