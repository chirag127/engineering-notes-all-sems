#### HBase vs RDBMS

- HBase and RDBMS are both types of database management systems, but they differ in several ways.
- RDBMS stands for Relational Database Management System, and it uses a relational data model, where data is stored in tables with predefined columns and rows. HBase stands for Hadoop Database, and it uses a column-family data model, where data is stored in column families, which contain columns and rows. HBase is often referred to as a NoSQL database because of its non-relational data model .
- RDBMS is more suitable for traditional, transactional applications that require strong consistency, ACID compliance, and structured data. HBase is better suited for big data applications that require horizontal scaling, high-speed processing, and semi-structured or unstructured data .
- Some of the main differences between HBase and RDBMS are:

| Feature | HBase | RDBMS |
|---------|-------|-------|
| Data model | Column-family | Relational |
| Schema | Schemaless | Fixed |
| Data size | Petabytes | Gigabytes or terabytes |
| Scalability | Horizontal | Vertical |
| Consistency | Eventual | Strong |
| Speed | Fast reads and writes | Fast reads and slow writes |
| ACID compliance | Partial | Full |
| Transactions | Single-row | Multi-row |
| Joins | Not supported | Supported |
| Referential integrity | Not enforced | Enforced |
| Indexing | Built-in | Optional |
| Query language | HBase shell, Java API, REST API, or MapReduce | SQL |

: https://www.geeksforgeeks.org/difference-between-rdbms-and-hbase/
: https://mindmajix.com/hadoop/difference-between-hbase-rdbms
: https://data-flair.training/blogs/hbase-vs-rdbms/