Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of integrity constraints for the notes of the unit 2 - relational data model and language in the subject of database management system.

### Integrity Constraints
- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- There are four main types of integrity constraints: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints
- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by using data types, domains, ranges, or formats.
- For example, the attribute `age` of the relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 150.

#### Key Constraints
- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by using primary keys, candidate keys, or superkeys.
- For example, the attribute `sid` of the relation `student` can be a primary key that uniquely identifies each student.

#### Entity Integrity Constraints
- Entity integrity constraints ensure that each tuple in a relation has a distinct and non-null value for its primary key.
- Entity integrity constraints can be enforced by using the `NOT NULL` and `UNIQUE` constraints on the primary key attributes.
- For example, the attribute `sid` of the relation `student` must not be null or duplicated.

#### Referential Integrity Constraints
- Referential integrity constraints ensure that the values of a foreign key in one relation match the values of a primary key in another relation, or are null.
- Referential integrity constraints can be enforced by using the `FOREIGN KEY` and `REFERENCES` constraints, and by specifying the actions to be taken when the referenced data is modified or deleted (such as `CASCADE`, `SET NULL`, or `RESTRICT`).
- For example, the attribute `cid` of the relation `enroll` is a foreign key that references the attribute `cid` of the relation `course`, and must either match an existing value in the `course` relation or be null.