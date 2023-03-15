Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Database Management System. Here is the content for the topic of Concepts of Super Key for the notes of the Unit 1 - Introduction:

### Concepts of Super Key

- A super key is a set of one or more attributes that can uniquely identify a tuple (or row) in a relation (or table) of a database.
- A super key may contain extra attributes that are not necessary for unique identification.
- For example, in a relation STUDENT with attributes RollNo, Name, Address, Phone, Email, the set {RollNo, Name, Address, Phone, Email} is a super key, as well as the set {RollNo, Name}, or the set {Email}.
- A super key is a superset of a candidate key, which is a minimal set of attributes that can uniquely identify a tuple in a relation.
- A candidate key can be derived from a super key by removing the redundant attributes, that is, the attributes that do not contribute to the uniqueness of the tuple.
- For example, in the relation STUDENT, the set {RollNo} is a candidate key derived from the super key {RollNo, Name, Address, Phone, Email} by removing the redundant attributes Name, Address, Phone, and Email.
- A relation may have more than one candidate key, but only one of them can be chosen as the primary key, which is the main identifier for the tuples in the relation.
- The primary key is usually underlined in the relation schema to indicate its importance.
- For example, in the relation STUDENT, the set {RollNo} or the set {Email} can be chosen as the primary key, but not both. If {RollNo} is chosen as the primary key, then it is underlined in the relation schema as STUDENT(RollNo, Name, Address, Phone, Email).
- The other candidate keys that are not chosen as the primary key are called alternate keys or secondary keys.
- For example, in the relation STUDENT, if {RollNo} is the primary key, then {Email} is an alternate key or a secondary key.