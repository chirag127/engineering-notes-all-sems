# Concepts of Super Key

A super key is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple in a relation. In other words, a super key is a set of attributes that can be used to uniquely identify a row in a table.

- A super key is a superset of a candidate key.
- Every relation has at least one super key, which is the set of all attributes in the relation.
- A super key may contain extraneous attributes, which means that some of the attributes in the super key may not be necessary to uniquely identify a row.
- A candidate key is a minimal super key, which means that it is a super key with no extraneous attributes.
- A primary key is a candidate key that is chosen by the database designer to be the main method of identifying rows in a table.

For example, consider a relation `Student` with attributes `StudentID`, `Name`, `Address`, and `PhoneNumber`. The set of attributes `{StudentID}` is a super key for the relation because no two students can have the same student ID. The set of attributes `{StudentID, Name}` is also a super key because it contains the candidate key `{StudentID}`. However, the attribute `Name` is extraneous in this super key because it is not necessary to uniquely identify a row. The set of attributes `{StudentID, Name, Address, PhoneNumber}` is also a super key because it contains all the attributes in the relation. However, this super key contains extraneous attributes because only the attribute `StudentID` is necessary to uniquely identify a row.
