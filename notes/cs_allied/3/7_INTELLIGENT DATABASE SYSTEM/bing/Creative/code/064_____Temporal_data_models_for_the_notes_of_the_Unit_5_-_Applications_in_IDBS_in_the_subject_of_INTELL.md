### Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, as well as the time references of the data.
- Temporal data models exist at three abstraction levels:
  - The conceptual level, in which the data models are generally extensions of the Entity-Relationship Model (ERM).
  - The logical level, in which the data models are generally extensions of the relational data model or of an object-oriented data model.
  - The physical level, in which the data model details how the data are to be stored.
- Temporal data models can be classified according to the type of time they capture :
  - Valid time, which is the time when the data is valid with respect to the real world. For example, the valid time of an employee's salary is the period when the employee actually receives that salary.
  - Transaction time, which is the time when the data is recorded in the database. For example, the transaction time of an employee's salary is the time when the salary is updated in the database.
  - Decision time, which is the time when a decision is made about the data. For example, the decision time of an employee's salary is the time when the salary is approved by the manager.
- Temporal data models can also be classified according to the number of time dimensions they capture:
  - Uni-temporal, which captures only one type of time (either valid time, transaction time, or decision time).
  - Bi-temporal, which captures two types of time (usually valid time and transaction time, or valid time and decision time).
  - Tri-temporal, which captures all three types of time (valid time, transaction time, and decision time).
- Temporal data models have several advantages over conventional data models:
  - They can support temporal queries, which can retrieve data based on time conditions. For example, a temporal query can ask for the salary of an employee at a given date, or the history of salary changes for an employee.
  - They can support temporal integrity constraints, which can ensure the consistency and validity of temporal data. For example, a temporal integrity constraint can prevent overlapping valid times for the same data, or enforce a temporal order between transactions.
  - They can support temporal reasoning, which can infer new information from temporal data. For example, a temporal reasoning system can deduce the causal relationships between events, or the temporal patterns of data.