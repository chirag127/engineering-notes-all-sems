### Conflict & View Serializable Schedule

#### Unit 4 - Transaction Processing Concept in Database Management System

- A **conflict serializable schedule** is a schedule whose effect on any consistent database state is guaranteed to be the same as that of some serial (one-at-a-time) schedule of transactions.

- A **view serializable schedule** is a schedule where the same set of transactions reading and writing the same data items and producing the same final result, as in a serial schedule.

- Conflict serializability is a more restrictive condition than view serializability.

- A schedule is conflict serializable if and only if its precedence graph is acyclic.

- A schedule is view serializable if it is view equivalent to a serial schedule.

- Conflict serializability can be tested in polynomial time, while view serializability is an NP-complete problem.

- Conflict serializability is used in practice because it is easier to test and enforce.

- View serializability is more general and allows for more concurrency, but it is more difficult to test and enforce.

- In summary, conflict and view serializability are two different conditions for ensuring the correctness of concurrent transaction execution in a database management system. Conflict serializability is more restrictive and easier to test, while view serializability is more general and allows for more concurrency, but is more difficult to test and enforce.