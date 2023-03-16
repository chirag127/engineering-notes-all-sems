# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic concurrency control are two-phase locking, timestamp ordering, and priority inheritance protocol.
  - Optimistic concurrency control allows conflicts to occur and resolves them after they are detected. Examples of optimistic concurrency control are multiversion concurrency control, validation-based concurrency control, and optimistic locking.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as performance considerations, correctness criteria, and transaction models.
  - Performance considerations for RTS include meeting deadlines, minimizing blocking time, and maximizing concurrency.
  - Correctness criteria for RTS include serializability, recoverability, and temporal consistency.
  - Transaction models for RTS include periodic, aperiodic, sporadic, and soft transactions.
- Concurrency control techniques for RTS should be tailored to the specific characteristics and requirements of the application domain, such as automotive, aerospace, robotics, energy, transportation, and finance.