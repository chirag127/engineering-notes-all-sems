# Keys Constraints

- A key is a set of one or more attributes that uniquely identifies a tuple or a row in a relation or a table.
- A constraint is a rule or a condition that is imposed on the data in a relation or a table to ensure its validity and integrity.
- There are different types of keys and constraints in a relational database, such as:

  - **Primary key**: A primary key is a key that uniquely identifies each tuple or row in a relation or table. A primary key cannot have null values or duplicate values. A relation or table can have only one primary key. For example, in a Student relation, the student_id attribute can be a primary key.

  - **Foreign key**: A foreign key is a key that refers to the primary key of another relation or table. A foreign key establishes a relationship between two relations or tables. A foreign key can have null values or duplicate values, but it must match the value of the primary key in the referenced relation or table, or be null. For example, in a Course relation, the student_id attribute can be a foreign key that references the Student relation.

  - **Candidate key**: A candidate key is a key that can uniquely identify each tuple or row in a relation or table. A candidate key can be a single attribute or a combination of attributes. A relation or table can have more than one candidate key, but only one of them can be chosen as the primary key. For example, in a Student relation, the student_id and the email attributes can be candidate keys, but only one of them can be the primary key.

  - **Alternate key**: An alternate key is a candidate key that is not chosen as the primary key. An alternate key can be used as a backup or a secondary key to identify the tuples or rows in a relation or table. For example, in a Student relation, if the student_id attribute is chosen as the primary key, then the email attribute can be an alternate key.

  - **Composite key**: A composite key is a key that consists of two or more attributes. A composite key can be a primary key, a foreign key, a candidate key, or an alternate key. A composite key can uniquely identify the tuples or rows in a relation or table based on the combination of values of the attributes. For example, in a Course relation, the course_id and the semester attributes can form a composite key.

  - **Super key**: A super key is a key that consists of one or more attributes that can uniquely identify each tuple or row in a relation or table. A super key can be a single attribute or a combination of attributes. A super key can have additional attributes that are not necessary for the uniqueness of the tuples or rows. A super key can be a primary key, a foreign key, a candidate key, an alternate key, or a composite key. For example, in a Student relation, the student_id, the email, and the name attributes can form a super key.

  - **Unique key**: A unique key is a key that can uniquely identify each tuple or row in a relation or table, but it is not a primary key. A unique key can have null values, but it cannot have duplicate values. A relation or table can have more than one unique key. A unique key can be a single attribute or a combination of attributes. A unique key can be a foreign key, a candidate key, an alternate key, or a composite key. For example, in a Student relation, the email attribute can be a unique key.