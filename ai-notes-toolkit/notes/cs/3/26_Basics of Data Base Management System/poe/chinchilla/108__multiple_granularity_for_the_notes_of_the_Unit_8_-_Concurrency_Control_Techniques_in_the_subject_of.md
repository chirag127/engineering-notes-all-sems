### Multiple Granularity Locking - Unit 8 - Concurrency Control Techniques

Concurrency control is an essential aspect of database management systems to ensure that multiple transactions accessing the same data do not interfere with each other. One of the techniques used for concurrency control is Multiple Granularity Locking (MGL). MGL helps to reduce lock contention and improve concurrency by allowing transactions to lock only the required resources at different levels of granularity.

#### What is Multiple Granularity Locking?

Multiple Granularity Locking is a technique used in database management systems to allow transactions to lock resources at different levels of granularity. MGL reduces lock contention, which occurs when multiple transactions are blocked while waiting for the same resource to be released. MGL allows transactions to lock only the required resources, which improves concurrency and reduces the likelihood of deadlocks.

#### Types of Locks in MGL

There are two types of locks in MGL:

1. Shared Locks - Shared locks are used to allow multiple transactions to read the same resource simultaneously. A shared lock can be granted to a transaction if no exclusive lock is held by any other transaction.

2. Exclusive Locks - Exclusive locks are used to prevent other transactions from accessing a resource. An exclusive lock can be granted to a transaction only if no other transaction holds any lock on that resource.

#### Granularity Levels in MGL

MGL allows transactions to lock resources at different levels of granularity, which helps to reduce lock contention and improve concurrency. There are three levels of granularity in MGL:

1. Coarse-grained Locking - Coarse-grained locking involves locking the entire database or a large portion of it. It is the simplest form of locking but can cause unnecessary blocking as transactions may be blocked from accessing resources that they do not need.

2. Medium-grained Locking - Medium-grained locking involves locking a subset of the database, such as a table or a set of rows. It provides better concurrency than coarse-grained locking but can still cause blocking if transactions need to access the same resource.

3. Fine-grained Locking - Fine-grained locking involves locking individual records or fields within a database. It provides the best concurrency but can cause overhead due to the increased number of locks.

#### Advantages of MGL

Multiple Granularity Locking has several advantages:

1. Improved Concurrency - MGL allows transactions to lock only the required resources, which reduces lock contention and improves concurrency.

2. Reduced Deadlocks - MGL reduces the likelihood of deadlocks as transactions can lock only the required resources.

3. Flexibility - MGL provides flexibility in choosing the level of granularity for locking resources, which can be adjusted based on the workload and the database schema.

#### Disadvantages of MGL

Multiple Granularity Locking has some disadvantages:

1. Overhead - Fine-grained locking can cause overhead due to the increased number of locks.

2. Complexity - MGL is more complex than other locking techniques, which can make it difficult to implement and maintain.

3. Increased Memory Usage - MGL requires additional memory to store the lock information, which can increase memory usage.

In conclusion, Multiple Granularity Locking is an important technique for concurrency control in database management systems. It allows transactions to lock resources at different levels of granularity, which reduces lock contention and improves concurrency. However, MGL is more complex than other locking techniques, and fine-grained locking can cause overhead, which should be considered when choosing a locking technique.