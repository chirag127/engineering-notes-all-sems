### Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, and allow querying and manipulating data based on temporal aspects .
- Temporal data models exist at three abstraction levels:
  - The conceptual level, in which the data models are generally extensions of the Entity-Relationship Model (ERM).
  - The logical level, in which the data models are generally extensions of the relational data model or of an object-oriented data model.
  - The physical level, in which the data model details how the data are to be stored.
- Temporal data models can be classified based on the type of time they capture:
  - Valid time: the time when the data is valid with respect to the real world (also called business time).
  - Transaction time: the time when the data is recorded in the database (also called system time).
  - Decision time: the time when a decision is made about the data (also called application time).
- Temporal data models can also be classified based on the number of time dimensions they capture:
  - Uni-temporal: a data model that captures only one type of time (either valid time or transaction time).
  - Bi-temporal: a data model that captures both valid time and transaction time.
  - Tri-temporal: a data model that captures valid time, transaction time and decision time.
- Temporal data models have various applications in intelligent database systems, such as:
  - Data warehousing: temporal data models can support the analysis of historical and current data, and enable trend detection and forecasting.
  - Data mining: temporal data models can facilitate the discovery of temporal patterns and associations in data, and support temporal classification and clustering.
  - Decision support systems: temporal data models can provide the context and rationale for decision making, and allow what-if analysis and scenario evaluation.
  - Knowledge management: temporal data models can capture the evolution and validity of knowledge, and support knowledge sharing and reuse.