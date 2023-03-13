Data Processing Operators are the main tools that Pig Latin provides to operate on the data. They allow you to transform the data by sorting, grouping, joining, projecting, and filtering. There are four types of Data Processing Operators in Pig:

- Relational Operators: These operators take one or more relations as input and produce another relation as output. They are used to perform common data operations such as loading, storing, filtering, grouping, joining, etc. Examples of relational operators are LOAD, STORE, FILTER, GROUP, JOIN, etc.
- Evaluation Operators: These operators are used to manipulate or generate values from the input data. They are usually embedded within relational operators. Examples of evaluation operators are arithmetic operators, comparison operators, string operators, etc.
- Diagnostic Operators: These operators are used to display information about the data or the execution of the Pig script. They are useful for debugging and testing purposes. Examples of diagnostic operators are DUMP, DESCRIBE, EXPLAIN, ILLUSTRATE, etc.
- Miscellaneous Operators: These operators are used to perform some additional tasks that are not covered by the other types of operators. Examples of miscellaneous operators are ORDER BY, LIMIT, DISTINCT, UNION, SPLIT, etc.

The following diagram illustrates the basic architecture of a Pig script using Data Processing Operators:

```
+----------------+   +----------------+   +----------------+   +----------------+
|                |   |                |   |                |   |                |
|    Relation    |   |    Relation    |   |    Relation    |   |    Relation    |
|                |   |                |   |                |   |                |
+----------------+   +----------------+   +----------------+   +----------------+
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
+----------------+   +----------------+   +----------------+   +----------------+
|                |   |                |   |                |   |                |
| Relational     |   | Evaluation     |   | Diagnostic     |   | Miscellaneous  |
| Operator       |   | Operator       |   | Operator       |   | Operator       |
|                |   |                |   |                |   |                |
+----------------+   +----------------+   +----------------+   +----------------+
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
       |                    |                    |                    |
+----------------+   +----------------+   +----------------+   +----------------+
|                |   |                |   |                |   |                |
|    Relation    |   |    Relation    |   |    Relation    |   |    Relation    |
|                |   |                |   |                |   |                |
+----------------+   +----------------+   +----------------+   +----------------+
```