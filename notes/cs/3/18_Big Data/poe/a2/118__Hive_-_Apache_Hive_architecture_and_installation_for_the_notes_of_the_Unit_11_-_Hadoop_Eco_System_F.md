 Here is the content in Markdown format with points and without emojis or external links as per your instructions:

### Hive - Apache Hive architecture and installation for the notes of the Unit 11 - Hadoop Eco System Frameworks in the subject of Big Data

1. Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis.
2. Hive architecture consists of three main components:

- Hive Metastore: It is a relational database that stores metadata such as database schemas, table definitions, and partitioning information.
- Hive Query Compiler: It converts HiveQL queries into MapReduce jobs which are executed on Hadoop.
- Hive Server: It receives queries from applications via the Thrift or JDBC/ODBC protocol and interacts with the Hive Metastore and Query Compiler.

3. The main advantages of Hive are:

- It provides an SQL-like language called HiveQL to query data stored in Hadoop.
- It enables interaction with Hadoop via JDBC/ODBC which provides compatibility with existing tools.
- It abstracts complexity of MapReduce and provides an easy to use interface for users to query and analyze data.

4. To install Hive, we need to:

- Install Hadoop as Hive runs on top of Hadoop.
- Download the Hive binaries and decompress the installation file.
- Set HIVE_HOME to point to the installation directory.
- Add $HIVE_HOME/bin to the PATH.
- Configure Hive metastore by initializing the schema by executing the command `schematool -dbType derby -initSchema`.
- Start Hive by executing `hive` in the terminal.