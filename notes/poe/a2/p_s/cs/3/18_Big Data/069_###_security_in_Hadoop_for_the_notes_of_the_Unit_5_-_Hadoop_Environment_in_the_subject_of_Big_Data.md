 Here is the content in markdown format for the given topic:

#### Comparison of Hive with traditional databases

1. Hive is a data warehouse system built on top of Hadoop, whereas traditional databases like MySQL, Oracle, etc. are independent systems.
2. Hive queries are translated into MapReduce jobs which are executed on Hadoop, whereas traditional databases have their own execution engines.
3. Hive is scalable and can handle huge volumes of data as it works on top of the distributed Hadoop framework. Traditional databases have limitations on the maximum amount of data they can store and process.
4. Hive queries can take minutes or even hours to execute as they involve executing MapReduce jobs on the huge data in Hadoop. Queries on traditional databases execute in seconds/milliseconds.
5. Hive uses a SQL-like language called HiveQL which gets translated to MapReduce jobs, whereas traditional databases use SQL which is directly executed on the data.
6. Hive is suitable for batch processing and ETL (Extract, Transform, Load) kinds of workloads. Traditional databases are suitable for random data access and OLTP (Online Transaction Processing) workloads which require fast query execution times.

To summarize, Hive is a suitable data warehouse system for large-scale data processing in a distributed and scalable environment, whereas traditional databases are suitable for transactional kinds of workloads requiring fast query execution. The choice between Hive and a traditional database depends on the nature of the use case and data characteristics.