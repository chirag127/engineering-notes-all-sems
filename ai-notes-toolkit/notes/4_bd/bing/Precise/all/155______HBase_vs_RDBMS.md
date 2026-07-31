#### HBase vs RDBMS

- **RDBMS** (Relational Database Management System) and **HBase** are both types of database management systems, but they differ in several ways.
- **Data Model**: RDBMS uses a relational data model, where data is stored in tables with predefined columns and rows. HBase, on the other hand, uses a column-family data model, where data is stored in column families, which contain columns and rows. HBase is often referred to as a NoSQL database because of its non-relational data model.
- **Scaling**: RDBMS is more suitable for traditional, transactional applications that require strong consistency, whereas HBase is better suited for big data applications that require horizontal scaling and high-speed processing.
- **Consistency**: HBase provides random access and strong consistency for large amounts of unstructured and semi-structured data in a schemaless database organized by column families.
- **Speed**: HBase works on top of Hadoop Distributed File System (HDFS) and is designed for high-speed processing of large datasets.
- **ACID Compliance**: In HBase, there is no transaction guaranty, whereas RDBMS mostly guarantees transaction integrity.
- **JOINs**: HBase supports JOINs, whereas RDBMS does not support JOINs.