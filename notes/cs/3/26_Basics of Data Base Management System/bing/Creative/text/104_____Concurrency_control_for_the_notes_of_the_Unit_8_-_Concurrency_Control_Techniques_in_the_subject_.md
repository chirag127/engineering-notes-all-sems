### Concurrency control

- Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system.
- Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases .
- Concurrency control is a procedure in DBMS which helps us for the management of two simultaneous processes to execute without conflicts between each other, these conflicts occur in multi user systems.
- Concurrency control refers to the various techniques that are used to preserve the integrity of the database when multiple users are updating rows at the same time.
- Incorrect concurrency can lead to problems such as dirty reads, phantom reads, and non-repeatable reads.

### Concurrency control techniques

- There are two main types of concurrency control techniques: pessimistic and optimistic .
- Pessimistic concurrency control assumes that conflicts are likely to happen and uses locks to prevent them. Locks are mechanisms that restrict access to data items by concurrent transactions .
- Optimistic concurrency control assumes that conflicts are rare and uses timestamps or versions to detect them. Timestamps or versions are identifiers that indicate the order or state of data items by concurrent transactions .
- Some examples of pessimistic concurrency control techniques are two-phase locking (2PL), strict two-phase locking (S2PL), and tree locking .
- Some examples of optimistic concurrency control techniques are timestamp ordering (TO), multiversion concurrency control (MVCC), and validation .