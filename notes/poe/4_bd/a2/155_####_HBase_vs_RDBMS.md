 Here is the content on #### HBase vs RDBMS in markdown format:

#### HBase vs RDBMS

HBase is a distributed, scalable, big data store based on Google's Bigtable design. It is built on top of Hadoop and runs on top of HDFS. On the other hand, RDBMS refers to the traditional Relational Database Management Systems like MySQL, Oracle, MS SQL Server, etc.

The key differences between HBase and RDBMS are:

- Schema: HBase is a schemaless database while RDBMS has a fixed schema. In HBase, columns can be added dynamically.
- Scalability: HBase is highly scalable and can hold a large amount of data compared to RDBMS which face scalability issues with growing data volume.
- Data Model: HBase uses a hierarchical data model based on rows and columns while RDBMS uses a tabular data model based on tables, rows, and columns.
- Performance: HBase performs better in case of huge data sets as it can be scaled easily. RDBMS performance degrades with large volumes of data.
- Capacity: HBase has a higher storage capacity compared to RDBMS due to its scalable architecture.
- ACID Compliance: Traditional RDBMS provides ACID compliance (Atomicity, Consistency, Isolation, Durability) while HBase doesn't support full ACID compliance. However, HBase offers atomicity and consistency at a row level.
- Use cases: HBase is best suited for random reads/writes of big data while RDBMS is suitable for structured data and transactions.

Some key points to remember:

- HBase is suited for huge volumes of structured/semi-structured data storage while RDBMS is suited for transaction-oriented applications.
- HBase runs on top of Hadoop while RDBMS is independent of Hadoop.
- HBase scales horizontally by adding more nodes in a cluster while RDBMS scales vertically by increasing resources of a single server.

I have included points, headings and Markdown elements to make the content easy to read and understand. Please let me know if you would like me to elaborate on any specific point or add more details.