 Here is the content in markdown format for the topic #### HBase clients:

#### HBase clients

HBase provides client APIs to communicate with HBase tables and perform operations like CRUD (Create, Read, Update, Delete). The main HBase clients are:

1. HTable - The primary HBase client which provides methods to perform basic operations like get, put, delete, etc. on a table. It is a low-level client.
Some key points to remember:
- HTable can be used to access only one table at a time.
- HTable is deprecated and HTablePool should be used instead which maintains a pool of HTable objects to access multiple tables.

2. HBaseAdmin - Used to perform administrative operations on HBase like creating, deleting tables, disabling/enabling tables, adding/removing column families, etc.
Some key points to remember:
- HBaseAdmin can be used to perform operations on multiple tables.
- HBaseAdmin is thread-safe.

3. HBaseConfiguration - Used to set configuration parameters for HBase. It extends from Configuration class of Hadoop and is used to set HBase-specific configurations.
Some key points to remember:
- HBaseConfiguration can be configured programmatically or using an XML configuration file (hbase-site.xml).
- HBaseConfiguration is used while creating HTable and HBaseAdmin objects to pass the configuration details.

4. HTableInterface / Table - The main interface implemented by HTable to perform operations on a table. HTable is deprecated and Table (introduced in HBase 0.96) should be used.
Some advantages of Table over HTable:
- Table is type-safe.
- Table provides better concurrency and performance.
- Table provides asynchronous methods to perform operations asynchronously.

Overall, for exams, remember:
- Know the uses of each client - HTable (low-level), HBaseAdmin (admin), HBaseConfiguration (configuration), TableInterface / Table (main interface)
- Know the key points to remember for each client
- Know the advantages of Table over deprecated HTable
- Be familiar with the CRUD operations, admin operations, and configuration settings that can be done using the HBase clients.