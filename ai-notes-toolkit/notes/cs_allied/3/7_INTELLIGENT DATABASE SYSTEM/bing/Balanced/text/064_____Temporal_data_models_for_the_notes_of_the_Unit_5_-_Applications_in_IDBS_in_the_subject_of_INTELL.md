### Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, as well as the time references that indicate when the data are valid or recorded.
- Temporal data models exist at three abstraction levels:
  - The conceptual level, in which the data models are generally extensions of the Entity-Relationship Model (ERM).
  - The logical level, in which the data models are generally extensions of the relational data model or of an object-oriented data model.
  - The physical level, in which the data model details how the data are to be stored.
- Temporal data models can be classified according to the type of time they capture :
  - Valid time, which is the time when the data are true in the real world.
  - Transaction time, which is the time when the data are recorded in the database.
  - Decision time, which is the time when the data are used for decision making.
- Temporal data models can also be classified according to the number of time dimensions they capture:
  - Uni-temporal, which capture only one type of time (either valid time or transaction time).
  - Bi-temporal, which capture both valid time and transaction time.
  - Tri-temporal, which capture valid time, transaction time and decision time.
- Temporal data models require special data types, operations and constraints to handle time values and intervals  .
  - Temporal data types include date, time, timestamp, interval and period.
  - Temporal operations include temporal selection, projection, join, aggregation, grouping and ordering.
  - Temporal constraints include temporal primary keys, foreign keys, referential integrity and temporal consistency.
- Temporal data models have various applications in intelligent database systems, such as data warehousing, data mining, temporal reasoning, temporal query processing and temporal data visualization .