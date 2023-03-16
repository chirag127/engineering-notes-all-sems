### Stateless and Stateful Processing

- Stream processing is the process of analyzing and processing data streams in real time.
- Stream processing can be either stateless or stateful, depending on whether the current data/events are processed independently of previous ones or not.
- Stateless stream processing :
  - The data is evaluated as it arrives without consideration for the prior state or knowledge.
  - Each record is processed individually and does not depend on any previous or future records.
  - Examples of stateless operations are filtering, mapping, and transforming data.
  - Stateless stream processing is simpler and faster, but less expressive and powerful.
- Stateful stream processing :
  - The data is evaluated in the context of the overall state of the data, which is maintained and updated over time.
  - Each record is processed in relation to the previous and future records, and the state is updated accordingly.
  - Examples of stateful operations are aggregating, joining, and windowing data.
  - Stateful stream processing is more complex and slower, but more expressive and powerful.