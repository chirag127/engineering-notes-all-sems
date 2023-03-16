# Data Delivery Semantics: Microbatching and One-Element-at-a-Time

- Data delivery semantics refer to how data is transferred from a source to a destination, and how the destination handles the data in terms of ordering, duplication, and completeness.
- There are two main types of data delivery semantics: microbatching and one-element-at-a-time.
- Microbatching is a technique where incoming data is grouped into small batches and processed periodically, rather than individually and continuously.
- One-element-at-a-time is a technique where incoming data is processed as soon as it arrives, without waiting for other data elements or batches.
- Both techniques have advantages and disadvantages, depending on the use case, the data characteristics, and the system requirements.

## Microbatching

- Microbatching is a middle-ground between batch processing and stream processing that balances latency and throughput and can be the ideal option for several use cases.
- It strives to increase the server throughput through some sort of batch processing, and, at the same time, reduces the latency at the client’s end.
- In microbatching, a server typically waits for a short duration of time (this can be milliseconds or several seconds), before executing a batch operation. The duration of time it waits is called the batch cycle, and the number of tasks within a cycle is called the batch size. The system can have an upper limit on the batch size as well.
- Microbatching has the following advantages:
  - It can handle variable and unpredictable data arrival rates, by adjusting the batch size and cycle dynamically.
  - It can reduce the overhead of processing each data element individually, by amortizing the cost over a batch.
  - It can improve the fault tolerance and reliability of the system, by allowing for checkpointing and recovery of batches in case of failures.
  - It can simplify the programming model and the state management, by providing a clear boundary between batches and a consistent view of the data within a batch.
- Microbatching has the following disadvantages:
  - It introduces some latency for each data element, as it has to wait for the batch cycle to complete before being processed.
  - It may not be suitable for applications that require very low latency or strict ordering guarantees, as batches may be processed out of order or delayed due to network or system issues.
  - It may incur some extra memory and storage costs, as it has to buffer the data elements until the batch is ready to be processed.

## One-Element-at-a-Time

- One-element-at-a-time is a technique where incoming data is processed as soon as it arrives, without waiting for other data elements or batches.
- It is also known as stream processing, event processing, or real-time processing, and it is suitable for applications that require very low latency and high responsiveness.
- In one-element-at-a-time, a server typically processes each data element individually and continuously, without any batching or buffering. The processing may involve stateful or stateless operations, depending on the application logic.
- One-element-at-a-time has the following advantages:
  - It can achieve very low latency for each data element, as it does not introduce any waiting or batching delays.
  - It can preserve the order and completeness of the data, as it does not reorder or drop any data elements.
  - It can support complex and dynamic processing logic, as it can apply stateful or stateless operations on each data element.
- One-element-at-a-time has the following disadvantages:
  - It may not be able to handle high and variable data arrival rates, as it may overload the server or cause backpressure issues.
  - It may increase the overhead of processing each data element individually, as it may incur more network and system calls.
  - It may reduce the fault tolerance and reliability of the system, as it may not have any checkpointing or recovery mechanisms for individual data elements.
  - It may complicate the programming model and the state management, as it may require more synchronization and coordination among concurrent processes.