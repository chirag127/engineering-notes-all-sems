#### Hive shell

- Hive shell is a command-line interface that allows users to interact with Hive and execute HiveQL commands.
- Hive shell can be launched by typing `hive` in the terminal. It will display a prompt `hive>` where users can enter HiveQL commands.
- Hive shell supports various options and commands to configure and control the Hive session. Some of the common options and commands are:

  - `-e "command"`: Executes the command and prints the output to the standard output.
  - `-f filename`: Executes the commands in the file and prints the output to the standard output.
  - `-h`: Prints the help message and exits.
  - `-i filename`: Executes the commands in the file before entering the interactive shell.
  - `-S`: Runs the shell in silent mode, which suppresses the progress and log information.
  - `-v`: Runs the shell in verbose mode, which prints the Hive log information to the standard error.
  - `!command`: Executes a shell command from the Hive shell.
  - `dfs command`: Executes a Hadoop file system command from the Hive shell.
  - `set name=value`: Sets a Hive configuration variable or property.
  - `source filename`: Executes the HiveQL commands in the file from the Hive shell.

- Hive shell supports various HiveQL commands to create, manage, and query tables and databases. Some of the common HiveQL commands are:

  - `CREATE DATABASE name`: Creates a new database with the given name.
  - `SHOW DATABASES`: Lists all the databases in Hive.
  - `USE name`: Sets the current database to the given name.
  - `DROP DATABASE name`: Drops the database with the given name and deletes its contents.
  - `CREATE TABLE name (column1 type1, column2 type2, ...)`: Creates a new table with the given name and columns.
  - `SHOW TABLES`: Lists all the tables in the current database.
  - `DESCRIBE name`: Shows the schema and properties of the table with the given name.
  - `DROP TABLE name`: Drops the table with the given name and deletes its contents.
  - `LOAD DATA [LOCAL] INPATH 'path' [OVERWRITE] INTO TABLE name`: Loads data from a file or directory into a table.
  - `SELECT expression [AS alias], ... FROM table [WHERE condition] [GROUP BY expression] [HAVING condition] [ORDER BY expression] [LIMIT number]`: Executes a query on a table and returns the result.
  - `INSERT INTO|OVERWRITE TABLE name SELECT expression, ... FROM table [WHERE condition] [GROUP BY expression] [HAVING condition] [ORDER BY expression]`: Executes a query on a table and inserts or overwrites the result into another table.
  - `ALTER TABLE name RENAME TO new_name`: Renames a table to a new name.
  - `ALTER TABLE name ADD|REPLACE COLUMNS (column1 type1, column2 type2, ...)`: Adds or replaces columns in a table.
  - `ALTER TABLE name CHANGE column old_type new_type`: Changes the type of a column in a table.
  - `ALTER TABLE name SET TBLPROPERTIES (property1 = value1, property2 = value2, ...)`: Sets the table properties in a table.

- Hive shell supports various built-in functions and operators to perform calculations and transformations on the data. Some of the common functions and operators are:

  - Arithmetic operators: `+`, `-`, `*`, `/`, `%`
  - Comparison operators: `=`, `<>`, `<`, `>`, `<=`, `>=`
  - Logical operators: `AND`, `OR`, `NOT`
  - String functions: `concat`, `length`, `lower`, `upper`, `trim`, `substr`, `regexp_replace`, `regexp_extract`, etc.
  - Mathematical functions: `abs`, `ceil`, `floor`, `round`, `sqrt`, `pow`, `log`, `exp`, `sin`, `cos`, `tan`, etc.
  - Date and time functions: `current_date`, `current_timestamp`, `date_add`, `date_sub`, `datediff`, `date_format`, `from_unixtime`, `to_date`, `unix_timestamp`, etc.
  - Aggregate functions: `count`, `sum`, `avg`, `min`, `max`, `stddev`, `variance`, etc.
  - Window functions: `row_number`, `rank`, `dense_rank`, `percent_rank`, `cume_dist`, `lag`, `lead`, `first_value`, `last_value`, etc.
  - Analytical functions: `corr`, `covar_pop`, `covar_samp`, `re