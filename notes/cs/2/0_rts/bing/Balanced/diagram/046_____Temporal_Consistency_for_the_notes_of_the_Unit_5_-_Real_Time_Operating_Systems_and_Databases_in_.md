### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, the system may make wrong decisions or miss deadlines.
- Temporal consistency can be measured by the difference between the actual value of a physical entity and the value of the corresponding data object in the database. This difference is called temporal error or temporal skew.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates: updating the data objects periodically or when a significant change occurs in the physical environment.
  - Temporal validity: assigning a validity interval to each data object and checking if the data object is still valid before reading it.
  - Temporal caching: caching the data objects in the memory of the processors and updating them when needed.
  - Temporal locking: locking the data objects for a certain duration and preventing other transactions from accessing them until they are updated.
- Temporal consistency can be traded off with other performance metrics, such as throughput, response time, deadline miss ratio, and memory usage. Different real-time systems may have different requirements and preferences for temporal consistency and other metrics.