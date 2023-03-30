
### Concurrency Control for the Notes of the Unit 8 - Concurrency Control Techniques in the Subject of Basics of Data Base Management System

1. Concurrency control is a technique used to ensure that multiple users can access and update a database concurrently without compromising data integrity.
2. Concurrency control is achieved by locking the data or resources when they are being accessed or modified by one user and preventing other users from accessing the same data or resource until the lock is released.
3. There are two main techniques used for concurrency control: locking and timestamp ordering.
4. Locking techniques allow a user to lock a record or resource while they are using it, and then release the lock when they are finished. This prevents other users from accessing or modifying the data until the lock is released.
5. Timestamp ordering techniques use timestamps to determine the order in which transactions are executed. This ensures that transactions are executed in the order they were received, preventing lost updates and other problems.
6. Deadlocks are a problem that can occur when two or more users are trying to access the same data or resource at the same time. To prevent deadlocks, a deadlock detection and resolution algorithm is used.
7. Concurrency control is an important part of database management systems, as it ensures that data integrity is maintained and that multiple users can access and update the same data without interference.