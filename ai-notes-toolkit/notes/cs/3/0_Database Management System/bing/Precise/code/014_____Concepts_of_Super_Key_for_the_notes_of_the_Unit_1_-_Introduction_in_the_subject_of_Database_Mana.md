### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **super key** is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple (row) in a relation (table).
- A super key can contain **extraneous attributes**, meaning attributes that are not necessary for unique identification.
- A **candidate key** is a minimal super key, meaning it is a super key without any extraneous attributes.
- A relation can have **multiple candidate keys**.
- One of the candidate keys is chosen as the **primary key**. The primary key is used to uniquely identify a tuple in the relation.
- The **primary key** is used to establish relationships between relations in a database.
- A **foreign key** is a set of attributes in a relation that refers to the primary key of another relation. The relation containing the foreign key is said to be the **referencing relation**, and the relation referred to by the foreign key is the **referenced relation**.
- The **referential integrity constraint** states that the values of the foreign key must either match the values of the primary key in the referenced relation or be null.
- A **super key** is not necessarily a **candidate key** or a **primary key**, but a **candidate key** and a **primary key** are always **super keys**.