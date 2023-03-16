### Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, as well as the time references that indicate when the data are valid or recorded.
- Temporal data models can be classified into three levels of abstraction: conceptual, logical, and physical.
  - Conceptual level: the data models are extensions of the Entity-Relationship Model, which represent entities, attributes, and relationships with temporal aspects.
  - Logical level: the data models are extensions of the relational data model or the object-oriented data model, which define temporal data types, temporal constraints, and temporal operations on tables or objects.
  - Physical level: the data models specify how the temporal data are stored, indexed, and accessed by the database system.
- Temporal data models can also be classified into three types of time references: valid time, transaction time, and decision time.
  - Valid time: the time when the data are true or valid in the real world. For example, the valid time of a person's employment record is the period when the person works for a company.
  - Transaction time: the time when the data are recorded or updated in the database. For example, the transaction time of a person's employment record is the time when the record is inserted, modified, or deleted in the database.
  - Decision time: the time when the data are used or decided by a user or an application. For example, the decision time of a person's employment record is the time when the record is queried or reported by a user or an application.
- Temporal data models can also be classified into three types of temporal databases: uni-temporal, bi-temporal, and tri-temporal.
  - Uni-temporal: the temporal database that captures only one type of time reference, either valid time or transaction time. For example, a uni-temporal database that captures valid time can store the history of data changes in the real world, but not the history of data changes in the database.
  - Bi-temporal: the temporal database that captures both valid time and transaction time. For example, a bi-temporal database can store the history of data changes in both the real world and the database, and support queries that compare the two histories.
  - Tri-temporal: the temporal database that captures valid time, transaction time, and decision time. For example, a tri-temporal database can store the history of data changes in the real world, the database, and the user's perspective, and support queries that compare the three histories.