 Here is the content in markdown format for the topic ### relational model terminology – domains for the notes of the Unit 3 - Relational Database Concepts in the subject of Basics of Data Base Management System:

### Domains
- A domain is a set of permissible values for a given attribute.
- Each attribute in a relation is associated with a domain.
- Domains are used to ensure data integrity by restricting the values that can be assigned to attributes.
- For example, the domain of attribute `age` may be the set of integer values between 0 and 120. This ensures that only valid age values are entered into the database.
- The DBMS enforces domains by checking that the values being inserted or updated for an attribute match the domain specification for that attribute.
- Domains can be:
	- Predefined (eg. integers, characters, dates, etc.)
	- User-defined (eg. names, addresses, etc.)
	- Derived from other domains

Advantages of domains:
- Ensure validity and consistency of data.
- Simplify database design.
- Allow some types of optimization.

Disadvantages of domains:
- May restrict the values that can be store to an artificial subset of the values that occur in practice.
- Additional processing is required to check domains during data manipulation.

[Detailed diagrams and examples can be added here to aid learning]

Applications of domains:
- Almost all database attributes have associated domains.
- Domains are a key part of the data definition in the relational model.
- Domains allow databases to enforce data integrity and consistency.