#### Apache Hive architecture

Apache Hive is a distributed, fault-tolerant data warehouse system that enables analytics at a massive scale. It is an open-source data warehousing tool for performing distributed processing and data analysis. It was developed by Facebook to reduce the work of writing the Java MapReduce program. Apache Hive uses a Hive Query language, which is a declarative language similar to SQL.

The major components of Apache Hive are:
- **Hive clients**
- **Hive services**
- **Processing framework and Resource Management**
- **Distributed Storage**

The key components of the Apache Hive architecture are:
- **Hive Server 2**: The Hive Server 2 accepts incoming requests from users and applications and creates an execution plan and auto generates a YARN job to process SQL queries.
- **Hive Query Language (HQL)**: A declarative language similar to SQL.
- **External Apache Hive Metastore**: Hive Metastore (HMS) provides a central repository of metadata that can easily be analyzed to make informed, data driven decisions, and therefore it is a critical component of many data lake architectures.
- **Hive Beeline Shell**: A command line shell for interacting with Hive.