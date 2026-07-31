### Data Delivery Semantics: Microbatching and One-Element-at-a-Time

- Data delivery semantics refer to how data is processed and delivered from the source to the destination in a distributed system.
- There are two main types of data delivery semantics: **at-most-once** and **exactly-once**.
- At-most-once semantics mean that each data element is processed and delivered at most once, but it may be lost or duplicated due to failures or network issues.
- Exactly-once semantics mean that each data element is processed and delivered exactly once, regardless of failures or network issues.
- Achieving exactly-once semantics is challenging and often requires additional coordination and overhead.
- There are two main approaches to achieve exactly-once semantics: **microbatching** and **one-element-at-a-time**.

#### Microbatching

- Microbatching is a technique where incoming data is grouped into small batches and processed in parallel, resulting in lower latency and higher throughput than batch processing.
- Microbatching can achieve exactly-once semantics by using checkpoints and idempotent operations.
- Checkpoints are periodic snapshots of the state of the processing system, such as the offsets of the input streams or the intermediate results of the computations.
- Idempotent operations are operations that can be applied multiple times without changing the outcome, such as appending to a file or updating a key-value store.
- By using checkpoints and idempotent operations, microbatching can ensure that each batch is processed and delivered exactly once, even if there are failures or retries.
- An example of a system that uses microbatching is **Spark Streaming**, which divides the input data into micro-batches called **DStreams** and processes them using the Spark engine.

#### One-Element-at-a-Time

- One-element-at-a-time is a technique where incoming data is processed and delivered one element at a time, resulting in lower latency and higher accuracy than microbatching.
- One-element-at-a-time can achieve exactly-once semantics by using transactions and deduplication.
- Transactions are atomic and isolated operations that ensure the consistency and durability of the processing system, such as committing the offsets of the input streams or the results of the computations to a durable storage.
- Deduplication is a process of removing duplicate data elements that may have been processed or delivered more than once due to failures or retries.
- By using transactions and deduplication, one-element-at-a-time can ensure that each element is processed and delivered exactly once, even if there are failures or retries.
- An example of a system that uses one-element-at-a-time is **Flink**, which uses a mechanism called **checkpointing** to periodically take consistent snapshots of the state of the processing system and uses a technique called **stateful stream processing** to process and deliver each element exactly once.