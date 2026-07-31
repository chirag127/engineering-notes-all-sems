### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **super key** is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple (row) in a relation (table).
- A super key can contain **extraneous attributes**, meaning attributes that are not necessary for unique identification.
- A **candidate key** is a minimal super key, meaning it is a super key without any extraneous attributes.
- A relation can have **multiple candidate keys**.
- One of the candidate keys is chosen as the **primary key**.
- The primary key is used to **uniquely identify** each tuple in the relation.
- The primary key is also used to **establish relationships** between relations in a database.
- All attributes that are not part of the primary key are called **non-prime attributes**.
- A **foreign key** is a set of attributes in a relation that refers to the primary key of another relation.
- The relation that contains the foreign key is called the **referencing relation**, and the relation that is referred to by the foreign key is called the **referenced relation**.
- The foreign key is used to **establish a relationship** between the tuples in the referencing and referenced relations.
- The foreign key must **match the primary key** of the referenced relation in both the number and type of attributes.
- The foreign key can be **null** if the relationship between the tuples in the referencing and referenced relations is **optional**.
- If the relationship between the tuples in the referencing and referenced relations is **mandatory**, the foreign key must **not be null**.
- A **super key** can be used to **enforce constraints** on the data stored in a relation.
- A **unique constraint** can be defined on a super key to ensure that no two tuples in the relation have the same values for the attributes in the super key.
- A **referential integrity constraint** can be defined on a foreign key to ensure that the values in the foreign key match the values in the primary key of the referenced relation.