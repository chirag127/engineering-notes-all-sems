### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on accurate and timely information about the environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the application logic.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not match the current state of the physical environment. Data staleness can be caused by delays in data acquisition, transmission, processing, or storage.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other. Data inconsistency can be caused by concurrent updates, replication, or failures.
- Temporal consistency can be measured by two metrics: absolute validity and relative validity.
  - Absolute validity is a metric that defines a maximum acceptable difference between the data stored in the database and the current state of the physical environment. Absolute validity can be expressed as a time interval or a value range.
  - Relative validity is a metric that defines a maximum acceptable difference between the data stored in the database and the data read by a transaction. Relative validity can be expressed as a time interval or a value range.
- Temporal consistency can be maintained by various techniques, such as:
  - Triggered updates, which are updates that are initiated by the data sources when the data changes in the physical environment. Triggered updates can reduce data staleness and improve absolute validity.
  - Eager updates, which are updates that are propagated to all the replicas of the data as soon as they are generated. Eager updates can reduce data inconsistency and improve relative validity.
  - Lazy updates, which are updates that are propagated to the replicas of the data only when they are needed by a transaction. Lazy updates can reduce the communication and storage overhead of eager updates, but may increase data inconsistency and degrade relative validity.
  - Concurrency control, which is a mechanism that coordinates the access and modification of the data by multiple transactions. Concurrency control can prevent data inconsistency and ensure relative validity, but may introduce delays and conflicts that affect the performance and schedulability of the transactions.
  - Data freshness, which is a mechanism that monitors the age and quality of the data stored in the database and discards or refreshes the data that are too old or inaccurate. Data freshness can improve absolute validity and relative validity, but may increase the workload and complexity of the system.