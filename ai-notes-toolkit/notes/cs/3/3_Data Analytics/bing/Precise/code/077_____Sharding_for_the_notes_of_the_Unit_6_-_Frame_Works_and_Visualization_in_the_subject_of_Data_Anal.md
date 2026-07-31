### Sharding

Sharding is a type of database partitioning that separates large databases into smaller, faster, more easily managed parts called data shards . It involves splitting and distributing one logical data set across multiple databases that share nothing and can be deployed across multiple servers . To achieve sharding, the rows or columns of a larger database table are split into multiple smaller tables. Once a logical shard is stored on another node, it is known as a physical shard .

#### Advantages of Sharding
- Increased read/write throughput: By distributing the dataset across multiple shards, both read and write operations can be performed faster .
- Increased storage capacity: By increasing the number of shards, you can also increase overall total storage capacity .
- High availability: Shards can provide high availability .

#### Applications of Sharding
- Big Data Analytics: When you have terabytes of data, sharding means you don't have to warehouse data to do analytics on it. With up to 1000 shards in capacity, Oracle Sharding can turn a relational database into a warehouse-sized data store .
- Event Stream Processing, Internet of Things, Log Analytics, metric store, and time series data: Oracle Sharding can be used for these applications, eliminating the need for a separate data pipeline .