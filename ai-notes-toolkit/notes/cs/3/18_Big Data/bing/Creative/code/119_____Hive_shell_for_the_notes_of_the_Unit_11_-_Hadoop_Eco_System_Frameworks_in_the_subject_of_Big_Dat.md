### Hive shell

Hive shell is a command-line interface that allows users to interact with Hive and execute Hive queries. Hive shell can be used in either interactive or batch mode. Some of the features and benefits of Hive shell are:

- It supports HiveQL, which is a SQL-like language for querying and analyzing data stored in Hadoop.
- It allows users to create, drop, alter, and query tables and partitions in Hive.
- It supports various built-in functions and operators for data manipulation and aggregation.
- It allows users to set variables and parameters for customizing the Hive configuration and behavior.
- It provides access to Hive metastore, which stores the metadata of tables, partitions, columns, and schemas.
- It supports multiple output formats, such as text, CSV, JSON, and XML.
- It can be integrated with other tools and frameworks, such as Spark, MapReduce, and Tez.

Some of the basic commands and syntax of Hive shell are:

- To launch Hive shell, use the command `$HIVE_HOME/bin/hive` .
- To exit Hive shell, use the command `quit` or `exit`.
- To run a Hive query, type the query and end it with a semicolon (;).
- To run a Hive script, use the command `source <script_file>` or `hive -f <script_file>` .
- To set a variable or parameter, use the command `set <key>=<value>` or `set hivevar:<key>=<value>`.
- To display the value of a variable or parameter, use the command `set <key>` or `set hivevar:<key>`.
- To list all the variables or parameters, use the command `set` or `set -v`.
- To create a table, use the command `CREATE TABLE <table_name> (<column_name> <data_type>, ...) [PARTITIONED BY (<partition_column> <data_type>, ...)] [ROW FORMAT <row_format>] [STORED AS <file_format>] [LOCATION <hdfs_path>] [TBLPROPERTIES (<property_key>=<property_value>, ...)]`.
- To drop a table, use the command `DROP TABLE [IF EXISTS] <table_name>`.
- To alter a table, use the command `ALTER TABLE <table_name> <alter_option>`. Some of the alter options are:

  - RENAME TO <new_table_name>
  - ADD COLUMNS (<column_name> <data_type>, ...)
  - CHANGE COLUMN <column_name> <new_column_name> <new_data_type>
  - ADD PARTITION (<partition_column>=<partition_value>, ...)
  - DROP PARTITION (<partition_column>=<partition_value>, ...)
  - SET TBLPROPERTIES (<property_key>=<property_value>, ...)
  - SET LOCATION <hdfs_path>

- To query a table, use the command `SELECT <columns> FROM <table_name> [WHERE <condition>] [GROUP BY <columns>] [HAVING <condition>] [ORDER BY <columns>] [LIMIT <number>]`.
- To join two or more tables, use the command `SELECT <columns> FROM <table_name_1> <join_type> <table_name_2> ON <join_condition> [WHERE <condition>] [GROUP BY <columns>] [HAVING <condition>] [ORDER BY <columns>] [LIMIT <number>]`. Some of the join types are:

  - INNER JOIN
  - LEFT OUTER JOIN
  - RIGHT OUTER JOIN
  - FULL OUTER JOIN
  - CROSS JOIN

- To use a built-in function or operator, use the syntax `<function_name>(<arguments>)` or `<operand_1> <operator> <operand_2>`. Some of the built-in functions and operators are:

  - Mathematical functions: +, -, *, /, %, abs, ceil, floor, round, sqrt, pow, log, sin, cos, tan, etc.
  - String functions: concat, length, lower, upper, trim, ltrim, rtrim, substr, split, regexp_replace, regexp_extract, etc.
  - Date functions: current_date, current_timestamp, date_add, date_sub, datediff, date_format, from_unixtime, to_date, unix_timestamp, etc.
  - Collection functions: array, map, struct, size, explode, posexplode, etc.
  - Conditional functions: if, case, when,