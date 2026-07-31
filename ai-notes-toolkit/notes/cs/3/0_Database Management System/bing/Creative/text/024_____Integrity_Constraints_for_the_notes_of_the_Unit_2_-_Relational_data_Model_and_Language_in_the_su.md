### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- There are four types of integrity constraints in the relational data model: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- For example, the attribute `age` of a relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 150.

#### Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- For example, the attribute `student_id` of a relation `student` can be a primary key that uniquely identifies each student.

#### Entity Integrity Constraints

- Entity integrity constraints ensure that each tuple in a relation has a distinct and non-null value for its primary key.
- Entity integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule.
- For example, the relation `student` cannot have two tuples with the same value for `student_id`, or a tuple with a null value for `student_id`.

#### Referential Integrity Constraints

- Referential integrity constraints ensure that the values of a foreign key in a relation match the values of a primary key in another relation.
- Referential integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule, or by cascading the changes to the related tuples.
- For example, the relation `enrollment` has a foreign key `student_id` that references the primary key `student_id` of the relation `student`. If a tuple is inserted or updated in `enrollment` with a value for `student_id` that does not exist in `student`, the referential integrity constraint is violated. This can be prevented by rejecting the operation, or by inserting or updating the corresponding tuple in `student`.