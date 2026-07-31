# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, where many events occur simultaneously and interact with each other.
- Real-time systems (RTS) are systems that respond to their environment within specified time constraints.
- RTS are inherently concurrent and typically manage shared data resources, such as sensors, actuators, files, databases, etc.
- Concurrency control is the process of ensuring both logical and timing correctness of concurrent accesses to shared data resources in RTS.
- Logical correctness means that the concurrent accesses do not violate the integrity and consistency of the data.
- Timing correctness means that the concurrent accesses do not cause any deadline misses or timing anomalies in the system.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by using locks, timestamps, or serialization protocols to coordinate concurrent accesses.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them by using validation, compensation, or restart mechanisms.
- Concurrency control techniques can also be classified into two levels: transaction level and data item level.
- Transaction level concurrency control techniques deal with the atomicity, consistency, isolation, and durability (ACID) properties of transactions, which are logical units of work that access or update shared data resources.
- Data item level concurrency control techniques deal with the granularity, freshness, and validity of data items, which are the smallest units of data that can be accessed or updated by transactions.
- Concurrency control techniques for RTS must consider not only the logical and timing correctness, but also the performance and predictability of the system.
- Performance measures the throughput, response time, and resource utilization of the system.
- Predictability measures the degree of certainty and stability of the system behavior under different workloads and scenarios.
- Concurrency control techniques for RTS must balance the trade-offs among these criteria and adapt to the dynamic and uncertain nature of the real-time environment.