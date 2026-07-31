### Classical Problems in Concurrency

- Concurrency is the execution of multiple instruction sequences at the same time.
- It occurs in an operating system when multiple process threads are executing concurrently.
- These threads can interact with each other via shared memory or message passing.
- Concurrency results in resource sharing, which causes issues like deadlocks and resource scarcity.
- A problem in concurrent computing is where a process is continuously denied the resources it needs to complete its work.
- It could be caused by errors in scheduling or mutual exclusion algorithm, but resource leaks may also cause it.
- Sharing of global resources safely is difficult.
- If two processes both make use of a global variable and both make changes to the variables value, then the order in which various changes take place are executed is critical.
- Optimal allocation of resources is also a challenge in concurrency.
- There are some classical problems in concurrency that illustrate the challenges and solutions of concurrent programming.
- These problems are:
  - The producer/consumer problem: This problem is generalized in terms of the Producer-Consumer problem, where a finite buffer pool is used to exchange messages between producer and consumer processes.
  - The dining-philosophers problem: This problem is a model of concurrent processes that compete for a limited number of resources.
  - The readers and writers problem: This problem is a model of concurrent access to a shared data structure.
  - The sleeping barber problem: This problem is a model of a system that provides service to customers who arrive randomly.
- These problems can be solved using various synchronization mechanisms, such as semaphores, locks, monitors, etc.