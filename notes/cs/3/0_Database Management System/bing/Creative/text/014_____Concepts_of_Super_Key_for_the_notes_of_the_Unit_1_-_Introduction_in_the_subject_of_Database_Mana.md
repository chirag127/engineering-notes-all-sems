### Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A **super key** is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- For example, in a relation STUDENT with attributes RollNo, Name, Address, Phone, Email, the set {RollNo, Name} is a super key, since no two students can have the same roll number and name. However, the attribute Name is not essential for uniqueness, as {RollNo} is also a super key by itself.
- A super key is a **generalization** of a candidate key, which is a minimal super key, meaning that it does not have any extra attributes that can be removed without losing the uniqueness property.
- A candidate key is also called a **primary key** if it is chosen as the main way of identifying tuples in a relation. There can be more than one candidate key in a relation, but only one primary key.
- For example, in the STUDENT relation, {RollNo} and {Email} are both candidate keys, since they can uniquely identify a student and they are minimal. However, only one of them can be chosen as the primary key, such as {RollNo}.
- A super key is also a **specialization** of a key, which is a set of attributes that can uniquely identify a tuple in a relation, as well as all tuples in any relation that is related to it by referential integrity constraints.
- A key is also called a **foreign key** if it is used to link two relations by referring to the primary key of another relation.
- For example, in a relation COURSE with attributes CourseID, CourseName, Instructor, the set {CourseID} is a key, since it can uniquely identify a course and any course that is related to it by enrollment or prerequisite relations. The attribute Instructor is a foreign key, since it refers to the primary key {RollNo} of the STUDENT relation.