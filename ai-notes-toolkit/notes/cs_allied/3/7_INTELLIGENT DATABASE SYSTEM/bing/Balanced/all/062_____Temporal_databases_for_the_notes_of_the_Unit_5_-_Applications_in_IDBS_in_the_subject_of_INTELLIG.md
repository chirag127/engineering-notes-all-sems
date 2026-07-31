# Temporal databases

- A temporal database is a database that has certain features that support time-sensitive status for entries .
- A temporal database can store data relating to past, present and future time instances.
- A temporal database can also track the history of data changes and support queries over different time dimensions  .
- Temporal databases can be classified into different types based on the time dimensions they support:
  - Uni-temporal: A database that supports only one time dimension, either valid time or transaction time.
  - Bi-temporal: A database that supports both valid time and transaction time dimensions.
  - Tri-temporal: A database that supports valid time, transaction time and decision time dimensions.
- Valid time is the time period during or event time at which a fact is true in the real world .
- Transaction time is the time period during which a fact is stored in the database .
- Decision time is the time point at which a fact is recorded or decided in the database.
- Temporal databases can offer various benefits for applications that need to handle time-sensitive data, such as auditing, historical analysis, trend detection, data recovery, compliance, etc .
- Temporal databases can also pose some challenges, such as increased storage requirements, complex query processing, data consistency, temporal integrity, etc.