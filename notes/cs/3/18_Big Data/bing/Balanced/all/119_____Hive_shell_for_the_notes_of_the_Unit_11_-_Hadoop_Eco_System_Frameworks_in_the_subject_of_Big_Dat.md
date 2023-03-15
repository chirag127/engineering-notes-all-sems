# Hive shell

Hive shell is a command-line interface for interacting with Hive, a data warehouse system built on top of Hadoop. Hive shell allows users to execute Hive queries and commands in either interactive or batch mode. Hive shell can also be used to access HiveServer2, a service that provides a JDBC/ODBC interface to Hive.

Some of the features and benefits of using Hive shell are:

- It supports HiveQL, a SQL-like language for querying and analyzing data stored in Hadoop.
- It provides a convenient way to create, alter, and drop tables, partitions, and databases in Hive.
- It allows users to set variables and parameters that can be used in Hive queries and commands.
- It supports various output formats, such as text, CSV, JSON, and XML.
- It can run scripts from local or HDFS files, or from standard input.
- It can connect to multiple Hive servers and switch between them using the !connect command.
- It can use Beeline, a JDBC client based on SQLLine, to access HiveServer2.

Some of the basic commands and syntax of Hive shell are:

- To start Hive shell, run the command `$HIVE_HOME/bin/hive` in a terminal.
- To exit Hive shell, type `quit` or `exit` and press Enter, or press Ctrl+D.
- To run a Hive query, type the query and end it with a semicolon (;). For example, `select * from employees;`
- To run a Hive command, type the command and end it with a semicolon (;). For example, `show tables;`
- To run a script from a local or HDFS file, use the `source` command. For example, `source /path/to/script.hql;`
- To run a script from standard input, use the `-f` option. For example, `hive -f - < /path/to/script.hql`
- To set a variable or parameter, use the `set` command. For example, `set hivevar:tablename=employees;`
- To use a variable or parameter in a query or command, use the `${}` syntax. For example, `select * from ${tablename};`
- To connect to a Hive server, use the `!connect` command. For example, `!connect jdbc:hive2://localhost:10000/default`
- To switch to Beeline mode, use the `!beeline` command. For example, `!beeline`