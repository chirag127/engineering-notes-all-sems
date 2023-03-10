 Here is the content in markdown format for the topic ### multiple granularity for the notes of the Unit 8 - Concurrency Control Techniques in the subject of Basics of Data Base Management System:

Multiple Granularity:
- Multiple granularity refers to locking data at different levels of breadth.
- Three standard locking granularities are:
    - Record-level locking: Locks are applied to individual records. Provides the finest concurrency but has high overhead.
    - Page-level locking: Locks are applied to pages of records. Coarse but less overhead.
    - Table-level locking: Entire tables are locked. Coarsest granularity with least overhead but low concurrency.
- Choosing granularity involves trading off concurrency versus overhead.
- Most DBMSs support multiple granularities and allow the application or user to select the appropriate one.

Advantages:
- Allows tuning of locking granularity to workload.
- Supports a range of concurrency-throughput tradeoffs.

Disadvantages:
- More complex to implement.
- Hard to determine appropriate granularity for a given workload.

Examples:
- Most DBMSs allow a choice of record-, page-, or table-level locking.
- Some systems allow locking at varying levels of a database hierarchy (e.g., tables, clusters of tables, databases).

Applications:
- Multiple granularity is useful when the workload is not well understood or is expected to change over time. It allows the granularity to be tuned to the workload.
- It is also useful when parts of the database have high concurrency requirements and other parts have high throughput requirements. Different granularities can be used for different parts of the database.

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.