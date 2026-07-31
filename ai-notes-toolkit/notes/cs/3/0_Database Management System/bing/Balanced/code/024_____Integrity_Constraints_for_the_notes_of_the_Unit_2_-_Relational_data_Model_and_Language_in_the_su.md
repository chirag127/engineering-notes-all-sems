Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of integrity constraints for the notes of the unit 2 - relational data model and language in the subject of database management system.

### Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is designed) or at the instance level (when the data is inserted or updated).
- There are four types of integrity constraints in the relational model: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

#### Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- For example, the attribute `age` of the relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 100.

#### Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by declaring primary keys or candidate keys for the relations.
- For example, the attribute `student_id` of the relation `student` can be declared as a primary key, which means that no two tuples in the relation can have the same value for `student_id`.

#### Entity Integrity Constraints

- Entity integrity constraints ensure that each tuple in a relation has a distinct and non-null value for its primary key.
- Entity integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule.
- For example, the relation `student` cannot have a tuple with a null value for `student_id` or a duplicate value for `student_id` with another tuple.

#### Referential Integrity Constraints

- Referential integrity constraints ensure that the values of a foreign key in a relation match the values of a primary key in another relation.
- Referential integrity constraints can be enforced by preventing the insertion, update, or deletion of tuples that violate this rule, or by cascading the changes to the related tuples.
- For example, the attribute `course_id` of the relation `enrollment` is a foreign key that references the attribute `course_id` of the relation `course`. This means that for every tuple in `enrollment`, there must be a corresponding tuple in `course` with the same value for `course_id`. If a tuple in `course` is deleted, then all the tuples in `enrollment` that reference it must also be deleted or updated.