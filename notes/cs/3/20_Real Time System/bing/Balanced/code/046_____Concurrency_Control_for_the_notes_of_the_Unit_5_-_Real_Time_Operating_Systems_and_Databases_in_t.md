### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, where many events and actions occur simultaneously.
- Real-time systems (RTS) are systems that respond to their environment within specified time constraints .
- RTS are inherently concurrent and typically manage shared data resources, such as sensors, actuators, files, databases, etc .
- Concurrency control is the process of ensuring both logical and timing correctness of concurrent accesses to shared data resources in RTS.
- Logical correctness means that the concurrent accesses do not violate the data integrity and consistency rules, such as mutual exclusion, serializability, etc.
- Timing correctness means that the concurrent accesses do not cause deadline misses or timing anomalies, such as priority inversion, blocking, etc.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by using locks, timestamps, or other mechanisms to coordinate concurrent accesses.
- Optimistic concurrency control techniques allow conflicts to occur and then resolve them by using validation, compensation, or restart mechanisms.
- Concurrency control techniques can also be classified into centralized and distributed, depending on whether there is a single or multiple coordinators for managing concurrent accesses.
- Concurrency control techniques should be designed and evaluated based on the following criteria: correctness, performance, scalability, and adaptability.
- Correctness criteria include logical and timing correctness, as well as deadlock-freedom, liveliness, and fairness.
- Performance criteria include throughput, response time, utilization, and overhead.
- Scalability criteria include the ability to handle increasing number of concurrent accesses, data resources, and system nodes.
- Adaptability criteria include the ability to cope with dynamic changes in the system workload, environment, and requirements.
- Concurrency control for real-time systems is a challenging and active research area, as it involves trade-offs and conflicts among different criteria and techniques.