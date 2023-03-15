Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Concepts of Super Key for the notes of the Unit 1 - Introduction in the subject of Database Management System.

### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- For example, in a relation STUDENT with attributes RollNo, Name, Address, Phone, Email, the set {RollNo, Name} is a super key, as it can uniquely identify any student. However, the attribute Name is not needed for unique identification, as RollNo alone can serve as a key.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple in a relation.
- A candidate key is also a super key, as it satisfies the property of unique identification. However, a super key may not be a candidate key, as it may contain extra attributes.
- For example, in the relation STUDENT, the set {RollNo} is a candidate key, as it is minimal and can uniquely identify any student. It is also a super key, as it satisfies the property of unique identification. However, the set {RollNo, Name, Phone} is a super key, but not a candidate key, as it contains extra attributes that are not needed for unique identification.
- A primary key is a special candidate key that is chosen by the database designer to identify tuples in a relation. There can be only one primary key for a relation, but there can be multiple candidate keys and super keys.
- A primary key should be non-null and unique, meaning that it cannot contain null values and it cannot have duplicate values in the relation.
- For example, in the relation STUDENT, the attribute RollNo can be chosen as the primary key, as it is non-null, unique, and minimal. It is also a candidate key and a super key.