### Temporal Data Models

- Temporal data models are data models that capture the changes of data over time, as well as the time references of the data.
- Temporal data models can be classified into three levels of abstraction: conceptual, logical, and physical.
- Conceptual level: the data models are generally extensions of the Entity-Relationship Model, which represent the entities, attributes, and relationships of a domain.
- Logical level: the data models are generally extensions of the relational data model or of an object-oriented data model, which define the structure, integrity constraints, and operations of the data.
- Physical level: the data models detail how the data are to be stored, accessed, and manipulated by the database system.
- Temporal data models can also be classified into three types of time references: valid time, transaction time, and decision time.
- Valid time: the time when the data is valid with respect to the real world, such as the birth date of a person, the duration of a contract, or the expiration date of a product.
- Transaction time: the time when the data is recorded in the database, such as the insertion, update, or deletion time of a row.
- Decision time: the time when the data is used for decision making, such as the time of a query, a report, or an analysis.
- Temporal data models can be uni-temporal, bi-temporal, or tri-temporal, depending on how many types of time references they capture.
- Uni-temporal: the data model captures only one type of time reference, either valid time or transaction time.
- Bi-temporal: the data model captures both valid time and transaction time, which allows tracking the history and evolution of the data.
- Tri-temporal: the data model captures valid time, transaction time, and decision time, which allows tracing the provenance and rationale of the data.