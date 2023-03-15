### Hive Services

Hive services are responsible for performing client interactions with Hive. For example, if a client wants to perform a query, it must talk with Hive services . Some of the services offered by Hive include:

1. **Meta store**: Metadata information of tables created in Hive is stored in Hive “Meta storage database” .
2. **File system**: Query results and data loaded in the tables are going to be stored in Hadoop cluster on HDFS .
3. **Job Client**: Communicates with Hive storage and performs actions .
4. **HiveServer2**: Supports the Beeline, a command shell that which the user can submit commands and queries to .
5. **Beeline**: A command shell that which the user can submit commands and queries to .
