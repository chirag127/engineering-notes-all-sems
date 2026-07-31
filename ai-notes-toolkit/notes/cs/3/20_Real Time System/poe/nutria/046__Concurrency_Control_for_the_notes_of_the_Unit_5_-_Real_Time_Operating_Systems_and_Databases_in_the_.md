
### Concurrency Control for Unit 5 - Real Time Operating Systems and Databases

1. Concurrency control is the process of ensuring that multiple users can access and modify data in a database concurrently, without compromising the integrity of the data.

2. It is important to note that while concurrency control is necessary in a multi-user environment, it is not a substitute for proper database design.

3. Concurrency control is achieved through the use of locking, which is a mechanism that prevents concurrent access to a database by multiple users.

4. Locking can be implemented in various ways, including optimistic and pessimistic locking.

5. Optimistic locking is a technique that allows concurrent access to a database but prevents concurrent modification of the same data.

6. Pessimistic locking is a technique that prevents concurrent access to the database, but allows concurrent modification of the same data.

7. Database transactions are used to ensure that all operations within a transaction are either committed or rolled back as a unit.

8. Concurrency control is also implemented through the use of database triggers, which are special procedures that are executed when certain conditions are met.

9. The most common type of trigger is the before trigger, which is executed before a data modification is performed.

10. The after trigger is executed after the data modification is performed.