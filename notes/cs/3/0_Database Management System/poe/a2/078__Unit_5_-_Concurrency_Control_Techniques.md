 Here is the formal content written in Markdown format without any emojis or external links:

## Unit 5 - Concurrency Control Techniques

1. Locks
- Exclusive lock: Only one process can access the shared resource at a time. Other processes will wait in a queue.
- Shared lock: Multiple processes can read a shared resource simultaneously but only one process can write to it at a time.

2. Semaphores
- A semaphore is a variable that indicates whether a shared resource is available or not.
- It is used to solve critical section problem and to achieve process synchronization.
- Initial value of a semaphore indicates the number of resources available.
- P and V are the two operations on semaphores:
-- P: Checks if semaphore value is greater than 0, if yes, decrements it and proceeds into critical section. If value is 0, it waits.
-- V: Increments the semaphore value to indicate that the resource is now available.

3. Monitors
- A monitor is a synchronization construct that allows only one process to execute in its critical section at a time.
- The monitor encapsulates data and procedures that operate on the data. The procedures are executed by entering the monitor.
- Condition variables help the processes to wait inside the monitor until a certain condition becomes true.

4. Message Passing
- Processes communicate with each other by sending and receiving messages.
- Messages are sent to mailboxes (queues). A process can receive a message by checking or waiting on its mailbox.
- It is a very robust method as there is no sharing of variables between processes. However, it may have some performance issues.