# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, the system may make wrong decisions or miss deadlines.
- Temporal consistency can be measured by the temporal error, which is the difference between the actual value of a data item and the value stored in the database. The temporal error should be within a predefined limit, otherwise the data is considered temporally inconsistent.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the system when the data changes in the environment, rather than by the user transactions.
  - Periodic refreshes, which are updates that are performed at regular intervals, regardless of the data changes in the environment.
  - Temporal validity, which is a property of data items that specifies the time interval during which they are valid and can be used by transactions.
  - Temporal isolation, which is a property of transactions that specifies the maximum temporal error that they can tolerate when accessing data items.
  - Temporal locking, which is a concurrency control mechanism that prevents transactions from accessing data items that are being updated or have a high temporal error.
  - Temporal caching, which is a technique that stores frequently accessed data items in a local memory to reduce the access time and the temporal error.