### Multiple Granularity for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

Concurrency control techniques are used to maintain consistency and correctness in a multi-user environment. Multiple Granularity is one such technique that allows transactions to lock only a portion of a resource instead of the entire resource. This technique is used in various database management systems to ensure efficient concurrency control.

Here are some important points to keep in mind regarding Multiple Granularity:

- Multiple Granularity allows transactions to lock only the portion of a resource that is required to complete the transaction. This way, other transactions can access the unlocked portions of the resource to perform their operations.

- Multiple Granularity is particularly useful in scenarios where transactions need to access large resources, such as tables or indexes. By locking only a portion of the resource, the technique allows multiple transactions to access different portions of the resource at the same time.

- Multiple Granularity can be implemented using two different methods: Strict Two-Phase Locking (S2PL) and Rigorous Two-Phase Locking (R2PL). S2PL is a less restrictive method that allows transactions to lock a portion of a resource without locking the entire resource. R2PL, on the other hand, is a more restrictive method that requires transactions to lock the entire resource before accessing any portion of it.

- Multiple Granularity can be used in conjunction with other concurrency control techniques, such as Time-stamp ordering, to ensure efficient and effective concurrency control. By combining different techniques, database systems can optimize their performance while maintaining consistency and correctness.

- Multiple Granularity is not without its limitations. One major limitation is the possibility of deadlocks, where two or more transactions are unable to proceed due to conflicting locks on resources. To avoid deadlocks, database systems must implement deadlock prevention or deadlock detection algorithms.

- In conclusion, Multiple Granularity is an important concurrency control technique that allows transactions to lock only a portion of a resource. By doing so, it enables multiple transactions to access different portions of the resource at the same time, improving system performance. However, the technique must be implemented carefully to avoid deadlocks and ensure consistency and correctness.