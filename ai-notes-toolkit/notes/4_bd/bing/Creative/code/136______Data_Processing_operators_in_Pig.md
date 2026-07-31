#### Data Processing operators in Pig

- Pig is a high-level scripting language that allows users to perform data analysis on large-scale data sets using a set of operators.
- Pig operators are classified into four categories: load/store operators, relational operators, evaluation operators, and diagnostic operators.
- Load/store operators are used to read data from and write data to external sources, such as files, databases, or Hadoop Distributed File System (HDFS).
- Relational operators are used to perform common data manipulation tasks, such as filtering, grouping, joining, sorting, and projecting data.
- Evaluation operators are used to compute values from data, such as arithmetic expressions, string functions, user-defined functions (UDFs), and casting operators.
- Diagnostic operators are used to debug and test Pig scripts, such as displaying the schema, sample data, or execution plan of a relation.

- Some examples of Pig operators are:

  - LOAD: reads data from an external source and creates a relation.
  - STORE: writes data from a relation to an external source.
  - FILTER: selects tuples from a relation that satisfy a given condition.
  - FOREACH: applies a transformation to each tuple in a relation and generates a new relation.
  - GROUP: groups tuples in a relation by one or more fields and creates a nested relation.
  - JOIN: combines two or more relations by matching tuples on common fields.
  - ORDER: sorts tuples in a relation by one or more fields in ascending or descending order.
  - LIMIT: limits the number of tuples in a relation to a specified value.
  - DUMP: displays the contents of a relation on the screen.
  - DESCRIBE: displays the schema of a relation on the screen.
  - EXPLAIN: displays the execution plan of a relation on the screen.
  - ILLUSTRATE: displays a sample of input and output data for each operator in a relation on the screen.