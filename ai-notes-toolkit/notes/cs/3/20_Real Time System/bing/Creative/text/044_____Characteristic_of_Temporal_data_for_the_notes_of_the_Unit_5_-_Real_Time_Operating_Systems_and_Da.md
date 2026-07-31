### Characteristics of Temporal Data

- Temporal data are any data that represent time in some form, and allow other data to be placed in a chronological sequence, or to be analyzed chronologically.
- Temporal data can be classified into three types: valid time, transaction time, and decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world. For example, the date of birth of a person is a valid time attribute.
  - Transaction time is the time period during which a fact is stored in the database. For example, the date of entry of a record is a transaction time attribute.
  - Decision time is the time period during which a fact is considered to be relevant for a decision or action. For example, the date of expiry of a contract is a decision time attribute.
- Temporal data can be stored in different ways in a database, such as using a time period datatype, defining valid and transaction time period attributes, or using bitemporal relations.
  - A time period datatype is a data type that can represent a time interval with a start and an end point, or an instant with no duration. For example, a date or a timestamp can be a time period datatype.
  - Valid and transaction time period attributes are attributes that store the valid and transaction time periods of a fact. For example, a table can have columns for valid_from, valid_to, transaction_from, and transaction_to to store the temporal information of each row.
  - Bitemporal relations are relations that store both valid and transaction time periods of a fact. For example, a table can have a primary key that consists of the original key and the transaction time period, and a valid time period attribute for each row.
- Temporal data can be queried and manipulated using temporal operators, such as overlap, contain, precede, follow, etc. For example, a query can ask for the facts that were valid and stored in a certain time period, or the facts that changed their validity or transaction time periods over time.
- Temporal data can be used for various purposes, such as historical analysis, auditing, versioning, temporal consistency, etc  .
  - Historical analysis is the process of examining the past states or changes of a fact over time. For example, a historical analysis can show the trends or patterns of a fact in different time periods.
  - Auditing is the process of verifying the accuracy and completeness of a fact over time. For example, an auditing can check the sources and updates of a fact in different time periods.
  - Versioning is the process of maintaining different versions of a fact over time. For example, a versioning can keep track of the revisions or modifications of a fact in different time periods.
  - Temporal consistency is the property of a fact that ensures its validity and transaction time periods are coherent and correct. For example, a temporal consistency can prevent or detect the anomalies or conflicts of a fact in different time periods.