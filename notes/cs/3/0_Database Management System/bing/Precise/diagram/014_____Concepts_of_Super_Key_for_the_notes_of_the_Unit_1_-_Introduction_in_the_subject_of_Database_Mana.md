### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **super key** is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple (row) in a relation (table).
- A super key can contain **redundant attributes**, meaning that some of the attributes in the super key may not be necessary to identify a tuple uniquely.
- A **candidate key** is a minimal super key, meaning that it is a super key with no redundant attributes.
- A relation can have **multiple candidate keys**.
- One of the candidate keys is chosen as the **primary key** of the relation.
- The primary key is used to **uniquely identify** each tuple in the relation.
- The primary key is also used to **establish relationships** between relations in a database.
- A **foreign key** is an attribute or a set of attributes in a relation that is used to **establish a link** to the primary key of another relation.
- The foreign key and the primary key must have the **same domain** (data type and constraints).
- The foreign key is used to **enforce referential integrity**, meaning that the value of the foreign key must either be null or match the value of the primary key in the related relation.