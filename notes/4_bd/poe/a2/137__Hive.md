 Here is the formal write-up on Hive in markdown format without any emojis or external links:

### Hive

1. Hive is a data warehouse system built on top of Hadoop. It provides a mechanism to project structure onto data within Hadoop and query the data using a SQL-like language called HiveQL.
2. Hive converts SQL queries into MapReduce jobs which are executed on Hadoop. This allows users familiar with SQL to query and manage large datasets residing in Hadoop clusters.
3. The metastore is a central repository of Hive metadata. It stores information about the tables, partitions and schemas in the warehouse. By default, Hive stores metadata in an embedded Derby database, but it also supports MySQL and PostgreSQL.
4. Hive partitions data using partitions. Partitions are helpful to prune data. For example, if we are interested only in data of a particular month, Hive can skip reading data of other months if we have partitioned data by month.
5. Hive supports user-defined functions (UDFs) and user-defined aggregate functions (UDAFs). This allows programmers to extend the functionality of Hive to suit their custom requirements.
6. Hive's language (HiveQL) is quite similar to SQL but with some differences. For example, HiveQL supports CREATE TABLE AS SELECT (CTAS), INSERT INTO, and JOINs, but not triggers, stored procedures, and views.
7. Hive on Tez provides significant performance improvements over MapReduce. Tez is an extensible framework that allows Hive to execute tasks more efficiently than MapReduce. It supports DAG (Directed Acyclic Graph) of tasks, in-memory processing, and reuse of intermediate data.