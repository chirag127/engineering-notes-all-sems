### Serializability of schedules

- A schedule is a sequence of database actions (read and write operations) performed by one or more transactions on a shared database.
- Serializability is a property of a schedule that ensures that the concurrent execution of transactions produces the same results as if they were executed one at a time in some order.
- Serializability is important for maintaining consistency and preventing conflicts in a database management system (DBMS).
- There are different types of serializability, such as conflict serializability, view serializability, and cursor stability serializability, that have different criteria and methods to achieve them.
- Conflict serializability is the most common type of serializability, which requires that the order of conflicting operations (those that access the same data item) in a schedule is the same as in some serial schedule.
- View serializability is a weaker type of serializability, which requires that the read and write operations on each data item in a schedule have the same effect as in some serial schedule, regardless of the order of non-conflicting operations.
- Cursor stability serializability is a type of serializability that applies to cursor-based transactions, which requires that the data item pointed by the cursor is not modified by other transactions until the cursor is moved or closed.
- Serializability can be checked by using different techniques, such as precedence graphs, conflict graphs, polygraphs, and testing for cycles.
- Serializability can be enforced by using different methods, such as locking, timestamping, validation, and multiversion concurrency control, that control the access and order of transactions on the database.