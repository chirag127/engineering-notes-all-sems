Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of integrity constraints for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System:

# Integrity Constraints

- Integrity constraints are rules that ensure the validity and consistency of the data in a relational database.
- Integrity constraints can be specified at the schema level (when the database is created or modified) or at the instance level (when the data is inserted or updated).
- Integrity constraints can be classified into four types: domain constraints, key constraints, entity integrity constraints, and referential integrity constraints.

## Domain Constraints

- Domain constraints specify the set of permissible values for each attribute of a relation.
- Domain constraints can be enforced by defining data types, formats, ranges, or enumerations for the attributes.
- For example, the attribute `age` of the relation `student` can have a domain constraint that limits its values to positive integers less than or equal to 150.

## Key Constraints

- Key constraints specify the attributes or combinations of attributes that uniquely identify each tuple in a relation.
- Key constraints can be enforced by defining primary keys or candidate keys for the relations.
- For example, the attribute `student_id` of the relation `student` can be a primary key that uniquely identifies each student.

## Entity Integrity Constraints

- Entity integrity constraints ensure that each tuple in a relation has a distinct and non-null value for its primary key.
- Entity integrity constraints can be enforced by preventing the insertion or update of tuples that violate this rule.
- For example, the relation `student` cannot have two tuples with the same value for `student_id`, or a tuple with a null value for `student_id`.

## Referential Integrity Constraints

- Referential integrity constraints ensure that the values of a foreign key in one relation match the values of a primary key in another relation, or are null.
- Referential integrity constraints can be enforced by preventing the insertion, update, or deletion of tuples that violate this rule, or by cascading the changes to the related tuples.
- For example, the attribute `course_id` of the relation `enrollment` can be a foreign key that references the attribute `course_id` of the relation `course`. The relation `enrollment` cannot have a tuple with a value for `course_id` that does not exist in the relation `course`, or a tuple with a null value for `course_id`. If a tuple in the relation `course` is deleted, the related tuples in the relation `enrollment` must also be deleted or updated.