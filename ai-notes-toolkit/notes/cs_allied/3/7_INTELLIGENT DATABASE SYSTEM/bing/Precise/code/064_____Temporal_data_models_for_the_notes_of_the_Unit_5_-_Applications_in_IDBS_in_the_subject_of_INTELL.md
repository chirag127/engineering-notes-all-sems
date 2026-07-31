### Temporal Data Models

Temporal data models are used to represent the changes in data over time. These models are commonly used in applications that require tracking of historical data, such as financial systems, medical records, and inventory management systems.

There are two main types of temporal data models: valid-time and transaction-time.

1. **Valid-time** models represent the time period during which a fact is true in the real world. For example, an employee's salary may change over time, and a valid-time model would represent the different salary values and the time periods during which each value was valid.

2. **Transaction-time** models represent the time period during which a fact is stored in the database. This type of model is useful for tracking the history of changes to the data, such as when a record was inserted, updated, or deleted.

In addition to these two types of temporal data models, there are also **bi-temporal** models, which combine both valid-time and transaction-time. These models are useful for applications that require tracking of both the history of changes to the data and the time periods during which the data was valid in the real world.

Temporal data models can be implemented using various techniques, such as timestamping, temporal elements, and temporal databases. These techniques provide different levels of support for temporal data management and querying.

Overall, temporal data models provide a powerful tool for representing and managing data that changes over time, and are widely used in a variety of applications in intelligent database systems.