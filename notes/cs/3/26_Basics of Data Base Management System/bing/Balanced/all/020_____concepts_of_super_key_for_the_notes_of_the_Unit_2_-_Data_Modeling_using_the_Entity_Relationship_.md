# Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify each record or tuple in a table  .
- A super key may have additional attributes that are not needed for unique identification .
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify each record or tuple in a table .
- There can be more than one super key for a table, but only one candidate key .
- A super key can also be NULL, unless the table has a primary key constraint.
- A super key can be used to enforce referential integrity, which means that the values of a super key in one table must match the values of a corresponding super key in another table.

## Example of Super Key

- Consider a table STUDENT with the following attributes: ID, Name, Age, Address, Phone, Email.
- A possible super key for this table is {ID, Name, Age, Address, Phone, Email}, which contains all the attributes of the table and can uniquely identify each student.
- Another possible super key for this table is {ID, Phone}, which contains only two attributes and can also uniquely identify each student.
- A candidate key for this table is {ID}, which is the minimal set of attributes that can uniquely identify each student.
- A primary key for this table can be {ID}, which is a candidate key that is chosen to be the main identifier for the table.