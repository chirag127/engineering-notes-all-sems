### Stateless and Stateful Processing

- Stream processing is the process of continuously analyzing and processing data streams in real time.
- Stream processing can be stateless or stateful, depending on whether the processing logic depends on the previous state of the data or not.
- In stateless stream processing, the current data/events are processed independently of previous ones. The data is evaluated as it arrives without consideration for the prior state or knowledge .
- Stateless stream processing is suitable for simple operations that do not require any context or history, such as filtering, mapping, or aggregating data.
- Stateless stream processing is also easier to scale and parallelize, as each data/event can be processed by any available worker node without synchronization or coordination.
- An example of stateless stream processing is a bank teller that processes a stream of customers, one at a time, without keeping track of the previous or next customers.
- In stateful stream processing, the current data/events are processed in relation to the previous ones. The data is evaluated as it arrives with consideration for the prior state or knowledge .
- Stateful stream processing is suitable for complex operations that require context or history, such as joining, windowing, or pattern matching data.
- Stateful stream processing is also more expressive and powerful, as it can capture the dynamics and trends of the data over time.
- An example of stateful stream processing is a temperature sensor that monitors the ambient temperature and alerts when it changes significantly from the previous readings.