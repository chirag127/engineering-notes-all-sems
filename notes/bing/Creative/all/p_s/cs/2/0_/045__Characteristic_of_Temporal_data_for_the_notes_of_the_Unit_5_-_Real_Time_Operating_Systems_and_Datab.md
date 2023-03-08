### Characteristic of Temporal Data for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Temporal data is data that has a time dimension associated with it, such as the time of creation, modification, validity, or occurrence  .
- Temporal data is generally used in real-time systems, which are systems that interact with the dynamic environment and have strict timing constraints .
- Examples of real-time systems that use temporal data are railway seat reservation, sensex, weather forecasting, air traffic control, etc .
- Temporal data can be classified into three types based on the time dimension: valid time, transaction time, and decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world, such as the birth date of a person, the duration of a flight, or the temperature of a location.
  - Transaction time is the time period during or event time at which a fact is stored, modified, or deleted in the database, such as the timestamp of a record, the log of a transaction, or the audit trail of a change.
  - Decision time is the time period during or event time at which a fact is known, decided, or acted upon by an agent, such as the date of a diagnosis, the deadline of a task, or the execution of a command.
- Temporal data can also be classified into two types based on the temporal consistency: absolute validity and relative validity.
  - Absolute validity is the property that ensures that the difference between the values stored in the database and the real values is within some predefined limit, such as the margin of error, the tolerance, or the freshness.
  - Relative validity is the property that ensures that the values stored in the database are consistent with each other, such as the temporal order, the temporal integrity, or the temporal coherence.
- Temporal data can be stored, manipulated, queried, and analyzed using temporal databases, which are databases that have built-in support for handling data involving time .
- Temporal databases can be uni-temporal, bi-temporal, or tri-temporal, depending on the number of time dimensions they support.
  - Uni-temporal databases support only one time dimension, either valid time or transaction time, such as historical databases, snapshot databases, or audit databases.
  - Bi-temporal databases support both valid time and transaction time, such as temporal data warehouses, temporal OLAP, or temporal data mining.
  - Tri-temporal databases support valid time, transaction time, and decision time, such as decision support systems, workflow management systems, or event processing systems.
- Temporal databases can use different data models, such as relational, object-oriented, or XML, to represent and store temporal data.
- Temporal databases can use different query languages, such as SQL, OQL, or XQuery, to access and manipulate temporal data.
- Temporal databases can use different techniques, such as indexing, partitioning, or compression, to optimize the performance and storage of temporal data.
- Temporal databases can use different methods, such as interpolation, extrapolation, or aggregation, to analyze and visualize temporal data .

Some possible mnemonics and learning tricks for the topic are:

- To remember the three types of time dimensions, use the acronym VTD: Valid Time, Transaction Time, and Decision Time.
- To remember the two types of temporal consistency, use the acronym ARR: Absolute validity and Relative validity.
- To remember the three types of temporal databases, use the acronym BUB: Bi-temporal, Uni-temporal, and Tri-temporal.
- To remember the difference between valid time and transaction time, use the phrase "valid in reality, transaction in database".
- To remember the difference between absolute validity and relative validity, use the phrase "absolute is accuracy, relative is consistency".