Data Processing Operators in Pig are the operators that take a relation as input and produce another relation as output. They allow you to transform the data by sorting, grouping, joining, projecting, and filtering. Some of the common data processing operators in Pig are:

- LOAD: This operator loads the data from the file system or other sources into a relation.
- STORE: This operator stores the data from a relation into the file system or other destinations.
- FILTER: This operator selects the tuples from a relation that satisfy a given condition.
- FOREACH: This operator applies a set of expressions to every tuple in a relation and generates a new relation.
- GROUP: This operator groups the tuples in a relation by one or more fields.
- JOIN: This operator joins two or more relations by a common field or a condition.
- COGROUP: This operator groups the tuples in two or more relations by a common field and creates a nested relation for each group.
- ORDER: This operator sorts the tuples in a relation by one or more fields in ascending or descending order.
- DISTINCT: This operator removes the duplicate tuples from a relation.
- LIMIT: This operator limits the number of tuples in a relation to a specified value.
- UNION: This operator combines two or more relations into a single relation.
- SPLIT: This operator splits a relation into two or more relations based on a condition or a percentage.
- SAMPLE: This operator randomly selects a fraction of tuples from a relation.

The following diagram illustrates the basic architecture of a data processing operator in Pig:

```
+-----------------+     +-----------------+     +-----------------+
| Input Relation  |     | Operator Logic  |     | Output Relation |
+-----------------+     +-----------------+     +-----------------+
| Tuple 1         |     |                 |     | Tuple 1'        |
| Tuple 2         | --> |                 | --> | Tuple 2'        |
| Tuple 3         |     |                 |     | Tuple 3'        |
| ...             |     |                 |     | ...             |
| Tuple N         |     |                 |     | Tuple N'        |
+-----------------+     +-----------------+     +-----------------+
```