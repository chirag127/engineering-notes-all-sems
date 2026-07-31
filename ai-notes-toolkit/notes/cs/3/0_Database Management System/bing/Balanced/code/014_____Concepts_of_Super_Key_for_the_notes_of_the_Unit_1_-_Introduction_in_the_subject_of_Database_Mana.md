Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System. Here is the content I have written for you in markdown format:

### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- For example, in a relation STUDENT with attributes ROLL_NO, NAME, AGE, and ADDRESS, the set {ROLL_NO, NAME} is a super key, since no two students can have the same roll number and name. However, the attribute NAME is not required for unique identification, as ROLL_NO alone can also serve as a key.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple in a relation.
- A candidate key is also a super key, but not every super key is a candidate key.
- For example, in the relation STUDENT, the set {ROLL_NO} is a candidate key as well as a super key, but the set {ROLL_NO, NAME, AGE} is only a super key and not a candidate key, as it contains extra attributes.
- A candidate key can be chosen as a primary key, which is a special key that is used to identify tuples in a relation and enforce referential integrity constraints in a database.
- A primary key is also a candidate key and a super key, but not every candidate key or super key is a primary key.
- For example, in the relation STUDENT, the attribute ROLL_NO can be chosen as a primary key, but the attribute NAME cannot be chosen as a primary key, even though it is a part of a super key.