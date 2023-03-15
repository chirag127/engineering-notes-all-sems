# Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple.
- A candidate key is also a super key, but not every super key is a candidate key.
- For example, consider a relation STUDENT with attributes RollNo, Name, Address, and Phone. A possible super key is {RollNo, Name}, since no two students can have the same roll number and name. However, this super key is not a candidate key, because we can remove the Name attribute and still have a unique identifier for each student. Therefore, a candidate key is {RollNo}.
- A super key can have any number of attributes, as long as they can uniquely identify a tuple. For example, {RollNo, Name, Address, Phone} is also a super key, but it is not minimal.
- A relation can have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier for the relation. The primary key is also a super key and a candidate key. The other candidate keys are called alternate keys or secondary keys.