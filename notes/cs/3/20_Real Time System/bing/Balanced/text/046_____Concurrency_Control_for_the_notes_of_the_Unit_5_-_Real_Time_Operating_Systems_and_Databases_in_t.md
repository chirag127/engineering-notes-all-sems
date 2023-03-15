### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, where many events and actions occur simultaneously.
- Real-time systems (RTS) are systems that respond to their environment within specified time constraints .
- RTS are inherently concurrent and typically manage shared data resources, such as sensors, actuators, files, databases, etc .
- Concurrency control is the process of ensuring both logical and timing correctness of concurrent access to shared data resources in RTS.
- Logical correctness means that the concurrent access does not violate the integrity and consistency of the data.
- Timing correctness means that the concurrent access does not cause any deadline misses or timing anomalies in the system.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by using locks, timestamps, or serialization protocols to coordinate the access to shared data.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them by using validation, compensation, or restart mechanisms.
- Concurrency control techniques can also be classified into two levels: transaction level and object level.
- Transaction level concurrency control techniques deal with the synchronization of transactions, which are sequences of operations that access shared data and have atomicity, consistency, isolation, and durability (ACID) properties.
- Object level concurrency control techniques deal with the synchronization of objects, which are units of data that have identity, state, and behavior.
- Concurrency control techniques for RTS must consider the timing constraints and the priority of the transactions or objects, as well as the logical correctness and the performance of the system.
- Concurrency control techniques for RTS must also be adaptable to the dynamic and unpredictable nature of the real-time environment, such as varying workload, resource availability, and system state.
- Some examples of concurrency control techniques for RTS are: priority inheritance protocol, priority ceiling protocol, earliest deadline first protocol, timestamp ordering protocol, optimistic concurrency control with compensation, and adaptive concurrency control.