#### Data Processing Operators in Pig

- Data processing operators are the main tools that Pig Latin provides to operate on the data. They allow you to transform it by sorting, grouping, joining, projecting, and filtering.
- A data processing operator takes a relation as input and produces another relation as output .
- There are different types of data processing operators in Pig, such as:
  - Relational operators: These operators perform basic operations on relations, such as loading, storing, filtering, grouping, joining, etc. Examples are LOAD, STORE, FILTER, GROUP, JOIN, etc .
  - Evaluation operators: These operators perform various calculations on the data, such as arithmetic, string, date, etc. Examples are +, -, *, /, CONCAT, SUBSTRING, ToDate, etc.
  - Diagnostic operators: These operators help in debugging and testing the Pig scripts, such as printing the schema, the data, or the execution plan. Examples are DESCRIBE, DUMP, EXPLAIN, etc.
  - Miscellaneous operators: These operators perform some special functions, such as splitting the data into multiple relations, ordering the data, limiting the number of tuples, etc. Examples are SPLIT, ORDER BY, LIMIT, etc.