### Candidate Key

- A candidate key is a minimal set of attributes that can uniquely identify each tuple in a relation.
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key.
- A candidate key must satisfy two properties: uniqueness and minimality.
- Uniqueness means that no two tuples in the relation can have the same values for the attributes of the candidate key.
- Minimality means that no proper subset of the candidate key can also uniquely identify each tuple in the relation.
- For example, consider the following relation STUDENT with attributes RollNo, Name, and Email.

| RollNo | Name | Email |
| ------ | ---- | ----- |
| 101 | Alice | alice@example.com |
| 102 | Bob | bob@example.com |
| 103 | Charlie | charlie@example.com |

- In this relation, RollNo, Name, and Email are all candidate keys, as they can uniquely identify each tuple.
- However, only one of them can be chosen as the primary key, say RollNo.
- The other candidate keys are called alternate keys.