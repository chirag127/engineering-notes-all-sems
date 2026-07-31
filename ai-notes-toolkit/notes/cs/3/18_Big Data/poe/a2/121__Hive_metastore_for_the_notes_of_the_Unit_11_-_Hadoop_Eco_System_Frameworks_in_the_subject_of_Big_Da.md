 Here is the formal content in markdown format without any emojis or external links for the topic "Hive metastore for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data":

### Hive metastore

- Hive metastore is a database that stores metadata or data about data. It stores information about the tables, partitions, databases in Hive and their schemas.
- This metastore is used by Hive to get metadata/information about the tables/databases/partitions in order to perform queries, create tables etc.
- The metastore can be an external database (RDBMS) or an internal Derby database (by default). Using an external database has more advantages like higher concurrency, better performance, and data persistency even after Hive service restarts.
- The information stored in the metastore includes:
-- Table names, column names and types
-- Table properties like storage handler, input/output formats
-- Partition keys and values if the table is partitioned
-- Table location (HDFS directory)
- Hence, metastore acts as a centralized repository of metadata which is used by Hive to get schema information and perform various operations on Hive tables, partitions and databases.

The content is written in points in a formal manner without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or add any other points to the content.