 Here is the content in markdown format for the given topic:

### Multiple Granularity for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

- Multiple granularity refers to controlling concurrency at different levels in the database. The different levels can be:

- Table level: Entire table is locked for reading/writing. Easy to implement but low concurrency.
- Page level: Entire page is locked for reading/writing. Medium concurrency but extra overhead to track pages.
- Row level: Only required row is locked. High concurrency but most overhead to track rows.

- There is a trade-off between concurrency and overhead. The appropriate granularity is chosen based on the requirements of the application.
- For applications with high contention (many users accessing same data), row level should be used. For applications with low contention, table level can be used for simplicity.
- Example: In a banking database, account balance table should use row level and customer personal details table can use table level locking.
- Granularity can be decided at schema design time or can be dynamically changed based on the contention. The database manager monitors the locks and dynamically chooses appropriate granularity.
- Advantages: Increased concurrency, meets different application requirements. Disadvantages: Extra overhead to track and lock at different granularities.
- Appropriate granularity along with other concurrency control techniques like timestamp ordering, wait-die, wound-wait helps in managing concurrency and maintaining database consistency.

[Detailed diagrams and examples can be added if required.]