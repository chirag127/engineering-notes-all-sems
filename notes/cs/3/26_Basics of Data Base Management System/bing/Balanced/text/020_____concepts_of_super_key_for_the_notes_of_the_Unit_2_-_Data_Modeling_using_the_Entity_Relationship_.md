### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- There can be more than one super key for a table, but only one candidate key .
- A super key can also be NULL, unless the table has a primary key constraint.
- An example of a super key is the combination of student ID and student name in a table of students. This combination can uniquely identify each student, but student ID alone is enough to do so. Therefore, student ID is a candidate key and a subset of the super key .