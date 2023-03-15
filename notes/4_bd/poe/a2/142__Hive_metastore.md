 Here is the content in markdown format with formal tone and without emojis:

#### Hive metastore

- Hive metastore is the central repository of Hive metadata. It stores metadata for Hive tables, partitions, schemas, columns, etc.
- The metastore is used by HiveQL parsers/compilers and Hive servers to get metadata and to update metadata.
- The metastore can be configured to use a built-in Java DB (derby) or an external database like MySQL or PostgreSQL.
- Using an external database has many benefits like better performance, scalability, and easier backup and recovery.
- The metastore tables store information such as table names, column names, data types, partition keys, locations, etc.
- The metastore service runs as a separate process and supports concurrent access from multiple clients.
- The metastore thrift service can be used by applications other than Hive to access the metadata. This enables the metastore to be used as a centralized metadata repository for an organization.

The content is written in points and in a formal tone without any emojis or external links. The formatting is in markdown. Please let me know if you would like me to modify or expand the content.