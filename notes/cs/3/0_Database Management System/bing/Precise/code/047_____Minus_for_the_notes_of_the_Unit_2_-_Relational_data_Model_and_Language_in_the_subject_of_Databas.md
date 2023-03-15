### Minus
Minus is a relational algebra operation that is used to find the difference between two relations. It is also known as the difference operation. The result of the minus operation is a relation that contains all the tuples that are in the first relation but not in the second relation.

Here are some key points to remember about the minus operation:
- The two relations must have the same number of attributes and the attributes must be of the same data type.
- The result of the minus operation will have the same schema as the input relations.
- The order of the relations in the minus operation matters. The result will contain tuples that are in the first relation but not in the second relation.
- Duplicate tuples are automatically eliminated in the result of the minus operation.

Example:
Consider the following two relations R and S:

R:
| A | B |
|---|---|
| 1 | 2 |
| 3 | 4 |
| 5 | 6 |

S:
| A | B |
|---|---|
| 3 | 4 |
| 7 | 8 |

The result of the minus operation R - S is:

| A | B |
|---|---|
| 1 | 2 |
| 5 | 6 |

This is because tuples (1,2) and (5,6) are in relation R but not in relation S. The tuple (3,4) is not included in the result because it is present in both relations.