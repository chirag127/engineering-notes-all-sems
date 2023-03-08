 Here are the points I would include for the topic ### querying data and user defined functions for the notes of the Unit 11 - Hadoop Eco System:

1. Querying Data in Hadoop
- HDFS: We can query data stored in HDFS using command line tools like hadoop fs shell or hdfs dfs shell commands.
- Hive: We can write SQL like queries to retrieve data from Hive tables/databases. HiveQL is translated to MapReduce/Tez jobs which read data from HDFS.
- Pig: We can write Pig Latin scripts to query and process data. Pig Latin is converted to MapReduce jobs which process data from HDFS.
- Impala: We can use ANSI SQL to query data from HDFS through Impala. Impala translates SQL queries to Impala Daemons which read data from HDFS.

2. User Defined Functions (UDFs)
- To extend the functionality of Hive and Pig beyond the built in functions, we can write our own UDFs (in Java/Python/C++).
- The UDFs are pluggable functions that can be used in HiveQL or Pig Latin statements. They enable us to implement custom processing logic.
- Types of UDFs: UDFs for processing values (scalar), UDFs for processing rows (collapsed), UDFs for processing multiple rows (general).
- Advantages: Code reuse, Complex functions/algorithms, Extensibility. Disadvantages: Can impact performance if not optimized.

[Include detailed notes, diagrams, examples, applications, etc. if required]