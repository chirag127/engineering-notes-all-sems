 Here is the content in markdown format for the topic #### comparison of Hive with traditional databases:

#### Comparison of Hive with traditional databases

Hive is a data warehouse system built on top of Hadoop for providing data summarization, query, and analysis. Some key differences between Hive and traditional RDBMS are:

- **Schema on read**: Hive does not require a schema definition before loading data. The schema is inferred from the input data at the time of reading. This makes it easy to work with changing or unpredictable schema. Traditional databases require schema definition before loading data.
- **Scale out architecture**: Hive scales out to large clusters via partitioning of data and parallel processing. This allows it to handle huge volumes of data. Traditional databases are scaled up by increasing the resources of a single server.
- **Latency vs Throughput tradeoff**: Hive focuses on throughput and scalability and hence has higher latency for queries. Traditional databases focus on low latency and have good response times but lower throughput.
- **Not suitable for OLTP**: Hive is suitable for OLAP use cases involving large volumes of data and complex queries. It is not suitable for OLTP use cases requiring fast response times and frequent Updates/Inserts/Deletes. Traditional databases handle OLTP workloads well.

Some mnemonics to remember:

- Hive is High on Volume, Low on Velocity
- Hive is for OLAP, not OLTP
- Schema on read vs Schema on write

The scale out architecture, huge data volumes handling capability and schema on read feature makes Hive suitable for data warehousing and analytics on huge data sets. However, the higher latency and unsuitability for OLTP makes it not fit for transactional use cases. Based on your use case, you can choose between Hive and a traditional RDBMS.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.