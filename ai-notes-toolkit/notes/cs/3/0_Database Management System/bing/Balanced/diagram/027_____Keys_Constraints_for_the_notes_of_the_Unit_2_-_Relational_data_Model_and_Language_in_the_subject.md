### Key Constraints for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- Key constraints are conditions that must hold on all valid relation states in a relational data model.
- Key constraints are also referred to as entity constraints.
- Key constraints imply that in a relation with a key attribute, no two tuples can have identical values for key attributes .
- A key attribute can not have NULL values.
- A key is a minimal set of attributes that uniquely identifies a tuple in a relation.
- A candidate key is a key that can be chosen as the primary key of the relation.
- A primary key is a candidate key that is selected to identify tuples uniquely within the relation.
- A foreign key is an attribute or a set of attributes in one relation that references the primary key of another relation.
- A foreign key establishes a referential integrity constraint between two relations .
- A referential integrity constraint ensures that a tuple in one relation that refers to another relation must refer to an existing tuple in that relation.
- A referential integrity constraint can be violated by insert, delete, or update operations.
- A referential integrity constraint can be enforced by using different actions such as cascade, set null, set default, or restrict.