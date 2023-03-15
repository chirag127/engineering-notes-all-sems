### Hive Services

Hive services are responsible for client interactions with Hive. For example, if a client wants to perform a query, it must talk with Hive services. Hive provides numerous services, including the Hive server2, Beeline, etc.

- **Meta store**: Metadata information of tables created in Hive is stored in Hive “Meta storage database”.
- **File system**: Query results and data loaded in the tables are going to be stored in Hadoop cluster on HDFS.
- **Job Client**: Hive services such as file system, job client, and meta store then communicates with Hive storage and stores things like metadata table information and query results.
- **Beeline**: HiveServer2 supports the Beeline, a command shell that which the user can submit commands and queries to.