 Here is the content in markdown format for Hive shell:

#### Hive shell

The Hive shell is an interactive command line interface for Hive. It allows you to execute Hive queries, view query results, and also provides Hive shell specific commands for controlling the Hive session.

Some key points about Hive shell:

- It is invoked using the `hive` command.
- It has a REPL (Read-Eval-Print Loop) interface where it waits for user input, evaluates the query, prints the results, and then waits for the next query.
- It supports HiveQL queries with various clauses like SELECT, FROM, WHERE, GROUP BY, etc.
- It supports Hive specific commands starting with `!` for controlling the Hive session like `!quit` to exit, `!help` to display help, etc.
- It displays results in a tabular form and also provides options to customize the output format, change the number of rows displayed, etc.
- It can be used for interactive data exploration and learning Hive.
- Some useful mnemonics to remember Hive shell commands:
    - !h - Display help
    - !q - Quit the shell
    - !s - Display the status of the Hive session
    - SET and RESET - Used to change Hive session variables

Here are some examples of using the Hive shell:

```
hive> SELECT * FROM employees;

hive> CREATE TABLE IF NOT EXISTS students (name STRING, age INT);

hive> !help

hive> SET mapred.reduce.tasks = 10;
```

The Hive shell provides a simple way to get started with Hive and explore data using HiveQL. It is easy to use and can be helpful for learning and understanding Hive queries. However, for production use cases, it is better to use the Beeline client or Hadoop ecosystem tools which provide more robust and scalable options to interact with Hive.