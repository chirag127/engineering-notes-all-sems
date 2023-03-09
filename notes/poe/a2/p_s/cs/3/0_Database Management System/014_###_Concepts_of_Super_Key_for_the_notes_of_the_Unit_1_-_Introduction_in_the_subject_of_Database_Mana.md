 Here is the content in markdown format for the topic ### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System:

1. Super Key: A super key is a set of one or more than one attributes of a relation schema whose values can uniquely identify a tuple in the relation. In other words, a super key is a set of attributes which can uniquely identify rows in a table.
2. Minimal Super Key: A minimal super key is a super key with the least number of attributes. A minimal super key cannot be made a super key by removing any of its attributes.
3. Candidate Key: A candidate key is a minimal super key. A candidate key is a set of attributes that can uniquely identify a tuple in a relation. A relation can have multiple candidate keys.
4. Primary Key: One of the candidate keys is chosen as the primary key of the relation. The primary key is used to uniquely identify each tuple/row in the relation. The primary key is chosen based on efficiency, simplicity etc.

Advantages of choosing a super key as primary key:
- Uniquely identifies each tuple.
- Prevents duplication of data.
- Facilitates faster search and retrieval of data.

Disadvantages of choosing a super key as primary key:
- May contain redundant attributes which can increase storage space.
- May not be simple and can degrade performance.

Examples of super keys and primary keys:
Table: Student (Rollno, Name, Class, Age)
Super keys: {Rollno}, {Name, Class}
Primary key: {Rollno}

Applications: Used in normalization of databases. Helps in uniquely identifying data and maintaining data integrity. Removes duplication of data.

Does this help? Let me know if you would like me to explain or add anything further.