### Multiple Granularity for the Notes of Unit 8 - Concurrency Control Techniques in Basics of Database Management System

Concurrency control is an essential aspect of database management systems that ensures that multiple users or applications can access the database simultaneously without causing any inconsistency in data. Multiple granularity is a technique used in concurrency control to manage different levels of data granularity. Here are some key points to understand multiple granularity:

- Multiple granularity is a technique used to partition data into smaller units to allow for more flexible concurrency control.
- It involves dividing the database into different levels of granularity, each with its own concurrency control mechanism.
- The levels of granularity can range from the entire database down to individual records, and each level has its own locking mechanism.
- This technique enables different transactions to lock only the relevant portion of the database they need to access, reducing the likelihood of conflicts and improving performance.
- Multiple granularity also allows for different concurrency control mechanisms to be used at different levels of granularity, depending on the needs of the application.
- For example, more restrictive locking mechanisms like exclusive locks can be used at a higher level of granularity, while less restrictive mechanisms like shared locks can be used at a lower level of granularity.
- Multiple granularity is particularly useful in systems with high contention for data, where many transactions are trying to access the same data simultaneously.
- However, it requires careful design and implementation to ensure that the different levels of granularity are properly coordinated and that deadlocks are avoided.

Overall, multiple granularity is a powerful technique for managing concurrency in database management systems, allowing for more flexible and efficient access to data.