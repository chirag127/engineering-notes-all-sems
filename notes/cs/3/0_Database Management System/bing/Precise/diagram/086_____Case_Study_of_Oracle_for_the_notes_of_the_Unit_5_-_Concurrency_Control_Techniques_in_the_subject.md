### Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Oracle uses a technique known as **Multi-version Concurrency Control (MVCC)** to implement its consistency model. Specifically, it uses three transaction isolation levels.
- Oracle maintains data concurrency, integrity, and consistency by using a **multiversion consistency model** and various types of **locks and transactions**.
- Oracle automatically provides **read consistency** to a query so that all the data that the query sees comes from a single point in time (statement-level read consistency).
- The database can present a view of data to multiple concurrent users, with each view consistent to a point in time.
- Various concurrency control techniques are: **Two-phase locking Protocol**, **Time stamp ordering Protocol**, **Multi version concurrency control**, and **Validation concurrency control**.
