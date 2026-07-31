### Candidate Key

- A candidate key is a set of attributes that can uniquely identify each tuple (row) in a relation (table) of a database .
- A candidate key is also a minimal superkey, which means that it has no redundant attributes and that removing any attribute would make it lose the uniqueness property .
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier of the relation .
- The other candidate keys that are not chosen as the primary key are called alternate keys or secondary keys.
- A candidate key can be a single attribute or a combination of attributes, depending on the data requirements and constraints.
- For example, in a relation STUDENT with attributes STUDENT_ID, NAME, EMAIL, and PHONE, the possible candidate keys are:

  - STUDENT_ID
  - EMAIL
  - PHONE
  - STUDENT_ID, NAME
  - STUDENT_ID, EMAIL
  - STUDENT_ID, PHONE
  - EMAIL, NAME
  - EMAIL, PHONE
  - PHONE, NAME

- In this case, STUDENT_ID is the most likely choice for the primary key, as it is the simplest and most efficient way to identify each student. The other candidate keys are alternate keys. Note that NAME is not a candidate key by itself, as it may not be unique for all students.