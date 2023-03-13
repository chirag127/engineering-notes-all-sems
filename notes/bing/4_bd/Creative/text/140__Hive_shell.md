#### Hive shell

- Hive shell is a command-line interface that allows users to interact with Hive and run Hive queries.
- Hive shell can be launched by typing `hive` in the terminal or by specifying a script file with the `-f` option.
- Hive shell supports various options and commands to configure and control the execution of Hive queries. For example, `-e` option can be used to execute a single query, `-v` option can be used to enable verbose mode, and `set` command can be used to change Hive configuration variables.
- Hive shell also supports some built-in functions and operators to manipulate data and expressions. For example, `concat` function can be used to concatenate strings, `+` operator can be used to add numbers, and `substr` function can be used to extract a substring.
- Hive shell can be used to create, alter, and drop tables, partitions, and views, as well as to load, insert, and query data. Hive shell supports both HiveQL and SQL syntax for most of the operations.
- Hive shell can be connected to different Hive servers, such as HiveServer2 or HiveServer1, by specifying the `-h` or `--hiveconf` options. HiveServer2 is the preferred server as it offers more features and security than HiveServer1.
- Hive shell can also be accessed remotely using SSH clients or Hive Shell service. Hive Shell service is a feature of Hiveon OS that provides remote access to workers using the Hiveon OS network infrastructure. Hive Shell service also allows console sharing and session management.