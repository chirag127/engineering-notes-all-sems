 Here are the key points about Concepts of Super Key for the notes of Unit 2 - Data Modeling using Entity Relationship Model:

### Concepts of Super Key

1. A superkey is a set of one or more attributes whose values uniquely identify a tuple in a relation.
2. A superkey must contain the primary key.
3. A superkey that has the minimum number of attributes is called a candidate key.
4. If a relation has two or more candidate keys, one of them is chosen to be the primary key.
5. The primary key must be:
- Unique
- Not null
- Minimal (no subset of it is a key)

For example, for a relation with attributes Roll No, Name, Age, Address, {Roll No} is a super key and {Roll No, Name} is also a super key. But {Roll No} is a candidate key and can be chosen as the primary key.

Advantages of identifying super keys:
- Ensures data integrity by avoiding duplicate and null values.
- Facilitates maintenance of databases by ensuring unique identification of each tuple.

Applications: Super keys and primary keys are fundamental concepts used in relational database design. They help in modeling the data efficiently and establishing relationships between data.

[Diagrams and examples can be added here for better understanding]

Hope this helps! Let me know if you would like me to explain anything in more detail.