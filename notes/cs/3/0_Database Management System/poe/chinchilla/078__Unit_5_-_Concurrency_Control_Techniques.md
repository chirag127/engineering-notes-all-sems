## Unit 5 - Concurrency Control Techniques

Concurrency control is an essential aspect of database management systems. It refers to the techniques used to ensure that multiple transactions can access and manipulate the same data without interfering with each other. The following are some of the important concurrency control techniques:

1. Lock-Based Concurrency Control:
   - Lock-based concurrency control is the most common technique employed by database management systems.
   - It involves placing locks on data items to prevent multiple transactions from accessing them simultaneously.
   - Locks can be shared or exclusive, and a transaction must acquire the appropriate lock before accessing a data item.
   - This technique ensures serializability but can lead to deadlocks.

2. Timestamp-Based Concurrency Control:
   - Timestamp-based concurrency control assigns a unique timestamp to each transaction and data item.
   - Transactions are ordered based on their timestamp, and a transaction can only access a data item if its timestamp is less than the timestamp of the data item.
   - This technique ensures serializability and avoids deadlocks, but it may lead to starvation.

3. Optimistic Concurrency Control:
   - Optimistic concurrency control assumes that conflicts between transactions are rare and allows multiple transactions to access the same data item simultaneously.
   - Each transaction maintains a copy of the data item and checks for conflicts at the time of commit.
   - If there are no conflicts, the transaction commits, and if there are conflicts, the transaction is rolled back.
   - This technique avoids locking overhead but can lead to a high rate of aborts.

4. Multi-Version Concurrency Control:
   - Multi-version concurrency control allows multiple versions of the same data item to coexist in the database.
   - Each version is associated with a timestamp and represents the state of the data item at a particular point in time.
   - Transactions can access any version of the data item that is consistent with their timestamp.
   - This technique avoids conflicts and provides good performance, but it requires additional storage space.

In conclusion, concurrency control techniques are crucial for ensuring the consistency and correctness of database transactions. Each technique has its advantages and disadvantages, and the choice of technique depends on the specific requirements of the application. It is important to understand these techniques thoroughly to design and implement efficient and reliable database systems.