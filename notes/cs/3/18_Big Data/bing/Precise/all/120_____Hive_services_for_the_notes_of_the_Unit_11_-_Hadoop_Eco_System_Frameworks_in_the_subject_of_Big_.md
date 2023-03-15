# Hive Services

Hive is a data warehousing and SQL-like query language for Hadoop. It provides a mechanism to project structure onto the data in Hadoop and to query that data using a SQL-like language called HiveQL. Hive services perform client interactions with Hive. For example, if a client wants to perform a query, it must talk with Hive services.

Hive services such as the Meta store, File system, and Job Client in turn communicate with Hive storage and perform the following actions:
- Metadata information of tables created in Hive is stored in Hive “Meta storage database”.
- Query results and data loaded in the tables are going to be stored in the Hadoop cluster on HDFS.

Hive provides numerous services, including the Hive server2, Beeline, etc. The services offered by Hive are:
- Beeline: HiveServer2 supports the Beeline, a command shell that which the user can submit commands and queries to.