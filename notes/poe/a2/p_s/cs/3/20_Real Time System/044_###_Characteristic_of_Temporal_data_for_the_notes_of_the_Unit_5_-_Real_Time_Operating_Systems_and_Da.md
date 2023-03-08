 Here is the content in markdown format for the topic -

### Characteristics of Temporal data

Following are the key characteristics of temporal data:

1. Time-varying: Temporal data changes with time. The values of attributes can change with time. For example, location of a moving object, temperature readings, stock prices, etc. change continuously with time.
2. Valid time: The time period during which a fact is true in the real world. For example, an employee was working in a department from January 1, 2020 to March 31, 2020. This is the valid time for that fact.
3. Transaction time: The time at which a fact was recorded in the database. For example, the fact that an employee changed department was recorded in the database on February 1, 2020. This is the transaction time for that database record.
4. Bi-temporal: Data that has both valid time and transaction time. This allows tracking the state of data at any point in the valid time and knowing when that state was recorded in the database.
5. Time-specific: The meaning of temporal data depends on the time it refers to. The analysis of temporal data must take the time dimension into account.
6. Expiry: Temporal data may have an expiry time after which the data is no longer valid or relevant. The database needs to handle the expiry of data and its effects.

The key applications of temporal databases are - data warehousing, geographic information systems, version control systems, etc. However, providing efficient query processing and ensuring data consistency are major research challenges for temporal databases.

The above points cover the key characteristics of temporal data. Please let me know if you would like me to elaborate on any of the points or add more details to the answer.