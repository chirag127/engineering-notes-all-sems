### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- There are four types of integrity constraints in the relational data model: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- For example, the attribute `age` of a relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 150.

#### Key Constraints

- Key constraints specify one or more attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- For example, the attribute `student_id` of a relation `student` can be a primary key that uniquely identifies each student.

#### Entity Integrity Constraints

- Entity integrity constraints ensure that every tuple in a relation has a unique and non-null value for its primary key.
- Entity integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule.
- For example, the relation `student` cannot have two tuples with the same value for `student_id`, or a tuple with a null value for `student_id`.

#### Referential Integrity Constraints

- Referential integrity constraints ensure that a value that appears in one relation for a given set of attributes also appears in another relation for a corresponding set of attributes.
- Referential integrity constraints can be enforced by declaring foreign keys that reference primary keys of other relations.
- For example, the attribute `course_id` of a relation `enrollment` can be a foreign key that references the primary key `course_id` of a relation `course`. This ensures that every course enrolled by a student exists in the `course` relation.