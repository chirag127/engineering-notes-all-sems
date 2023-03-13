Hive services are the components that perform client interactions with Hive. They include the following:

- Hive CLI: A command-line interface that allows users to submit Hive queries and commands.
- HiveServer2: A service that provides a JDBC/ODBC server and a Thrift server for remote clients to access Hive.
- Beeline: A command shell that connects to HiveServer2 and allows users to submit queries and commands using HiveQL.
- WebHCat: A REST API service that provides metadata and job execution access to Hive, Pig, and MapReduce.
- Metastore: A service that stores the metadata of Hive tables, partitions, columns, etc. in a relational database.
- HCatalog: A service that provides a table abstraction layer for data stored in HDFS and other storage systems.

The following diagram illustrates the basic architecture of Hive services using ASCII characters:

```
+-----------------+   +-----------------+   +-----------------+
|    Client       |   |    Client       |   |    Client       |
+-----------------+   +-----------------+   +-----------------+
| Hive CLI/Beeline|   | JDBC/ODBC       |   | WebHCat         |
+-----------------+   +-----------------+   +-----------------+
         |                    |                    |
         |                    |                    |
         +--------------------+--------------------+
                            |
                            |
                            v
                    +-----------------+
                    |  HiveServer2    |
                    +-----------------+
                            |
                            |
                            v
                    +-----------------+
                    |  Metastore      |
                    +-----------------+
                            |
                            |
                            v
                    +-----------------+
                    |  RDBMS          |
                    +-----------------+
                            |
                            |
                            v
                    +-----------------+
                    |  HCatalog       |
                    +-----------------+
                            |
                            |
                            v
                    +-----------------+
                    |  HDFS           |
                    +-----------------+
```