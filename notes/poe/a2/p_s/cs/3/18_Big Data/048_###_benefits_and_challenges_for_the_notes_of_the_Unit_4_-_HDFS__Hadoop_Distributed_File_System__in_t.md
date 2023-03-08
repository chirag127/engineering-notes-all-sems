 Here is the content in markdown format for the given topic:

#### Comparison of Pig with Databases

Pig is a data flow language and execution framework for parallel computation while databases are data storage and management systems. Though Pig can be used with databases, the major differences are:

1. Pig is a programming language while databases use SQL query language. Pig Latin scripts are written to process and analyze data using Pig's operators and functions.
2. Pig is suitable for intensive data processing tasks and complex data analysis while databases are optimized for storing and retrieving data. Pig is thus more suitable for ETL and machine learning use cases.
3. Pig works on top of a cluster computing framework like Hadoop and processes data in parallel while databases are single server systems. This makes Pig suitable for big data processing.
4. In Pig, the intermediate data is stored as files in the HDFS while in databases, the data is stored in tables. The default storage in Pig is unstructured while databases store data in structured format.
5. Pig integrates with databases like MySQL to read and write data. However, for intensive processing, it is more efficient to load the data into Pig for analysis instead of running complex queries on the database.

Some key advantages of Pig over databases are:

- Scalability: Pig can handle large data volumes using parallel processing on clusters.
- Flexibility: Pig can work with various data formats and schemas. It provides a high-level language with extensive library of functions.
- Low cost: Pig uses a shared nothing architecture and commodity hardware resulting in lower costs.

However, some limitations of Pig compared to databases are:

- Less efficiency for low-latency queries: Databases are optimized for fast queries while Pig has higher latency.
- Limited GUI tools: Pig has limited GUI tools and the programming complexity is higher than SQL.
- Learning curve: The Pig Latin language has a learning curve for users familiar with SQL.

In summary, Pig and databases are both useful but suited for different use cases. The choice between Pig and databases depends on the specific data processing requirements and complexity. For big data analytics, Pig could be used along with or as an alternative to databases.